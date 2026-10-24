// POST /api/practice/submit  (DRAFT, not wired into worker/index.js and not deployed).
// A pure Web-API handler (Request -> Response) so it runs on Cloudflare Workers and in Node 20+ tests.
// It never trusts a mark from the browser: every answer is re-marked here from the stored answer key (mark.js).
// The store is injected: supabaseStore() for production, an in-memory store in the tests / the local stub.
//
// Wire-up at go-live (3 lines in worker/index.js, owner approval first):
//   import { onRequest as practiceSubmit } from '../practice/submit/handler.js';  ROUTES['/api/practice/submit'] = practiceSubmit;
import M from './mark.js';   // UMD file: default import works in Workers (esbuild) and Node

// explainChars / explainItems: the typed explanation of a self-check item (EXPLAIN-TO-TUTOR); only the tutor's report reads it, it is never sent back to the browser.
export const LIMITS = { bodyBytes: 64000, items: 400, answerChars: 200, boxes: 12, explainChars: 500, explainItems: 60 };
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
  const allowed = ['v', 'unit', 'unit_version', 'sid', 'rev', 'answers', 'self', 'explain', 'client_marks'];
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
  const ex = b.explain === undefined ? {} : b.explain;
  if (!ex || typeof ex !== 'object' || Array.isArray(ex)) return 'explain';
  const eids = Object.keys(ex);
  if (eids.length > LIMITS.explainItems) return 'too_many';
  for (const id of eids) {
    if (!ITEM.test(id) || typeof ex[id] !== 'string') return 'explain';
    if (ex[id].length > LIMITS.explainChars) return 'too_long';
  }
  return null;
}

// Clean a typed explanation: control characters out, trimmed, at most explainChars characters, empty -> null.
export const cleanExplain = (t) => (typeof t === 'string' ? t.replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, '').trim().slice(0, LIMITS.explainChars).trim() || null : null);

// keys: [{id, marking_mode, type, key, ordered, equivalent, slips, paper_only}]  ->  rows ready to store
export function markAll(keys, answers, self, explain) {
  const byId = new Map(keys.map((k) => [k.id, k]));
  for (const id of Object.keys(answers)) if (!byId.has(id)) return { error: 'unknown_item' };
  for (const id of Object.keys(self || {})) if (!byId.has(id)) return { error: 'unknown_item' };
  for (const id of Object.keys(explain || {})) if (!byId.has(id)) return { error: 'unknown_item' };
  const rows = [], counts = { auto: 0, right: 0, wrong: 0, skipped: 0, self: 0, self_got: 0, open: 0 };
  for (const k of keys) {
    const v = Object.prototype.hasOwnProperty.call(answers, k.id) ? answers[k.id] : null;   // an item the browser did not send is a skipped item
    const r = M.mark(k, v), d = r.detail || {};
    const typed = k.marking_mode === 'auto' && M.answered(k.type, v);
    rows.push({
      item_id: k.id, marking_mode: k.marking_mode, mark: r.mark,
      // free text of a self-checked or open item is not stored as an answer (answer_text stays null); only that something was written. The typed EXPLANATION (explain_text, at most 500 characters)
      // is kept for the tutor's report only for self and open items: never for an auto-marked item, and never returned to the browser.
      answer_text: typed ? (Array.isArray(v) ? v.join(' | ') : String(v)).slice(0, LIMITS.answerChars) : null,
      answered: M.answered(k.type, v),
      partial_found: d.found ?? (d.boxes ? d.boxes.filter(Boolean).length : null), partial_of: d.of ?? (d.boxes ? d.boxes.length : null),
      slip_idx: r.slip ?? null, note: d.reason ?? null,
      explain_text: k.marking_mode !== 'auto' && !k.paper_only ? cleanExplain((explain || {})[k.id]) : null,
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
  const m = markAll(g.keys, body.answers, body.self, body.explain);
  if (m.error) return bad(m.error);
  const rec = await store.record(th, { unit: body.unit, unit_version: body.unit_version, sid: body.sid, rev: body.rev, rows: m.rows, counts: m.counts });
  if (!rec.ok) return bad(rec.error, { session: 401, consent: 403, entitlement: 403, rate: 429, sid_unit: 409 }[rec.error] || 400);   // sid_unit: a client_sid already belongs to another unit
  // Round-1 audit L4: the reply does NOT carry the marks or counts. The page marks nothing from this reply (sheet.js reads only ok), the stored marks go to the reports,
  // and a child (or a script) that resubmits revision after revision learns nothing about the answer key from the reply.
  return reply({ ok: true, rev: rec.rev, duplicate: !!rec.duplicate, stale: !!rec.stale });
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
