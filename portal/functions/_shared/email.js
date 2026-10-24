// Provider-agnostic email adapter. sendEmail(env, message, opts) picks a provider by env.EMAIL_PROVIDER (default "resend").
// message = { subject, text, html, replyTo? }; opts = { to, idempotencyKey?, fetch? }.
// Secrets: RESEND_API_KEY. Config: EMAIL_FROM (for example "Math Inquirers <downloads@YOUR-DOMAIN>", the domain must be verified in Resend), EMAIL_REPLY_TO (optional).
// No tracking pixels or link rewriting are added here; also leave open/click tracking OFF in the Resend domain settings.
export const RESEND_API = 'https://api.resend.com/emails';

export async function sendViaResend(env, message, opts) {
  if (!env.RESEND_API_KEY) throw new Error('RESEND_API_KEY missing');
  if (!env.EMAIL_FROM) throw new Error('EMAIL_FROM missing');
  const to = Array.isArray(opts.to) ? opts.to : [opts.to];
  if (!to.length || to.some((a) => !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(a))) throw new Error('bad recipient');
  const payload = { from: env.EMAIL_FROM, to, subject: message.subject, html: message.html, text: message.text };
  const replyTo = message.replyTo || env.EMAIL_REPLY_TO;
  if (replyTo) payload.reply_to = replyTo;
  const headers = { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' };
  if (opts.idempotencyKey) headers['Idempotency-Key'] = String(opts.idempotencyKey).slice(0, 256);
  const r = await (opts.fetch || fetch)(RESEND_API, { method: 'POST', headers, body: JSON.stringify(payload) });
  if (!r.ok) throw new Error(`resend failed: ${r.status}`);   // never include the body: it can echo the address
  const body = await r.json().catch(() => ({}));
  return { ok: true, id: body.id || null };
}
const PROVIDERS = { resend: sendViaResend };
export async function sendEmail(env, message, opts = {}) {
  const p = PROVIDERS[String(env.EMAIL_PROVIDER || 'resend').toLowerCase()];
  if (!p) throw new Error('unknown EMAIL_PROVIDER');
  return p(env, message, opts);
}

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
export function sgtDate(iso) {
  return new Intl.DateTimeFormat('en-SG', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Singapore' }).format(new Date(iso));
}
// links = [{ name, url, expires_at, max_downloads }]. The licence line is DRAFT wording for the lawyer (see docs/shop/privacy_additions.md).
export function buildDeliveryEmail({ orderId, links, env = {} }) {
  const wa = env.SUPPORT_WHATSAPP ? String(env.SUPPORT_WHATSAPP) : '';
  const first = links[0] || {};
  const expiry = first.expires_at ? sgtDate(first.expires_at) : '';
  const max = first.max_downloads || 5;
  const licence = 'Licence: these files are for your own family\'s personal use. Please do not share, resell or upload them.';
  const subject = 'Your Math Inquirers download';
  const textLinks = links.map((l) => `- ${l.name}\n  ${l.url}`).join('\n');
  const text = [
    'Thank you for your order.', '', `Order: ${orderId}`, '', 'Your download links:', textLinks, '',
    `Each link works up to ${max} times and expires on ${expiry} (Singapore time). Keep this email, or save the PDF to your device when it downloads.`, '',
    licence, wa ? `Need help? WhatsApp us on ${wa} with your order number.` : 'Need help? Reply to this email with your order number.', '', 'Math Inquirers',
  ].join('\n');
  const htmlLinks = links.map((l) => `<li><a href="${esc(l.url)}">${esc(l.name)}</a></li>`).join('');
  const html = `<!doctype html><html><body style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.5;color:#222">` +
    `<p>Thank you for your order.</p><p>Order: <strong>${esc(orderId)}</strong></p><p>Your download links:</p><ul>${htmlLinks}</ul>` +
    `<p>Each link works up to ${esc(max)} times and expires on <strong>${esc(expiry)}</strong> (Singapore time). Keep this email, or save the PDF to your device when it downloads.</p>` +
    `<p style="font-size:14px;color:#555">${esc(licence)}</p>` +
    `<p>${wa ? `Need help? WhatsApp us on ${esc(wa)} with your order number.` : 'Need help? Reply to this email with your order number.'}</p><p>Math Inquirers</p></body></html>`;
  return { subject, text, html };
}
