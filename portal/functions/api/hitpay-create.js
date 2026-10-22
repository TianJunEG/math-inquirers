// POST /api/hitpay-create   Authorization: Bearer <Supabase user access token>   body: {"enrolment_id": "<uuid>"}
// Creates a HitPay payment request for the caller's own pending enrolment and returns {url} (hosted checkout).
// The amount always comes from the database, never from the browser.
import { json, requireEnv, hitpayBase, supabaseRpc, UUID_RE } from '../lib.js';

export async function onRequestPost({ request, env }) {
  const missing = requireEnv(env, ['SUPABASE_URL', 'SUPABASE_ANON_KEY', 'SUPABASE_SERVICE_ROLE_KEY', 'HITPAY_API_KEY', 'SITE_URL']);
  if (missing) { console.error('hitpay-create: missing env', missing.join(',')); return json({ error: 'Payments are not configured yet.' }, 500); }

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
  try { rows = await supabaseRpc(env, 'service_begin_hitpay', { p_enrolment: enrolmentId, p_parent: user.id }); }
  catch (e) { console.error(String(e)); return json({ error: 'Could not look up your reservation.' }, 502); }
  const row = rows && rows[0];
  if (!row) return json({ error: 'Reservation not found.' }, 404);
  if (row.payment_status !== 'pending' || row.enrolment_status !== 'pending_payment') return json({ error: 'This reservation is not waiting for payment.' }, 409);

  // 3. create the HitPay payment request (JSON body; see https://docs.hitpayapp.com/apis/payment-request/create-request)
  const site = env.SITE_URL.replace(/\/$/, '');
  const payload = {
    amount: (row.amount_cents / 100).toFixed(2),
    currency: 'SGD',
    payment_methods: ['card', 'paynow_online'],
    purpose: 'Math Inquirers beta program',
    reference_number: enrolmentId,
    redirect_url: `${site}/portal/?paid=${enrolmentId}`,
    webhook: `${site}/api/hitpay-webhook`,
    email: row.parent_email || undefined,
    name: row.parent_name || undefined,
  };
  const hp = await fetch(`${hitpayBase(env)}/v1/payment-requests`, {
    method: 'POST',
    headers: { 'X-BUSINESS-API-KEY': env.HITPAY_API_KEY, 'Content-Type': 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
    body: JSON.stringify(payload),
  });
  if (!hp.ok) { console.error('hitpay-create: HitPay returned', hp.status); return json({ error: 'The payment provider did not accept the request. Please try again.' }, 502); }
  const made = await hp.json();
  if (!made || typeof made.url !== 'string' || !made.id) return json({ error: 'Unexpected reply from the payment provider.' }, 502);
  try { await supabaseRpc(env, 'service_attach_hitpay', { p_enrolment: enrolmentId, p_request_id: String(made.id) }); }
  catch (e) { console.error(String(e)); /* not fatal: the webhook matches on reference_number */ }
  return json({ url: made.url });
}

export async function onRequest() { return json({ error: 'Method not allowed' }, 405); }
