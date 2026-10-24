// Soft-copy delivery core. Pure Web APIs (fetch, crypto.subtle, R2 binding) so it runs on Cloudflare Workers and in Node 22 tests.
// Nothing here is a route: Cloudflare only treats files that export onRequest* under /functions as routes.
//
// Token model: link_nonce (32 random bytes, stored) -> token = HMAC-SHA256(DELIVERY_TOKEN_SALT, nonce) (never stored) -> token_hash = SHA-256(token) (stored, unique).
// A database-only leak therefore cannot rebuild any link; the Worker can rebuild a link (success page, resend) without storing the token.
import { json, timingSafeEqual, toHex, supabaseRpc } from '../lib.js';
import { sendEmail, buildDeliveryEmail } from './email.js';

export const DEFAULT_EXPIRY_DAYS = 14;
export const DEFAULT_MAX_DOWNLOADS = 5;
export const TOKEN_RE = /^[A-Za-z0-9_-]{43}$/;
export const SESSION_RE = /^cs_(test|live)_[A-Za-z0-9]{10,200}$/;
const enc = new TextEncoder();

export function b64url(bytes) {
  let s = ''; for (const b of new Uint8Array(bytes)) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}
export function randomNonce() { return b64url(crypto.getRandomValues(new Uint8Array(32))); }
async function hmacBytes(secret, msg) {
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return crypto.subtle.sign('HMAC', key, enc.encode(msg));
}
export async function sha256Hex(s) { return toHex(await crypto.subtle.digest('SHA-256', enc.encode(s))); }
function needSalt(env) { if (!env.DELIVERY_TOKEN_SALT || String(env.DELIVERY_TOKEN_SALT).length < 24) throw new Error('DELIVERY_TOKEN_SALT missing or shorter than 24 characters'); return env.DELIVERY_TOKEN_SALT; }

export async function tokenFromNonce(env, nonce) { return b64url(await hmacBytes(needSalt(env), 'mi-dl-v1|' + nonce)); }   // 43 chars
export async function tokenHash(token) { return sha256Hex('mi-dl-token|' + token); }
export async function newLinkSecrets(env) { const nonce = randomNonce(); const token = await tokenFromNonce(env, nonce); return { nonce, token, hash: await tokenHash(token) }; }
// Constant-time check that a presented token belongs to a stored nonce/hash (used by admin tools and tests; the download route looks up by hash).
export async function verifyToken(env, token, nonce, storedHash) {
  if (typeof token !== 'string' || !TOKEN_RE.test(token)) return false;
  const a = timingSafeEqual(await tokenHash(token), storedHash);
  const b = nonce ? timingSafeEqual(await tokenFromNonce(env, nonce), token) : true;
  return a && b;
}
export async function ipHash(env, ip) { return ip ? toHex(await hmacBytes(needSalt(env), 'mi-ip|' + ip)).slice(0, 32) : null; }
export function clientIp(request) { return request.headers.get('CF-Connecting-IP') || null; }
export function linkUrl(env, token) { return `${String(env.SITE_URL || '').replace(/\/+$/, '')}/api/download/${token}`; }

// ---------- manifest ----------
export function manifestKey(productId, format = 'pdf') { return `${productId}:${format}`; }
export function lookupManifest(manifest, productId, format = 'pdf') {
  const e = manifest && manifest.files && manifest.files[manifestKey(productId, format)];
  return e && e.r2_key && e.filename ? e : null;
}
async function defaultManifest() { return (await import('../../data/delivery_manifest.json', { with: { type: 'json' } })).default; }

// ---------- Stripe session -> items ----------
// Contract for the shop checkout (documented in docs/shop/delivery_plan.md): Checkout Session metadata
//   mi_items = "ext-p1:pdf,ext-p2:pdf"  (product_id:format, comma separated; physical items are simply not listed)
//   mi_order = optional short order reference shown to the buyer (else MI-<last 8 of the session id>)
export function itemsFromSession(session) {
  const raw = session && session.metadata && session.metadata.mi_items;
  if (typeof raw !== 'string') return [];
  const out = [], seen = new Set();
  for (const part of raw.split(',')) {
    const [p, f = 'pdf'] = part.trim().split(':');
    if (!/^[a-z0-9][a-z0-9._-]{0,79}$/i.test(p || '') || !/^(pdf|zip|other)$/.test(f)) continue;
    const k = p + ':' + f; if (seen.has(k)) continue; seen.add(k); out.push({ product_id: p, format: f });
  }
  return out;
}
export function buyerEmailOf(session) {
  const e = (session.customer_details && session.customer_details.email) || session.customer_email || '';
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e) && e.length <= 254 ? e.toLowerCase() : null;
}
export function orderIdOf(session) {
  const m = session.metadata && session.metadata.mi_order;
  if (typeof m === 'string' && /^[A-Za-z0-9-]{3,40}$/.test(m)) return m;
  return 'MI-' + String(session.id || 'unknown').slice(-8).toUpperCase();
}

