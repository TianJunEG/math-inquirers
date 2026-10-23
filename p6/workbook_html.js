// P6 student workbook (A + D style). Run in p2/:  node workbook_html.js && python3 wb_pdf.py
const C = require('../hp/common_html.js');
const { fs, t, p, q, lines, banner, AlignmentType } = C;
const L = require('./data.js');
const PROG = L.program, SLOGAN = L.slogan, QB = L.qbank;
const FIG = require('../levels/figs_l4_6.js');
const H = Object.assign({}, C, { fig: (s, o) => '<div class="p img" style="text-align:center">' + FIG.fit(s, 6, Object.assign({ minPt: 7.3 }, o)) + '</div>' });
const W = [];
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const LASTQ1 = { 1: 3, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 7: 2, 8: 2, 9: 4, 10: 3 };
const FASTPTR = n => '<span style="float:right;font-size:11px;line-height:1.2;font-weight:700;color:#1F7A6F;text-align:right;text-decoration:none;max-width:330px;margin-top:2px;letter-spacing:0"><span style="display:inline-block;background:#FFC93C;color:#1B2A49;border:1.5px solid #1B2A49;padding:0 6px;margin-right:4px">Start here</span> After question ' + LASTQ1[n] + ' you may choose: carry on, or try Think harder.</span>';
const SB3 = { 1: 'L1_Sequence_Tester.sb3', 2: 'L2_Prime_Checker.sb3', 3: 'L3_Below_Zero.sb3', 4: 'L4_Function_Machine.sb3', 5: 'L5_Every_Order.sb3', 6: 'L6_Chance_Lab.sb3', 7: 'L7_Turtle_Start.sb3', 8: 'L8_Code_Machine.sb3', 9: 'L9_Mean_Machine.sb3', 10: 'starters L10A to L10D (pick one)' };
const SP = require('../levels/spine_wb.js');   // strategy card + common look-back (docs/pedagogy/spine_routine_spec.md); wording in levels/spine.json
const LEVEL = 6;
const COMPACT = new Set([1, 2, 3, 6, 7, 8, 9]);   // lessons whose first page is too full for the full card: compact chip in the header row (see docs/pedagogy/spine_routine_build_notes.md)
const hdr = (n, topic, title, pb = true, fast = false, file = '') => {   // fast = the lesson's "Start here" page (it carries the strategy card)
  const first = fast;
  const choose = first && SP.DATA.lessons[`${LEVEL}.${n}`].main === 'choose';
  const compact = first && COMPACT.has(n);
  const card = first && !compact ? SP.card(LEVEL, n) : '';
  const chip = compact ? SP.card(LEVEL, n, true) : '';
  const fp = fast ? FASTPTR(n) : '';
  return [
  `<div class="p lh${pb ? ' pb' : ''}"><span class="lbadge">Lesson ${n}</span><span class="ltopic">${topic}</span>${chip}${file ? `<span style="float:right;font-size:11px;font-weight:700;color:#1F7A6F;margin-top:6px;letter-spacing:0">Scratch file: ${file}</span>` : ''}</div>`,
  choose || !card ? `<div class="p ltitle">${fp}${title}</div>` : `<div class="p ltrow" style="display:flex;align-items:center;justify-content:space-between;gap:4mm;margin:4px 0 6px"><div class="ltitle" style="flex:1;min-width:0;margin:0 0 8px;${title.length > 15 ? 'font-size:29px;line-height:1.12' : ''}">${title}</div>${card}</div>`,
  `<div class="p namer"><b>Name</b><span></span><b>Group</b><span style="max-width:90px"></span><b>Date</b><span style="max-width:110px"></span></div>`,
  ...(card && fp ? [`<div class="p" style="overflow:hidden;margin:0">${fp.replace('float:right;', 'float:right;margin-right:0;')}</div>`] : []),
  ...(choose ? [card] : [])
  ];
};
const LN = n => Array.from({ length: n }, () => '<div class="ln"></div>').join('');
const boxStyle = 'border:2.5px solid #1B2A49;box-shadow:4px 4px 0 #1B2A49;background:#fff;border-radius:4px;padding:12px 12px 6px;margin:16px 4px 12px;';
const row = s => '<div style="display:flex;align-items:flex-end;gap:6px;margin:3px 0"><span style="font-weight:700;white-space:nowrap;font-size:15px">' + s + '</span><span style="flex:1;border-bottom:2px dotted #8A94AD;height:22px"></span></div>';
const finish = (n) => {
  const ls = L.lessons[n - 1], g = L.gaps[String(n)];
  const out = [...hdr(n, ls.topic, 'FINISH PAGE')];
  out.push(p(t('Everyone gets to this page. The investigation is for anyone who wants it, at any time. The exit slip and looking back are for everyone.', { italics: true, size: 22 }), { after: 50, align: AlignmentType.CENTER }));
  out.push('<div class="p" style="' + boxStyle + 'font-size:15px;line-height:1.35"><span style="display:inline-block;background:#FFC93C;border:2px solid #1B2A49;padding:1px 10px;font-weight:800;font-size:13px;margin-right:8px">Investigation</span><b>' + esc(g.inv.title.replace(/^Open investigation: /, '')) + '</b><div style="margin:6px 0 2px;font-weight:600">' + esc(g.inv.q) + '</div><div style="margin:6px 0 2px;color:#1F7A6F;font-weight:700">' + esc(g.inv.first) + '</div>' + LN(4) + '</div>');
  out.push('<div class="p" style="' + boxStyle + 'font-size:15px;line-height:1.35"><span style="display:inline-block;background:#DDEBF7;border:2px solid #1B2A49;padding:1px 10px;font-weight:800;font-size:13px;margin-right:8px">Exit slip</span><b>' + esc(ls.exit.q) + '</b><div style="margin-top:4px">' + LN(3) + '</div></div>');
  const tick = s => '<span style="display:inline-block;margin-right:14px;white-space:nowrap;font-size:13.5px">[&nbsp;&nbsp;]&nbsp;' + s + '</span>';
  out.push(SP.lookback(LEVEL));   // common look-back (three prompts, tool ticks, still stuck / pass); replaces the old Looking back box
  return out;
};
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const out = [...hdr(n, ls.topic, 'THINK HARDER')];
  out.push(p(t('Draw a model, make a list or make a table. Then write how you know.', { italics: true, size: 24 }), { after: 50, align: AlignmentType.CENTER }));
  out.push('<div class="p" style="border:2.5px solid #1F7A6F;background:#E8F4F1;border-radius:6px;padding:6px 12px;margin:0 0 4px;font-size:13.5px;line-height:1.35"><b style="color:#1F7A6F">Choose any question.</b> You can start here after question ' + LASTQ1[n] + ', or when you finish the Start here pages. You can go back to Start here at any time. Everyone joins Talk time and the exit slip.</div>');
  const TH = ls.th;
  TH.forEach((x, i) => { out.push(q(i + 1, x.q, { before: i < 4 ? 100 : 60, after: 20, keepNext: true })); out.push(...lines(i < 4 ? 2 : 1)); });
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 40 }));
  out.push(banner('Go further'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q(i + TH.length + 1, x.q, { before: 120, after: 30, keepNext: true })); out.push(...lines(i === 2 ? 3 : 2)); });
  return out;
};
const stamps = L.lessons.map(ls => `<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 6 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);
L.content.forEach(c => {
  const l = c.lesson;
  W.push(...hdr(l.n, l.topic, l.title.toUpperCase(), true, true, SB3[l.n]));
  W.push(...c.workbook(H));
  W.push(...finish(l.n));
  W.push(...extra(l.n));
});
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());
W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 6 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
