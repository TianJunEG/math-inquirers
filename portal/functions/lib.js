// Shared helpers for the HitPay Pages Functions. Pure Web APIs (fetch, crypto.subtle) so they run on Cloudflare Workers and in Node 20+.
// NOTE: Cloudflare Pages would treat this file as a route module only if it exports onRequest*; it does not.

export const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

export function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
}

export function requireEnv(env, names) {
  const missing = names.filter((n) => !env[n]);
  return missing.length ? missing : null;
}

export function hitpayBase(env) {
  return env.HITPAY_ENV === 'live' ? 'https://api.hit-pay.com' : 'https://api.sandbox.hit-pay.com';   // default to sandbox: live must be asked for
}

const enc = new TextEncoder();
async function hmacKey(secret, usage) {
  return crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, usage);
}
export function toHex(buf) { return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join(''); }
function fromHex(hex) {
  if (typeof hex !== 'string' || hex.length % 2 || !/^[0-9a-f]+$/i.test(hex)) return null;
  return Uint8Array.from(hex.match(/../g).map((x) => parseInt(x, 16)));
}
export async function hmacHex(secret, message) {
  return toHex(await crypto.subtle.sign('HMAC', await hmacKey(secret, ['sign']), enc.encode(message)));
}
// Constant-time check (crypto.subtle.verify compares in constant time).
export async function verifyHmacHex(secret, message, sigHex) {
  const sig = fromHex(sigHex);
  if (!sig) return false;
  return crypto.subtle.verify('HMAC', await hmacKey(secret, ['verify']), sig, enc.encode(message));
}

// Legacy HitPay scheme (per-request `webhook` URL, form-encoded body with an `hmac` field): sort keys, concatenate key+value, HMAC-SHA256 with the salt.
// UNVERIFIED against live HitPay, see README.
export function legacyPayload(params) {
  return Object.keys(params).filter((k) => k !== 'hmac').sort().map((k) => k + params[k]).join('');
}

export async function supabaseRpc(env, fn, args) {
  const r = await fetch(`${env.SUPABASE_URL}/rest/v1/rpc/${fn}`, {
    method: 'POST',
    headers: { apikey: env.SUPABASE_SERVICE_ROLE_KEY, Authorization: `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(args),
  });
  if (!r.ok) throw new Error(`supabase rpc ${fn} failed: ${r.status}`);
  return r.json();
}
