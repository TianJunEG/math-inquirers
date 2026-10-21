const fs = require('fs');
const L = require('../hp/lessons.js').lessons;
const out = __dirname + '/project/slides/';
const foot = c => `<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:${c}">Maths Detectives Holiday Lab  •  Spot it. Solve it. Say why.</p>`;
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const pill = (t, bg, fg) => `<p style="align-self:flex-start;background:${bg};color:${fg};border-radius:999px;padding:8px 24px;font-size:28px;font-weight:700">${t}</p>`;
const card = (inner) => `<div style="background:#FFFFFF;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:16px">${inner}</div>`;
const pic = t => `<p style="border:3px dashed #1F7A6F;border-radius:24px;padding:20px 32px;font-size:28px;font-style:italic;color:#3B4A6B">Picture: ${esc(t)}</p>`;
const cream = (id, body, notes) => `<section id="${id}" data-transition="fade" style="background:#FFF9EC;color:#1B2A49;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">\n${body}\n${foot('#5B6785')}\n<aside>${esc(notes)}</aside>\n</section>\n`;
const h2 = t => `<h2 style="font-family:'Fredoka', Arial, sans-serif;font-size:72px;font-weight:600;line-height:1.1">${esc(t)}</h2>`;

// per-lesson extra content: today, warmShort, exploreShort, keyHead, keyRows(optional table), keyBig, keySmall, picWarm, picKey
const D = {
 3: { today: 'Vote, build a picture graph, and read it to find the most, the fewest and how many more.',
  warm: 'Quick vote. Choose ONE fruit and put your sticky dot on it.',
  explore: 'Turn the class vote into a picture graph. One counter is one child. Read it aloud: most, fewest, same, how many more.',
  keyHead: 'Key idea: read the graph',
  table: [['Fruit','Orange','Grape','Banana','Watermelon'],['Children','6','8','5','5']],
  big: 'Key: 1 symbol = 1 child.', small: 'How many more? Take away the smaller from the bigger. Total? Count by 5s to be quick.',
  picW: 'five fruit pictures on a wall (apple, orange, banana, grape, watermelon) with children placing sticky dots under them.',
  picK: 'a picture graph with five columns of small smiley faces, one smiley for each child, and a key box that says “1 face = 1 child”.' },
 4: { today: 'Find the core of a repeating pattern, predict far places, and grow a stick pattern.',
  warm: 'Clap-snap-stomp patterns. What comes next? What comes in the 10th place?',
  explore: 'Build 1, 2 and 3 triangles in a row with sticks. Count the sticks. Predict the 4th before you build it.',
  keyHead: 'Key idea: core and growth',
  table: [['Triangles','1','2','3','4','5'],['Sticks','3','5','7','9','11']],
  big: 'Each new triangle shares a side, so we add only 2 sticks.', small: 'For a repeating pattern, count how long the core is. A pattern of 3 repeats on every multiple of 3.',
  picW: 'a row of shapes: circle, square, triangle, circle, square, triangle, with a question mark after the last one.',
  picK: 'a row of triangles made from straws, each joined to the one before, with a count of sticks written underneath each.' },
 5: { today: 'Solve “I think of a number” puzzles by working backwards and by using a number machine.',
  warm: 'Think of a number, add 3, and the answer is 8. What was your number?',
  explore: 'Hide a secret number of counters under a cup, add 5 more, and tell your partner the total. Your partner works back to find the secret number.',
  keyHead: 'Key idea: undo it',
  table: [['IN','15','8','26'],['OUT','19','12','30']],
  big: 'To undo adding, take away. To undo taking away, add. Undo the steps in the reverse order.', small: 'Number machine rule: add 4.',
  picW: 'a paper cup hiding some counters, with 5 loose counters next to it and the total “12” written on a card.',
  picK: 'a start-to-finish arrow: a box “?” then an arrow “+5” then a box “12”, with a second arrow underneath going back, labelled “−5”.' },
 6: { today: 'Make an amount in every way, work from the biggest coin down, and say how we know we have them all.',
  warm: 'Coin shop. Pay exactly with play coins. Who can pay with the fewest coins?',
  explore: 'Make 20¢ in as many ways as you can with 20¢, 10¢ and 5¢ coins. Record each way on your whiteboard.',
  keyHead: 'Key idea: start with the biggest',
  table: [['20¢','10¢','5¢','Total'],['1','0','0','20¢'],['0','2','0','20¢'],['0','1','2','20¢'],['0','0','4','20¢']],
  big: 'Start with the biggest coin and work down. Keep a table so you do not repeat a way.', small: '10 + 5 + 5 and 5 + 10 + 5 are the same way.',
  picW: 'a toy shop counter with price tags of 5¢, 10¢, 20¢ and 50¢ and a tray of play coins.',
  picK: 'the table above with the coins drawn as small circles in each row.' },
 7: { today: 'Describe shapes by their sides and corners, then count the triangles hiding in a picture.',
  warm: 'Shape hunt. Find a circle, a triangle, a square and a rectangle in two minutes.',
  explore: 'Fold a paper square along a diagonal and cut. What two shapes do you get? Put them together a new way. What shapes can you make?',
  keyHead: 'Key idea: sides and corners',
  table: [['Shape','Triangle','Square','Pentagon','Hexagon'],['Sides','3','4','5','6'],['Corners','3','4','5','6']],
  big: 'The number of sides equals the number of corners.', small: 'To count triangles, count the small ones first, then the bigger ones made of two or more.',
  picW: 'a paper square folded in half corner to corner, with scissors cutting along the fold.',
  picK: 'a big square with both diagonals drawn, showing 4 small triangles and 4 bigger triangles made of two small ones.' },
 8: { today: 'Order things from clues, sort with two rules in a Venn diagram and use a grid to solve a puzzle.',
  warm: 'Guess my number from 1 to 20. Ask yes or no questions. Use as few as you can.',
  explore: 'Overlap two string loops. Sort the buttons by two rules and find the ones that belong in the middle.',
  keyHead: 'Key idea: a tick and a cross',
  table: [['','Dog','Cat','Fish'],['Ali','✗','✗','✓'],['Mei','✗','✓','✗'],['Ben','✓','✗','✗']],
  big: 'Every cross helps you fill another box.', small: 'Numbers in the middle of the Venn diagram follow both rules.',
  picW: 'a hand holding a card with a hidden number, and a speech bubble that says “Is it more than 10?”.',
  picK: 'two overlapping circles, one labelled “less than 6” and one “odd”, with 1, 3 and 5 in the overlap.' },
 9: { today: 'Measure with equal units, compare lengths, and see why a bigger unit gives a smaller count.',
  warm: 'Longer or shorter? Predict, then lay two objects side by side to check.',
  explore: 'Measure a pencil, a book and a shoe with cubes. Estimate first, then measure. Then measure the book in hand spans.',
  keyHead: 'Key idea: equal units',
  table: [['Object','Pencil','Pen'],['Cubes','8','11']],
  big: 'No gaps and no overlaps. Start at zero.', small: 'A bigger unit gives a smaller number. 1 clip = 2 erasers, so 5 clips = 10 erasers.',
  picW: 'a pencil and a pen laid side by side with their left ends lined up on a line.',
  picK: 'a row of linking cubes laid end to end under a pencil, with no gaps, starting exactly at the pencil’s tip.' },
 10: { today: 'Use everything we have learned in new puzzles and explain our thinking.',
  warm: 'Mental maths relay. A chain of quick questions from all nine lessons is passed around the group.',
  explore: 'Four puzzle cards: coins, patterns, logic and measuring. Pairs get ONE card for 10 minutes, then swap with another pair for a second 4-minute round. Online: one card per breakout room; each pair reports in 30 seconds.',
  keyHead: 'Key idea: the detective rules',
  table: null,
  big: 'Look for the pattern. Try it with objects first. Check your answer. Say why.', small: 'Pick one puzzle and teach it to the group in two sentences.',
  picW: 'four tables, each with a puzzle card and the matching materials: coins, cubes, a pattern strip and a clue card.',
  picK: 'four detective badges in a row, one for each rule, each with a small magnifying glass.' }
};

