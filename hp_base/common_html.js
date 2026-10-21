const fs = require('fs');
const px = tw => (tw / 15).toFixed(1) + 'px';
const AlignmentType = { LEFT: 'left', RIGHT: 'right', CENTER: 'center' };
const FILLS = { 'D9D9D9': '#FFC93C', 'EDEDED': '#FFF0C2', 'F2F2F2': '#FFF4D1' };
const CW = 9900;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
class TextRun { constructor(h) { this.h = h; } toString() { return this.h; } }
const t = (s, o = {}) => {
  let st = '';
  if (o.size) st += `font-size:${(o.size / 2 * 1.333).toFixed(1)}px;`;
  if (o.color) st += `color:#${o.color};`;
  if (o.bold) st += 'font-weight:700;'; if (o.italics) st += 'font-style:italic;';
  return new TextRun(`<span style="${st}">${esc(s)}</span>`);
};
const inner = c => Array.isArray(c) ? c.map(String).join('') : (c instanceof TextRun ? String(c) : esc(c));
const p = (c, o = {}) => {
  let cls = 'p'; if (o.keepNext) cls += ' kn'; const BR = o.pb ? '<div class="brk"></div>' : '';
  let st = `margin-top:${px(o.before || 0)};margin-bottom:${px(o.after === undefined ? 140 : o.after)};`;
  if (o.align) st += `text-align:${o.align};`;
  if (o.indent && o.indent.left) st += `padding-left:${px(o.indent.left)};`;
  if (typeof c === 'string' && (o.size || o.bold || o.color)) c = [t(c, o)];
  return BR + `<div class="${cls}" style="${st}">${inner(c) || '&nbsp;'}</div>`;
};
const cell = (c, w, o = {}) => {
  const items = (Array.isArray(c) ? c : [c]).map(x => (typeof x === 'string' && !/^\s*<(div|table)/.test(x)) ? `<div style="text-align:${o.align || 'center'};${o.size ? 'font-size:' + (o.size / 2 * 1.333).toFixed(1) + 'px;' : ''}${o.bold ? 'font-weight:700;' : ''}${o.color ? 'color:#' + o.color + ';' : ''}">${esc(x)}</div>` : (x instanceof TextRun ? `<div style="text-align:${o.align || 'center'}">${x}</div>` : x)).join('');
  const fill = o.fill ? (FILLS[o.fill] || '#' + o.fill) : '#FFFFFF';
  return `<td style="width:${(w / CW * 100).toFixed(2)}%;padding:${px(o.h || 100)} 8px;background:${fill}" ${o.span ? 'colspan=' + o.span : ''}>${items}</td>`;
};
const row = (cells, o = {}) => `<tr>${cells.join('')}</tr>`;
const tbl = (widths, rows) => `<table class="tb">${rows.join('')}</table>`;
const q = (n, text, o = {}) => {
  let cls = 'p q'; if (o.keepNext) cls += ' kn'; const BR = o.pb ? '<div class="brk"></div>' : '';
  return BR + `<div class="${cls}" style="margin-top:${px(o.before === undefined ? 160 : o.before)};margin-bottom:${px(o.after === undefined ? 120 : o.after)}"><span class="qn">${n}</span><span class="qt">${inner(Array.isArray(text) ? text : [t(text)])}</span></div>`;
};
const sub = (l, text, o = {}) => `<div class="p sub${o.keepNext ? ' kn' : ''}" style="margin-bottom:${px(o.after === undefined ? 120 : o.after)}"><span class="sl">${l}</span><span>${inner(Array.isArray(text) ? text : [t(text)])}</span></div>`;
const ans = (label = 'Answer:', ind = 1000) => `<div class="p ans" style="padding-left:${px(ind)}"><b>${esc(label)}</b><span class="al"></span></div>`;
const lines = n => Array.from({ length: n }, () => '<div class="ln"></div>');
const img = (file, w, h, align) => `<div class="p img" style="text-align:${align || 'center'}"><img src="data:image/png;base64,${fs.readFileSync(file).toString('base64')}" style="width:${Math.round(w * 1.0)}px;max-width:100%"></div>`;
const gap = (n = 120) => `<div style="height:${px(n)}"></div>`;
const banner = s => `<div class="banner kn">${esc(s)}</div>`;
const dots = (n, c, size = 40) => { let s = ''; for (let i = 0; i < n; i++) { s += '●' + ((i + 1) % 5 === 0 && i < n - 1 ? '   ' : ' '); } return p(t(s.trim(), { size, color: c }), { after: 0, align: 'left' }); };
module.exports = { fs, D: {}, FONT: 'x', CW, t, p, cell, tbl, row, q, sub, ans, lines, img, gap, banner, footer: () => '', page: {}, dots, AlignmentType, BorderStyle: {}, WidthType: {}, ShadingType: {}, VerticalAlign: {}, Paragraph: class {}, TextRun, TableCell: class {}, B1: {}, borders: {}, Table: class {}, TableRow: class {} };
