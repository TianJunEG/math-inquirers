// GET /api/download/<token>   streams a purchased PDF from the PRIVATE R2 bucket (binding DELIVERY_BUCKET). See docs/shop/delivery_plan.md.
// Secrets/vars: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, DELIVERY_TOKEN_SALT. Never cached, never public, no personal data in logs.
import { handleDownload } from '../../_shared/delivery.js';
export async function onRequest({ request, env, params }) {
  const token = Array.isArray(params && params.token) ? params.token[0] : params && params.token;
  return handleDownload({ request, env, token });
}
