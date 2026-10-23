// P3 student workbook (A + D style). Run in p2/:  node workbook_html.js && python3 wb_pdf.py
const C = require('../hp/common_html.js');
const { fs, t, p, q, lines, banner, AlignmentType } = C;
const GF = JSON.parse(fs.readFileSync(__dirname + '/gifted.json', 'utf8'));
const L = require('./data.js');
const PROG = L.program, SLOGAN = L.slogan, QB = L.qbank;
const H = Object.assign({}, C, { fig: s => '<div class="p img" style="text-align:center">' + s + '</div>' });
const W = [];
const FG = require('./figs_l3.js').FX;   // Level 3 figures (shared helper hp/figs_l1_3.js); keys '<lesson>.<q>', '<lesson>.<q><part>', '<lesson>.t<n>', '<lesson>.c<n>'
let CUR = 0, LASTQ = 0;
H.q = (n, text, o) => { LASTQ = n; return C.q(n, text, o) + (FG[CUR + '.' + n] ? '\n' + FG[CUR + '.' + n]() : ''); };
H.sub = (l, text, o) => C.sub(l, text, o) + (l && FG[CUR + '.' + LASTQ + l] ? '\n' + FG[CUR + '.' + LASTQ + l]() : '');
const SP = require('../levels/spine_wb.js');   // strategy card + common look-back (docs/pedagogy/spine_routine_spec.md); wording in levels/spine.json
const LEVEL = 3;
const COMPACT = new Set([3, 5, 7, 10]);   // lessons whose first page is too full for the full card: compact chip in the header row (see docs/pedagogy/spine_routine_build_notes.md)
const hdr = (n, topic, title, pb = true, first = false) => {   // first = the lesson's "Start here" page: it carries the strategy card
  const choose = first && SP.DATA.lessons[`${LEVEL}.${n}`].main === 'choose';
  const compact = first && COMPACT.has(n) && !choose;
  const card = first && !compact ? SP.card(LEVEL, n, choose && COMPACT.has(n)) : '';
  const chip = compact ? SP.card(LEVEL, n, true) : '';
  return [
  `<div class="p lh${pb ? ' pb' : ''}"><span class="lbadge" style="white-space:nowrap">Lesson ${n}</span><span class="ltopic">${topic}</span>${chip}</div>`,
  choose || !card ? `<div class="p ltitle">${title}</div>` : `<div class="p ltrow" style="display:flex;align-items:center;justify-content:space-between;gap:4mm;margin:4px 0 6px"><div class="ltitle" style="flex:1;min-width:0;margin:0 0 8px;${title.length > 15 ? 'font-size:29px;line-height:1.12' : ''}">${title}</div>${card}</div>`,
  `<div class="p namer"><b>Name</b><span></span><b>Group</b><span style="max-width:90px"></span><b>Date</b><span style="max-width:110px"></span></div>`,
  ...(choose ? [card] : [])
  ];
};

