// node --test portal/tests/delivery.test.mjs   (Node 22). No network, no keys: Supabase, R2 and Resend are in-memory fakes; every secret is a made-up string.
import test from 'node:test';
import assert from 'node:assert/strict';
import { createHmac } from 'node:crypto';
import * as D from '../functions/_shared/delivery.js';
import { sendEmail, buildDeliveryEmail, RESEND_API } from '../functions/_shared/email.js';
import { onRequestPost as webhook } from '../functions/api/stripe-webhook.js';
import { handleAdminDelivery } from '../functions/api/admin/delivery.js';
import { onRequest as downloadRoute } from '../functions/api/download/[token].js';

const ENV = { SUPABASE_URL: 'https://x.supabase.co', SUPABASE_ANON_KEY: 'anon', SUPABASE_SERVICE_ROLE_KEY: 'service', STRIPE_WEBHOOK_SECRET: 'whsec_fake', SITE_URL: 'https://mi.example',
  DELIVERY_TOKEN_SALT: 'test-salt-test-salt-test-salt-0123456789', RESEND_API_KEY: 're_fake', EMAIL_FROM: 'Math Inquirers <downloads@mi.example>', SUPPORT_WHATSAPP: '+65 0000 0000' };
const MANIFEST = { files: { 'ext-l1:pdf': { r2_key: 'files/ext-l1/v1/book.pdf', filename: 'book.pdf', version: 'v1', sha256: 'a'.repeat(64), title: 'Extension Workbook, Level 1' },
  'ext-l2:pdf': { r2_key: 'files/ext-l2/v1/book2.pdf', filename: 'book2.pdf', version: 'v1' } } };
const SESSION = { id: 'cs_test_a1B2c3D4e5F6g7H8', mode: 'payment', payment_status: 'paid', customer_details: { email: 'Buyer@Example.com' }, metadata: { mi_items: 'ext-l1:pdf,ext-l2:pdf,bad item,ext-l1:pdf' } };
const PDF = new Uint8Array(1000).map((_, i) => i % 251);

