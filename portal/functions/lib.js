// Shared helpers for the Stripe Pages Functions. Pure Web APIs (fetch, crypto.subtle) so they run on Cloudflare Workers and in Node 20+.
// NOTE: Cloudflare Pages would treat this file as a route module only if it exports onRequest*; it does not.

export const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
export const STRIPE_API = 'https://api.stripe.com/v1';
export const STRIPE_TOLERANCE_SECONDS = 300;

export function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
}

export function requireEnv(env, names) {
  const missing = names.filter((n) => !env[n]);
  return missing.length ? missing : null;
}

const enc = new TextEncoder();
export function toHex(buf) { return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join(''); }
export async function hmacHex(secret, message) {
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return toHex(await crypto.subtle.sign('HMAC', key, enc.encode(message)));
}
// Constant-time comparison of two strings (length is not secret: signatures are fixed-length hex).
export function timingSafeEqual(a, b) {
  const x = enc.encode(String(a)), y = enc.encode(String(b));
  let diff = x.length ^ y.length;
  const n = Math.max(x.length, y.length);
  for (let i = 0; i < n; i++) diff |= (x[i] || 0) ^ (y[i] || 0);
  return diff === 0;
}

// Stripe-Signature header: "t=1700000000,v1=<hex>,v1=<hex>,v0=<hex>". Signed payload = `${t}.${rawBody}`, HMAC-SHA256 with the endpoint secret (whsec_...).
// Returns {ok:true} or {ok:false, reason}. `nowSec` is injectable for tests.
export async function verifyStripeSignature(secret, rawBody, header, nowSec = Math.floor(Date.now() / 1000), tolerance = STRIPE_TOLERANCE_SECONDS) {
  if (!secret || typeof header !== 'string' || !header) return { ok: false, reason: 'missing' };
  let t = null; const v1 = [];
  for (const part of header.split(',')) {
    const i = part.indexOf('=');
    if (i < 0) continue;
    const k = part.slice(0, i).trim(), v = part.slice(i + 1).trim();
    if (k === 't') t = v; else if (k === 'v1') v1.push(v);
  }
  if (!t || !/^\d{1,12}$/.test(t) || !v1.length) return { ok: false, reason: 'malformed' };
  if (Math.abs(nowSec - Number(t)) > tolerance) return { ok: false, reason: 'stale' };
  const expected = await hmacHex(secret, `${t}.${rawBody}`);
  let match = false;
  for (const s of v1) if (timingSafeEqual(expected, s)) match = true;   // no early exit
  return match ? { ok: true } : { ok: false, reason: 'mismatch' };
}

// Stripe wants application/x-www-form-urlencoded with bracket notation for nested objects and arrays.
export function stripeForm(obj, prefix = '', out = []) {
  for (const [k, v] of Object.entries(obj)) {
    if (v === undefined || v === null) continue;
    const key = prefix ? `${prefix}[${k}]` : k;
    if (Array.isArray(v)) v.forEach((x, i) => (x !== null && typeof x === 'object' ? stripeForm(x, `${key}[${i}]`, out) : out.push([`${key}[${i}]`, String(x)])));
    else if (typeof v === 'object') stripeForm(v, key, out);
    else out.push([key, String(v)]);
  }
  return out;
}
export function stripeBody(obj) { return stripeForm(obj).map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`).join('&'); }

export async function supabaseRpc(env, fn, args) {
  const r = await fetch(`${env.SUPABASE_URL}/rest/v1/rpc/${fn}`, {
    method: 'POST',
    headers: { apikey: env.SUPABASE_SERVICE_ROLE_KEY, Authorization: `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(args),
  });
  if (!r.ok) throw new Error(`supabase rpc ${fn} failed: ${r.status}`);
  return r.json();
}
