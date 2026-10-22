// Math Inquirers P4 Holiday Program — Lesson 9: Data Detectives (Tables and line graphs)
// Every answer below was worked out and checked with a script (changes between days, row and column totals,
// where two lines meet, missing points from totals).
const tip = require('../tip.js');
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const F = 'Arial, sans-serif';
const tx = (x, y, s, size = 15, o = {}) => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.c || N}" font-family="${F}"${o.rot ? ` transform="rotate(-90 ${x} ${y})"` : ''}>${s}</text>`;

// Accurate line graph. o: {x, y, w, h, xl, y0, y1, step, lab, yt, series:[{v, c, mark, dash, name}], legend}
// Points sit on the vertical grid lines; v[i] === null leaves a gap (no point, no line to it).
const graph = o => {
  const L = o.x + 52, T = o.y + (o.legend ? 34 : 12), R = o.x + o.w - 14, B = o.y + o.h - 46;
  const n = o.xl.length, xs = i => L + 26 + i * (R - L - 52) / (n - 1), ys = v => B - (v - o.y0) * (B - T) / (o.y1 - o.y0);
  let s = `<rect x="${L}" y="${T}" width="${R - L}" height="${B - T}" fill="${WH}"/>`;
  for (let v = o.y0; v <= o.y1 + 1e-9; v += o.step) {
    const yy = ys(v), major = Math.abs((v - o.y0) % o.lab) < 1e-9;
    s += `<line x1="${L}" y1="${yy}" x2="${R}" y2="${yy}" stroke="${N}" stroke-opacity="${major ? 0.3 : 0.13}" stroke-width="1"/>`;
    if (major) s += tx(L - 8, yy + 5, v, 15, { a: 'end' });
  }
  o.xl.forEach((l, i) => { s += `<line x1="${xs(i)}" y1="${T}" x2="${xs(i)}" y2="${B}" stroke="${N}" stroke-opacity="0.13"/>` + tx(xs(i), B + 20, l, 15); });
  s += `<line x1="${L}" y1="${T - 4}" x2="${L}" y2="${B}" stroke="${N}" stroke-width="2.5"/><line x1="${L}" y1="${B}" x2="${R}" y2="${B}" stroke="${N}" stroke-width="2.5"/>`;
  s += tx(o.x + 14, (T + B) / 2, o.yt, 15, { rot: true });
  if (o.xt) s += tx((L + R) / 2, B + 40, o.xt, 15);
  o.series.forEach((se, k) => {
    let d = '';
    se.v.forEach((v, i) => {
      if (v === null) return;
      const prev = i > 0 ? se.v[i - 1] : null;
      d += (prev === null ? 'M' : 'L') + xs(i).toFixed(1) + ' ' + ys(v).toFixed(1) + ' ';
    });
    s += `<path d="${d}" fill="none" stroke="${se.c}" stroke-width="3"${se.dash ? ' stroke-dasharray="9 6"' : ''}/>`;
    se.v.forEach((v, i) => {
      if (v === null) return;
      const X = xs(i), Yv = ys(v);
      s += se.mark === 'sq' ? `<rect x="${X - 6}" y="${Yv - 6}" width="12" height="12" fill="${WH}" stroke="${se.c}" stroke-width="3"/>` : `<circle cx="${X}" cy="${Yv}" r="6" fill="${Y}" stroke="${se.c}" stroke-width="3"/>`;
    });
    if (o.legend) {
      const lx = L + 10 + k * 150;
      s += `<line x1="${lx}" y1="${o.y + 14}" x2="${lx + 36}" y2="${o.y + 14}" stroke="${se.c}" stroke-width="3"${se.dash ? ' stroke-dasharray="9 6"' : ''}/>` +
        (se.mark === 'sq' ? `<rect x="${lx + 12}" y="${o.y + 8}" width="12" height="12" fill="${WH}" stroke="${se.c}" stroke-width="3"/>` : `<circle cx="${lx + 18}" cy="${o.y + 14}" r="6" fill="${Y}" stroke="${se.c}" stroke-width="3"/>`) +
        tx(lx + 44, o.y + 19, se.name, 15, { a: 'start' });
    }
  });
  return s;
};
const svg = (w, h, body, label, dw) => `<svg aria-label="${label}" viewBox="0 0 ${w} ${h}" width="${dw || w}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${body}</svg>`;
const titled = (t, x) => tx(x, 18, t, 16);