// ---------- grantEntitlements: THE HOOK the Stripe webhook calls on payment success ----------
// grantEntitlements(env, session, items, opts) -> { order_id, granted:[{product_id,format,url,created}], missing:[product ids not in the manifest], emailed:boolean|null }
// Idempotent: a repeated webhook for the same session returns the same links (same nonce) and does not send a second email.
// Throws only on infrastructure failure (database down), so the webhook can answer non-2xx and Stripe retries.
export async function grantEntitlements(env, session, items, opts = {}) {
  const rpc = opts.rpc || ((fn, args) => supabaseRpc(env, fn, args));
  const manifest = opts.manifest || await defaultManifest();
  const now = opts.now ? opts.now() : Date.now();
  const days = Number(env.DELIVERY_EXPIRY_DAYS) > 0 ? Number(env.DELIVERY_EXPIRY_DAYS) : DEFAULT_EXPIRY_DAYS;
  const max = Number(env.DELIVERY_MAX_DOWNLOADS) > 0 ? Number(env.DELIVERY_MAX_DOWNLOADS) : DEFAULT_MAX_DOWNLOADS;
  const orderId = orderIdOf(session), email = buyerEmailOf(session), sid = String(session.id || '');
  if (!sid) throw new Error('grantEntitlements: session has no id');
  const granted = [], missing = [];
  for (const it of items || []) {
    const m = lookupManifest(manifest, it.product_id, it.format || 'pdf');
    if (!m) { missing.push(it.product_id); console.error(`delivery: NEEDS OWNER ATTENTION product ${it.product_id} has no manifest entry (order ${orderId})`); continue; }
    const s = await newLinkSecrets(env);
    const row = await rpc('service_grant_entitlement', {
      p_order_id: orderId, p_session_id: sid, p_product_id: it.product_id, p_format: it.format || 'pdf', p_email: email,
      p_r2_key: m.r2_key, p_filename: m.filename, p_version: m.version || null, p_sha256: m.sha256 || null,
      p_nonce: s.nonce, p_token_hash: s.hash, p_expires_at: new Date(now + days * 86400000).toISOString(), p_max: max, p_source: 'stripe', p_note: null, p_created_by: null,
    });
    const token = await tokenFromNonce(env, row.link_nonce);   // the existing row's nonce on a repeat, ours on first grant
    granted.push({ product_id: it.product_id, format: row.format, name: m.title || m.filename, filename: row.filename, url: linkUrl(env, token), expires_at: row.expires_at, max_downloads: row.max_downloads, created: row.created });
  }
  let emailed = null;
  if (granted.length && email && env.RESEND_API_KEY && env.EMAIL_FROM) {
    const claimed = await rpc('service_claim_email', { p_session_id: sid });
    if (claimed === true) {
      try {
        await sendEmail(env, buildDeliveryEmail({ orderId, links: granted, env }), { idempotencyKey: `mi-delivery-${sid}`, to: email, fetch: opts.fetch });
        await rpc('service_mark_emailed', { p_session_id: sid });
        emailed = true;
      } catch (e) { emailed = false; console.error('delivery: email failed (links still work on the order page; resend from admin):', String(e && e.message || e)); }
    }
  }
  return { order_id: orderId, granted, missing, emailed };
}

// ---------- shop amount check (STUB: prices are on hold, owner decision 23 Oct 2026) ----------
// SHOP_PRICES_CENTS maps product_id -> expected price in SGD cents. While it is EMPTY nothing is checked (documented gap, audit F6): safety then rests on
// the owner creating Stripe Payment Links with the right price and metadata. Once prices are decided, fill it in (or load from a price table); then a paid
// session whose amount_total differs from the sum of its listed products, or whose currency is not SGD, is NOT granted and is logged for the owner.
// An item with no price entry is not checked individually; if ANY listed item has a price, ALL listed items must have one (otherwise the sum is unknowable and the order is held).
export const SHOP_PRICES_CENTS = {};
export function checkShopAmount(session, items, prices = SHOP_PRICES_CENTS) {
  const priced = (items || []).filter(i => Object.prototype.hasOwnProperty.call(prices, i.product_id));
  if (!priced.length) return { ok: true, checked: false };
  if (priced.length !== items.length) return { ok: false, checked: true, reason: 'unpriced_item' };
  if (String(session.currency || '').toUpperCase() !== 'SGD') return { ok: false, checked: true, reason: 'currency_mismatch' };
  const expected = items.reduce((s, i) => s + prices[i.product_id], 0);
  return session.amount_total === expected ? { ok: true, checked: true } : { ok: false, checked: true, reason: 'amount_mismatch', expected };
}

