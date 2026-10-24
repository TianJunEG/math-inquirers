// GET /api/order-links?session_id=cs_...   the order success page asks for the download links of its own checkout session.
// The Stripe session id (unguessable, only in the buyer's redirect URL) is the proof of purchase. Rate limited. Never cached.
import { handleOrderLinks } from '../_shared/delivery.js';
export async function onRequest({ request, env }) { return handleOrderLinks({ request, env }); }