const DAYS7 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
const juiceSvg = () => svg(600, 200, titled('Cups of sugarcane juice sold each day', 300) +
  graph({ x: 0, y: 22, w: 600, h: 178, xl: DAYS7, y0: 0, y1: 80, step: 5, lab: 10, yt: 'Number of cups', series: [{ v: [40, 55, 50, 75, 65, 25, 30], c: N }] }),
  'Line graph of cups of sugarcane juice sold: Monday 40, Tuesday 55, Wednesday 50, Thursday 75, Friday 65, Saturday 25, Sunday 30');
const moneySvg = () => svg(600, 196, titled('Money in each money box at the end of each week', 300) +
  graph({ x: 0, y: 22, w: 600, h: 174, xl: ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4', 'Wk 5', 'Wk 6'], y0: 0, y1: 60, step: 5, lab: 10, yt: 'Money ($)', legend: true,
    series: [{ v: [10, 20, 30, 40, 50, 60], c: TEAL, name: 'Ali' }, { v: [30, 35, 40, 45, 50, 55], c: RED, mark: 'sq', dash: true, name: 'Mei' }] }),
  'Two line graphs: Ali has 10, 20, 30, 40, 50, 60 dollars in weeks 1 to 6; Mei has 30, 35, 40, 45, 50, 55 dollars', 500);
const shopsSvg = () => svg(600, 182,
  tx(150, 18, 'Shop A: phone cases sold', 15) + tx(450, 18, 'Shop B: phone cases sold', 15) +
  graph({ x: 0, y: 22, w: 295, h: 160, xl: ['Jan', 'Feb', 'Mar', 'Apr'], y0: 0, y1: 100, step: 20, lab: 20, yt: 'Number sold', series: [{ v: [20, 40, 60, 80], c: N }] }) +
  graph({ x: 305, y: 22, w: 295, h: 160, xl: ['Jan', 'Feb', 'Mar', 'Apr'], y0: 40, y1: 60, step: 4, lab: 4, yt: 'Number sold', series: [{ v: [44, 48, 52, 56], c: N }] }),
  'Two line graphs that look the same. Shop A: 20, 40, 60, 80 on a scale from 0 to 100. Shop B: 44, 48, 52, 56 on a scale from 40 to 60', 500);