// Called from the Stripe webhook (one marked line there). Returns a Response when the event was a shop order, else null so the webhook carries on.
export async function maybeHandleShopOrder({ env, type, session }, opts = {}) {
  const items = itemsFromSession(session);
  if (!items.length) return null;
  if (!['checkout.session.completed', 'checkout.session.async_payment_succeeded'].includes(type)) return json({ ok: true, ignored: 'shop: ' + type });
  if (session.payment_status !== 'paid') return json({ ok: true, ignored: 'shop: awaiting payment' });
  const amt = checkShopAmount(session, items, opts.prices);
  if (!amt.ok) { console.error(`delivery: NEEDS OWNER ATTENTION shop ${amt.reason} session=${session.id} amount_total=${session.amount_total} expected=${amt.expected}`); return json({ ok: true, shop: false, result: amt.reason }); }   // 200: a retry would not fix it
  try {
    const r = await grantEntitlements(env, session, items, opts);
    return json({ ok: true, shop: true, order: r.order_id, granted: r.granted.length, missing: r.missing, emailed: r.emailed });
  } catch (e) { console.error('delivery: grant failed', String(e && e.message || e)); return json({ error: 'try again' }, 502); }   // non-2xx so Stripe retries
}

// ---------- download ----------
// RFC 7233, single range only. Returns null (no/ignored header), {start,end} (inclusive) or 'invalid' (-> 416).
export const RANGE_RE = /^bytes=(\d*)-(\d*)$/;
export function parseRange(header, size) {
  if (!header) return null;
  const m = RANGE_RE.exec(String(header).trim());
  if (!m) return null;                      // multi-range, other units: ignored, the whole file is sent (and counted)
  if (m[1] === '' && m[2] === '') return 'invalid';
  let start, end;
  if (m[1] === '') { const n = Number(m[2]); if (n === 0) return 'invalid'; start = Math.max(size - n, 0); end = size - 1; }
  else { start = Number(m[1]); end = m[2] === '' ? size - 1 : Math.min(Number(m[2]), size - 1); }
  if (start >= size || start > end) return 'invalid';
  return { start, end };
}
export function contentDisposition(filename) {
  const ascii = String(filename).replace(/[^\x20-\x7e]/g, '_').replace(/["\\]/g, '_');
  return `attachment; filename="${ascii}"; filename*=UTF-8''${encodeURIComponent(filename)}`;
}
function baseHeaders() {
  return { 'Cache-Control': 'no-store, private', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'no-referrer', 'X-Robots-Tag': 'noindex, nofollow', 'Accept-Ranges': 'bytes' };
}
function page(status, title, msg) {
  const body = `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>${title}</title>` +
    `<body style="font:16px/1.5 system-ui,sans-serif;max-width:32rem;margin:3rem auto;padding:0 1rem"><h1>${title}</h1><p>${msg}</p></body></html>`;
  return new Response(body, { status, headers: { ...baseHeaders(), 'Content-Type': 'text/html; charset=utf-8' } });
}
const WHY = {
  not_found: [404, 'Link not found', 'This download link is not valid. Please check you copied the whole link.'],
  expired: [410, 'Link expired', 'This download link has expired. Message us on WhatsApp with your order number and we will send a new one.'],
  revoked: [410, 'Link withdrawn', 'This download link is no longer active. Message us on WhatsApp with your order number.'],
  exhausted: [410, 'Download limit reached', 'This link has been used the maximum number of times. Message us on WhatsApp with your order number and we will help.'],
  range_denied: [403, 'Start the download again', 'Please start the download from the beginning.'],
  rate_limited: [429, 'Too many requests', 'Please wait a few minutes and try again.'],
};

// In-isolate burst limiter (first line of defence; the database limit in service_download_begin is the real one). Exported for tests.
const burst = new Map();
export function burstLimited(key, now = Date.now(), max = 60, windowMs = 60000) {
  if (!key) return false;
  const arr = (burst.get(key) || []).filter((t) => now - t < windowMs);
  arr.push(now); burst.set(key, arr);
  if (burst.size > 5000) for (const [k, v] of burst) if (!v.length || now - v[v.length - 1] > windowMs) burst.delete(k);
  return arr.length > max;
}
export function _resetBurst() { burst.clear(); }

export async function handleDownload({ request, env, token }, opts = {}) {
  if (request.method !== 'GET') return new Response(null, { status: 405, headers: { ...baseHeaders(), Allow: 'GET' } });   // HEAD is refused so link checkers and previews never use a download
  const rpc = opts.rpc || ((fn, args) => supabaseRpc(env, fn, args));
  if (!env.DELIVERY_BUCKET || !env.SUPABASE_URL || !env.SUPABASE_SERVICE_ROLE_KEY || !env.DELIVERY_TOKEN_SALT) { console.error('download: not configured'); return page(503, 'Not available', 'Downloads are not available right now. Please message us on WhatsApp.'); }
  if (!TOKEN_RE.test(token || '')) return page(...WHY.not_found);
  const ip = await ipHash(env, clientIp(request));
  if (burstLimited(ip, opts.now ? opts.now() : Date.now())) return page(...WHY.rate_limited);
  const hash = await tokenHash(token);
  const rangeHeader = request.headers.get('Range');
  // Parse the range before touching the database: the first byte decides whether this request consumes a download.
  const probe = rangeHeader ? RANGE_RE.exec(rangeHeader.trim()) : null;
  const count = !(probe && probe[1] !== '' && Number(probe[1]) > 0);
  let res;
  try { res = await rpc('service_download_begin', { p_token_hash: hash, p_ip_hash: ip, p_count: count, p_rate_max: 30, p_rate_window_min: 10 }); }
  catch (e) { console.error('download: database error', String(e && e.message || e)); return page(503, 'Try again', 'Something went wrong on our side. Please try again in a minute.'); }
  if (!res || res.status !== 'ok') { const w = WHY[res && res.status] || WHY.not_found; return page(...w); }
  const release = async () => { if (count) { try { await rpc('service_download_release', { p_entitlement: res.entitlement_id }); } catch (e) { console.error('download: release failed', String(e)); } } };
  let head;
  try { head = await env.DELIVERY_BUCKET.head(res.r2_key); } catch (e) { head = null; console.error('download: R2 head failed', String(e)); }
  if (!head) { await release(); console.error(`download: NEEDS OWNER ATTENTION file missing in R2: ${res.r2_key} (order ${res.order_id})`); return page(503, 'Try again later', 'We could not fetch your file. Your download was not used. Please message us on WhatsApp and we will fix it.'); }
  const size = head.size;
  const rg = parseRange(rangeHeader, size);
  if (rg === 'invalid') { await release(); return new Response(null, { status: 416, headers: { ...baseHeaders(), 'Content-Range': `bytes */${size}` } }); }
  let obj;
  try { obj = rg ? await env.DELIVERY_BUCKET.get(res.r2_key, { range: { offset: rg.start, length: rg.end - rg.start + 1 } }) : await env.DELIVERY_BUCKET.get(res.r2_key); }
  catch (e) { obj = null; console.error('download: R2 get failed', String(e)); }
  if (!obj || !obj.body) { await release(); return page(503, 'Try again later', 'We could not fetch your file. Your download was not used. Please message us on WhatsApp.'); }
  const headers = { ...baseHeaders(), 'Content-Type': 'application/pdf', 'Content-Disposition': contentDisposition(res.filename) };
  if (rg) { headers['Content-Range'] = `bytes ${rg.start}-${rg.end}/${size}`; headers['Content-Length'] = String(rg.end - rg.start + 1); return new Response(obj.body, { status: 206, headers }); }
  headers['Content-Length'] = String(size);
  return new Response(obj.body, { status: 200, headers });
}

// ---------- order success page data ----------
export async function handleOrderLinks({ request, env }, opts = {}) {
  const rpc = opts.rpc || ((fn, args) => supabaseRpc(env, fn, args));
  if (request.method !== 'GET') return json({ error: 'Method not allowed' }, 405);
  if (!env.SUPABASE_URL || !env.SUPABASE_SERVICE_ROLE_KEY || !env.DELIVERY_TOKEN_SALT) return json({ error: 'not configured' }, 503);
  const sid = new URL(request.url).searchParams.get('session_id') || '';
  if (!SESSION_RE.test(sid)) return json({ error: 'bad session' }, 400);
  try {
    const ip = await ipHash(env, clientIp(request));
    if (ip && !(await rpc('service_links_rate', { p_ip_hash: ip, p_max: 20, p_window_min: 10 }))) return json({ error: 'too many requests' }, 429);
    const rows = await rpc('service_order_entitlements', { p_session_id: sid });
    if (!rows || !rows.length) return json({ status: 'pending' }, 202);   // webhook has not run yet; the page polls
    const links = [];
    for (const r of rows) links.push({ product_id: r.product_id, name: r.filename, revoked: !!r.revoked, expires_at: r.expires_at, remaining: Math.max(r.max_downloads - r.download_count, 0), url: r.revoked ? null : linkUrl(env, await tokenFromNonce(env, r.link_nonce)) });
    return json({ status: 'ready', order_id: rows[0].order_id, links });
  } catch (e) { console.error('order-links:', String(e && e.message || e)); return json({ error: 'try again' }, 503); }
}