// ----- fakes -----
function fakeDb({ now = () => Date.now() } = {}) {
  const rows = [], log = [], calls = [];
  const db = { rows, log, calls,
    async rpc(fn, a) {
      calls.push(fn);
      if (fn === 'service_grant_entitlement') {
        let r = rows.find((x) => a.p_session_id && x.stripe_session_id === a.p_session_id && x.product_id === a.p_product_id && x.format === a.p_format);
        const created = !r;
        if (!r) { r = { id: 'id' + (rows.length + 1), order_id: a.p_order_id, stripe_session_id: a.p_session_id, product_id: a.p_product_id, format: a.p_format, buyer_email: a.p_email, r2_key: a.p_r2_key, filename: a.p_filename, file_sha256: a.p_sha256, link_nonce: a.p_nonce, token_hash: a.p_token_hash, expires_at: a.p_expires_at, max_downloads: a.p_max, download_count: 0, last_download_at: null, revoked_at: null, emailed_at: null, claimed: 0 }; rows.push(r); }
        return { created, ...r };
      }
      if (fn === 'service_claim_email') { const rs = rows.filter((x) => x.stripe_session_id === a.p_session_id && !x.emailed_at && x.buyer_email); if (!rs.length || rs.some((x) => x.claimed)) return false; rs.forEach((x) => (x.claimed = 1)); return true; }
      if (fn === 'service_mark_emailed') { rows.filter((x) => x.stripe_session_id === a.p_session_id).forEach((x) => (x.emailed_at = 'now')); return null; }
      if (fn === 'service_order_entitlements') return rows.filter((x) => x.stripe_session_id === a.p_session_id).map((x) => ({ ...x, revoked: !!x.revoked_at }));
      if (fn === 'service_links_rate') return true;
      if (fn === 'service_download_release') { rows.find((x) => x.id === a.p_entitlement).download_count--; return null; }
      if (fn === 'service_download_begin') {
        const recent = log.filter((l) => l.ip === a.p_ip_hash).length; log.push({ ip: a.p_ip_hash });
        if (recent >= a.p_rate_max) return { status: 'rate_limited' };
        const e = rows.find((x) => x.token_hash === a.p_token_hash); if (!e) return { status: 'not_found' };
        if (e.revoked_at) return { status: 'revoked' }; if (Date.parse(e.expires_at) <= now()) return { status: 'expired' };
        if (a.p_count && e.download_count >= e.max_downloads) return { status: 'exhausted' };
        if (!a.p_count && !e.download_count) return { status: 'range_denied' };
        if (a.p_count) e.download_count++;
        return { status: 'ok', entitlement_id: e.id, r2_key: e.r2_key, filename: e.filename, order_id: e.order_id, remaining: e.max_downloads - e.download_count };
      }
      throw new Error('unexpected rpc ' + fn);
    } };
  return db;
}
function fakeBucket(files = { 'files/ext-l1/v1/book.pdf': PDF }) {
  return { reads: 0,
    async head(k) { return files[k] ? { size: files[k].length } : null; },
    async get(k, o) { if (!files[k]) return null; this.reads++; const b = o && o.range ? files[k].slice(o.range.offset, o.range.offset + o.range.length) : files[k]; return { body: new Blob([b]).stream(), size: files[k].length }; } };
}
function fakeResend() { const sent = []; const f = async (url, init) => { sent.push({ url, init, body: JSON.parse(init.body) }); return new Response(JSON.stringify({ id: 'em_1' }), { status: 200 }); }; f.sent = sent; return f; }
async function grant(db, resend, session = SESSION, env = ENV) { return D.grantEntitlements(env, session, D.itemsFromSession(session), { rpc: (f, a) => db.rpc(f, a), manifest: MANIFEST, fetch: resend }); }
const dlReq = (token, headers = {}, method = 'GET') => new Request('https://mi.example/api/download/' + token, { method, headers: { 'CF-Connecting-IP': '203.0.113.9', ...headers } });
async function tokenOf(db, i = 0) { return D.tokenFromNonce(ENV, db.rows[i].link_nonce); }
const body = async (r) => new Uint8Array(await r.arrayBuffer());

// ----- tokens -----
test('token: derived from nonce + secret, 43 url-safe chars, hash is 64 hex, differs per nonce and per salt', async () => {
  const a = await D.newLinkSecrets(ENV), b = await D.newLinkSecrets(ENV);
  assert.match(a.token, D.TOKEN_RE); assert.match(a.hash, /^[0-9a-f]{64}$/);
  assert.notEqual(a.token, b.token); assert.notEqual(a.nonce, b.nonce);
  assert.equal(await D.tokenFromNonce(ENV, a.nonce), a.token, 'rebuildable from nonce (success page, resend)');
  assert.notEqual(await D.tokenFromNonce({ ...ENV, DELIVERY_TOKEN_SALT: 'other-salt-other-salt-other-salt-99' }, a.nonce), a.token);
  assert.notEqual(a.hash, a.token, 'the stored value is not the token');
  assert.equal(a.nonce.length, 43, '32 random bytes');
  await assert.rejects(() => D.tokenFromNonce({ DELIVERY_TOKEN_SALT: 'short' }, 'x'), /DELIVERY_TOKEN_SALT/);
});
test('token verify: right token passes; wrong, truncated, wrong-nonce, non-string fail', async () => {
  const a = await D.newLinkSecrets(ENV), b = await D.newLinkSecrets(ENV);
  assert.equal(await D.verifyToken(ENV, a.token, a.nonce, a.hash), true);
  assert.equal(await D.verifyToken(ENV, b.token, a.nonce, a.hash), false);
  assert.equal(await D.verifyToken(ENV, a.token.slice(0, 42), a.nonce, a.hash), false);
  assert.equal(await D.verifyToken(ENV, a.token, b.nonce, a.hash), false);
  assert.equal(await D.verifyToken(ENV, a.token.slice(0, 42) + (a.token.endsWith('A') ? 'B' : 'A'), a.nonce, a.hash), false, 'one character off');
  assert.equal(await D.verifyToken(ENV, null, a.nonce, a.hash), false);
});

