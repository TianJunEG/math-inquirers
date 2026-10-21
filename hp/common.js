const fs = require('fs');
const D = require('docx');
const { Paragraph, TextRun, Table, TableRow, TableCell, WidthType, AlignmentType, BorderStyle, ShadingType, ImageRun, Footer, PageNumber, VerticalAlign, Tab, TabStopType } = D;
const FONT = 'Arial';
const CW = 9900;
const t = (s, o = {}) => new TextRun({ text: s, font: FONT, size: o.size || 26, bold: o.bold, italics: o.italics, color: o.color });
const p = (c, o = {}) => new Paragraph({
  children: Array.isArray(c) ? c : (c instanceof TextRun ? [c] : [t(c, o)]),
  spacing: { before: o.before || 0, after: o.after === undefined ? 140 : o.after, line: o.line || 320, lineRule: 'auto' },
  alignment: o.align, indent: o.indent, keepNext: o.keepNext, keepLines: true, pageBreakBefore: o.pb, shading: o.shading
});
const B1 = { style: BorderStyle.SINGLE, size: 8, color: '000000' };
const borders = { top: B1, bottom: B1, left: B1, right: B1 };
const cell = (c, w, o = {}) => new TableCell({
  width: { size: w, type: WidthType.DXA }, borders: o.borders || borders, verticalAlign: VerticalAlign.CENTER,
  margins: { top: o.h || 100, bottom: o.h || 100, left: 100, right: 100 },
  shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: 'auto' } : undefined, columnSpan: o.span,
  children: (Array.isArray(c) ? c : [c]).map(x => typeof x === 'string'
    ? p(x, { align: o.align || AlignmentType.CENTER, after: 0, size: o.size || 24, bold: o.bold, color: o.color })
    : (x instanceof TextRun ? p([x], { align: o.align || AlignmentType.CENTER, after: 0 }) : x))
});
const tbl = (widths, rows) => new Table({ width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: widths, rows });
const row = (cells, o = {}) => new TableRow({ children: cells, cantSplit: true, height: o.h ? { value: o.h, rule: 'atLeast' } : undefined });
const q = (n, text, o = {}) => p([t(n + '.', { bold: true }), new TextRun({ children: [new Tab()], font: FONT, size: 26 }), ...(Array.isArray(text) ? text : [t(text)])],
  { indent: { left: 560, hanging: 560 }, tabStops: [{ type: TabStopType.LEFT, position: 560 }], before: o.before === undefined ? 160 : o.before, after: o.after === undefined ? 120 : o.after, keepNext: o.keepNext, pb: o.pb });
const sub = (l, text, o = {}) => p([t('(' + l + ')  ', { bold: true }), ...(Array.isArray(text) ? text : [t(text)])], { indent: { left: 1000, hanging: 440 }, after: o.after === undefined ? 120 : o.after, keepNext: o.keepNext });
const ans = (label = 'Answer:', ind = 1000) => p([t(label + ' ', { bold: true }), t('______________________________')], { indent: { left: ind }, after: 140 });
const lines = (n) => Array.from({ length: n }, () => new Paragraph({ children: [], spacing: { before: 280, after: 80 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '777777', space: 1 } }, indent: { left: 560 } }));
const img = (file, w, h, align) => p([new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width: w, height: h }, altText: { title: file, description: file, name: file } })], { align: align || AlignmentType.CENTER, after: 120 });
const gap = (n = 120) => p('', { after: n });
const banner = (s) => tbl([CW], [row([cell(t(s, { bold: true, size: 26 }), CW, { fill: 'EDEDED', align: AlignmentType.LEFT, h: 70 })])]);
const footer = (txt) => new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: txt + '  •  Page ', font: FONT, size: 18, color: '777777' }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18, color: '777777' })] })] });
const page = { size: { width: 11906, height: 16838 }, margin: { top: 800, right: 1003, bottom: 800, left: 1003 } };
const dots = (n, c, size = 40) => { // drawn circles (PNG made by gapkit.py), not a text glyph
  const sp = Math.round(size * 0.5), f = require('path').join(__dirname, `dots_${n}_${c}.png`);
  if (!fs.existsSync(f)) require('child_process').execFileSync('python3', [require('path').join(__dirname, 'gapkit.py'), 'dots', String(n), c, String(sp)]);
  const w = n * (sp + 6) + Math.floor(n / 5) * 14 + 4;
  return p([new ImageRun({ type: 'png', data: fs.readFileSync(f), transformation: { width: w, height: sp + 2 }, altText: { title: 'dots', description: n + ' pictures', name: 'dots' } })], { after: 0, align: AlignmentType.LEFT });
};
module.exports = { D, fs, FONT, CW, t, p, borders, B1, cell, tbl, row, q, sub, ans, lines, img, gap, banner, footer, page, dots, AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign, Paragraph, TextRun, Table, TableRow, TableCell };
