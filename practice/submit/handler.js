// POST /api/practice/submit  (DRAFT, not wired into worker/index.js and not deployed).
// A pure Web-API handler (Request -> Response) so it runs on Cloudflare Workers and in Node 20+ tests.
// It never trusts a mark from the browser: every answer is re-marked here from the stored answer key (mark.js).
// The store is injected: supabaseStore() for production, an in-memory store in the tests / the local stub.
//
// Wire-up at go-live (3 lines in worker/index.js, owner approval first):
//   import { onRequest as practiceSubmit } from '../practice/submit/handler.js';  ROUTES['/api/practice/submit'] = practiceSubmit;
import M from './mark.js';   // UMD file: default import works in Workers (esbuild) and Node

export const LIMITS = { bodyBytes: 20000, items: 400, answerChars: 200, boxes: 12 };
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const UNIT = /^[a-z0-9][a-z0-9-]{2,39}$/, VER = /^[A-Za-z0-9._-]{1,30}$/, TOKEN = /^[A-Za-z0-9_-]{32,128}$/, ITEM = /^[A-Za-z0-9_.-]{1,40}$/;
const enc = new TextEncoder();
const reply = (obj, status = 200) => new Response(JSON.stringify(obj), { status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });
const bad = (code, status = 400) => reply({ ok: false, error: code }, status);   // fixed words only: no input is ever echoed back or logged