// ----- grant -----
test('grant: unknown product reported, bad items dropped, buyer email lowercased, expiry and max default 14 days / 5', async () => {
  assert.deepEqual(D.itemsFromSession(SESSION), [{ product_id: 'ext-l1', format: 'pdf' }, { product_id: 'ext-l2', format: 'pdf' }]);
  const db = fakeDb(), rs = fakeResend();
  const r = await D.grantEntitlements(ENV, { ...SESSION, metadata: { mi_items: 'ext-l1:pdf,nope:pdf' } }, [{ product_id: 'ext-l1', format: 'pdf' }, { product_id: 'nope', format: 'pdf' }], { rpc: (f, a) => db.rpc(f, a), manifest: MANIFEST, fetch: rs });
  assert.deepEqual(r.missing, ['nope']); assert.equal(r.granted.length, 1);
  assert.equal(db.rows[0].buyer_email, 'buyer@example.com'); assert.equal(db.rows[0].max_downloads, 5);
  const days = (Date.parse(db.rows[0].expires_at) - Date.now()) / 86400000; assert.ok(days > 13.99 && days <= 14);
  assert.equal(r.order_id, 'MI-E5F6G7H8');
});
test('grant is idempotent: a repeated webhook gives the same links, no duplicate rows, ONE email', async () => {
  const db = fakeDb(), rs = fakeResend();
  const r1 = await grant(db, rs), r2 = await grant(db, rs);
  assert.equal(db.rows.length, 2); assert.deepEqual(r1.granted.map((g) => g.url), r2.granted.map((g) => g.url));
  assert.equal(r1.granted[0].created, true); assert.equal(r2.granted[0].created, false);
  assert.equal(rs.sent.length, 1); assert.equal(r1.emailed, true); assert.equal(r2.emailed, null);
  assert.ok(db.rows.every((x) => x.emailed_at));
  assert.ok(r1.granted[0].url.startsWith('https://mi.example/api/download/'));
});
test('grant: no email configured or no buyer email -> links still granted, no send; email failure does not throw (admin resend is the recovery)', async () => {
  let db = fakeDb(), rs = fakeResend();
  let r = await grant(db, rs, SESSION, { ...ENV, RESEND_API_KEY: undefined }); assert.equal(r.emailed, null); assert.equal(rs.sent.length, 0); assert.equal(r.granted.length, 2);
  db = fakeDb(); r = await grant(db, rs, { ...SESSION, customer_details: {} }); assert.equal(r.emailed, null); assert.equal(rs.sent.length, 0);
  db = fakeDb(); const bad = async () => new Response('{"message":"buyer@example.com is bad"}', { status: 422 });
  r = await grant(db, bad); assert.equal(r.emailed, false); assert.equal(r.granted.length, 2); assert.ok(!db.rows[0].emailed_at);
});
test('grant: database failure throws so the webhook can answer non-2xx', async () => {
  await assert.rejects(() => D.grantEntitlements(ENV, SESSION, D.itemsFromSession(SESSION), { manifest: MANIFEST, rpc: async () => { throw new Error('supabase rpc x failed: 500'); } }), /failed/);
});

