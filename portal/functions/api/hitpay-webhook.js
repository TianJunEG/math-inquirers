// POST /api/hitpay-webhook   called by HitPay when a payment request is completed.
// 1. verify the HMAC-SHA256 signature with HITPAY_SALT  2. ignore anything that is not a completed payment
// 3. mark the payment paid through the service-role-only SQL function (idempotent, checks the amount).
import { json, requireEnv, verifyHmacHex, legacyPayload, supabaseRpc, UUID_RE } from '../lib.js';

export async function onRequestPost({ request, env }) {
  const missing = requireEnv(env, ['SUPABASE_URL', 'SUPABASE_SERVICE_ROLE_KEY', 'HITPAY_SALT']);
  if (missing) { console.error('hitpay-webhook: missing env', missing.join(',')); return json({ error: 'not configured' }, 500); }

  const raw = await request.text();            // hash the exact bytes HitPay sent, never a re-serialised copy
  const headerSig = request.headers.get('Hitpay-Signature');
  let data;
  if (headerSig) {                              // current scheme: JSON body + Hitpay-Signature header
    if (!(await verifyHmacHex(env.HITPAY_SALT, raw, headerSig))) return json({ error: 'bad signature' }, 401);
    try { data = JSON.parse(raw); } catch { return json({ error: 'bad body' }, 400); }
  } else if ((request.headers.get('Content-Type') || '').includes('application/x-www-form-urlencoded')) {   // legacy per-request webhook
    const params = Object.fromEntries(new URLSearchParams(raw));
    if (!params.hmac || !(await verifyHmacHex(env.HITPAY_SALT, legacyPayload(params), params.hmac))) return json({ error: 'bad signature' }, 401);
    data = params;
  } else {
    return json({ error: 'bad signature' }, 401);
  }

  // Only completed payments matter. Everything else is acknowledged so HitPay stops retrying.
  const status = String(data.status || '').toLowerCase();
  if (status !== 'completed' && status !== 'succeeded') return json({ ok: true, ignored: status || 'no status' });
  const enrolmentId = data.reference_number;
  if (typeof enrolmentId !== 'string' || !UUID_RE.test(enrolmentId)) return json({ ok: true, ignored: 'unknown reference' });
  if (data.currency && String(data.currency).toUpperCase() !== 'SGD') { console.error('hitpay-webhook: unexpected currency for', enrolmentId); return json({ ok: true, ignored: 'currency' }); }
  const amount = Number(data.amount);
  if (!Number.isFinite(amount) || amount <= 0) return json({ ok: true, ignored: 'amount' });
  const cents = Math.round(amount * 100);
  const requestId = data.payment_request_id || data.id || null;
  const paymentId = data.payment_id || (Array.isArray(data.payments) && data.payments[0] && data.payments[0].id) || null;

  let result;
  try { result = await supabaseRpc(env, 'service_mark_hitpay_paid', { p_enrolment: enrolmentId, p_request_id: requestId && String(requestId), p_payment_id: paymentId && String(paymentId), p_amount_cents: cents }); }
  catch (e) { console.error(String(e)); return json({ error: 'try again' }, 502); }   // non-2xx so HitPay retries
  if (result === 'amount_mismatch' || result === 'paid_enrolment_cancelled') console.error(`hitpay-webhook: NEEDS OWNER ATTENTION ${result} enrolment=${enrolmentId}`);
  return json({ ok: true, result });
}

export async function onRequest() { return json({ error: 'Method not allowed' }, 405); }
