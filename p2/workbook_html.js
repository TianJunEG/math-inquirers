// P2 student workbook (A + D style). Run in p2/:  node workbook_html.js && python3 wb_pdf.py
const C = require('../hp/common_html.js');
const { fs, t, p, q, lines, banner, AlignmentType } = C;
const L = require('./data.js');
const PROG = L.program, SLOGAN = L.slogan, QB = L.qbank;
const H = Object.assign({}, C, { fig: s => '<div class="p img" style="text-align:center">' + s + '</div>' });
const W = [];
const SP = require('../levels/spine_wb.js');   // strategy card + common look-back (docs/pedagogy/spine_routine_spec.md); wording in levels/spine.json
const LEVEL = 2;
const COMPACT = new Set([4]);   // lessons whose first page is too full for the full card: compact chip in the header row (see docs/pedagogy/spine_routine_build_notes.md)
const hdr = (n, topic, title, pb = true, note = '', first = false) => {   // first = the lesson's "Start here" page: it carries the strategy card
  const choose = first && SP.DATA.lessons[`${LEVEL}.${n}`].main === 'choose';
  const compact = first && COMPACT.has(n) && !choose;
  const card = first && !compact ? SP.card(LEVEL, n, choose && COMPACT.has(n)) : '';
  const chip = compact ? SP.card(LEVEL, n, true) : '';
  return [
  `<div class="p lh${pb ? ' pb' : ''}"><span class="lbadge" style="white-space:nowrap">Lesson ${n}</span><span class="ltopic">${topic}</span>${chip}${note}</div>`,
  choose || !card ? `<div class="p ltitle">${title}</div>` : `<div class="p ltrow" style="display:flex;align-items:center;justify-content:space-between;gap:4mm;margin:4px 0 6px"><div class="ltitle" style="flex:1;min-width:0;margin:0 0 8px;${title.length > 15 ? 'font-size:29px;line-height:1.12' : ''}">${title}</div>${card}</div>`,
  `<div class="p namer"><b>Name</b><span></span><b>Group</b><span style="max-width:90px"></span><b>Date</b><span style="max-width:110px"></span></div>`,
  ...(choose ? [card] : [])
  ];
};

// ---- close-the-gaps pieces: fast-track note, open investigation grid, reflection ----
const faceSvg = m => `<svg width="26" height="26" viewBox="0 0 30 30" style="vertical-align:middle"><circle cx="15" cy="15" r="13" fill="#FFC93C" stroke="#1B2A49" stroke-width="2"/><circle cx="10" cy="12" r="1.8" fill="#1B2A49"/><circle cx="20" cy="12" r="1.8" fill="#1B2A49"/><path d="${m}" fill="none" stroke="#1B2A49" stroke-width="2" stroke-linecap="round"/></svg>`;
const tick = '<span style="display:inline-block;width:13px;height:13px;border:2px solid #1B2A49;border-radius:3px;margin:0 5px -2px 14px;background:#fff"></span>';
const gridSvg = () => { let g = '<svg aria-label="Square grid for drawing shapes" viewBox="0 0 600 130" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">'; for (let r = 0; r < 4; r++) for (let c = 0; c < 19; c++) g += `<rect x="${12 + c * 30}" y="${8 + r * 30}" width="30" height="30" fill="#fff" stroke="#8A94AD" stroke-width="1.5"/>`; return g + '</svg>'; };
const fastNote = () => `<span style="flex:1;margin:0 0 3px 14px;border:1.5px solid #8A94AD;background:#F4F6FA;border-radius:5px;padding:2px 8px;font-size:11px;font-weight:700;line-height:1.25;min-width:150px;color:#1B2A49"><b style="color:#1F7A6F">START HERE.</b> ${esc0(L.gaps.common.neutral)}</span>`;
function esc0(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
const line = w => `<span style="display:inline-block;border-bottom:2px dotted #8A94AD;width:${w}%">&nbsp;</span>`;
const reflect = g => SP.lookback(LEVEL);   // common look-back (three prompts, tool ticks, still stuck / pass); replaces the old Looking back box
const invest = (g, n) => `<div class="p" style="border:2.5px dashed #1F7A6F;border-radius:6px;background:#F4FAF8;padding:6px 14px 8px;margin:10px 4px 0;font-size:14px;line-height:1.45;break-inside:avoid"><b style="font-size:17px;color:#1F7A6F">Investigation</b> <span style="font-size:12.5px">(a puzzle with more than one good answer. Try it any time you like, or at home.)</span><div style="margin-top:3px"><b>${esc0(g.invest.title)}.</b> ${esc0(g.invest.text)}${g.invest.need ? ' <i>' + esc0(g.invest.need) + '</i>' : ''}</div><div style="color:#1F7A6F;margin:3px 0 4px"><b>${esc0(g.invest.first)}</b></div>`
  + (g.fig === 'grid' ? gridSvg() + '<br>' + line(96) : [1, 2, 3, 4, 5, 6].map(() => line(96)).join('<br>')) + '</div>';
const coreEnd = n => { const g = L.gaps[String(n)]; const ls = L.lessons[n - 1];
  return [`<div class="p lh pb"><span class="lbadge">Lesson ${n}</span><span class="ltopic">Before you go: Investigation and Looking back</span></div>`, invest(g, n), reflect(g)]; };
// One short 'make up your own' (problem posing) prompt per lesson, printed at the foot of the Go further page.
const POSE = {
  1: 'a 3-digit number riddle with 2 or 3 clues, so that only ONE number fits. Swap with a partner.',
  2: 'a missing-digit sum with two boxes that has only ONE answer. Swap with a partner.',
  3: 'a \u201chow many of each\u201d puzzle with two kinds of things, so that there is only ONE answer.',
  4: 'a pattern of 4 shapes. Write a question about the 30th shape for a partner.',
  5: 'a before-and-after story that ends with 40. Can a partner work out the start?',
  6: 'a coin puzzle about paying exactly $1. Solve it, then swap with a partner.',
  7: 'a fair-sharing story about a cake cut into 8 equal pieces and shared by 3 children. Write each share as a fraction.',
  8: 'a stack of cubes with exactly 20 cubes. Draw its layers.',
  9: 'a jug puzzle with two jugs and a goal. Check it by writing every pour in a table.',
  10: 'a puzzle for next year\u2019s group. Write the answer on the back.'
};
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const out = [...hdr(n, ls.topic, 'THINK HARDER')];
  out.push(p(t('Draw a model, make a list or make a table. Then write how you know.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  out.push(banner('Think harder'));
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q(i + 1, x.q, { before: 90, after: 30, keepNext: true })); if (x.fig) out.push(H.fig(x.fig)); out.push(...lines(x.fig || x.q.length > 200 || [3,4,8].includes(n) ? 2 : 3)); });
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner('Go further'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q(i + 5, x.q, { before: 90, after: 30, keepNext: true })); out.push(...lines([4, 5, 8, 10].includes(n) ? 2 : 3)); });
  out.push(p([t('Make up your own: ', { bold: true, size: 24, color: '1F7A6F' }), t(POSE[n], { size: 24 })], { before: 120, after: 30, keepNext: true }));
  out.push(...lines(2));
  return out;
};
const stamps = L.lessons.map(ls => `<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 2 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);
L.content.forEach(c => {
  const l = c.lesson;
  W.push(...hdr(l.n, l.topic, l.title.toUpperCase(), true, fastNote(), true));
  W.push(...c.workbook(H));
  W.push(...coreEnd(l.n));
  W.push(...extra(l.n));
});
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());
W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 2 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