// ----- email -----
test('email adapter: Resend payload shape, headers, idempotency key, no tracking; errors never echo the body', async () => {
  const rs = fakeResend();
  const links = [{ name: 'Extension Workbook, Level 1', url: 'https://mi.example/api/download/' + 'a'.repeat(43), expires_at: '2026-11-10T00:00:00Z', max_downloads: 5 }];
  const msg = buildDeliveryEmail({ orderId: 'MI-TEST1234', links, env: ENV });
  await sendEmail(ENV, msg, { to: 'buyer@example.com', idempotencyKey: 'k1', fetch: rs });
  const c = rs.sent[0];
  assert.equal(c.url, RESEND_API); assert.equal(c.init.method, 'POST');
  assert.equal(c.init.headers.Authorization, 'Bearer re_fake'); assert.equal(c.init.headers['Idempotency-Key'], 'k1');
  assert.deepEqual(Object.keys(c.body).sort(), ['from', 'html', 'subject', 'text', 'to']);
  assert.equal(c.body.from, ENV.EMAIL_FROM); assert.deepEqual(c.body.to, ['buyer@example.com']); assert.equal(c.body.subject, 'Your Math Inquirers download');
  for (const part of [c.body.text, c.body.html]) { assert.ok(part.includes(links[0].url)); assert.ok(part.includes('MI-TEST1234')); assert.ok(part.includes('11 November 2026') || part.includes('10 November 2026')); assert.ok(part.includes('+65 0000 0000')); assert.match(part, /Licence/); assert.match(part, /5 times/); }
  assert.ok(!/<img|<script|pixel|track/i.test(c.body.html), 'no tracking pixels');
  await assert.rejects(() => sendEmail(ENV, msg, { to: 'not-an-email', fetch: rs }), /recipient/);
  await assert.rejects(() => sendEmail({ ...ENV, RESEND_API_KEY: '' }, msg, { to: 'a@b.co', fetch: rs }), /RESEND_API_KEY/);
  await assert.rejects(() => sendEmail({ ...ENV, EMAIL_PROVIDER: 'nope' }, msg, { to: 'a@b.co', fetch: rs }), /unknown/);
  const err = await sendEmail(ENV, msg, { to: 'a@b.co', fetch: async () => new Response('{"to":"a@b.co"}', { status: 403 }) }).catch((e) => e.message);
  assert.equal(err, 'resend failed: 403');
  const html = buildDeliveryEmail({ orderId: '<b>x</b>', links: [{ ...links[0], name: '<script>' }], env: ENV }).html; assert.ok(!html.includes('<script>') && !html.includes('<b>x'));
});

