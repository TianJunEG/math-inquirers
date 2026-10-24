// In-memory stand-in for the database functions (service_practice_keys / service_practice_record). TEST AND LOCAL STUB ONLY.
export const KEYS = [
  { id: 'q1', marking_mode: 'auto', type: 'number', key: 9, slips: [{ a: [7], say: 'x' }] },
  { id: 'q2', marking_mode: 'auto', type: 'number', key: 1000 },
  { id: 'q3', marking_mode: 'auto', type: 'fields', key: [3, 4] },
  { id: 'q4', marking_mode: 'auto', type: 'set', key: [12, 15, 18], ordered: false },
  { id: 'q5', marking_mode: 'auto', type: 'choice', key: '>', options: ['<', '=', '>'] },
  { id: 'q6', marking_mode: 'self', type: 'selfcheck' },
  { id: 'q7', marking_mode: 'auto', type: 'number', key: 5 },
  { id: 'q8', marking_mode: 'self', type: 'selfcheck', paper_only: true },
  { id: 'q9', marking_mode: 'auto', type: 'number', key: 2 },
  { id: 'q10', marking_mode: 'none', type: 'open' },
];
export function memoryStore({ tokenHash, consent = true, keys = KEYS }) {
  const s = { data: new Map(), consent, rateLeft: 99, calls: [] };
  const gate = (th) => th !== tokenHash ? 'session' : !s.consent ? 'consent' : s.rateLeft <= 0 ? 'rate' : null;
  s.getKeys = async (th, unit) => { const e = gate(th); if (e) return { ok: false, error: e }; if (unit !== 'ext-l2u01') return { ok: false, error: 'unit' }; return { ok: true, keys }; };
  s.record = async (th, p) => {
    const e = gate(th); if (e) return { ok: false, error: e };
    s.calls.push(p);
    const old = s.data.get(p.sid);
    if (old && p.rev === old.rev) return { ok: true, duplicate: true, rev: old.rev };
    if (old && p.rev < old.rev) return { ok: true, stale: true, rev: old.rev };
    s.rateLeft--; s.data.set(p.sid, { rev: p.rev, rows: p.rows, counts: p.counts });
    return { ok: true, rev: p.rev };
  };
  return s;
}