const tbl = rows => rows ? `<table style="font-size:34px">${rows.map((r, i) => `<tr${i % 2 ? ' style="background:#FFFFFF"' : ''}>${r.map(c => i === 0 ? `<th style="text-align:left">${esc(c)}</th>` : `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</table>` : '';

for (const l of L.filter(x => x.n >= 3)) {
  const d = D[l.n], id = 'l' + l.n;
  // title
  fs.writeFileSync(out + id + '-title.html', `<section id="${id}-title" data-transition="fade" style="background:#1B2A49;color:#FFF9EC;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">
<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">LESSON ${l.n}  •  WEEK ${l.week}</p>
<h1 style="font-family:'Fredoka', Arial, sans-serif;font-size:128px;font-weight:600;line-height:1.05">${esc(l.title)}</h1>
<p style="font-size:44px;color:#C9D4EC">${esc(l.topic)}</p>
<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px">
<p style="font-size:28px;font-weight:700;letter-spacing:3px;color:#FFC93C">TODAY WE WILL</p>
<p style="font-size:44px;font-weight:600">${esc(d.today)}</p>
</div>
${foot('#B7C3DD')}
<aside>${esc('Objective: ' + l.objective + ' Materials: ' + l.materials + ' Online: ' + l.online)}</aside>
</section>
`);
  // warm
  fs.writeFileSync(out + id + '-warm.html', cream(id + '-warm', `${h2(l.title)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px">
${card(pill('WARM-UP', '#FFC93C', '#1B2A49') + `<p style="font-size:38px;font-weight:600">${esc(d.warm)}</p>`)}
${card(pill('EXPLORE', '#1F7A6F', '#FFF9EC') + `<p style="font-size:38px;font-weight:600">${esc(d.explore)}</p>`)}
</div>
${pic(d.picW)}`, 'Warm-up: 10 minutes. Explore: 15 minutes in pairs. ' + l.warmup + ' ' + l.explore + ' Online: ' + l.online));
  // key
  fs.writeFileSync(out + id + '-key.html', cream(id + '-key', `${h2(d.keyHead)}
${tbl(d.table)}
${card(`<p style="font-size:40px;font-weight:600">${esc(d.big)}</p><p style="font-size:34px;color:#3B4A6B">${esc(d.small)}</p>`)}
${pic(d.picK)}`, 'Mini-lesson: 10 minutes. ' + l.mini + ' Common mistakes: ' + l.mistakes.join(' ')));
  // exit
  fs.writeFileSync(out + id + '-exit.html', cream(id + '-exit', `${h2('Talk time and exit ticket')}
${card(pill('TALK TIME', '#FFC93C', '#1B2A49') + `<p style="font-size:40px;font-weight:600">${esc(l.share)}</p>`)}
${card(pill('EXIT TICKET', '#1F7A6F', '#FFF9EC') + `<p style="font-size:40px;font-weight:600">${esc(l.exit.q)}</p>`)}`, 'Answer: ' + l.exit.a + ' Stamp the passport once the child has answered. Extension: ' + l.extension));
}
// end
fs.writeFileSync(out + 'end.html', `<section id="end" data-transition="fade" style="background:#1B2A49;color:#FFF9EC;font-family:'Nunito Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:40px">
<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:#FFC93C">WELL DONE, DETECTIVES</p>
<h1 style="font-family:'Fredoka', Arial, sans-serif;font-size:128px;font-weight:600;line-height:1.05">Case closed!</h1>
<p style="font-family:'Fredoka', Arial, sans-serif;font-size:64px;font-weight:500;color:#FFC93C">Spot it. Solve it. Say why.</p>
<p style="font-size:36px;color:#C9D4EC">Certificates and a last stamp for every detective.</p>
<aside>Hand out certificates. Ask each child to name one puzzle they enjoyed. Give parents the one-page summary from the programme guide.</aside>
</section>
`);
console.log(fs.readdirSync(out).length);