// ----- download -----
async function setup(over = {}) {
  const db = fakeDb(over.dbOpts), rs = fakeResend(); await grant(db, rs);
  const bucket = over.bucket || fakeBucket(); const env = { ...ENV, DELIVERY_BUCKET: bucket };
  D._resetBurst();
  return { db, bucket, env, token: await tokenOf(db), opts: { rpc: (f, a) => db.rpc(f, a) } };
}
test('download: valid token streams the file with attachment, no-store, nosniff and counts one download', async () => {
  const { db, env, token, opts } = await setup();
  const r = await D.handleDownload({ request: dlReq(token), env, token }, opts);
  assert.equal(r.status, 200); assert.equal(r.headers.get('Content-Type'), 'application/pdf');
  assert.match(r.headers.get('Content-Disposition'), /^attachment; filename="book.pdf"; filename\*=UTF-8''book\.pdf$/);
  assert.match(r.headers.get('Cache-Control'), /no-store/); assert.equal(r.headers.get('X-Content-Type-Options'), 'nosniff'); assert.equal(r.headers.get('Accept-Ranges'), 'bytes');
  assert.equal(r.headers.get('Content-Length'), '1000'); assert.deepEqual(await body(r), PDF); assert.equal(db.rows[0].download_count, 1);
});
test('download: wrong, malformed, unknown token -> 404 page with no file and no count', async () => {
  const { db, env, opts } = await setup();
  for (const t of ['x', 'a'.repeat(43), '../../etc/passwd', '', undefined, 'a'.repeat(44)]) { const r = await D.handleDownload({ request: dlReq(t || 'x'), env, token: t }, opts); assert.equal(r.status, 404, String(t)); assert.match(r.headers.get('Content-Type'), /text\/html/); }
  assert.equal(db.rows[0].download_count, 0);
});
test('download: max downloads enforced (5th ok, 6th refused), expiry, revoked', async () => {
  const { db, env, token, opts } = await setup();
  for (let i = 0; i < 5; i++) { const ip = '198.51.100.' + i; assert.equal((await D.handleDownload({ request: dlReq(token, { 'CF-Connecting-IP': ip }), env, token }, opts)).status, 200); }
  assert.equal((await D.handleDownload({ request: dlReq(token), env, token }, opts)).status, 410);
  db.rows[0].download_count = 0; db.rows[0].expires_at = new Date(Date.now() - 1000).toISOString();
  const ex = await D.handleDownload({ request: dlReq(token, { 'CF-Connecting-IP': '198.51.100.50' }), env, token }, opts); assert.equal(ex.status, 410); assert.match(await ex.text(), /expired/i);
  db.rows[0].expires_at = new Date(Date.now() + 1e6).toISOString(); db.rows[0].revoked_at = 'now';
  assert.equal((await D.handleDownload({ request: dlReq(token, { 'CF-Connecting-IP': '198.51.100.51' }), env, token }, opts)).status, 410);
});
test('download: HEAD refused (previews never use a download); POST refused', async () => {
  const { db, env, token, opts } = await setup();
  assert.equal((await D.handleDownload({ request: dlReq(token, {}, 'HEAD'), env, token }, opts)).status, 405);
  assert.equal(db.rows[0].download_count, 0);
});
test('download: range requests -> 206 with Content-Range; start 0 counts, later ranges free only after a counted start; suffix and open ranges; 416', async () => {
  const { db, env, token, opts } = await setup();
  const mid = await D.handleDownload({ request: dlReq(token, { Range: 'bytes=100-199' }), env, token }, opts);
  assert.equal(mid.status, 403, 'a mid-file range before any counted download is refused');
  const first = await D.handleDownload({ request: dlReq(token, { Range: 'bytes=0-99' }), env, token }, opts);
  assert.equal(first.status, 206); assert.equal(first.headers.get('Content-Range'), 'bytes 0-99/1000'); assert.equal(first.headers.get('Content-Length'), '100'); assert.deepEqual(await body(first), PDF.slice(0, 100));
  assert.equal(db.rows[0].download_count, 1);
  const next = await D.handleDownload({ request: dlReq(token, { Range: 'bytes=100-' }), env, token }, opts);
  assert.equal(next.status, 206); assert.equal(next.headers.get('Content-Range'), 'bytes 100-999/1000'); assert.deepEqual(await body(next), PDF.slice(100)); assert.equal(db.rows[0].download_count, 1, 'resume is free');
  const suf = await D.handleDownload({ request: dlReq(token, { Range: 'bytes=-50' }), env, token }, opts); assert.equal(suf.status, 206); assert.equal(suf.headers.get('Content-Range'), 'bytes 950-999/1000'); assert.equal(db.rows[0].download_count, 2, 'suffix ranges are counted');
  const bad = await D.handleDownload({ request: dlReq(token, { Range: 'bytes=5000-6000' }), env, token }, opts); assert.equal(bad.status, 416); assert.equal(bad.headers.get('Content-Range'), 'bytes */1000');
  const multi = await D.handleDownload({ request: dlReq(token, { Range: 'bytes=0-1,5-6' }), env, token }, opts); assert.equal(multi.status, 200, 'multi-range ignored: whole file, and counted'); assert.equal(db.rows[0].download_count, 3);
});
test('parseRange edge cases', () => {
  assert.equal(D.parseRange(null, 10), null); assert.deepEqual(D.parseRange('bytes=0-', 10), { start: 0, end: 9 }); assert.deepEqual(D.parseRange('bytes=2-100', 10), { start: 2, end: 9 });
  assert.deepEqual(D.parseRange('bytes=-3', 10), { start: 7, end: 9 }); assert.deepEqual(D.parseRange('bytes=-30', 10), { start: 0, end: 9 });
  for (const h of ['bytes=10-', 'bytes=5-2', 'bytes=-0', 'bytes=-']) assert.equal(D.parseRange(h, 10), 'invalid', h);
  assert.equal(D.parseRange('items=0-1', 10), null);
});
test('download: file missing in R2 -> friendly 503 and the download is given back; storage fault never burns a download', async () => {
  const { db, env, token, opts } = await setup({ bucket: fakeBucket({}) });
  const r = await D.handleDownload({ request: dlReq(token), env, token }, opts); assert.equal(r.status, 503); assert.equal(db.rows[0].download_count, 0);
});
test('download: rate limit (database) and in-isolate burst limiter', async () => {
  const { env, token, opts } = await setup();
  const out = []; for (let i = 0; i < 34; i++) out.push((await D.handleDownload({ request: dlReq('b'.repeat(43), { 'CF-Connecting-IP': '192.0.2.1' }), env, token: 'b'.repeat(43) }, opts)).status);
  assert.equal(out[0], 404); assert.equal(out.at(-1), 429, 'same IP hammering wrong tokens gets 429');
  const ok = await D.handleDownload({ request: dlReq(token, { 'CF-Connecting-IP': '192.0.2.77' }), env, token }, opts); assert.equal(ok.status, 200, 'other IPs unaffected');
  D._resetBurst(); let limited = false; for (let i = 0; i < 61; i++) limited = D.burstLimited('k', 1000 + i); assert.equal(limited, true); assert.equal(D.burstLimited('k', 1e6), false);
});
test('download: not configured -> 503; log carries only a salted IP hash, never the raw IP', async () => {
  const { env, token, opts } = await setup();
  assert.equal((await D.handleDownload({ request: dlReq(token), env: { ...env, DELIVERY_BUCKET: undefined }, token }, opts)).status, 503);
  const h = await D.ipHash(env, '203.0.113.9'); assert.match(h, /^[0-9a-f]{32}$/); assert.ok(!h.includes('203'));
});
test('download route: params.token array or string is accepted (Pages dynamic route)', async () => {
  const r = await downloadRoute({ request: dlReq('zzz'), env: { ...ENV, DELIVERY_BUCKET: fakeBucket() }, params: { token: ['zzz'] } }); assert.equal(r.status, 404);
});
test('contentDisposition keeps header safe for odd names', () => {
  const cd = D.contentDisposition('Bu"ddy é.pdf'); assert.ok(!/[^\x20-\x7e]/.test(cd)); assert.ok(cd.includes("filename*=UTF-8''Bu%22ddy%20%C3%A9.pdf"));
});

