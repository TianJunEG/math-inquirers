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
const bx = '<span style="display:inline-block;width:20px;height:20px;border:2.5px solid #1B2A49;border-radius:5px;vertical-align:-4px;margin:0 6px 0 10px"></span>';
const reflect = () => `<div class="p" style="border:3px solid #1F7A6F;border-radius:14px;padding:8px 16px;margin-top:14px;background:#F3FAF8;page-break-inside:avoid"><div style="font-weight:800;font-size:20px;color:#1F7A6F;margin-bottom:4px">What was hard?  <span style="font-weight:400;font-size:16px;color:#444">(just for you: nobody marks this)</span></div>
<div style="margin:5px 0">The hardest part was ______________________________________________________________</div>
<div style="margin:5px 0">I got unstuck by:${bx}drawing a picture or model${bx}making a list or table${bx}trying a simpler number${bx}asking my partner${bx}checking my estimate</div>
<div style="margin:5px 0">Next time I will try ______________________________________________________________</div></div>`;
const fast = () => `<div class="p" style="border:2.5px dashed #D9662B;border-radius:12px;padding:6px 14px;margin:4px 0 6px;background:#FFF6EE;font-size:17px"><b style="color:#D9662B">Fast track.</b> Got BOTH Warm-up check questions right and can explain why? Your tutor may send you straight to the Think Harder pages and the Open Investigation while the group works this page. Come back for talk time. It is a choice of starting place, not a label, and you can swap at any time.</div>`;
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const out = [...hdr(n, ls.topic, 'THINK HARDER')];
  out.push(p(t('Draw a model, make a list or make a table. Then write how you know. Draw a big, neat diagram first and label every length or angle you know.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  out.push(banner(n === 7 ? 'Stretch  (Q1: preview of P6, percentage change)' : 'Stretch'));
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q(i + 1, x.q, { before: 140, after: 40, keepNext: true })); out.push(...lines(n === 7 && i < 2 ? 1 : 3)); });
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner(n === 7 ? 'Challenge  (for strong thinkers: P6 preview)' : 'Challenge  (for strong thinkers)'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q(i + 5, x.q, { before: 200, after: 40, keepNext: true })); out.push(...lines(4)); });
  const inv = L.content[n - 1].investigation;
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner('Open investigation: ' + inv.title));
  out.push(q(8, '(a) ' + inv.parts[0], { before: 120, after: 30, keepNext: true }));
  out.push(`<div class="p" style="margin:4px 0 4px 28px"><b>(b)</b> ${inv.parts[1]}</div>`);
  out.push(`<div class="p" style="margin:4px 0 4px 28px"><b>(c)</b> ${inv.parts[2]}</div>`);
  out.push(...lines(7));
  out.push(reflect());
  return out;
};
const stamps = L.lessons.map(ls => `<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 5 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);
L.content.forEach(c => {
  const l = c.lesson;
  W.push(...hdr(l.n, l.topic, l.title.toUpperCase()));
  W.push(fast());
  W.push(...c.workbook(H));
  W.push(...extra(l.n));
});
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());
W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 5 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