module.exports = {
  lesson: {
    n: 9, week: 5, session: 'A', title: 'Data Detectives', topic: 'Tables and line graphs',
    objective: 'Read values and trends from line graphs (using the scale), find the biggest increase or decrease, find missing values in tables and graphs from totals and patterns, compare two lines on one graph, and explain why a graph with a different scale can mislead.',
    skills: 'Reading scales, comparing changes, working from totals, reasoning about how a graph is drawn',
    materials: 'Mini whiteboards, a ruler and two coloured pencils per child, the blank graph grids from the kit page (or squared paper), the queue table for the explore task.',
    online: 'Children use the printed Graph grids page or squared paper and hold it up to the camera; the tutor plots on the slide graphs while children call out where each point goes.',
    warmup: 'Which graph tells the story? Four small line graphs (up then down, flat, steadily up, steadily down) and four stories (a bath filling, a hawker centre from 10 am to 3 pm, a candle burning, a piggy bank nobody touches). Children match each story to a graph and say why.',
    explore: 'Pairs plot a line graph from a table: the number of people in the queue at a chicken rice stall every half hour from 11:00 to 2:00 (4, 9, 18, 22, 15, 7, 3). They choose a scale, plot and join the points, then write three things the graph tells them (longest queue, fastest growth, best time to buy).',
    mini: 'Read a line graph: title, axes, scale (each line is worth 10; halfway between 20 and 30 is 25). The biggest change is the steepest line: list the change between neighbours and say up or down. Missing values in a table: use the row and column totals, then check that both ways give the same grand total. Before page 2: two lines on one graph (where they cross the values are the same, the gap is the difference, the steeper line grows faster); values that go up by the same amount each time; check where the scale starts before comparing two graphs.',
    share: 'Two graphs show the same numbers, but one line looks much steeper. How can that be? How would you draw a fair graph?',
    exit: { q: 'Visitors: Mon 35, Tue 50, Wed 20, Thu 45. Between which two days was the biggest change? Was it an increase or a decrease?', a: 'Tuesday to Wednesday: a decrease of 30.' },
    mistakes: [
      'Reading the scale as 1 for each line when each line is worth 10 (or 5), so 75 is read as 7 and a half.',
      'Looking only for the biggest increase and missing a bigger decrease, or comparing the heights of points instead of the change between them.',
      'Comparing two graphs by how steep the lines look without checking where each scale starts and what each line is worth.'
    ],
    extension: 'Draw two line graphs of the same numbers (52, 54, 56, 58): one that makes the change look huge and one that makes it look tiny. Write a sentence a shop owner might say with each graph.',
    key: [
      ['Q1', '(a) 75 cups; 55 cups (25 + 30)  (b) Wednesday to Thursday, up 25  (c) Friday to Saturday, down 40  (d) It is the steepest line going down. A reason such as: the office workers do not come to work on Saturday and Sunday.'],
      ['Q2', '4A Week 2: 47.  4B Week 1: 41.  4C total: 97.  Totals: Week 1 124, Week 2 128, altogether 252.  (a) 4B (41 is more than 29)  (b) 146 (128 + 6 + 6 + 6)'],
      ['Q3', '(a) $40; $10  (b) Week 5 ($50 each); Week 6  (c) $15 (Ali $80, Mei $65)'],
      ['Q4', 'Day 1: 10, Day 3: 18, Day 4: 22.  (a) 4 more each day (26 − 14 = 12 over 3 days); 90 pages'],
      ['Q5', '(a) Shop A: 60.  Shop B: 12.  (b) No. The scales are different: Shop A’s starts at 0 and each line is 20; Shop B’s starts at 40 and each line is 4. Shop A’s sales went up by 48 more than Shop B’s.']
    ]
  },

  script: {
    hook: ['Good morning, Data Detectives! A graph is a picture of numbers. A good detective reads it carefully, and also checks whether the picture is telling the truth.', 'Today we read line graphs and tables, find numbers that are missing, and catch a graph that tries to trick us. Notice it. Test it. Explain why.'],
    warmIntro: ['Here are four tiny graphs with no numbers at all. I will read a story. Point to the graph that tells the story, and be ready to say why.', 'Listen: a bath filling up with water. Which line? Why not the one that goes up and then down?'],
    predict: ['You will plot the queue at a chicken rice stall from 11:00 to 2:00. Before you plot: at what time do you think the queue is longest? Write your guess at the top of your grid.'],
    exploreHints: ['Stuck on the scale: the biggest number is 22. If each line is 2 people, how many lines do you need to reach 22?', 'Points in the wrong place: put your finger on the time, go straight up, then check the number on the side.', 'Finished early: between which two times did the queue grow the most? Show it on your graph without working out every change.'],
    think: [
      '“First the title and the axes: books borrowed, Monday to Friday. Then the scale: each line on the side is worth 10. Tuesday’s point is on the 40 line, so 40. Monday’s point is halfway between 20 and 30, so 25.”',
      '“Which day had the biggest change? I list each change: Monday to Tuesday up 15, Tuesday to Wednesday down 5, Wednesday to Thursday up 25, Thursday to Friday down 10. The biggest increase is 25, and on the graph it is the steepest line going up.”',
      '“A table with missing numbers: Ali’s row must add up to 61. 61 − 26 = 35. I fill the rows first, then the columns. Last, I check: the column totals and the row totals must give the same grand total.”'
    ],
    circulate: ['Point to a line and ask: “Is this an increase or a decrease? By how much?”', 'Ask: “What is each line on the side worth? How do you know?”', 'Ask: “How can you check your missing number?”'],
    hints: ['Hint 1: “Find what one line on the scale is worth before you read anything.”', 'Hint 2: “Write the change between each pair of neighbours, with up or down.”', 'Hint 3: “Add the numbers you know, then take them away from the total.”'],
    talk: ["“Two graphs show the same numbers, but one line looks much steeper. How can that be?”"],
    talkWeekly: ["“How would you draw a fair graph if you wanted to compare two shops?”"],
    talkAns: 'The scales are different. If a scale starts at a big number, or each line is worth very little, a small change looks huge. To compare fairly, use the same scale for both graphs, starting at 0.',
    close: ['“Today you read graphs like detectives: scale first, then the changes, and you caught a graph that was trying to trick you.”', '“Hand me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Read line graphs and tables, find missing values, compare two lines and catch a graph that misleads.',
    warmGame: 'Which graph tells the story? Match four stories (a bath filling, a hawker centre from 10 am to 3 pm, a candle burning, a piggy bank nobody touches) to four line shapes, and say why.',
    warmQs: [["75 − 48 = ?", "27"], ["On a scale in 10s, what is halfway between 40 and 50?", "45"], ["38 + 47 + 15 = ?", "100"]],
    warmWeekly: [["Four numbers total 200. Three are 45, 60 and 50. The fourth?", "45"], ["Bigger change: 120 to 95, or 60 to 90?", "60 to 90 (30)"]],
    expSetup: ['Look at the table: people in the queue at a chicken rice stall every half hour.', 'Choose a scale for the side of your grid (how much is each line worth?).', 'Plot each point and join the points with straight lines.', 'Write three things your graph tells you.'],
    expPic: 'a table of queue lengths (11:00 4, 11:30 9, 12:00 18, 12:30 22, 1:00 15, 1:30 7, 2:00 3) beside an empty graph grid with the times along the bottom.',
    expAsk: [["When was the queue longest?", "12:30, with 22 people."], ["Between which two times did the queue grow the most?", "11:30 to 12:00: up 9 people (the steepest line going up)."]],
    mini1: { head: 'Reading a line graph', body: ['Books borrowed: Mon 25, Tue 40, Wed 35, Thu 60, Fri 50.', 'Scale: each line is worth 10. Monday is halfway between 20 and 30.', 'Changes: up 15, down 5, up 25, down 10. Which is the biggest increase?'], ans: 'Wednesday to Thursday: up 25. It is the steepest line going up.' },
    mini2: { head: 'Missing values in a table', table: [['', 'June', 'July', 'Total'], ['Ali', '26', '?', '61'], ['Mei', '?', '18', '50'], ['Ravi', '40', '27', '?'], ['Total', '?', '?', '?']], body: ['Use the row totals first, then add the columns.', 'Check: both ways must give the same grand total.'], ans: 'Ali 35, Mei 32, Ravi 67. June 98, July 80, altogether 178.' },
    keyHead: 'Key idea: scale first, then the changes',
    keyBig: 'Read the scale before you read a point. The steeper the line, the bigger the change.',
    keySmall: 'Totals help you find missing values. Always check where the scale starts before you compare two graphs.',
    brk: 'Human line graph. The tutor tells a story ("the temperature rises slowly, then drops fast"). Move your arm like the line: slow climb, fast drop, flat.',
    ws1: 'Page 1, in pairs: Q1 the sugarcane juice graph, Q2 the library table.',
    ws2: 'Page 2, on your own: Q3 two money boxes, Q4 Siti’s pages, Q5 the two shops.'
  },

  qbank: {
    core: [
      { q: 'On a line graph, each line on the scale is worth 10. Draw the scale from 30 to 40. A point is halfway between the 30 line and the 40 line. What number does it show?', a: '35' },
      { q: 'A stall sold 45 bowls of laksa on Monday and 60 bowls on Tuesday. By how many bowls did sales go up?', a: '15 bowls' },
      { q: 'A table shows 32 visitors on Monday, 48 on Tuesday and 20 on Wednesday. How many visitors came altogether?', a: '100' },
      { q: 'A line graph goes up from 8 am to 10 am, then down until 12 pm. Sketch what it looks like. At what time was the number the highest?', a: '10 am' },
      { q: 'A table shows that Ali has 25 cards and Mei has 18 more cards than Ali. Draw a bar for each child. How many cards do they have altogether?', a: '68 (Mei has 43; 25 + 43 = 68)' },
      { q: 'Three days of sales add up to 90. Day 1 is 30 and Day 2 is 25. What is Day 3?', a: '35' }
    ],
    stretch: [
      { q: 'A table shows that Class 4A has 28 boys and 6 more girls than boys. Class 4B has 63 pupils, with 5 more girls than boys. Which class has more girls?', a: 'Neither: both have 34 girls. (4A: 28 + 6 = 34. 4B: 63 − 5 = 58, 58 ÷ 2 = 29 boys, 29 + 5 = 34 girls.)' },
      { q: 'A graph\'s scale starts at 100 and each line is worth 25. Ali\'s point is 3 lines above the start and Mei\'s point is 7 lines above the start. How much more is Mei\'s number than Ali\'s? Mei says hers is more than double Ali\'s. Is she right?', a: 'Ali 175 and Mei 275, so Mei has 100 more. She is not right: double Ali\'s is 350, and 275 is less than that. (Her point is more than twice as many lines up, 7 against 3, but the scale starts at 100, so counting lines gives the wrong picture.)' },
      { q: 'A stall\'s line graph starts on Monday with 40 cups sold. The line goes up by 15 cups each day until Wednesday, then down by 15 cups each day. How many cups were sold on Friday? Which day sold the same as Thursday?', a: 'Monday 40, Tuesday 55, Wednesday 70, Thursday 55, Friday 40. Friday: 40 cups. Thursday (55) matches Tuesday (55).' },
      { q: 'Ali’s height: age 7, 120 cm; age 8, 127 cm; age 9, 131 cm; age 10, 137 cm. In which year did he grow the most? How much did he grow altogether from age 7 to age 10?', a: 'From age 7 to 8 (7 cm). Altogether 17 cm.' },
      { q: 'Shop A sold 30, 35, 40 and 45 cakes in weeks 1 to 4. Shop B sold 50, 48, 46 and 44 cakes. In which week did Shop A first sell more than Shop B?', a: 'Week 4 (45 is more than 44).' },
      { q: 'A graph’s scale starts at 40. Mei says a point at 60 is "double" a point at 50 because it is twice as high on the graph. Is she right? Explain.', a: 'No. 60 is only 10 more than 50. It looks twice as high because 50 is 10 above the bottom (40) and 60 is 20 above it.' },
      { q: 'Kai draws a line graph of the books he reads. The scale starts at 0 and each line is worth 5. His points for weeks 1 to 4 are 3 lines, 5 lines, 5 lines and 9 lines up. In which week did the number go up the most, and by how much? In which week did it stay the same?', a: 'The numbers are 15, 25, 25 and 45. It went up the most in week 4: up by 20 (week 2 went up by 10). It stayed the same in week 3.' },
      { q: 'The temperature went up by 2 °C every hour from 8 am to 1 pm. At 1 pm it was 33 °C. What was the temperature at 8 am?', a: '23 °C (5 hours, so 10 °C less)' }
    ],
    challenge: [
      { q: 'A shop’s sales go up by the same amount every week. In week 2 it sold 45 toys and in week 6 it sold 85 toys. How many toys did it sell in week 1? In which week did it first sell more than 100 toys?', a: 'Week 1: 35 (4 jumps make 40, so 10 a week). First more than 100: week 8 (105).' },
      { q: 'A stall sold 250 bowls of noodles from Monday to Friday. Monday 40 and Friday 50. Tuesday and Wednesday were the same, and Thursday was 10 more than Tuesday. Find the sales for Tuesday, Wednesday and Thursday.', a: 'Tuesday 50, Wednesday 50, Thursday 60. (Tue + Wed + Thu = 160; take away the extra 10, 150 shared by 3 = 50.)' },
      { q: 'On Ben’s graph each line is worth 2. On Mei’s graph each line is worth 10. Both lines go up by 3 grid lines from Monday to Tuesday. Whose number went up more, and by how much more?', a: 'Mei’s: hers went up 30 and Ben’s went up 6, so 24 more.' },
      { q: 'A graph’s scale starts at 200 and each line is worth 50. Monday’s point is 2 lines up and Tuesday’s point is 6 lines up. Ravi says Tuesday’s number is 3 times Monday’s. Is he right? Explain.', a: 'No. Monday is 300 and Tuesday is 500. 3 times 300 is 900.' },
      { q: 'At a pool, the number of swimmers went up by 15 every hour from 9 am to 11 am, then went down by 10 every hour until 1 pm. At 1 pm there were 50 swimmers. How many were there at 9 am?', a: '40. Work backwards: 12 pm 60, 11 am 70, 10 am 55, 9 am 40.' },
      { q: 'A stall sold 400 plates of nasi lemak from Monday to Friday. Each day it sold 10 more plates than the day before. How many plates did it sell on Monday?', a: '60 (60, 70, 80, 90, 100)' },
      { q: 'Four teams scored 100 points altogether. Team A scored twice as many as Team B. Team C scored 10 more than Team B. Team D scored 22. How many points did each team score?', a: 'A 34, B 17, C 27, D 22. (A + B + C = 78: four equal parts and 10 more, so one part is 68 ÷ 4 = 17.)' },
      { q: 'Tank A has 80 litres of water and loses 6 litres every hour. Tank B has 20 litres and gains 9 litres every hour. On a line graph the two lines cross. After how many hours do the tanks hold the same amount? How much is in each?', a: 'After 4 hours: 56 litres each. The gap of 60 litres closes by 15 litres every hour.' },
      { q: 'Four numbers: 52, 54, 56, 58. Choose where the scale starts and how much each line is worth, so that a line graph of these numbers looks (a) like a huge increase and (b) like hardly any increase. Write both scales and a sentence a shop owner might say with each graph. Which graph is fair? Why?', a: 'Answers vary. (a) Start at 50 with each line worth 1: the line climbs steeply. (b) Start at 0 with each line worth 20: the line is almost flat. A fair graph starts at 0 or says clearly that it does not, so the viewer can see the real change of 6. Both graphs show the same numbers.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.q(1, 'A sugarcane juice stall is next to an office building. The line graph shows how many cups it sold each day for one week. Read the scale first!', { before: 40, keepNext: true }));
    W.push(H.fig(juiceSvg()));
    W.push(H.sub('a', 'Cups sold on Thursday?  ______    On Saturday and Sunday together?  ______'));
    W.push(H.sub('b', 'Biggest increase: from ________ to ________, up by ______ cups'));
    W.push(H.sub('c', 'Biggest decrease: from ________ to ________, down by ______ cups'));
    W.push(H.sub('d', 'How can you see (c) on the graph without working out every change? Why might sales drop on those days?'));
    W.push(...H.lines(1));
    W.push(H.q(2, 'The table shows how many books three classes borrowed from the library. Fill in the missing numbers.', { keepNext: true }));
    const ws = [2475, 2475, 2475, 2475];
    const r = (cells, head) => H.row(cells.map((c, i) => H.cell(c, ws[i], head || i === 0 ? { bold: true, fill: 'EDEDED', h: 36 } : { h: 36 })));
    W.push(H.tbl(ws, [r(['Class', 'Week 1', 'Week 2', 'Total'], true), r(['4A', '38', '', '85']), r(['4B', '', '29', '70']), r(['4C', '45', '52', '']), r(['Total', '', '', ''])]));
    W.push(H.gap(40));
    W.push(H.sub('a', 'Which class borrowed more in Week 1 than in Week 2?  ________'));
    W.push(H.sub('b', 'In Week 3, each class borrowed 6 more books than in Week 2. Week 3 total?  ______'));

    W.push(H.q(3, 'The graph shows how much money Ali and Mei had in their money boxes at the end of each week.', { pb: true, before: 0, keepNext: true }));
    W.push(H.fig(moneySvg()));
    W.push(tip('read each dot. Ali, weeks 1 to 6: $___ $___ $___ $___ $___ $___    Mei: $___ $___ $___ $___ $___ $___'));
    W.push(H.sub('a', 'Mei’s money in Week 3?  $______     Ali saves each week?  $______'));
    W.push(H.sub('b', 'Same amount in Week ____     Ali first has more in Week ____'));
    W.push(H.sub('c', 'They keep saving the same way. In Week 8, Ali has $______ more than Mei.'));
    W.push(H.q(4, 'Siti reads more pages each day, always the same number more. Fill in the table.', { keepNext: true }));
    const wd = [1650, 1650, 1650, 1650, 1650, 1650];
    W.push(H.tbl(wd, [H.row(['Day', '1', '2', '3', '4', '5'].map((c, i) => H.cell(c, wd[i], { bold: true, fill: 'EDEDED', h: 30 }))),
      H.row(['Pages', '', '14', '', '', '26'].map((c, i) => H.cell(c, wd[i], i === 0 ? { bold: true, fill: 'EDEDED', h: 50 } : { h: 50 })))]));
    W.push(H.gap(40));
    W.push(H.sub('a', 'How many more each day?  ______     Pages in the 5 days?  ______'));
    W.push(H.q(5, 'Two shops drew line graphs of the phone cases they sold. Ravi says, “Both shops’ sales went up by the same amount, because the lines look the same.”', { keepNext: true }));
    W.push(H.fig(shopsSvg()));
    W.push(tip('read the scale of each graph.  Shop A starts at ____ and each line is worth ____.   Shop B starts at ____ and each line is worth ____.'));
    W.push(H.sub('a', 'January to April: Shop A went up by ______.  Shop B went up by ______.'));
    W.push(H.sub('b', 'Is Ravi right? Explain why the two graphs look the same.'));
    W.push(...H.lines(1));
    return W;
  }
};

// ---- close_gaps + fix pass: sneak-peek puzzles, Investigation (with an easy first step), Looking back, Go further (docs/audit/close_gaps_p4.md, fixpass_p4.md)
module.exports.gaps = {
 "idea": "line graphs",
 "check": [
  {
   "q": "A stall sold cups of juice: Monday 30, Tuesday 45, Wednesday 25. Which day sold the most? Which day sold the fewest? Draw a small bar for each day if you like.",
   "a": "Tuesday sold the most (45). Wednesday sold the fewest (25).",
   "s": "Most: Tuesday (45). Fewest: Wednesday (25).",
   "kind": "access"
  },
  {
   "q": "A line graph has gridlines at 0, 50, 100, 150 and 200. A point is exactly halfway between the 100 line and the 150 line. What number does it show?",
   "a": "125. Halfway between 100 and 150 is 100 + 25.",
   "s": "125.",
   "kind": "think"
  }
 ],
 "why": "Read the scale first: what is each line worth? Halfway between two lines is half of the step.",
 "invest": {
  "kind": "What if we change ...? What stays the same?",
  "head": "Sales have doubled!",
  "intro": "A shop sold 50 phone cases in May and 100 in June. A newspaper says: \"Sales have doubled!\" (That is true: 100 is twice 50.) The same two numbers can be drawn as a graph that looks like a huge jump or as a graph that looks almost flat.",
  "parts": [
   "On the first Graph grid, draw a line graph of May and June. Go up in 10s from 0 to 100. Is the line steep or gentle?",
   "Now draw the same two numbers on the second grid so the rise looks HUGE. Choose a different scale and write it. Then say how you would make the rise look almost flat.",
   "Which graph is the most honest? What would you ask the newspaper to add to its graph?"
  ],
  "lines": 4,
  "key": "(a) Points (May, 50) and (June, 100); on a scale of 0 to 100 in 10s the line rises through 5 lines, a fair picture. (b) Any scale that starts above 0 with small steps makes the jump look huge (for example start at 45 and go up in 5s: 50 is 1 line up, 100 is 11 lines up). A tall scale that goes from 0 to 1000 in 100s makes the same rise look almost flat (50 is half a line, 100 is one line). Same numbers, different picture. (c) A graph that starts at 0, has equal steps and says what each line is worth is the fairest; the headline is only true because the numbers say so. Look for a child who says \"I read the scale before I looked at the line\" and who notices that the numbers did not change, only the drawing did. Easy first step: plot the two points on a 0 to 100 scale in 10s.",
  "easy": "On the Graph grid, write 0, 10, 20 ... up the side. Plot the points (May, 50) and (June, 100) and join them."
 },
 "reflect": "Something I did well: I read the scale first. The hardest part was reading between the lines on the scale. What helped me: writing what each line was worth. One thing I could try next: writing the scale before I read any numbers.",
 "go2": {
  "q": "Draw the same graph again with a different scale. Does the story look different? Why?",
  "a": "Yes. A scale with small steps, or one that starts above 0, makes the line look steeper; big steps make it look flatter. The numbers are the same: only the picture changed."
 },
 "cap": "Page 2 is on your own. Aim for Q3 and Q4 first. Q5 is a choice for the last few minutes."
};
