// P5 student workbook (A + D style). Run in p2/:  node workbook_html.js && python3 wb_pdf.py
const C = require('../hp/common_html.js');
const { fs, t, p, q, lines, banner, AlignmentType } = C;
const L = require('./data.js');
const PROG = L.program, SLOGAN = L.slogan, QB = L.qbank;
const H = Object.assign({}, C, { fig: s => '<div class="p img" style="text-align:center">' + s + '</div>' });
const W = [];
const hdr = (n, topic, title, pb = true) => [
  `<div class="p lh${pb ? ' pb' : ''}"><span class="lbadge">Lesson ${n}</span><span class="ltopic">${topic}</span></div>`,
  `<div class="p ltitle">${title}</div>`,
  `<div class="p namer"><b>Name</b><span></span><b>Group</b><span style="max-width:90px"></span><b>Date</b><span style="max-width:110px"></span></div>`
];
const bx = '<span style="display:inline-block;width:20px;height:20px;border:2.5px solid #1B2A49;border-radius:5px;vertical-align:-4px;margin:0 6px 0 12px"></span>';
// Reflection: short and safe. A small box on the page every child gets (the Investigation page), never under the Go further page.
const reflect = () => `<div class="p" style="border:3px solid #1F7A6F;border-radius:14px;padding:8px 16px;margin-top:14px;background:#F3FAF8;page-break-inside:avoid"><div style="font-weight:800;font-size:20px;color:#1F7A6F;margin-bottom:2px">My reflection  <span style="font-weight:400;font-size:15px;color:#444">(2 minutes. Your tutor may read this privately to plan the next lesson. It is never marked or shown to others. &ldquo;Pass&rdquo; is always OK.)</span></div>
<div style="margin:5px 0">Something I did well ____________________________________________________________</div>
<div style="margin:5px 0">The hardest part was ______________________________________________________________</div>
<div style="margin:5px 0">What helped me:${bx}a picture or model${bx}a list or table${bx}a simpler number${bx}my partner${bx}I asked for help${bx}checking my estimate</div>
<div style="margin:5px 0">${bx}I am still stuck (my tutor will check in with me)${bx}Pass</div></div>`;
// Neutral choice line at the top of page 1 (replaces the old printed fast-track criterion).
// The number is the last question printed on page 1 of that lesson (2 or 3), computed in data.js from the real page break.
const choose = n => `<div class="p" style="border:2.5px solid #D9662B;border-radius:12px;padding:6px 14px;margin:4px 0 6px;background:#FFF6EE;font-size:17px"><b style="color:#D9662B">After question ${L.choiceQ(n)}</b> you may choose: carry on, or try Think harder. You can swap at any time. <b style="color:#D9662B">&#9733; take-home</b> parts are for home.</div>`;
const planLine = txt => `<div class="p" style="border:2px solid #1F7A6F;border-radius:10px;padding:4px 12px;margin:2px 0 6px;background:#F3FAF8;font-size:16px"><b style="color:#1F7A6F">Page 2 plan.</b> Start with ${txt}. Then choose what to try next. You do not have to finish the page. The Investigation is on the next page.</div>`;
const BRK = '<div class="brk"></div>';
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const inv = L.content[n - 1].investigation;
  const out = [];
  // Page 3: the Investigation (an option for everyone, with an easy first step) and the reflection box
  out.push(...hdr(n, ls.topic, 'INVESTIGATION'));
  out.push(banner('Investigation: ' + inv.title));
  out.push(`<div class="p" style="border:2px dashed #1F7A6F;border-radius:10px;padding:5px 12px;margin:4px 0 6px;background:#F3FAF8;font-size:17px"><b style="color:#1F7A6F">An open puzzle for everyone.</b> <b style="color:#D9662B">&#9733; take-home</b> (or the start of the next lesson). ${inv.first}</div>`);
  out.push(q('C', '(a) ' + inv.parts[0], { before: 80, after: 30, keepNext: true }));
  out.push(`<div class="p" style="margin:4px 0 4px 28px"><b>(b)</b> ${inv.parts[1]}</div>`);
  out.push(`<div class="p" style="margin:4px 0 4px 28px"><b>(c)</b> ${inv.parts[2]}</div>`);
  out.push(...lines(6));
  out.push(reflect());
  // Page 4: Think harder
  out.push(...hdr(n, ls.topic, 'THINK HARDER'));
  out.push(p(t('Draw a model, make a list or make a table. Then write how you know. Draw a big, neat diagram first and label every length or angle you know.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  out.push(banner(n === 7 ? 'Think harder  (A1 is a puzzle that goes further: percentage change)' : 'Think harder'));
  // Think harder questions are numbered A1 to A4 and Go further questions B1 to B3, so no printed number repeats Start here Q1 to Q6.
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q('A' + (i + 1), x.q, { before: x.fig ? 90 : 140, after: 40, keepNext: true })); if (x.fig) out.push(H.fig(x.fig)); out.push(...lines(x.fig ? 1 : (n === 7 && i < 2 ? 1 : 3))); });
  // Page 5: Go further
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner('Go further  (a puzzle that goes further)'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q('B' + (i + 1), x.q, { before: 200, after: 40, keepNext: true })); if (x.fig) out.push(H.fig(x.fig)); out.push(...lines(x.fig ? 2 : 4)); });
  // One problem-posing prompt per lesson (think for 30 seconds first). Open-ended, so there is no answer line.
  if (ls.pose) out.push(`<div class="p" style="border:2.5px dashed #D9662B;border-radius:12px;padding:8px 14px;margin:10px 0 0;background:#FFF6EE;font-size:17px"><b style="color:#D9662B">Make up your own.</b> ${ls.pose} <i>(Think for 30 seconds before anyone speaks.)</i></div>`);
  return out;
};
// Page 2 gets a small "Start here" banner and a neutral plan line after its page break.
const page2 = (arr, n) => {
  const i = arr.findIndex(x => typeof x === 'string' && x.startsWith(BRK));
  if (i < 0) return arr;
  const el = arr[i];
  arr.splice(i, 1, BRK, banner('Start here: page 2'), planLine(L.lessons[n - 1].solo), el.slice(BRK.length));
  return arr;
};
const stamps = L.lessons.map(ls => `<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 5 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);
L.content.forEach(c => {
  const l = c.lesson;
  W.push(...hdr(l.n, l.topic, l.title.toUpperCase()));
  W.push(banner('Start here'));
  W.push(choose(l.n));
  W.push(...page2(c.workbook(H), l.n));
  W.push(...extra(l.n));
});
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());
W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 5 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