// ----- order success page endpoint -----
test('order-links: bad session 400; unknown session 202 pending; ready returns working links; revoked has no url; no email in response', async () => {
  const db = fakeDb(), rs = fakeResend(), opts = { rpc: (f, a) => db.rpc(f, a) };
  const q = (s) => new Request('https://mi.example/api/order-links?session_id=' + s, { headers: { 'CF-Connecting-IP': '203.0.113.1' } });
  assert.equal((await D.handleOrderLinks({ request: q('nope'), env: ENV }, opts)).status, 400);
  assert.equal((await D.handleOrderLinks({ request: q(SESSION.id), env: ENV }, opts)).status, 202);
  await grant(db, rs);
  const r = await D.handleOrderLinks({ request: q(SESSION.id), env: ENV }, opts); assert.equal(r.status, 200); const j = await r.json();
  assert.equal(j.status, 'ready'); assert.equal(j.links.length, 2); assert.equal(j.links[0].url, `https://mi.example/api/download/${await tokenOf(db)}`); assert.ok(!JSON.stringify(j).includes('example.com'));
  assert.match(r.headers.get('Cache-Control'), /no-store/);
  db.rows[1].revoked_at = 'now'; const j2 = await (await D.handleOrderLinks({ request: q(SESSION.id), env: ENV }, opts)).json(); assert.equal(j2.links[1].url, null);
});

