// Worker entry for the Workers static-assets deploy (wrangler.jsonc "main"). Pages Functions in /functions are not run on Workers,
// so this routes the same handlers by hand. Everything that is not a known /api route goes to the static site (env.ASSETS).
import { onRequest as download } from '../portal/functions/api/download/[token].js';
import { onRequest as orderLinks } from '../portal/functions/api/order-links.js';
import { onRequest as adminDelivery } from '../portal/functions/api/admin/delivery.js';
import * as stripeWebhookMod from '../portal/functions/api/stripe-webhook.js';
import * as stripeCheckoutMod from '../portal/functions/api/stripe-create-checkout.js';

// Pages semantics: a method-specific export (onRequestPost) wins over the catch-all onRequest (which answers 405).
const byMethod = (mod) => (ctx) => (ctx.request.method === 'POST' && mod.onRequestPost ? mod.onRequestPost(ctx) : mod.onRequest(ctx));
const stripeWebhook = byMethod(stripeWebhookMod);
const stripeCheckout = byMethod(stripeCheckoutMod);

const DOWNLOAD_PREFIX = '/api/download/';
const ROUTES = {
  '/api/order-links': orderLinks,
  '/api/admin/delivery': adminDelivery,
  '/api/stripe-webhook': stripeWebhook,
  '/api/stripe-create-checkout': stripeCheckout,
};

export async function route(request, env, ctx) {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/+$/, '') || '/';
  if (url.pathname.startsWith(DOWNLOAD_PREFIX)) {
    const token = decodeURIComponent(url.pathname.slice(DOWNLOAD_PREFIX.length).split('/')[0] || '');
    return download({ request, env, ctx, params: { token } });
  }
  const handler = ROUTES[path];
  if (handler) return handler({ request, env, ctx, params: {} });
  if (path.startsWith('/api/')) return new Response(JSON.stringify({ error: 'Not found' }), { status: 404, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });
  return env.ASSETS.fetch(request);
}

export default { fetch: (request, env, ctx) => route(request, env, ctx) };
