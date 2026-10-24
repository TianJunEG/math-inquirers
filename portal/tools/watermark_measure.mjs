// Measures what stamping a footer on every page with pdf-lib would cost (CPU, wall time, memory). NOT used by the shop: watermarking is not enabled (docs/shop/delivery_plan.md).
//   mkdir /tmp/pdfl && cd /tmp/pdfl && npm i pdf-lib@1.17.1 && cp <repo>/portal/tools/watermark_measure.mjs . && node watermark_measure.mjs <repo>/outputs/print/Math_Inquirers_P2_Workbook_PRINT.pdf
import { PDFDocument, StandardFonts, rgb } from 'pdf-lib';
import fs from 'node:fs';
const f = process.argv[2];
const bytes = fs.readFileSync(f);
const c0 = process.cpuUsage(), m0 = process.memoryUsage().rss, t0 = Date.now();
const doc = await PDFDocument.load(bytes, { updateMetadata: false });
const font = await doc.embedFont(StandardFonts.Helvetica);
const pages = doc.getPages();
for (const p of pages) p.drawText('Licensed to order MI-ABC123 buyer@example.com - personal use only', { x: 30, y: 14, size: 7, font, color: rgb(0.45,0.45,0.45) });
const out = await doc.save({ useObjectStreams: true });
const c = process.cpuUsage(c0);
console.log(f.split('/').pop(), 'in', (bytes.length/1e6).toFixed(1)+'MB', 'out', (out.length/1e6).toFixed(1)+'MB', 'pages', pages.length, 'cpu_ms', Math.round((c.user+c.system)/1000), 'wall_ms', Date.now()-t0, 'rss_delta_MB', Math.round((process.memoryUsage().rss-m0)/1e6));
