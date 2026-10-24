const fs = require('fs');
const L = require('../hp/lessons.js').lessons;
const DATA = require('./data.js');
const QB = JSON.parse(fs.readFileSync(__dirname + '/../hp/qbank.json', 'utf8'));
const out = __dirname + '/project/slides/';
const PROG = 'Math Inquirers Holiday Program', SLOGAN = 'Notice it. Test it. Explain why.';
const FOOT = `${PROG}  •  ${SLOGAN}`;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const foot = c => `<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:${c}">${FOOT}</p>`;
const pill = (t, bg, fg) => `<p style="align-self:flex-start;background:${bg};color:${fg};border-radius:999px;padding:8px 24px;font-size:28px;font-weight:700">${esc(t)}</p>`;
const time = t => `<p style="position:absolute;right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:#1F7A6F">${esc(t)}</p>`;
const card = inner => `<div style="background:#FFFFFF;border-radius:24px;padding:36px 40px;display:flex;flex-direction:column;gap:14px">${inner}</div>`;
const pic = t => `<p style="border:3px dashed #1F7A6F;border-radius:24px;padding:18px 32px;font-size:28px;font-style:italic;color:#3B4A6B">Picture: ${esc(t)}</p>`;
const h2 = t => `<h2 style="font-family:'Fredoka', Arial, sans-serif;font-size:68px;font-weight:600;line-height:1.1">${esc(t)}</h2>`;
const cream = (id, body, notes, tm) => `<section id="${id}" data-transition="fade" style="background:#FFF9EC;color:#1B2A49;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:28px">\n${tm ? time(tm) + '\n' : ''}${body}\n${foot('#5B6785')}\n<aside>${esc(notes)}</aside>\n</section>\n`;
const dark = (id, body, notes) => `<section id="${id}" data-transition="fade" style="background:#1B2A49;color:#FFF9EC;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n${body}\n${foot('#B7C3DD')}\n<aside>${esc(notes)}</aside>\n</section>\n`;
const tbl = rows => rows ? `<table style="font-size:34px">${rows.map((r, i) => `<tr${i % 2 ? ' style="background:#FFFFFF"' : ''}>${r.map(c => i === 0 ? `<th style="text-align:left">${esc(c)}</th>` : `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</table>` : '';
const numbered = (items, size = 38) => items.map((q, i) => card(`<p style="font-size:${size}px;font-weight:600"><span style="color:#1F7A6F">${i + 1}.</span>  ${esc(q)}</p>`)).join('\n');
const w = (id, s) => fs.writeFileSync(out + id + '.html', s);

// shared slides
w('cover', dark('cover', `<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">PRIMARY 1 HOLIDAY PROGRAM</p>
<h1 style="font-family:'Fredoka', Arial, sans-serif;font-size:140px;font-weight:600;line-height:1.05">Math Inquirers</h1>
<p style="font-family:'Fredoka', Arial, sans-serif;font-size:64px;font-weight:500;color:#FFC93C">${SLOGAN}</p>
<p style="font-size:36px;color:#C9D4EC">10 lessons  •  90 minutes each  •  Face to face or online</p>`, 'Welcome the children by name. Tell them they are inquirers for the next five weeks: they notice patterns, test ideas with real things and explain their thinking. They collect a stamp in their inquiry journal after every lesson.').replace(`<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">${FOOT}</p>\n`, ''));
w('routine', cream('routine', `${h2('How every lesson runs')}
<table style="font-size:32px">
<tr><th style="width:20%;text-align:left">Minutes</th><th style="width:25%;text-align:left">Part</th><th style="width:55%;text-align:left">What we do</th></tr>
<tr style="background:#FFFFFF"><td>0–10</td><td><b>Warm-up</b></td><td>A quick game and quick questions</td></tr>
<tr><td>10–25</td><td><b>Explore</b></td><td>Hands-on with objects, in pairs</td></tr>
<tr style="background:#FFFFFF"><td>25–35</td><td><b>Mini-lesson</b></td><td>Worked examples and the key idea</td></tr>
<tr><td>35–40</td><td><b>Brain break</b></td><td>Move and drink water</td></tr>
<tr style="background:#FFFFFF"><td>40–70</td><td><b>Worksheet</b></td><td>Pairs, then on your own, then stretch</td></tr>
<tr><td>70–80</td><td><b>Talk time</b></td><td>Share your answer and explain why</td></tr>
<tr style="background:#FFFFFF"><td>80–90</td><td><b>Exit ticket</b></td><td>One question, then a stamp</td></tr>
</table>`, 'Show this slide in Lesson 1 and refer back to it in Lesson 2. After that children know the routine. Online: ask children to keep materials and the workbook beside them from the first minute.'));
const rule = (n, s) => `<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-family:'Fredoka', Arial, sans-serif;font-size:72px;font-weight:600;color:#FFC93C">${n}</p><p style="font-size:48px;font-weight:600">${s}</p></div>`;
w('rules', `<section id="rules" data-transition="fade" style="background:#1B2A49;color:#FFF9EC;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:48px">
<h2 style="font-family:'Fredoka', Arial, sans-serif;font-size:80px;font-weight:600;line-height:1.1">The inquirer rules</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px">${rule(1, 'Notice the pattern.')}${rule(2, 'Test it with objects.')}${rule(3, 'Check your answer.')}${rule(4, 'Explain why.')}</div>
${foot('#B7C3DD')}
<aside>${esc('Read the four rules aloud together. Come back to this slide whenever a child is stuck: which rule could help?')}</aside>
</section>
`);
w('end', dark('end', `<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">WELL DONE, INQUIRERS</p>
<h1 style="font-family:'Fredoka', Arial, sans-serif;font-size:128px;font-weight:600;line-height:1.05">Keep asking why</h1>
<p style="font-family:'Fredoka', Arial, sans-serif;font-size:64px;font-weight:500;color:#FFC93C">${SLOGAN}</p>
<p style="font-size:36px;color:#C9D4EC">Certificates and a last stamp for every inquirer.</p>`, 'Hand out certificates. Ask each child to name one puzzle they enjoyed. Give parents the one-page summary from the tutor guide.'));

const order = ['cover', 'routine', 'rules'];
const sections = { s0: { description: 'Welcome, how every lesson runs and the inquirer rules.', start: 'cover' } };
const stale = [];
for (const l of L) {
  const n = l.n, d = DATA[n], id = 'l' + n, q = QB[n];
  const ids = ['title', 'warm1', 'warm2', 'explore1', 'explore2', 'mini1', 'mini2', 'key', 'break', 'ws1', 'ws2', 'stretch', 'challenge', 'talk', 'exit'].map(s => id + '-' + s);
  order.push(...ids);
  sections['s' + n] = { description: `Lesson ${n}: ${l.title}.`, start: id + '-title' };
  stale.push(id + '-warm');
  // title
  w(id + '-title', dark(id + '-title', `<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">LESSON ${n}  •  WEEK ${l.week}</p>
<h1 style="font-family:'Fredoka', Arial, sans-serif;font-size:128px;font-weight:600;line-height:1.05">${esc(l.title)}</h1>
<p style="font-size:44px;color:#C9D4EC">${esc(l.topic)}</p>
<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:#FFC93C">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">${esc(d.today)}</p></div>`, `Objective: ${l.objective} Materials: ${l.materials} Online: ${l.online} Time plan: warm-up 0 to 10, explore 10 to 25, mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70, talk time 70 to 80, exit ticket 80 to 90.`));
  w(id + '-warm1', cream(id + '-warm1', `${h2('Warm-up: ' + l.title)}${card(pill('WARM-UP GAME', '#FFC93C', '#1B2A49') + `<p style="font-size:42px;font-weight:600">${esc(d.warmGame)}</p>`)}`, `Minutes 0 to 5. ${l.warmup}`, '0–5 MIN'));
  w(id + '-warm2', cream(id + '-warm2', `${h2('Quick questions')}${numbered(d.warmQs.map(x => x[0]), 40)}`, 'Minutes 5 to 10. Ask each question aloud, pause, then take answers. Answers: ' + d.warmQs.map((x, i) => `${i + 1}) ${x[1]}`).join('  '), '5–10 MIN'));
  w(id + '-explore1', cream(id + '-explore1', `${h2('Explore: what to do')}${card(pill('EXPLORE', '#1F7A6F', '#FFF9EC') + `<ol style="font-size:36px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:10px">${d.expSetup.map(s => `<li>${esc(s)}</li>`).join('')}</ol>`)}${pic(d.expPic)}`, `Minutes 10 to 15. Pairs work with the materials: ${l.materials} ${l.explore} Online: ${l.online}`, '10–15 MIN'));
  w(id + '-explore2', cream(id + '-explore2', `${h2('Explore: talk about it')}${numbered(d.expAsk.map(x => x[0]), 40)}`, 'Minutes 15 to 25. Let pairs keep working and move around the room (or breakout rooms). Gather them to answer these. Answers: ' + d.expAsk.map((x, i) => `${i + 1}) ${x[1]}`).join('  '), '15–25 MIN'));
  const mini = m => cream('', `${h2(m.head)}${tbl(m.table)}${card(m.body.map(s => `<p style="font-size:38px;font-weight:600">${esc(s)}</p>`).join(''))}`, '', '');
  const mk = (sid, m, tm, extra) => w(id + '-' + sid, cream(id + '-' + sid, `${h2(m.head)}${tbl(m.table)}${card(m.body.map(s => `<p style="font-size:38px;font-weight:600">${esc(s)}</p>`).join(''))}`, `${extra} Answer: ${m.ans}`, tm));
  mk('mini1', d.mini1, '25–30 MIN', 'Worked example 1. Model it, then let children try.');
  mk('mini2', d.mini2, '30–33 MIN', 'Worked example 2. Ask children to explain each step in their own words. ' + l.mini);
  w(id + '-key', cream(id + '-key', `${h2(d.keyHead)}${card(`<p style="font-size:44px;font-weight:700">${esc(d.keyBig)}</p><p style="font-size:34px;color:#3B4A6B">${esc(d.keySmall)}</p>`)}${card(pill('COMMON MISTAKES', '#FFC93C', '#1B2A49') + l.mistakes.map(m => `<p style="font-size:30px">• ${esc(m)}</p>`).join(''))}`, 'Minutes 33 to 35. Say the key idea together. Common mistakes are for the tutor to watch for during the worksheet.', '33–35 MIN'));
  w(id + '-break', `<section id="${id}-break" data-transition="fade" style="background:#1F7A6F;color:#FFF9EC;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">
<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">35–40 MIN</p>
<h2 style="font-family:'Fredoka', Arial, sans-serif;font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>
<p style="font-size:48px;font-weight:600">${esc(d.brk)}</p>
<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>
${foot('#D7EFEA')}
<aside>Five minutes. Online: children stay in view of the camera and move in place.</aside>
</section>
`);
  w(id + '-ws1', cream(id + '-ws1', `${h2('Worksheet: with your partner')}${card(pill('PAGE 1', '#1F7A6F', '#FFF9EC') + `<p style="font-size:42px;font-weight:600">${esc(d.ws1)}</p>`)}${card(`<p style="font-size:34px">Remember the rules: <b>notice</b> the pattern, <b>test</b> it with objects, <b>check</b> your answer, <b>explain</b> why.</p>`)}`, 'Minutes 40 to 55. Walk around. Ask “How do you know?” before giving any help. Answers are in the tutor guide.', '40–55 MIN'));
  w(id + '-ws2', cream(id + '-ws2', `${h2('Worksheet: on your own')}${card(pill('PAGE 2', '#1F7A6F', '#FFF9EC') + `<p style="font-size:42px;font-weight:600">${esc(d.ws2)}</p>`)}${card(`<p style="font-size:34px">Finished early? Move to the <b>Stretch</b> and <b>Challenge</b> slides next.</p>`)}`, 'Minutes 55 to 65. Children work alone. Note who needs a short catch-up next lesson.', '55–65 MIN'));
  const S = q.stretch.slice(0, 3).map(x => x.q), Sa = q.stretch.slice(0, 3).map(x => x.a);
  const G = q.challenge.slice(-2).map(x => x.q), Ga = q.challenge.slice(-2).map(x => x.a);
  w(id + '-stretch', cream(id + '-stretch', `${h2('Stretch')}${numbered(S, 36)}`, 'Minutes 65 to 70. For children who finish early; take the whole group through one together if time allows. More are in the question bank. Answers: ' + Sa.map((a, i) => `${i + 1}) ${a}`).join('  '), '65–70 MIN'));
  w(id + '-challenge', cream(id + '-challenge', `${h2('Challenge')}${numbered(G, 34)}`, 'Use as a pair challenge or in talk time. Ask for the reason every time. More are in the question bank. Answers: ' + Ga.map((a, i) => `${i + 1}) ${a}`).join('  '), '65–80 MIN'));
  w(id + '-talk', cream(id + '-talk', `${h2('Talk time')}${card(pill('TALK TIME', '#FFC93C', '#1B2A49') + `<p style="font-size:42px;font-weight:600">${esc(l.share)}</p>`)}${card(`<p style="font-size:34px;color:#3B4A6B">Sentence starters:</p><p style="font-size:38px;font-weight:600">“I noticed that …”   “I tested it by …”   “I know because …”</p>`)}`, 'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Praise the reasons, not only the answers.', '70–80 MIN'));
  w(id + '-exit', cream(id + '-exit', `${h2('Exit ticket')}${card(pill('EXIT TICKET', '#1F7A6F', '#FFF9EC') + `<p style="font-size:46px;font-weight:600">${esc(l.exit.q)}</p>`)}${card(`<p style="font-size:34px">Write your answer on a slip of paper. Tick it when your tutor shows the answer. Then collect your stamp in your inquiry journal.</p>`)}`, `Minutes 80 to 90. Answer: ${l.exit.a} Extension: ${l.extension}`, '80–90 MIN'));
}
order.push('end');
sections.s11 = { description: 'Wrap-up and certificates.', start: 'end' };
const deck = JSON.parse(fs.readFileSync(__dirname + '/project/deck.json', 'utf8'));
deck.order = order; deck.sections = sections; deck.title = 'Math Inquirers Holiday Program: Primary 1 Lesson Slides';
fs.writeFileSync(__dirname + '/project/deck.json', JSON.stringify(deck, null, 2));
fs.writeFileSync(__dirname + '/stale.json', JSON.stringify(stale));
console.log(order.length, 'slides');
