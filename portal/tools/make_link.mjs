#!/usr/bin/env node
// One-off download link WITHOUT payment (beta PDF fallback, WhatsApp delivery). Run on the owner's own computer.
//   SUPABASE_URL=... SUPABASE_SERVICE_ROLE_KEY=... DELIVERY_TOKEN_SALT=... SITE_URL=https://YOUR-DOMAIN \
//     node portal/tools/make_link.mjs --product beta-workbook-l1 [--email parent@example.com] [--days 14] [--max 5] [--note "Tan family"]
// The three secrets come from your shell environment (never type them into chat or commit them). The same DELIVERY_TOKEN_SALT as in Cloudflare is required,
// otherwise the printed link would not match the stored hash. --dry-run prints the SQL-free plan without calling the database.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { newLinkSecrets, linkUrl, lookupManifest } from '../functions/_shared/delivery.js';
import { supabaseRpc } from '../functions/lib.js';

const a = process.argv.slice(2); const opt = (n, d) => { const i = a.indexOf('--' + n); return i >= 0 ? a[i + 1] : d; };
const manifest = JSON.parse(readFileSync(join(dirname(fileURLToPath(import.meta.url)), '..', 'data', 'delivery_manifest.json'), 'utf8'));
const product = opt('product'); if (!product) { console.error('usage: --product <id> (one of: ' + Object.keys(manifest.files).map((k) => k.replace(/:pdf$/, '')).join(', ') + ')'); process.exit(2); }
const m = lookupManifest(manifest, product, 'pdf'); if (!m) { console.error('unknown product ' + product); process.exit(2); }
const env = process.env;
for (const n of ['SUPABASE_URL', 'SUPABASE_SERVICE_ROLE_KEY', 'DELIVERY_TOKEN_SALT', 'SITE_URL']) if (!env[n]) { console.error('missing environment variable ' + n); process.exit(2); }
const s = await newLinkSecrets(env);
const days = Number(opt('days', 14)), max = Number(opt('max', 5));
const orderId = 'MANUAL-' + s.nonce.replace(/[^A-Za-z0-9]/g, '').slice(0, 8).toUpperCase();
const row = await supabaseRpc(env, 'service_grant_entitlement', { p_order_id: orderId, p_session_id: null, p_product_id: product, p_format: 'pdf', p_email: opt('email', null),
  p_r2_key: m.r2_key, p_filename: m.filename, p_version: m.version, p_sha256: m.sha256 || null, p_nonce: s.nonce, p_token_hash: s.hash,
  p_expires_at: new Date(Date.now() + days * 86400000).toISOString(), p_max: max, p_source: 'manual', p_note: opt('note', null), p_created_by: null });
console.log(`Order ${row.order_id}, expires ${row.expires_at}, ${row.max_downloads} downloads.\nSend this link (WhatsApp is fine):\n${linkUrl(env, s.token)}`);
