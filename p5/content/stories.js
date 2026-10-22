// P5 "Story break" data: one mathematician per lesson. Source of truth is docs/stories/final_p5.json (researched, with source URLs).
// This module only (1) formats the text for children (Singapore number style), (2) holds the short workbook blurbs, and
// (3) lists the few wording changes made for the P5 rules. Every try-it answer is verified in docs/audit/stories_verify_p5.py.
const fs = require('fs'), path = require('path');
const RAW = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', 'docs', 'stories', 'final_p5.json'), 'utf8'));
const NB = ' ';
// 2,450,000 -> "2 450 000" (non-breaking spaces); 1,250 -> "1250"; "x" between numbers -> "×"; " / " -> " ÷ "
const fmt = s => String(s)
  .replace(/\d{1,3}(?:,\d{3})+/g, m => { const d = m.replace(/,/g, ''); return d.length >= 5 ? d.replace(/\B(?=(\d{3})+(?!\d))/g, NB) : d; })
  .replace(/(?<=[\d)]|cm) x (?=[\d(])/g, ' × ')
  .replace(/(?<=\d) \/ (?=\d)/g, ' ÷ ')
  .replace(/(?<=[\d)]) - (?=[\d$(])/g, ' − ')
  .replace(/(\d+) degrees?\b/g, '$1°')
  .replace(/\bsquare cm\b/g, 'cm²').replace(/\bcubic cm\b/g, 'cm³');

// Wording changes for the P5 rules (the program does not use the word "speed": rate per hour is P5, speed is not).
const OVERRIDE = {
  6: {
    story: s => s.replace('a wind tunnel that blew air at almost twice the speed of sound over model aircraft', 'a wind tunnel that blew air over model aircraft almost twice as fast as sound travels'),
    link: 'A wind tunnel test is full of rates: how far air or a plane moves in each hour or each second, just like the rates you work with today.',
    q: 'A model plane flies 840 km in 3 hours at a steady rate. How far does it fly in 1 hour? At that rate, how far would it fly in 5 hours?',
    a: '840 ÷ 3 = 280 km in 1 hour (a rate of 280 km per hour). In 5 hours: 280 × 5 = 1400 km.'
  }
};
// Short labels for the slide title and the guide table
const SHORT = { 7: 'Adam Ries' };
// Short place and date labels for the slide and the workbook box (the guide table uses the full text from the JSON)
const CSHORT = { 2: 'England and the United States', 3: "England and Charlemagne's court", 8: 'Iran and the United States', 9: 'Baghdad (today Iraq)', 10: 'Hungary, Switzerland and the United States' };
const YSHORT = { 4: '3rd century CE', 5: 'about 287 to about 212 BC' };
// Child-facing version of the legend note when the research note has a tutor-only part
const LEGEND_KID = { 7: 'Sources give his birth year as 1492 or 1493.' };
const ALSO = { 7: 'also spelled Adam Riese' };
// Corner-box blurbs for the workbook (2 to 3 sentences, every fact taken from the researched story)
const BLURB = {
  1: 'Dorothy Vaughan was a maths teacher who joined the NACA laboratory at Langley (it later became NASA) in 1943. She became head of a team of "human computers" who did long calculations by hand. When electronic computers arrived, she taught herself the FORTRAN programming language and taught it to her team too.',
  2: 'Eugenia Cheng is a mathematician, born in England in 1976, who explains maths with food. Her book How to Bake Pi (2015) opens each chapter with a dessert recipe, and one example is about three brothers and sisters trying to share a cake.',
  3: 'Alcuin of York was a monk and teacher from Northumbria who helped the emperor Charlemagne run schools. A Latin book of about fifty number puzzles, Problems to Sharpen the Young, is linked with him. Historians think he collected the puzzles, so he may not have invented them all.',
  4: 'Liu Hui lived in China in the 3rd century. In the year 263 he wrote a commentary on The Nine Chapters on the Mathematical Art, explaining why its rules for the areas of fields work. He often cut shapes into pieces and moved the pieces around.',
  5: 'Archimedes lived in Syracuse, Sicily, about 2300 years ago. He wrote a real book called On Floating Bodies and studied the volumes of solid shapes. A famous bath-and-wreath tale is told about him, but it was written down about 200 years later and historians doubt the details.',
  6: 'Mary Jackson was born in 1921 in Hampton, Virginia. She began as a human computer at the NACA laboratory at Langley, then worked on a wind tunnel for model aircraft. After graduate-level courses she became an aerospace engineer in 1958.',
  7: 'Adam Ries was born in what is now Germany around 1492 and ran a calculation school in Erfurt. He wrote arithmetic books in German, not Latin, so apprentices could read them, with everyday examples about prices, wages, profit and loss, and interest. In Germany people still say a sum is right "nach Adam Riese".',
  8: 'Maryam Mirzakhani grew up in Tehran, Iran, and won gold medals at the International Mathematical Olympiad in 1994 and 1995. She often thought by drawing big sketches, and she studied the paths of a ball bouncing around a billiard table. In 2014 she became the first woman to win the Fields Medal.',
  9: 'Al-Karaji lived about a thousand years ago and spent most of his life in Baghdad. In his algebra book Al-Fakhri he explained rules for working with unknown numbers. He also wrote about a pattern: add the cubes of 1, 2, 3 and so on, and you get the square of the sum of those numbers.',
  10: 'George Polya was born in Budapest, Hungary, in 1887 and later taught in Switzerland and the United States. His 1945 book How to Solve It gave four steps for any problem: understand it, make a plan, carry it out, and look back at your work. His helpful ideas include drawing a picture and working backwards.'
};
const out = {};
RAW.forEach(r => {
  const o = OVERRIDE[r.lesson] || {};
  const fixYears = s => s.replace(/(\d)-(?=\d|about)/g, '$1–');
  out[r.lesson] = {
    lesson: r.lesson,
    name: r.name, short: SHORT[r.lesson] || r.name, also: ALSO[r.lesson] || '',
    years: fixYears(r.years), yshort: YSHORT[r.lesson] || fixYears(r.years), country: r.country_or_region, cshort: CSHORT[r.lesson] || r.country_or_region, who: r.who,
    story: fmt(o.story ? o.story(r.story) : r.story),
    link: fmt(o.link || r.link_to_lesson),
    q: fmt(o.q || r.try_it.q), a: fmt(o.a || r.try_it.a),
    legend: r.legend_note || '', legendKid: LEGEND_KID[r.lesson] || r.legend_note || '', confidence: r.confidence,
    blurb: BLURB[r.lesson]
  };
});
module.exports = out;