// ---- gifted-style additions: fast track note, investigation, look-back reflection (data in p3/gifted.json) ----
const NAVY = '#1B2A49';
const esc2 = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const fr = (n, d) => `<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.1;margin:0 3px;font-weight:600"><span style="padding:0 3px">${n}</span><span style="border-top:2px solid ${NAVY};padding:0 3px">${d}</span></span>`;
const rich = s => esc2(s).replace(/\[\[(\d+)\/(\d+)\]\]/g, (m, n, d) => fr(n, d));
const tick = `<span style="display:inline-block;width:13px;height:13px;border:2px solid ${NAVY};border-radius:3px;background:#fff;vertical-align:-2px;margin:0 5px 0 14px"></span>`;
const startHere = () => C.tbl([9900], [C.row([C.cell([`<div style="text-align:left;font-size:12.5px;line-height:1.4"><b>Start here.</b> After question 3 you may choose: carry on, or try Think harder.</div>`], 9900, { align: 'left', fill: 'F2F2F2', h: 25 })])]);
const stairsSvg = () => {
  const u = 26; let s = `<svg aria-label="Staircases with 1, 2 and 3 steps" viewBox="0 0 600 110" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:420px">`;
  [[1, 20], [2, 130], [3, 270]].forEach(([k, x0]) => {
    for (let c = 1; c <= k; c++) for (let r = 0; r < c; r++) s += `<rect x="${x0 + (c - 1) * u}" y="${90 - (r + 1) * u}" width="${u}" height="${u}" fill="#FFC93C" stroke="${NAVY}" stroke-width="2.5"/>`;
    s += `<text x="${x0 + k * u / 2}" y="106" font-size="14" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${k} step${k > 1 ? 's' : ''}</text>`;
  });
  return s + '</svg>';
};
const investigation = (n) => {
  const g = GF[String(n)].inv, out = [];
  out.push(banner('Investigation: ' + g.title));
  out.push(q(8, [rich(g.intro)], { before: 100, after: 40, keepNext: true }));
  out.push(p(t(g.easy.replace(/\[\[(\d+)\/(\d+)\]\]/g, '$1/$2'), { italics: true, size: 20, color: '1F7A6F' }), { after: 60 }));
  if (g.fig === 'stairs') out.push('<div class="p img" style="text-align:center">' + stairsSvg() + '</div>');
  g.parts.forEach((pt, i) => {
    out.push(C.sub('abc'[i], [rich(pt)], { after: 60 }));
    if (i === 0 && g.table) {
      const nc = g.table.cols.length, hasLab = g.table.rows.some(r => r !== ''), first = hasLab ? 1700 : 0;
      const w = hasLab ? [first, ...Array(nc - 1).fill(Math.floor((9900 - first) / (nc - 1)))] : Array(nc).fill(Math.floor(9900 / nc));
      const rh = g.table.rows.length > 8 ? 34 : 70;
      out.push(C.tbl(w, [C.row(g.table.cols.map((c, j) => C.cell(c, w[j], { bold: true, fill: 'D9D9D9', size: 18, h: 40 }))), ...g.table.rows.map(r => C.row(w.map((ww, j) => (j === 0 && hasLab) ? C.cell(r, ww, { bold: true, fill: 'EDEDED', size: 20, h: rh }) : C.cell('', ww, { h: rh }))))]));
      out.push(C.gap(40));
    }
  });
  out.push(...lines(g.table ? g.lines : g.lines + 3));
  return out;
};
const lookBack = (n) => [SP.lookback(LEVEL)];   // common look-back (three prompts, tool ticks, still stuck / pass); replaces the old reflection box
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const out = [...hdr(n, ls.topic, 'THINK HARDER')];
  out.push(p(t('Draw a model, make a list or make a table. Then write how you know.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  out.push(p(t('Think harder is for anyone who wants it. Try a question, then try the Investigation on the last page of this lesson if you like.', { italics: true, size: 20, color: '1F7A6F' }), { after: 60, align: AlignmentType.CENTER }));
  out.push(banner('Think harder'));
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q(i + 1, x.q, { before: 140, after: 40, keepNext: true })); const fx = FG[n + '.t' + (i + 1)]; if (fx) out.push(fx()); out.push(...lines(fx ? 1 : (n === 8 ? 2 : 3))); });
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner('Go further'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q(i + 5, x.q, { before: 200, after: 40, keepNext: true })); const fx = FG[n + '.c' + (i + 5)]; if (fx) out.push(fx()); out.push(...lines(fx ? 2 : 4)); });
  const th = (L.content[n - 1].deck.takeHome || []);   // quick questions the lesson did not have time for (answers are in the tutor guide)
  if (th.length) {
    out.push(banner('★ Take-home'));
    out.push(p(t('For home, if you like. These were extra warm-up questions. They are not for the lesson.', { italics: true, size: 20, color: '1F7A6F' }), { after: 60 }));
    th.forEach((x, i) => out.push(C.sub('abc'[i], x[0] + '   ______________', { after: 70 })));
  }
  out.push(...hdr(n, ls.topic, 'INVESTIGATION AND LOOK BACK'));
  out.push(...investigation(n));
  out.push(...lookBack(n));
  return out;
};
const coreEnd = (n) => { const g = GF[String(n)].inv; return C.tbl([9900], [C.row([C.cell([`<div style="text-align:left;font-size:12.5px;line-height:1.4"><b>Want more? You choose.</b> Think harder is the next page. Or try the Investigation (${esc2(g.title)}) on the last page of this lesson. ${esc2(g.easy).replace(/\[\[(\d+)\/(\d+)\]\]/g, '$1/$2')}</div>`], 9900, { align: 'left', fill: 'F2F2F2', h: 25 })])]); };
const stamps = L.lessons.map(ls => `<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 3 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);
L.content.forEach(c => {
  const l = c.lesson;
  CUR = l.n;
  W.push(...hdr(l.n, l.topic, l.title.toUpperCase(), true, true));
  W.push(startHere());
  W.push(...c.workbook(H));
  W.push(coreEnd(l.n));
  W.push(...extra(l.n));
});
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());
W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 3 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
