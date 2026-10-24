// POST /api/stripe-create-checkout   Authorization: Bearer <Supabase user access token>   body: {"enrolment_id": "<uuid>"}
// Creates a Stripe Checkout Session (mode payment, SGD, card + PayNow) for the caller's own pending enrolment and returns {url}.
// The amount always comes from the database, never from the browser. Secrets: STRIPE_SECRET_KEY, SUPABASE_SERVICE_ROLE_KEY (Cloudflare secrets).
import { json, requireEnv, supabaseRpc, stripeBody, STRIPE_API, UUID_RE } from '../lib.js';

export async function onRequestPost({ request, env }) {
  const missing = requireEnv(env, ['SUPABASE_URL', 'SUPABASE_ANON_KEY', 'SUPABASE_SERVICE_ROLE_KEY', 'STRIPE_SECRET_KEY', 'SITE_URL']);
  if (missing) { console.error('stripe-create-checkout: missing env', missing.join(',')); return json({ error: 'Payments are not configured yet.' }, 500); }

  // 1. who is calling? Ask Supabase Auth to validate the user's token.
  const auth = request.headers.get('Authorization') || '';
  const token = auth.startsWith('Bearer ') ? auth.slice(7) : '';
  if (!token) return json({ error: 'Please log in again.' }, 401);
  const u = await fetch(`${env.SUPABASE_URL}/auth/v1/user`, { headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${token}` } });
  if (!u.ok) return json({ error: 'Please log in again.' }, 401);
  const user = await u.json();
  if (!user || !UUID_RE.test(user.id || '')) return json({ error: 'Please log in again.' }, 401);

  // 2. which enrolment? Must belong to this user and still be unpaid.
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Bad request.' }, 400); }
  const enrolmentId = body && body.enrolment_id;
  if (typeof enrolmentId !== 'string' || !UUID_RE.test(enrolmentId)) return json({ error: 'Bad request.' }, 400);
  let rows;
  try { rows = await supabaseRpc(env, 'service_begin_payment', { p_enrolment: enrolmentId, p_parent: user.id }); }
  catch (e) { console.error(String(e)); return json({ error: 'Could not look up your reservation.' }, 502); }
  const row = rows && rows[0];
  if (!row) return json({ error: 'Reservation not found.' }, 404);
  if (row.payment_status !== 'pending' || row.enrolment_status !== 'pending_payment') return json({ error: 'This reservation is not waiting for payment.' }, 409);
  if (!Number.isInteger(row.amount_cents) || row.amount_cents <= 0 || String(row.currency).toUpperCase() !== 'SGD') return json({ error: 'This reservation cannot be paid online.' }, 409);
  if (row.group_fee_cents !== row.amount_cents) console.error(`stripe-create-checkout: group fee changed since reservation payment=${row.payment_id}; charging the reserved amount`);

  // 3. create the Checkout Session. Card and PayNow (PayNow requires SGD). Redirect-based: no Stripe.js on our pages.
  const site = env.SITE_URL.replace(/\/$/, '');
  const form = {
    mode: 'payment',
    payment_method_types: ['paynow', 'card'],
    line_items: [{ quantity: 1, price_data: { currency: 'sgd', unit_amount: row.amount_cents, product_data: { name: `Math Inquirers beta program${row.group_name ? ' | ' + row.group_name : ''}` } } }],
    client_reference_id: row.payment_id,
    customer_email: row.parent_email || undefined,
    metadata: { payment_id: row.payment_id, enrolment_id: enrolmentId, reference: row.reference },
    payment_intent_data: { metadata: { payment_id: row.payment_id, enrolment_id: enrolmentId, reference: row.reference }, description: `Math Inquirers ${row.reference}` },
    success_url: `${site}/portal/?paid=${enrolmentId}&session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${site}/portal/?cancelled=${enrolmentId}`,
  };
  const st = await fetch(`${STRIPE_API}/checkout/sessions`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded',
      // one key per payment and attempt: a double click returns the same session; after an expiry the DB bumps `attempt`.
      'Idempotency-Key': `mi-checkout-${row.payment_id}-${row.attempt || 0}`,
    },
    body: stripeBody(form),
  });
  if (!st.ok) { console.error('stripe-create-checkout: Stripe returned', st.status); return json({ error: 'The payment provider did not accept the request. Please try again.' }, 502); }
  const made = await st.json();
  if (!made || typeof made.url !== 'string' || !made.id || !made.url.startsWith('https://checkout.stripe.com/')) return json({ error: 'Unexpected reply from the payment provider.' }, 502);
  try { await supabaseRpc(env, 'service_attach_session', { p_payment: row.payment_id, p_session_id: String(made.id) }); }
  catch (e) { console.error(String(e)); /* not fatal: the webhook matches on client_reference_id */ }
  return json({ url: made.url });
}

export async function onRequest() { return json({ error: 'Method not allowed' }, 405); }