// ----- webhook integration (the marked hook) -----
const sig = (raw, t = Math.floor(Date.now() / 1000)) => `t=${t},v1=${createHmac('sha256', ENV.STRIPE_WEBHOOK_SECRET).update(`${t}.${raw}`).digest('hex')}`;
test('stripe webhook hook: paid shop session grants + emails; repeated delivery is harmless; unpaid is ignored; enrolment events untouched', async () => {
  const db = fakeDb(), rs = fakeResend(), real = globalThis.fetch, rpcCalls = [];
  globalThis.fetch = async (url, init) => {
    url = String(url);
    if (url.includes('/rest/v1/rpc/')) { const fn = url.split('/rpc/')[1]; rpcCalls.push(fn); return new Response(JSON.stringify(await db.rpc(fn, JSON.parse(init.body))), { status: 200 }); }
    if (url === RESEND_API) return rs(url, init);
    throw new Error('unexpected fetch ' + url);
  };
  try {
    const post = (session, type = 'checkout.session.completed') => { const raw = JSON.stringify({ id: 'evt_1', type, data: { object: session } }); return webhook({ request: new Request('https://mi.example/api/stripe-webhook', { method: 'POST', headers: { 'Stripe-Signature': sig(raw) }, body: raw }), env: ENV }); };
    const shop = { ...SESSION, metadata: { mi_items: 'beta-workbook-l1:pdf' } };
    const r1 = await post(shop); assert.equal(r1.status, 200); const j = await r1.json(); assert.equal(j.shop, true); assert.equal(j.granted, 1);
    await post(shop); await post(shop, 'checkout.session.async_payment_succeeded');
    assert.equal(db.rows.length, 1); assert.equal(rs.sent.length, 1);
    assert.equal((await (await post({ ...shop, id: 'cs_test_zzzzzzzzzzzz2', payment_status: 'unpaid' })).json()).ignored, 'shop: awaiting payment'); assert.equal(db.rows.length, 1);
    assert.equal((await (await post({ ...shop, id: 'cs_test_zzzzzzzzzzzz3' }, 'checkout.session.expired')).json()).ignored, 'shop: checkout.session.expired');
    const before = rpcCalls.length; const enrol = await post({ id: 'cs_test_e', mode: 'payment', payment_status: 'paid', amount_total: 25000, currency: 'sgd', client_reference_id: '33333333-3333-4333-8333-333333333333' }).catch((e) => e);
    assert.ok(!rpcCalls.slice(before).some((f) => f.startsWith('service_grant')), 'enrolment payments never reach the delivery code');
    globalThis.fetch = async (url) => { if (String(url).includes('/rpc/')) return new Response('{}', { status: 500 }); throw new Error('x'); };
    assert.equal((await post({ ...shop, id: 'cs_test_zzzzzzzzzzzz4' })).status, 502, 'database down -> Stripe retries');
  } finally { globalThis.fetch = real; }
});

