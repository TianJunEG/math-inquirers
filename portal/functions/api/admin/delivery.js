// POST /api/admin/delivery   admin only. Body: { action, ... }; header Authorization: Bearer <admin's Supabase access token>.
// Every database call runs AS THE ADMIN (their token), so the SQL admin_* functions enforce is_admin(); this file adds no extra trust.
//   list            { limit? }                                  -> entitlements (no tokens)
//   create          { product_id? | r2_key, email?, days?, max?, note? } -> one-off link, WITHOUT payment (beta PDF fallback, WhatsApp delivery). The link is shown ONCE here.
//   resend          { id, days?, reset_count? }                  -> extends expiry, emails the buyer (or returns the link when there is no email)
//   revoke          { id, reason? }
//   purge_log       { days? }                                    -> deletes download log rows older than days (default 90)
import { json, UUID_RE } from '../../lib.js';
import { newLinkSecrets, tokenFromNonce, linkUrl, lookupManifest, DEFAULT_EXPIRY_DAYS, DEFAULT_MAX_DOWNLOADS } from '../../_shared/delivery.js';
import { sendEmail, buildDeliveryEmail } from '../../_shared/email.js';

async function userRpc(env, token, fn, args, f = fetch) {
  const r = await f(`${env.SUPABASE_URL}/rest/v1/rpc/${fn}`, { method: 'POST', headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' }, body: JSON.stringify(args) });
  if (r.status === 401 || r.status === 403) { const e = new Error('forbidden'); e.code = 403; throw e; }
  if (!r.ok) { const e = new Error(`rpc ${fn} failed: ${r.status}`); e.code = 502; throw e; }
  return r.json();
}

export async function handleAdminDelivery({ request, env }, opts = {}) {
  if (request.method !== 'POST') return json({ error: 'Method not allowed' }, 405);
  if (!env.SUPABASE_URL || !env.SUPABASE_ANON_KEY || !env.DELIVERY_TOKEN_SALT) return json({ error: 'not configured' }, 503);
  const m = /^Bearer (.+)$/.exec(request.headers.get('Authorization') || '');
  if (!m) return json({ error: 'sign in' }, 401);
  let b; try { b = await request.json(); } catch { return json({ error: 'bad body' }, 400); }
  const rpc = (fn, args) => (opts.rpc ? opts.rpc(fn, args, m[1]) : userRpc(env, m[1], fn, args));
  const manifest = opts.manifest || (await import('../../../data/delivery_manifest.json', { with: { type: 'json' } })).default;
  try {
    switch (b.action) {
      case 'list': return json({ rows: await rpc('admin_list_entitlements', { p_limit: Math.min(Number(b.limit) || 100, 500) }) });
      case 'revoke': {
        if (!UUID_RE.test(b.id || '')) return json({ error: 'bad id' }, 400);
        return json({ revoked: await rpc('admin_revoke_entitlement', { p_id: b.id, p_reason: String(b.reason || '').slice(0, 200) || null }) });
      }
      case 'purge_log': return json({ deleted: await rpc('admin_purge_delivery_log', { p_days: Math.max(Number(b.days) || 90, 1) }) });
      case 'create': {
        let key, filename;
        if (b.product_id) { const e = lookupManifest(manifest, String(b.product_id), b.format || 'pdf'); if (!e) return json({ error: 'product not in manifest' }, 400); key = e.r2_key; filename = e.filename; }
        else if (typeof b.r2_key === 'string' && /^[A-Za-z0-9._\/-]{1,300}$/.test(b.r2_key) && !b.r2_key.includes('..')) { key = b.r2_key; filename = String(b.filename || key.split('/').pop()).slice(0, 150); }
        else return json({ error: 'product_id or r2_key required' }, 400);
        const bucket = opts.bucket || env.DELIVERY_BUCKET;
        if (bucket && !(await bucket.head(key))) return json({ error: 'file not found in the bucket (upload it first)' }, 400);
        const email = b.email ? String(b.email).trim() : null;
        if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ error: 'bad email' }, 400);
        const s = await newLinkSecrets(env);
        const row = await rpc('admin_create_manual_entitlement', { p_label: String(b.product_id || 'manual'), p_r2_key: key, p_filename: filename, p_email: email, p_nonce: s.nonce, p_token_hash: s.hash,
          p_days: Number(b.days) || DEFAULT_EXPIRY_DAYS, p_max: Number(b.max) || DEFAULT_MAX_DOWNLOADS, p_note: b.note ? String(b.note).slice(0, 300) : null });
        const url = linkUrl(env, s.token);
        let emailed = false;
        if (email && b.send_email && env.RESEND_API_KEY && env.EMAIL_FROM) {
          try { await sendEmail(env, buildDeliveryEmail({ orderId: row.order_id, links: [{ name: row.filename, url, expires_at: row.expires_at, max_downloads: row.max_downloads }], env }), { to: email, idempotencyKey: 'mi-manual-' + row.id, fetch: opts.fetch }); emailed = true; }
          catch (e) { console.error('admin/delivery: email failed', String(e && e.message || e)); }
        }
        return json({ order_id: row.order_id, id: row.id, url, expires_at: row.expires_at, max_downloads: row.max_downloads, emailed });
      }
      case 'resend': {
        if (!UUID_RE.test(b.id || '')) return json({ error: 'bad id' }, 400);
        const rows = await rpc('admin_prepare_resend', { p_id: b.id, p_extend_days: Number(b.days) || DEFAULT_EXPIRY_DAYS, p_reset_count: !!b.reset_count });
        const r = Array.isArray(rows) ? rows[0] : rows;
        if (!r) return json({ error: 'not found or revoked' }, 404);
        const url = linkUrl(env, await tokenFromNonce(env, r.link_nonce));
        let emailed = false;
        if (r.buyer_email && env.RESEND_API_KEY && env.EMAIL_FROM) {
          try { await sendEmail(env, buildDeliveryEmail({ orderId: r.order_id, links: [{ name: r.filename, url, expires_at: r.expires_at, max_downloads: r.max_downloads }], env }), { to: r.buyer_email, fetch: opts.fetch }); emailed = true; }
          catch (e) { console.error('admin/delivery: resend email failed', String(e && e.message || e)); }
        }
        return json({ order_id: r.order_id, url: emailed ? undefined : url, emailed, expires_at: r.expires_at });
      }
      default: return json({ error: 'unknown action' }, 400);
    }
  } catch (e) {
    if (e && e.code === 403) return json({ error: 'forbidden' }, 403);
    if (e && /forbidden/.test(String(e.message))) return json({ error: 'forbidden' }, 403);
    console.error('admin/delivery:', String(e && e.message || e)); return json({ error: 'failed' }, 502);
  }
}
export async function onRequest(ctx) { return handleAdminDelivery(ctx); }
