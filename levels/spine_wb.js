// Strategy card and common look-back for the HOLIDAY workbooks (docs/pedagogy/spine_routine_spec.md sections 2 and 3).
// Pure HTML strings, no colour (black ink, white fill) so the black-and-white print converter leaves them alone.
//   const SP = require('../levels/spine_wb.js');   SP.card(level, n)  -> html of the card;   SP.lookback(level)  -> html of the look-back box
const fs = require('fs'), path = require('path');
const DATA = JSON.parse(fs.readFileSync(path.join(__dirname, 'spine.json'), 'utf8'));
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const svgCache = {};
const icon = (id, mm) => {
  if (!svgCache[id]) svgCache[id] = fs.readFileSync(path.join(__dirname, 'spine_icons', id + '.svg'), 'utf8').trim().replace(/\s*\n\s*/g, ' ');   // one line: p2-p6 wb_pdf.py groups the body line by line
  return svgCache[id].replace('width="64" height="64"', `width="${mm}mm" height="${mm}mm"`).replace('<svg ', '<svg style="color:#1B2A49;flex:none;display:block" ');
};
const tool = id => DATA.tools.find(t => t.id === id);
const band = lv => DATA.bands[String(lv)];
const tick = mm => `<span style="display:inline-block;width:${mm}mm;height:${mm}mm;border:0.5mm solid #1B2A49;border-radius:0.6mm;background:#fff;flex:none"></span>`;
const L = DATA.card_labels;

// Card on the first ("Start here") page of a lesson: right-aligned beside the title.
function card(level, n, compact) {
  const row = DATA.lessons[`${level}.${n}`];
  const box = 'border:0.5mm solid #1B2A49;border-radius:1.5mm;background:#fff;color:#1B2A49;font-family:\'Nunito Sans\',Arial,sans-serif;break-inside:avoid;';
  if (row.main === 'choose' && compact) {   // compact version for a first page that is too full (Level 4 Lesson 10): sits beside the title; label over eight icons with tick boxes
    const cs = DATA.tools.map(t => `<span style="display:inline-flex;align-items:center;gap:0.6mm">${icon(t.id, 7)}${tick(3.2)}</span>`).join('');
    return `<div class="p spcard spchoose" data-spine="card" style="${box}width:104mm;padding:1mm 2mm 1.2mm;display:flex;flex-direction:column;gap:0.8mm;flex:none"><span style="font-size:9pt;font-weight:800;letter-spacing:.05em">${L.tool_of_day}: ${L.choose_one}</span><span style="display:flex;justify-content:space-between">${cs}</span></div>`;
  }
  if (row.main === 'choose' && compact) {   // slim version of the Lesson 10 row (one line of icons, label inside the row) for first pages with no slack
    const cells = DATA.tools.map(t => `<div style="display:flex;align-items:center;gap:0.8mm">${icon(t.id, 8)}${tick(3.4)}</div>`).join('');
    return `<div class="p spcard spchoose" data-spine="card" style="${box}padding:1mm 2.5mm;margin:1mm 0 2mm;display:flex;align-items:center;justify-content:space-between;gap:2mm"><span style="font-size:9pt;font-weight:800;letter-spacing:.05em;line-height:1.15">${L.tool_of_day}:<br>${L.choose_one}. Tick one.</span>${cells}</div>`;
  }
  if (row.main === 'choose') {
    const cells = DATA.tools.map(t => `<div style="display:flex;flex-direction:column;align-items:center;gap:0.8mm;width:21mm">${icon(t.id, 10)}<div style="display:flex;align-items:center;gap:1mm">${tick(3.6)}<span style="font-size:9pt;font-weight:700">${L.chose}</span></div></div>`).join('');
    return `<div class="p spcard spchoose" data-spine="card" style="${box}padding:1.5mm 2.5mm 1.8mm;margin:1mm 0 3mm"><div style="font-size:9pt;font-weight:800;letter-spacing:.06em;margin-bottom:1mm">${L.tool_of_day}: ${L.choose_one}. Choose one tool and tick it.</div><div style="display:flex;justify-content:space-between">${cells}</div></div>`;
  }
  const t = tool(row.main), def = t.def[band(level)];
  if (compact) {   // compact chip for the lesson header row (used where the first page is too full for the full card): icon + name + tick, no definition
    return `<span class="spcard spcompact" data-spine="card" style="${box}display:inline-flex;align-items:center;gap:1.8mm;padding:0.6mm 2mm;margin-left:3mm;white-space:nowrap;flex:none"><span style="font-size:9pt;font-weight:800;letter-spacing:.05em">${L.tool_of_day}</span>${icon(t.id, 8)}<span style="font-family:Fredoka,Arial,sans-serif;font-size:12pt;font-weight:700">${esc(t.name)}</span><span style="display:inline-flex;align-items:center;gap:1mm;font-size:9pt;font-weight:700">${tick(3.6)}${L.used}</span></span>`;
  }
  const also = row.also.length ? `<div style="font-size:9pt;margin-top:0.6mm"><b>${L.also.trim()}</b> ${row.also.map(a => esc(tool(a).name)).join(', ')}</div>` : '';
  return `<div class="p spcard" data-spine="card" style="${box}width:96mm;padding:1mm 2.5mm;display:flex;gap:2.5mm;align-items:center;flex:none"><div style="width:13mm;flex:none">${icon(t.id, 13)}</div><div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between;align-items:center;gap:2mm"><span style="font-size:9pt;font-weight:800;letter-spacing:.06em">${L.tool_of_day}</span><span style="display:inline-flex;align-items:center;gap:1mm;font-size:9pt;font-weight:700">${tick(3.6)}${L.used}</span></div><div style="font-family:Fredoka,Arial,sans-serif;font-size:13pt;font-weight:700;line-height:1.15">${esc(t.name)}</div><div style="font-size:9pt;line-height:1.2">${esc(def)}</div>${also}</div></div>`;
}

