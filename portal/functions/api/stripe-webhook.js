// POST /api/stripe-webhook   called by Stripe. Events: checkout.session.completed, checkout.session.async_payment_succeeded,
// checkout.session.async_payment_failed, checkout.session.expired.
// 1. verify the Stripe-Signature header (HMAC-SHA256, 5 minute tolerance, constant-time) over the RAW body
// 2. mark paid / reset through service-role-only SQL functions (idempotent; DB checks amount in cents and currency).
// Secrets: STRIPE_WEBHOOK_SECRET (whsec_...), SUPABASE_SERVICE_ROLE_KEY.
import { json, requireEnv, verifyStripeSignature, supabaseRpc, UUID_RE } from '../lib.js';

function paymentIdOf(session) {
  const id = session.client_reference_id || (session.metadata && session.metadata.payment_id);
  return typeof id === 'string' && UUID_RE.test(id) ? id : null;
}

export async function onRequestPost({ request, env }) {
  const missing = requireEnv(env, ['SUPABASE_URL', 'SUPABASE_SERVICE_ROLE_KEY', 'STRIPE_WEBHOOK_SECRET']);
  if (missing) { console.error('stripe-webhook: missing env', missing.join(',')); return json({ error: 'not configured' }, 500); }

  const raw = await request.text();   // verify the exact bytes Stripe sent, never a re-serialised copy
  const v = await verifyStripeSignature(env.STRIPE_WEBHOOK_SECRET, raw, request.headers.get('Stripe-Signature'));
  if (!v.ok) { console.error('stripe-webhook: signature rejected:', v.reason); return json({ error: 'bad signature' }, 400); }
  let event;
  try { event = JSON.parse(raw); } catch { return json({ error: 'bad body' }, 400); }
  const type = event && event.type, session = event && event.data && event.data.object;
  if (!type || !session || typeof session !== 'object') return json({ ok: true, ignored: 'no object' });

  const handled = ['checkout.session.completed', 'checkout.session.async_payment_succeeded', 'checkout.session.async_payment_failed', 'checkout.session.expired'];
  if (!handled.includes(type)) return json({ ok: true, ignored: type });
  if (session.mode && session.mode !== 'payment') return json({ ok: true, ignored: 'mode' });
  // MI-DELIVERY-HOOK: shop orders carry metadata.mi_items (soft-copy products); grant download links and email them. Docs: docs/shop/delivery_plan.md
  if (session.metadata && session.metadata.mi_items) { const shop = await (await import('../_shared/delivery.js')).maybeHandleShopOrder({ env, type, session }); if (shop) return shop; }
  const paymentId = paymentIdOf(session);
  if (!paymentId) return json({ ok: true, ignored: 'unknown reference' });

  let result;
  try {
    if (type === 'checkout.session.expired' || type === 'checkout.session.async_payment_failed') {
      result = await supabaseRpc(env, 'service_mark_session_failed', { p_payment: paymentId, p_session_id: String(session.id || '') });
    } else {
      // completed: PayNow may still be unpaid here (bank transfer pending); the money is confirmed by async_payment_succeeded.
      if (session.payment_status !== 'paid') return json({ ok: true, ignored: 'awaiting payment' });
      const cents = session.amount_total;
      if (!Number.isInteger(cents) || cents <= 0) return json({ ok: true, ignored: 'amount' });
      const pi = typeof session.payment_intent === 'string' ? session.payment_intent : (session.payment_intent && session.payment_intent.id) || null;
      result = await supabaseRpc(env, 'service_mark_paid', { p_payment: paymentId, p_session_id: session.id ? String(session.id) : null, p_payment_intent: pi, p_amount_cents: cents, p_currency: String(session.currency || '') });
    }
  } catch (e) { console.error(String(e)); return json({ error: 'try again' }, 502); }   // non-2xx so Stripe retries
  if (['amount_mismatch', 'currency_mismatch', 'paid_enrolment_cancelled', 'not_found'].includes(result)) console.error(`stripe-webhook: NEEDS OWNER ATTENTION ${result} payment=${paymentId} event=${event.id}`);
  return json({ ok: true, result });
}

export async function onRequest() { return json({ error: 'Method not allowed' }, 405); }
