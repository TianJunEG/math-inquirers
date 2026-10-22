// P4 student workbook (A + D style). Run in p4/:  node workbook_html.js && python3 wb_pdf.py
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

// ---- fix pass: neutral labels, the Investigation + Looking back page every child reaches, solo-page note ----
const px = n => (n / 15).toFixed(1) + 'px';
const esc = x => String(x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const neutralLine = (txt) => `<div class="p" style="margin:0 4px 6px 4px;font-size:14.5px;line-height:1.4;color:#3B4A6B;break-inside:avoid"><b style="color:#1F7A6F">Start here.</b> <i>${esc(txt)}</i></div>`;
const capLine = (txt) => `<div class="p" style="margin:0 4px 0 4px;font-size:13.5px;line-height:1.25;color:#3B4A6B;break-inside:avoid"><i>${esc(txt)}</i></div>`;
const tickBox = '<span style="display:inline-block;width:12px;height:12px;border:2px solid #1B2A49;border-radius:3px;margin:0 4px -2px 12px;background:#fff"></span>';
const reflectBox = () => `<div class="p" style="margin:14px 4px 4px 4px;padding:6px 12px 8px;border:2.5px dashed #1F7A6F;border-radius:10px;background:#F3FBF9;break-inside:avoid"><div style="font-weight:700;color:#1F7A6F;font-size:16px">Looking back <span style="font-weight:400;font-size:12.5px;color:#3B4A6B">2 minutes at the end. You can write, tick or pass. Nobody marks this. It is not shown to the group. Your tutor may look at it on camera if you hold it up.</span></div><div class="p ans" style="margin:6px 0 2px"><b>Something I did well</b><span class="al" style="max-width:520px"></span></div><div class="p ans" style="margin:6px 0 2px"><b>The hardest part was</b><span class="al" style="max-width:520px"></span></div><div style="margin:8px 0 2px;font-size:14px;line-height:1.9"><b>What helped me</b><span style="white-space:nowrap">${tickBox}drawing it</span> <span style="white-space:nowrap">${tickBox}a list or table</span> <span style="white-space:nowrap">${tickBox}a smaller number</span> <span style="white-space:nowrap">${tickBox}my partner</span> <span style="white-space:nowrap">${tickBox}reading it again</span> <span style="white-space:nowrap">${tickBox}I asked for help</span> <span style="white-space:nowrap">${tickBox}other: ________</span> </div><div style="margin:2px 0 2px;font-size:14px;line-height:1.9"><b>One thing I could try next</b><span style="white-space:nowrap">${tickBox}drawing it</span> <span style="white-space:nowrap">${tickBox}a list or table</span> <span style="white-space:nowrap">${tickBox}a smaller number</span> <span style="white-space:nowrap">${tickBox}a partner</span> <span style="white-space:nowrap">${tickBox}another question like this</span> <span style="white-space:nowrap">${tickBox}other: ________</span> <span style="white-space:nowrap">${tickBox}<b>I pass on this one</b></span> <br><span style="white-space:nowrap">${tickBox}<b>I am still stuck</b> (my tutor will check in with me)</span> <span style="white-space:nowrap">${tickBox}<b>I pass today</b> (that is fine)</span> </div></div>`;
const investBlock = (g) => {
  const iv = g.invest, out = [];
  let top = q('Investigation', [t(iv.head + '.  ', { bold: true }), t(iv.kind + '  ', { italics: true, color: '1F7A6F' }), t(iv.intro)], { before: 100, after: 60, keepNext: true }).replace('class="p q', 'class="p q open');
  out.push(top);
  if (iv.fig) out.push(H.fig(iv.fig));
  out.push(`<div class="p easy" style="margin:2px 4px 8px 4px;padding:5px 12px;border-left:6px solid #FFC93C;background:#FFF9E5;font-size:14.5px;line-height:1.4;break-inside:avoid"><b>Easy first step.</b> ${esc(iv.easy)} <span style="color:#3B4A6B">Then carry on with the parts below, as far as you like.</span></div>`);
  iv.parts.forEach((x, i) => out.push(H.sub('abcdef'[i], x, { after: 60 })));
  out.push(...H.lines(iv.lines));
  return out;
};
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const lab = () => p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 });
  const out = [];
  // page 3: the page every child reaches: Investigation (with an easy first step) and Looking back
  out.push(p('', { pb: true, after: 0 }));
  out.push(lab());
  out.push(banner('Investigation  and  Looking back'));
  out.push(...investBlock(L.content[n - 1].gaps));
  out.push(reflectBox());
  // page 4: Think harder
  out.push(p('', { pb: true, after: 0 }));
  out.push(lab());
  out.push(banner('Think harder'));
  out.push(p(t('Draw a model, make a list or make a table. Then write how you know. Choose these any time, or take them home.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q(i + 1, x.q, { before: 140, after: 40, keepNext: true })); if (x.fig) out.push(H.fig(x.fig)); out.push(...lines(x.fig ? 2 : 3)); });
  // page 5: Go further
  out.push(p('', { pb: true, after: 0 }));
  out.push(lab());
  out.push(banner('Go further'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q(i + 5, x.q, { before: 200, after: 40, keepNext: true })); if (x.fig) out.push(H.fig(x.fig)); out.push(...lines(x.fig ? 2 : 4)); });
  return out;
};
// page 1 gets the neutral choice line; page 2 gets the "on your own" note (placed after the page break)
const corePages = (n, c) => {
  const arr = c.workbook(H), BR = '<div class="brk"></div>', cap = c.gaps.cap;
  const out = [neutralLine(c.gaps.p1)];
  let done = false;
  arr.forEach(e => {
    if (!done && typeof e === 'string' && e.startsWith(BR + '<div class="p q')) { done = true; out.push(BR + capLine(cap) + '\n' + e.slice(BR.length)); }
    else out.push(e);
  });
  if (!done) throw new Error('page-2 break not found for lesson ' + n);
  return out;
};
const stamps = L.lessons.map(ls => `<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 4 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);
L.content.forEach(c => {
  const l = c.lesson;
  W.push(...hdr(l.n, l.topic, l.title.toUpperCase()));
  W.push(...corePages(l.n, c));
  W.push(...extra(l.n));
});
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());
W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 4 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