export async function sha256Hex(s) {
  const d = await crypto.subtle.digest('SHA-256', enc.encode(s));
  return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

// Returns the cleaned payload or an error word.
export function validate(b) {
  if (!b || typeof b !== 'object' || Array.isArray(b)) return 'shape';
  const allowed = ['v', 'unit', 'unit_version', 'sid', 'rev', 'answers', 'self', 'client_marks'];
  if (Object.keys(b).some((k) => !allowed.includes(k))) return 'unknown_field';
  if (b.v !== 1) return 'version';
  if (!UNIT.test(String(b.unit || '')) || !VER.test(String(b.unit_version || ''))) return 'unit';
  if (!UUID.test(String(b.sid || ''))) return 'sid';
  if (!Number.isInteger(b.rev) || b.rev < 1 || b.rev > 200) return 'rev';
  if (!b.answers || typeof b.answers !== 'object' || Array.isArray(b.answers)) return 'answers';
  const ids = Object.keys(b.answers);
  if (ids.length > LIMITS.items) return 'too_many';
  for (const id of ids) {
    if (!ITEM.test(id)) return 'item_id';
    const v = b.answers[id];
    if (v === null) continue;
    if (typeof v === 'string') { if (v.length > LIMITS.answerChars) return 'too_long'; continue; }
    if (Array.isArray(v) && v.length <= LIMITS.boxes && v.every((x) => typeof x === 'string' && x.length <= LIMITS.answerChars)) continue;
    return 'answer_type';
  }
  const self = b.self || {};
  if (typeof self !== 'object' || Array.isArray(self)) return 'self';
  for (const [id, r] of Object.entries(self)) if (!ITEM.test(id) || !['got', 'not_yet', 'checked'].includes(r)) return 'self';
  return null;
}

// keys: [{id, marking_mode, type, key, ordered, equivalent, slips, paper_only}]  ->  rows ready to store
export function markAll(keys, answers, self) {
  const byId = new Map(keys.map((k) => [k.id, k]));
  for (const id of Object.keys(answers)) if (!byId.has(id)) return { error: 'unknown_item' };
  for (const id of Object.keys(self || {})) if (!byId.has(id)) return { error: 'unknown_item' };
  const rows = [], counts = { auto: 0, right: 0, wrong: 0, skipped: 0, self: 0, self_got: 0, open: 0 };
  for (const k of keys) {
    const v = Object.prototype.hasOwnProperty.call(answers, k.id) ? answers[k.id] : null;   // an item the browser did not send is a skipped item
    const r = M.mark(k, v), d = r.detail || {};
    const typed = k.marking_mode === 'auto' && M.answered(k.type, v);
    rows.push({
      item_id: k.id, marking_mode: k.marking_mode, mark: r.mark,
      // free text from self-checked and open items is NEVER stored (could hold anything); only that something was written
      answer_text: typed ? (Array.isArray(v) ? v.join(' | ') : String(v)).slice(0, LIMITS.answerChars) : null,
      answered: M.answered(k.type, v),
      partial_found: d.found ?? (d.boxes ? d.boxes.filter(Boolean).length : null), partial_of: d.of ?? (d.boxes ? d.boxes.length : null),
      slip_idx: r.slip ?? null, note: d.reason ?? null,
      self_result: k.marking_mode === 'self' ? ((self || {})[k.id] || null) : null,
    });
    if (r.mark === 'self') { counts.self++; if (rows[rows.length - 1].self_result === 'got') counts.self_got++; }
    else if (r.mark === 'open') counts.open++;
    else { counts.auto++; counts[r.mark]++; }
  }
  return { rows, counts };
}

export async function handle(request, env, store) {
  if (request.method !== 'POST') return bad('method', 405);
  // same-origin only: no CORS headers are ever sent; a browser page on another site cannot read the answer, and Origin must match when present
  const origin = request.headers.get('origin');
  if (origin && new URL(request.url).origin !== origin) return bad('origin', 403);
  if (!(request.headers.get('content-type') || '').toLowerCase().startsWith('application/json')) return bad('content_type', 415);
  const auth = request.headers.get('authorization') || '';
  const token = auth.startsWith('Bearer ') ? auth.slice(7).trim() : '';
  if (!TOKEN.test(token)) return bad('session', 401);
  const text = await request.text();
  if (text.length > LIMITS.bodyBytes) return bad('too_large', 413);
  let body; try { body = JSON.parse(text); } catch (e) { return bad('json'); }
  const err = validate(body); if (err) return bad(err);
  const th = await sha256Hex(token);
  const g = await store.getKeys(th, body.unit, body.unit_version);          // checks session, consent and rate in the database too
  if (!g.ok) return bad(g.error, { session: 401, consent: 403, entitlement: 403, unit: 404, rate: 429 }[g.error] || 400);
  const m = markAll(g.keys, body.answers, body.self);
  if (m.error) return bad(m.error);
  const rec = await store.record(th, { unit: body.unit, unit_version: body.unit_version, sid: body.sid, rev: body.rev, rows: m.rows, counts: m.counts });
  if (!rec.ok) return bad(rec.error, { session: 401, consent: 403, entitlement: 403, rate: 429 }[rec.error] || 400);
  return reply({ ok: true, rev: rec.rev, duplicate: !!rec.duplicate, stale: !!rec.stale, counts: m.counts, marks: Object.fromEntries(m.rows.map((r) => [r.item_id, r.mark])) });
}

export const onRequest = (ctx) => handle(ctx.request, ctx.env, supabaseStore(ctx.env));

// Production store: Supabase REST RPC with the SERVICE ROLE key (a Worker secret). Both functions are executable by service_role only.
export function supabaseStore(env, fetchImpl = fetch) {
  const call = async (fn, args) => {
    const r = await fetchImpl(`${env.SUPABASE_URL}/rest/v1/rpc/${fn}`, { method: 'POST', headers: { 'content-type': 'application/json', apikey: env.SUPABASE_SERVICE_ROLE_KEY, authorization: `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}` }, body: JSON.stringify(args) });
    if (!r.ok) return { ok: false, error: 'server' };
    return r.json();
  };
  return {
    getKeys: (th, unit, ver) => call('service_practice_keys', { p_token_hash: th, p_unit: unit, p_version: ver }),
    record: (th, p) => call('service_practice_record', { p_token_hash: th, p_unit: p.unit, p_version: p.unit_version, p_sid: p.sid, p_rev: p.rev, p_rows: p.rows }),
  };
}