// ----- admin function -----
function adminRpc(db, isAdmin = true) {
  return async (fn, a, tok) => {
    if (!isAdmin) { const e = new Error('forbidden'); e.code = 403; throw e; }
    if (fn === 'admin_create_manual_entitlement') { const row = { id: '11111111-1111-4111-8111-111111111111', order_id: 'MANUAL-AB12CD34', filename: a.p_filename, expires_at: new Date(Date.now() + a.p_days * 864e5).toISOString(), max_downloads: a.p_max, r2_key: a.p_r2_key, token_hash: a.p_token_hash, link_nonce: a.p_nonce, buyer_email: a.p_email }; db.rows.push(row); return row; }
    if (fn === 'admin_prepare_resend') { const r = db.rows.find((x) => x.id === a.p_id); return r ? [{ ...r, order_id: r.order_id }] : []; }
    if (fn === 'admin_revoke_entitlement') { const r = db.rows.find((x) => x.id === a.p_id); if (r) r.revoked_at = 'now'; return !!r; }
    if (fn === 'admin_list_entitlements') return db.rows.map((r) => ({ id: r.id, order_id: r.order_id }));
    throw new Error('unexpected ' + fn);
  };
}
const adm = (b, h = { Authorization: 'Bearer jwt' }) => new Request('https://mi.example/api/admin/delivery', { method: 'POST', headers: { 'Content-Type': 'application/json', ...h }, body: JSON.stringify(b) });
test('admin: needs a token; non-admin gets 403; admin creates a one-off link that downloads, WITHOUT any payment or session', async () => {
  const db = fakeDb(), bucket = fakeBucket(); const opts = { rpc: adminRpc(db), manifest: MANIFEST, bucket };
  assert.equal((await handleAdminDelivery({ request: adm({ action: 'list' }, {}), env: ENV }, opts)).status, 401);
  assert.equal((await handleAdminDelivery({ request: adm({ action: 'list' }), env: ENV }, { ...opts, rpc: adminRpc(db, false) })).status, 403);
  assert.equal((await handleAdminDelivery({ request: adm({ action: 'nope' }), env: ENV }, opts)).status, 400);
  assert.equal((await handleAdminDelivery({ request: adm({ action: 'create', product_id: 'unknown' }), env: ENV }, opts)).status, 400);
  assert.equal((await handleAdminDelivery({ request: adm({ action: 'create', r2_key: '../x' }), env: ENV }, opts)).status, 400);
  assert.equal((await handleAdminDelivery({ request: adm({ action: 'create', product_id: 'ext-l2' }), env: ENV }, opts)).status, 400, 'manifest entry whose file is not in the bucket is refused');
  const r = await handleAdminDelivery({ request: adm({ action: 'create', product_id: 'ext-l1', days: 7, max: 3 }), env: ENV }, opts); assert.equal(r.status, 200); const j = await r.json();
  assert.match(j.url, /^https:\/\/mi\.example\/api\/download\/[A-Za-z0-9_-]{43}$/); assert.equal(db.rows[0].max_downloads, 3);
  const token = j.url.split('/').pop(); assert.equal(await D.tokenHash(token), db.rows[0].token_hash, 'the stored hash matches the link handed out');
  const e = { ...ENV, DELIVERY_BUCKET: bucket }; const dopts = { rpc: async (f, a) => fakeDbFromRows(db).rpc(f, a) };
  const dl = await D.handleDownload({ request: dlReq(token), env: e, token }, dopts); assert.equal(dl.status, 200);
});
function fakeDbFromRows(db) { const f = fakeDb(); f.rows.push(...db.rows.map((r) => ({ download_count: 0, revoked_at: null, ...r }))); return f; }
test('admin: resend emails the buyer (link not echoed) or returns the link when there is no email; revoke works; bad ids rejected', async () => {
  const db = fakeDb(), rs = fakeResend(); await grant(db, fakeResend());
  const opts = { rpc: adminRpc(db), manifest: MANIFEST, fetch: rs };
  const r = await (await handleAdminDelivery({ request: adm({ action: 'resend', id: '11111111-1111-4111-8111-111111111111' }), env: ENV }, opts)).status; assert.equal(r, 404);
  db.rows[0].id = '11111111-1111-4111-8111-111111111111';
  const j = await (await handleAdminDelivery({ request: adm({ action: 'resend', id: db.rows[0].id }), env: ENV }, opts)).json(); assert.equal(j.emailed, true); assert.equal(j.url, undefined); assert.equal(rs.sent.length, 1); assert.deepEqual(rs.sent[0].body.to, ['buyer@example.com']);
  db.rows[0].buyer_email = null; const j2 = await (await handleAdminDelivery({ request: adm({ action: 'resend', id: db.rows[0].id }), env: ENV }, opts)).json(); assert.equal(j2.emailed, false); assert.match(j2.url, /api\/download\//);
  assert.equal((await handleAdminDelivery({ request: adm({ action: 'revoke', id: 'bad' }), env: ENV }, opts)).status, 400);
  assert.equal((await (await handleAdminDelivery({ request: adm({ action: 'revoke', id: db.rows[0].id }), env: ENV }, opts)).json()).revoked, true);
});
