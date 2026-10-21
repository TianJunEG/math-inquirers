// P2 student workbook (A + D style). Run in p2/:  node workbook_html.js && python3 wb_pdf.py
const C = require('../hp/common_html.js');
const { fs, t, p, q, lines, banner, AlignmentType } = C;
const L = require('./data.js');
const PROG = L.program, SLOGAN = L.slogan, QB = L.qbank;
const H = Object.assign({}, C, { fig: s => '<div class="p img" style="text-align:center">' + s + '</div>' });
const W = [];
const hdr = (n, topic, title, pb = true, note = '') => [
  `<div class="p lh${pb ? ' pb' : ''}"><span class="lbadge">Lesson ${n}</span><span class="ltopic">${topic}</span>${note}</div>`,
  `<div class="p ltitle">${title}</div>`,
  `<div class="p namer"><b>Name</b><span></span><b>Group</b><span style="max-width:90px"></span><b>Date</b><span style="max-width:110px"></span></div>`
];

// ---- close-the-gaps pieces: fast-track note, open investigation grid, reflection ----
const faceSvg = m => `<svg width="26" height="26" viewBox="0 0 30 30" style="vertical-align:middle"><circle cx="15" cy="15" r="13" fill="#FFC93C" stroke="#1B2A49" stroke-width="2"/><circle cx="10" cy="12" r="1.8" fill="#1B2A49"/><circle cx="20" cy="12" r="1.8" fill="#1B2A49"/><path d="${m}" fill="none" stroke="#1B2A49" stroke-width="2" stroke-linecap="round"/></svg>`;
const tick = '<span style="display:inline-block;width:13px;height:13px;border:2px solid #1B2A49;border-radius:3px;margin:0 5px -2px 14px;background:#fff"></span>';
const gridSvg = () => { let g = '<svg aria-label="Square grid for drawing shapes" viewBox="0 0 600 130" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">'; for (let r = 0; r < 4; r++) for (let c = 0; c < 19; c++) g += `<rect x="${12 + c * 30}" y="${8 + r * 30}" width="30" height="30" fill="#fff" stroke="#8A94AD" stroke-width="1.5"/>`; return g + '</svg>'; };
const fastNote = () => `<span style="flex:1;margin:0 0 3px 14px;border:1.5px dashed #1F7A6F;background:#EAF6F3;border-radius:5px;padding:1px 6px;font-size:10px;line-height:1.2;min-width:150px"><b style="color:#1F7A6F">${esc0(L.gaps.common.fast.split('.')[0])}.</b> ${esc0(L.gaps.common.fast.split('.').slice(1).join('.').trim())}</span>`;
function esc0(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
const reflect = g => `<div class="p" style="border:2.5px solid #1B2A49;border-radius:6px;background:#FFFBEA;padding:3px 12px 2px;margin:4px 4px 0;font-size:12.5px;line-height:1.35;break-inside:avoid"><div style="display:flex;align-items:center;gap:6px"><b style="font-size:15px;color:#1F7A6F">What was hard?</b><span style="margin-left:10px">This lesson felt:${tick}${faceSvg('M9 18 Q15 25 21 18')} easy${tick}${faceSvg('M10 20 H20')} OK${tick}${faceSvg('M9 22 Q15 15 21 22')} tricky</span></div>`
  + `<div>The hardest part was <span style="display:inline-block;border-bottom:2px dotted #8A94AD;width:68%">&nbsp;</span></div>`
  + `<div>I got unstuck by:${g.unstuck.map(u => tick + esc0(u)).join('')}</div>`
  + `<div style="margin-bottom:2px">Next time I will try <span style="display:inline-block;border-bottom:2px dotted #8A94AD;width:70%">&nbsp;</span></div></div>`;
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const out = [...hdr(n, ls.topic, 'THINK HARDER')];
  out.push(p(t('Draw a model, make a list or make a table. Then write how you know.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  out.push(banner('Stretch'));
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q(i + 1, x.q, { before: 90, after: 30, keepNext: true })); out.push(...lines(3)); });
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner('Challenge  (for strong thinkers)'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q(i + 5, x.q, { before: 90, after: 30, keepNext: true })); out.push(...lines([4, 5, 8, 10].includes(n) ? 2 : 3)); });
  const g = L.gaps[String(n)];
  out.push(q(8, 'Open investigation: ' + g.invest.title + '. ' + g.invest.text, { before: 90, after: 30, keepNext: true }));
  if (g.fig === 'grid') out.push(H.fig(gridSvg()));
  else out.push(...lines(2));
  out.push(reflect(g));
  return out;
};
const stamps = L.lessons.map(ls => `<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 2 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);
L.content.forEach(c => {
  const l = c.lesson;
  W.push(...hdr(l.n, l.topic, l.title.toUpperCase(), true, fastNote()));
  W.push(...c.workbook(H));
  W.push(...extra(l.n));
});
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());
W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 2 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