// Look-back box on the last page of a lesson (replaces the old 'Look-back' box).
function lookback(level) {
  const b = band(level), P = DATA.lookback.prompts[b], lb = DATA.lookback;
  const line = `<span style="flex:1;border-bottom:0.4mm dotted #1B2A49;height:5.5mm;min-width:20mm"></span>`;
  const yn = `<span style="display:inline-flex;align-items:center;gap:1mm;white-space:nowrap">${tick(4)}<b style="font-size:10pt">yes</b></span><span style="display:inline-flex;align-items:center;gap:1mm;white-space:nowrap">${tick(4)}<b style="font-size:10pt">not yet</b></span>`;
  const r = (n, q, right) => `<div style="display:flex;align-items:center;gap:3mm;margin-top:1.6mm"><span style="flex:none;width:6mm;height:6mm;border:0.5mm solid #1B2A49;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:800;font-size:10pt">${n}</span><span style="flex:1;font-size:11pt;font-weight:700;line-height:1.15">${esc(q)}</span><span style="display:flex;align-items:center;gap:3mm;flex:none;${n === 3 ? 'width:62mm' : ''}">${right}</span></div>`;
  const a3 = b === 'A' ? `<span style="font-size:9pt;white-space:nowrap">${esc(lb.answer3.A)}:</span>${line}` : `<span style="font-size:9pt;white-space:nowrap">${esc(lb.answer3[b])}</span>${line}`;
  const tools = DATA.tools.map(t => `<span style="display:inline-flex;align-items:center;gap:0.8mm">${icon(t.id, 7)}${tick(3.6)}</span>`).join('');
  return `<div class="p splook" data-spine="lookback" style="border:0.5mm solid #1B2A49;border-radius:2mm;background:#fff;color:#1B2A49;font-family:'Nunito Sans',Arial,sans-serif;padding:2mm 4mm 2.2mm;margin-top:4mm;break-inside:avoid"><div style="display:flex;align-items:baseline;gap:3mm"><span style="font-family:Fredoka,Arial,sans-serif;font-weight:700;font-size:15pt">Look back</span><span style="font-size:9pt">${esc(lb.intro)}</span></div>${r(1, P[0], yn)}${r(2, P[1], yn)}${r(3, P[2], a3)}<div style="display:flex;align-items:center;justify-content:space-between;gap:2mm;margin-top:2.2mm;border-top:0.4mm solid #1B2A49;padding-top:1.6mm"><span style="font-size:9pt;font-weight:800;white-space:nowrap">${esc(lb.footer_tools)}:</span>${tools}</div><div style="display:flex;gap:6mm;margin-top:1.4mm;font-size:9pt"><span style="display:inline-flex;align-items:center;gap:1.2mm">${tick(3.6)}${esc(lb.stuck)}</span><span style="display:inline-flex;align-items:center;gap:1.2mm">${tick(3.6)}${esc(lb.pass)}</span></div></div>`;
}
module.exports = { card, lookback, DATA, icon, tool, band };
