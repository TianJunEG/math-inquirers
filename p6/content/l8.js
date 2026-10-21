// Math Inquirers P6 — Lesson 8: Secret Codes (clock / modular arithmetic; lists, letters and mod)
// Every answer below was worked out and checked by computer: letter numbers A = 0 … Z = 25,
// code number = (letter number + shift) mod 26; clock and calendar answers use mod 12 and mod 7. The Python program was run.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// ---------- code blocks: our own simple coloured shapes (never Scratch artwork) ----------
// prog: [kind, text] or [kind, text, [children]] for a C-shaped block; {…} marks a white slot.
const BC = { event: [YEL, NAVY], ctrl: [WHITE, NAVY], motion: [SKY, NAVY], sense: [SKY, NAVY], pen: [TEAL, WHITE], var: [RED, WHITE], looks: [YEL, NAVY] };
const cwid = (s, fs) => [...s].reduce((a, c) => a + fs * (/[iltfjr .,:()'|]/.test(c) ? 0.36 : /[A-Zmw%×]/.test(c) ? 0.78 : 0.62), 0);
const segs = t => t.split(/(\{[^}]*\})/).filter(s => s.trim()).map(s => s[0] === '{' ? { t: s.slice(1, -1), slot: true } : { t: s.trim(), slot: false });
function blocks(prog, o = {}) {
  const fs = o.fs || 15, h = o.h || 30, pad = 9, arm = 16, gap = 6, sp = 8;
  const lineW = t => segs(t).reduce((a, g) => a + cwid(g.t, fs) + (g.slot ? 2 * sp : 0) + gap, 0) - gap + 2 * pad;
  const ty = y => (y + h / 2 + fs * 0.36).toFixed(1);
  const txt = (x, y, t, fg) => {
    let s = '', cx = x + pad;
    for (const g of segs(t)) {
      const w = cwid(g.t, fs);
      if (g.slot) {
        s += `<rect x="${cx.toFixed(1)}" y="${y + 5}" width="${(w + 2 * sp).toFixed(1)}" height="${h - 10}" rx="${(h - 10) / 2}" fill="${WHITE}" stroke="${NAVY}" stroke-width="1.5"/>`;
        s += `<text x="${(cx + sp + w / 2).toFixed(1)}" y="${ty(y)}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(g.t)}</text>`;
        cx += w + 2 * sp + gap;
      } else {
        s += `<text x="${cx.toFixed(1)}" y="${ty(y)}" font-size="${fs}" font-weight="700" fill="${fg}" font-family="Arial">${esc(g.t)}</text>`;
        cx += w + gap;
      }
    }
    return s;
  };
  let maxX = 0;
  const draw = (items, x, y) => {
    let s = '';
    for (const [kind, t, kids] of items) {
      const [bg, fg] = BC[kind];
      if (kids) {
        const w = Math.max(lineW(t), 110), r = draw(kids, x + arm, y + h + 2);
        const yb = Math.max(r.y, y + h + 16), wb = Math.max(w * 0.45, 70);
        s += `<path d="M${x} ${y} H${(x + w).toFixed(1)} V${y + h} H${x + arm} V${yb} H${(x + wb).toFixed(1)} V${yb + 14} H${x} Z" fill="${bg}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>` + txt(x, y, t, fg) + r.s;
        maxX = Math.max(maxX, x + w, r.maxX || 0); y = yb + 16;
      } else {
        const w = lineW(t);
        s += `<rect x="${x}" y="${y}" width="${w.toFixed(1)}" height="${h}" rx="${kind === 'event' ? 14 : 7}" fill="${bg}" stroke="${NAVY}" stroke-width="2"/>` + txt(x, y, t, fg);
        maxX = Math.max(maxX, x + w); y += h + 2;
      }
    }
    return { s, y, maxX };
  };
  const r = draw(prog, 2, 2);
  return { svg: r.s, w: Math.ceil(maxX + 4), h: Math.ceil(r.y + 2) };
}
