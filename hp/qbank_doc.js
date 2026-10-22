const C = require('./common.js');
const { D, fs, t, p, tbl, row, cell, banner, footer, page, gap, AlignmentType, TextRun, FONT, CW } = C; const { Tab, TabStopType } = D;
const L = require('./lessons.js');
const Q = JSON.parse(fs.readFileSync(__dirname + '/qbank.json', 'utf8'));
const PROG = L.program, SLOGAN = L.slogan;
const S = 23;
const qline = (tag, text, o = {}) => p([t(tag, { bold: true, size: S }), new TextRun({ children: [new Tab()], font: FONT, size: S }), t(text, { size: S })],
  { indent: { left: 640, hanging: 640 }, tabStops: [{ type: TabStopType.LEFT, position: 640 }], before: 60, after: 60, line: 290 });
const aline = (tag, text) => p([t(tag, { bold: true, size: 20 }), new TextRun({ children: [new Tab()], font: FONT, size: 20 }), t(text, { size: 20 })],
  { indent: { left: 640, hanging: 640 }, tabStops: [{ type: TabStopType.LEFT, position: 640 }], before: 20, after: 20, line: 260 });
const tiers = [['core', 'C', 'CORE (low floor: start with objects, drawing or counting)'], ['stretch', 'S', 'THINK HARDER (use this lesson\'s idea in a new setting)'], ['challenge', 'G', 'CHALLENGE (after the topic: extend, justify, make up your own)']];
const W = [];
W.push(p(t(PROG.toUpperCase(), { bold: true, size: 40 }), { align: AlignmentType.CENTER, before: 200, after: 60 }));
W.push(p(t('Question Bank  •  Level 1', { bold: true, size: 32 }), { align: AlignmentType.CENTER, after: 60 }));
W.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { align: AlignmentType.CENTER, after: 240 }));
W.push(banner('How to use this bank'));
[
 'Each lesson has three levels. Every child starts with Core, then moves up when they are ready. Challenge questions are the ones to talk about together.',
 'CORE questions are low floor: a child who has not yet learnt the topic can start them with objects, a drawing, counting or guess-and-check. No special method is needed. Use them for warm-ups and for children who need confidence.',
 'THINK HARDER questions need the idea taught in the lesson, used in a new setting: two-step problems, patterns with a hidden rule, simple unknowns and larger numbers.',
 'GO FURTHER questions are for any child who chooses them after the topic. They need the lesson idea plus an extension: more than one step, finding every way, working backwards, justifying an answer, changing one thing and asking what happens, or making up a puzzle of their own. Open questions have no single right answer; check the reasoning. This uses low-floor, high-ceiling task ideas and problem-solving habits from enrichment research. It does not label children, it is not an official GEP standard, and this program is not affiliated with MOE.',
 'Ask for the reason every time: “How do you know?” A correct answer with no reason is only half done.',
 'Answers are at the back. Do not hand the answer pages to children.'
].forEach(s => W.push(p(t(s, { size: 24 }), { after: 100, indent: { left: 300 } })));
W.push(gap(120));
W.push(banner('What each lesson practises'));
const rows = L.lessons.map(l => row([cell(t('Lesson ' + l.n, { bold: true, size: 22 }), 1600, { h: 60, align: AlignmentType.LEFT }), cell(t(l.title + ' (' + l.topic + ')', { size: 22 }), 4700, { h: 60, align: AlignmentType.LEFT }), cell(t(Q[l.n].core.length + ' + ' + Q[l.n].stretch.length + ' + ' + Q[l.n].challenge.length + ' questions', { size: 22 }), 3600, { h: 60, align: AlignmentType.LEFT })]));
W.push(tbl([1600, 4700, 3600], rows));
L.lessons.forEach(l => {
  W.push(p(t('Lesson ' + l.n + ': ' + l.title, { bold: true, size: 32 }), { pb: true, after: 40 }));
  W.push(p(t(l.topic + '  •  Week ' + l.week, { italics: true, size: 24, color: '555555' }), { after: 80 }));
  tiers.forEach(([key, tag, label], ti) => {
    W.push(banner(label));
    Q[l.n][key].forEach((x, i) => W.push(qline(tag + (i + 1) + '.', x.q)));
    if (ti < tiers.length - 1) W.push(gap(60));
  });
});
W.push(p(t('Answer key (tutor only)', { bold: true, size: 36 }), { pb: true, after: 80 }));
L.lessons.forEach(l => {
  W.push(p(t('Lesson ' + l.n + ': ' + l.title, { bold: true, size: 24 }), { before: 160, after: 40, keepNext: true }));
  tiers.forEach(([key, tag]) => {
    Q[l.n][key].forEach((x, i) => W.push(aline(tag + (i + 1) + '.', x.a)));
  });
});
const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: 24 } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + '  •  Question Bank') }, children: W }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync(__dirname + '/Math_Inquirers_Level1_Question_Bank.docx', b); console.log('qbank built'); });
