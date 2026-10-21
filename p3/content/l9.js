// Math Inquirers P3, Lesson 9: Measure and Money Masters (length, mass, volume, money, time)
module.exports = {
  lesson: {
    n: 9, week: 5, session: 'A', title: 'Measure and Money Masters', topic: 'Length, mass, volume, money and time',
    objective: 'Change compound units (m and cm, kg and g, ℓ and ml, $ and ¢) to one unit to compare, add and subtract; plan a budget; find durations and start and end times by drawing a time line, in 12-hour and 24-hour time.',
    skills: 'Converting units, comparing, budgeting, drawing a time line, working backwards, explaining',
    materials: 'Party menu cards (one per pair), play money, a measuring tape or metre ruler, a kitchen scale and a measuring jug if available, a clock with movable hands, mini whiteboards.',
    online: 'Show the menu card on screen; children use paper and pencil (play money optional). Pairs work in breakout rooms and type their best party plan in the chat.',
    warmup: 'Name that unit: the tutor names an object and a number (a bus is 12 __ long); children write the best unit (m, cm, km, g, kg, ml or ℓ) on whiteboards. Then 5 quick questions: unit changes and a 24-hour time.',
    explore: 'Party planner. Pairs have $20 to plan a party for 8 friends from a menu card (pizza $8.90, chicken wings $6.50, curry puffs $4.20, fruit punch 2 ℓ $3.15, cupcakes $5.75, balloons $2.40). Each friend drinks 250 ml of punch. Buy at least 2 ℓ of punch (any number of bottles) and at least one food. You may buy more than one of an item. Spend as close to $20 as you can. Can you spend exactly $20?',
    mini: 'Heuristic 1, change to one unit: 2 m 35 cm = 235 cm, 1 kg 250 g = 1250 g, 1 ℓ 300 ml = 1300 ml, $3.45 = 345¢; then add, subtract or compare and change back (2 kg 100 g − 850 g = 1250 g = 1 kg 250 g). Heuristic 2, draw a time line and jump to the next o’clock: 9:45 a.m. to 11:20 a.m. is 15 min + 1 h + 20 min = 1 h 35 min; 2:50 p.m. + 1 h 45 min = 4:35 p.m. 24-hour clock: p.m. hours add 12.',
    share: 'Which is longer: 3 m 5 cm or 350 cm? How do you know? Why is 2 m 5 cm not 25 cm?',
    exit: { q: 'A swimming lesson starts at 16:50 and lasts 1 h 25 min. When does it end? Give the 24-hour time.', a: '18:15 (16:50 + 10 min = 17:00, + 1 h = 18:00, + 15 min = 18:15), which is 6:15 p.m.' },
    mistakes: [
      'Writing the small unit straight after the big one: 2 m 5 cm as 25 cm, 3 kg 40 g as 340 g (it is 205 cm and 3040 g).',
      'Treating time like ordinary numbers: 9:45 to 11:20 worked out as 11.20 − 9.45 = 1.75, or counting 100 minutes in an hour.',
      'In the 24-hour clock, adding 12 to a.m. times or to 12:30 p.m., or reading 17:00 as 7 p.m.'
    ],
    extension: 'Plan a real outing (a trip to the zoo or a hawker lunch): find the times on a timetable, the total cost for your family and the change from a $50 note.',
    key: [
      ['Q1', '(a) 306 cm  (b) 2450 g  (c) 4 ℓ 80 ml  (d) 4 × 65 cm = 260 cm; 300 cm − 260 cm = 40 cm'],
      ['Q2', '(a) 1 kg, 1 kg 3 g, 1030 g, 1 kg 300 g  (b) 1 kg is 1000 g, so 1 kg 30 g = 1030 g, not 130 g.'],
      ['Q3', '(a) No: $7.85 + $6.90 + $5.50 = $20.25, which is 25¢ more than $20.  (b, if time) Book, pen set and puzzle: $19.35. Change: 65¢.'],
      ['Q4', '(a) 07:15, 15:40, 8:05 p.m., 12:30  (b) 17 − 12 = 5, so 17:00 is 5 p.m., not 7 p.m.'],
      ['Q5', '(a) 1 h 25 min (15 min + 1 h + 10 min)  (b) 17:25  (c) 19:25 (21:15 back 15 min = 21:00, back 1 h = 20:00, back 35 min = 19:25)'],
      ['Q6', '(if time) (a) Buses: 06:40, 07:05, 07:30, 07:55, 08:20. Next bus 08:20; he waits 5 minutes.  (b) 08:55']
    ]
  },
  script: {
    hook: ['A tailor, a baker, a pharmacist and a bus captain all measure things every day: metres and centimetres, kilograms and grams, litres and millilitres, dollars and cents, hours and minutes. Today we become Measure and Money Masters. Our two tricks: change to one unit, and draw a time line.'],
    warmIntro: ['I will name an object and a number. You write the best unit on your whiteboard: m, cm, km, g, kg, ml or ℓ. Ready? A bus is 12 what long? Hold up! Now tell your partner why it is not 12 cm or 12 km.'],
    predict: ['Look at the menu card. Before you add anything: do you think you can buy pizza, wings and cupcakes with $20? Show thumbs up or down, then we will check.'],
    exploreHints: ['Stuck on the punch: “How many millilitres do 8 friends drink? How many ml is 2 ℓ?”', 'Adding prices: “Change each price to cents, or add the dollars first and then the cents.”', 'Over $20: “Which item could you swap for a cheaper one?”', 'Finished early: “Can you spend EXACTLY $20? Look at the cents: which prices end in 5?”'],
    think: [
      '“2 m 35 cm. 1 m is 100 cm, so 2 m is 200 cm. 200 and 35 more is 235 cm. Careful with 2 m 5 cm: that is 200 and 5, so 205 cm, not 25.”',
      '“The flour bag has 2 kg 100 g. I change it to grams: 2100 g. Mum uses 850 g. 2100 − 850 = 1250 g. Now I change back: 1000 g is 1 kg, so 1 kg 250 g. I check: 1250 + 850 = 2100.”',
      '“From 9:45 to 11:20. Time does not work like ordinary numbers, because an hour is 60 minutes, not 100. So I draw a time line and jump to the next o’clock: 15 minutes to 10:00, 1 hour to 11:00, 20 minutes to 11:20. Altogether 1 hour 35 minutes.”'
    ],
    circulate: ['Ask: “What did you change the units to? Why that unit?”', 'Ask: “Show me your time line. Where did you jump to the o’clock?”', 'Ask: “How do you know your change is right? Add it back on.”'],
    hints: ['Hint 1: “Change everything to the smaller unit first: cm, g, ml, ¢ or minutes.”', 'Hint 2: “Draw a time line. Jump to the next o’clock, then whole hours, then the minutes left.”', 'Hint 3: “For the 24-hour clock: after 12 noon, add 12 to the hour.”'],
    talk: ['“Which is longer: 3 m 5 cm or 350 cm? How do you know?”', '“Why can we not just do 11.20 − 9.45 to find how long it is from 9:45 to 11:20?”'],
    talkAns: '350 cm is longer: 3 m 5 cm = 305 cm. Time is not like ordinary numbers: an hour has 60 minutes, not 100, so we count on with a time line (15 min + 1 h + 20 min = 1 h 35 min).',
    close: ['“Today you changed to one unit to compare and calculate, you planned a budget, and you drew time lines to count across the hour. Measure and Money Masters!”']
  },
  deck: {
    today: 'Change to one unit to compare and calculate. Plan a budget. Draw a time line for durations and the 24-hour clock.',
    warmGame: 'Name that unit. The tutor names an object and a number; write the best unit: m, cm, km, g, kg, ml or ℓ.',
    warmQs: [['1 m 40 cm = __ cm', '140 cm'], ['3 kg = __ g', '3000 g'], ['2 ℓ 50 ml = __ ml', '2050 ml'], ['1 hour 20 minutes = __ minutes', '80 minutes'], ['2:00 p.m. in 24-hour time is __', '14:00']],
    expSetup: ['You have $20 to plan a party for 8 friends.', 'Each friend drinks 250 ml of punch. Buy at least 2 ℓ of punch (any number of bottles).', 'Buy at least one food. You may buy more than one of an item. Spend as close to $20 as you can.', 'Challenge: can you spend exactly $20?'],
    expPic: 'a party menu card: pizza $8.90, chicken wings $6.50, curry puffs $4.20, fruit punch 2 ℓ $3.15, cupcakes $5.75, balloons $2.40.',
    expAsk: [['How much punch do 8 friends need? How many bottles?', '8 × 250 ml = 2000 ml = 2 ℓ, so at least 1 bottle. You may buy more.'], ['Who got closest to $20? How did you add the prices?', 'Open. Changing to cents, or adding dollars then cents, both work.'], ['Can you spend exactly $20?', 'Yes, 3 ways: pizza + 2 punch + 2 balloons; wings + 2 punch + 3 balloons; cupcakes + 3 punch + 2 balloons.']],
    mini1: { head: 'Change to one unit', body: ['A bag has 2 kg 100 g of flour. Mum uses 850 g.', 'How much flour is left?'], ans: '2 kg 100 g = 2100 g. 2100 − 850 = 1250 g = 1 kg 250 g.' },
    mini2: { head: 'Draw a time line', body: ['A movie starts at 2:50 p.m. and lasts 1 h 45 min.', 'When does it end?'], ans: '2:50 + 10 min = 3:00, + 1 h = 4:00, + 35 min = 4:35 p.m.' },
    keyHead: 'Key idea: one unit, and a time line',
    keyBig: 'Change to one unit before you compare, add or subtract. For time, draw a time line and jump to the next o’clock.',
    keySmall: '1 m = 100 cm, 1 kg = 1000 g, 1 ℓ = 1000 ml, $1 = 100¢, 1 h = 60 min. After 12 noon, add 12 for the 24-hour clock.',
    brk: 'Human clock. Stretch one arm as the hour hand and one as the minute hand. Show 3 o’clock, 6 o’clock, quarter past 9 … and 15:00!',
    ws1: 'Page 1, in pairs: Q1 change the units (including the ribbon), Q2 order masses and fix a mistake, Q3 Siti’s $20 budget (Q3b if time).',
    ws2: 'Page 2, on your own: Q4 the 24-hour clock, Q5 durations, end and start times; then Q6 the bus timetable if you have time.'
  },
  qbank: {
    core: [
      { q: '2 m 45 cm = ____ cm', a: '245 cm' },
      { q: '3060 g = ____ kg ____ g', a: '3 kg 60 g' },
      { q: 'A pail holds 4 ℓ 500 ml. A jug holds 1 ℓ 750 ml. How much more does the pail hold?', a: '2 ℓ 750 ml (4500 ml − 1750 ml = 2750 ml)' },
      { q: 'Ali buys a sandwich for $3.80 and a drink for $1.45. He pays with a $10 note. How much change does he get?', a: '$4.75 ($3.80 + $1.45 = $5.25; $10 − $5.25 = $4.75)' },
      { q: 'Write 6:20 p.m. in 24-hour time.', a: '18:20' },
      { q: 'A lesson starts at 10:45 a.m. and ends at 12:05 p.m. How long is it?', a: '1 h 20 min (15 min + 1 h + 5 min)' }
    ],
    stretch: [
      { q: 'A 2 ℓ bottle of juice is poured into cups. Each cup holds 300 ml. How many cups can be filled? How much juice is left over?', a: '6 cups, 200 ml left (300, 600, 900, 1200, 1500, 1800 ml; 2000 − 1800 = 200 ml)' },
      { q: 'A shop opens at 09:30 and closes at 21:00. How long is it open?', a: '11 h 30 min (30 min to 10:00, then 11 h to 21:00)' },
      { q: 'A box with 4 books weighs 1 kg 50 g. The empty box weighs 250 g. All the books weigh the same. How heavy is one book?', a: '200 g (1050 g − 250 g = 800 g; 800 ÷ 4 = 200 g)' },
      { q: 'Buses leave the interchange every 25 minutes. The first bus leaves at 06:40. The ride to school takes 35 minutes. Ravi must reach school by 08:30. Which is the latest bus he can take?', a: 'The 07:55 bus (buses: 06:40, 07:05, 07:30, 07:55, 08:20; 07:55 + 35 min = 08:30; the 08:20 bus arrives at 08:55, too late).' },
      { q: 'Ben has only 20¢ and 50¢ coins. He has 9 coins worth $3 altogether. How many of each coin does he have?', a: 'Four 50¢ coins and five 20¢ coins ($2 + $1 = $3)' },
      { q: 'A night train leaves at 22:40 and arrives at 01:15 the next morning. How long is the trip?', a: '2 h 35 min (20 min to 23:00, 1 h to 00:00, 1 h to 01:00, 15 min to 01:15)' },
      { q: 'Siti’s home is 1 km 250 m from school. She walks there and back every day. How far does she walk in 2 days?', a: '5 km (1250 m × 4 = 5000 m)' },
      { q: 'Ali needs 2 ℓ of milk. A 250 ml carton costs $1.10 and a 1 ℓ carton costs $3.60. What is the cheapest way to buy 2 ℓ?', a: 'Two 1 ℓ cartons: $7.20 (one 1 ℓ and four small: $8.00; eight small: $8.80)' },
      { q: 'Mei goes to sleep at 21:45 and wakes up at 06:30. How long does she sleep?', a: '8 h 45 min (15 min to 22:00, 8 h to 06:00, 30 min to 06:30)' }
    ],
    challenge: [
      { q: 'A 5 m ribbon is cut into two pieces. One piece is 80 cm longer than the other. How long is each piece?', a: '2 m 10 cm and 2 m 90 cm (500 − 80 = 420; 420 ÷ 2 = 210)' },
      { q: 'You have a 300 ml cup, a 500 ml cup (no marks on either) and a tap. How can you get exactly 100 ml in a cup?', a: 'Fill the 300 ml cup and pour it into the 500 ml cup. Fill the 300 ml cup again and pour until the 500 ml cup is full (200 ml goes in). 100 ml is left in the 300 ml cup.' },
      { q: 'Ravi has $10. He buys some erasers at 85¢ each and gets $1.50 change. How many erasers does he buy?', a: '10 erasers ($10 − $1.50 = $8.50 = 850¢; 10 × 85¢ = 850¢)' },
      { q: 'A pail has 4 ℓ 200 ml of water. Ali fills 3 bottles that hold 900 ml each. He pours the rest equally into 2 jugs. How much water is in each jug?', a: '750 ml (3 × 900 = 2700 ml; 4200 − 2700 = 1500 ml; 1500 ÷ 2 = 750 ml)' },
      { q: 'School starts at 08:15. There are 5 lessons of 35 minutes and a 20-minute recess after the 3rd lesson. When does the last lesson end?', a: '11:30 (5 × 35 = 175 min, + 20 = 195 min = 3 h 15 min)' },
      { q: 'Ali and Ben have $24 altogether. After Ali spends $3.60, they have the same amount of money. How much did Ali have at first?', a: '$13.80 ($24 − $3.60 = $20.40; half is $10.20; Ali had $10.20 + $3.60 = $13.80, Ben $10.20)' },
      { q: 'A bottle full of water weighs 1 kg 200 g. After half of the water is poured out, it weighs 750 g. How heavy is the empty bottle?', a: '300 g (half the water = 1200 − 750 = 450 g; all the water = 900 g; bottle = 1200 − 900 = 300 g)' },
      { q: 'Mei buys 3 pens and 2 files for $9.20. Each file costs 60¢ more than each pen. How much does one pen cost?', a: '$1.60 (take away the extra 2 × 60¢ = $1.20: $8.00 for 5 pens; 800¢ ÷ 5 = 160¢. A file is $2.20.)' },
      { q: 'The clock at the station is 10 minutes fast. The train leaves when this clock shows 13:05. The trip takes 1 h 40 min. What is the real (correct) time when the train arrives? Give it in 24-hour and 12-hour time.', a: '14:35, which is 2:35 p.m. (real start 12:55; + 5 min = 13:00, + 1 h = 14:00, + 35 min = 14:35)' }
    ]
  },
  workbook: H => {
    const { q, sub, ans, lines, p, tbl, row, cell, gap, t } = H;
    const W = [];
    // ---------- page 1 ----------
    W.push(q(1, 'Trick 1: change to ONE unit.   1 m = 100 cm    1 kg = 1000 g    1 ℓ = 1000 ml    $1 = 100¢', { before: 40, keepNext: true }));
    W.push(sub('a', '3 m 6 cm  =  ________ cm              (b)  2 kg 450 g  =  ________ g'));
    W.push(sub('c', '4080 ml  =  ____ ℓ  ____ ml'));
    W.push(sub('d', 'Mei cuts 4 pieces, each 65 cm long, from a ribbon 3 m long. How much ribbon is left?   ________ cm'));
    W.push(q(2, 'Four bags of rice are weighed:     1 kg 300 g      1030 g      1 kg      1 kg 3 g', { keepNext: true }));
    W.push(sub('a', 'Order them, lightest first:  ________,  ________,  ________,  ________'));
    W.push(sub('b', 'Ben says, “1 kg 30 g is the same as 130 g.” Explain his mistake.'));
    W.push(...lines(1));
    W.push(q(3, 'Siti has $20. She wants to buy 3 different things from this list.', { keepNext: true }));
    { const ws = [1980, 1980, 1980, 1980, 1980];
      W.push(tbl(ws, [row(['Book', 'Pen set', 'Puzzle', 'Stickers', 'Water bottle'].map((s, i) => cell(s, ws[i], { bold: true, fill: 'EDEDED', h: 30 }))),
        row(['$7.85', '$4.60', '$6.90', '$2.35', '$5.50'].map((s, i) => cell(s, ws[i], { h: 40, size: 26 })))])); }
    W.push(sub('a', 'Can she buy the book, the puzzle and the water bottle? Show how you know.  ______________________'));
    W.push(sub('b', '(if time) Which 3 things should she buy to spend as much of her $20 as she can? How much change will she get?'));
    W.push(...lines(1));
    // ---------- page 2 ----------
    W.push(q(4, 'The 24-hour clock. After 12 noon, add 12 to the hour.', { pb: true, before: 0, keepNext: true }));
    { const ws = [2475, 2475, 2475, 2475];
      W.push(tbl(ws, [row(['7:15 a.m.', '3:40 p.m.', '________', '12:30 p.m.'].map((s, i) => cell(s, ws[i], { h: 90, size: 24 }))),
        row(['________', '________', '20:05', '________'].map((s, i) => cell(s, ws[i], { h: 90, size: 24, bold: true, fill: 'EDEDED' })))])); }
    W.push(sub('a', 'Fill in the table. The top row is 12-hour time; the bottom row is 24-hour time.'));
    W.push(sub('b', 'Siti says, “17:00 is 7 p.m.” Is she right? Explain.'));
    W.push(...lines(1));
    W.push(q(5, 'Trick 2: draw a time line and jump to the next o’clock.', { keepNext: true }));
    W.push(sub('a', 'Ali’s swimming lesson starts at 3:45 p.m. and ends at 5:10 p.m. How long is it?   ____ h ____ min'));
    W.push(...lines(1));
    W.push(sub('b', 'Mei’s piano lesson starts at 16:35 and lasts 50 minutes. When does it end? Use 24-hour time.   ________'));
    W.push(...lines(1));
    W.push(sub('c', 'A film lasts 1 h 50 min. It ends at 21:15. When did it start?   ________'));
    W.push(...lines(1));
    W.push(q(6, '(if time) Buses leave the interchange every 25 minutes. The first bus leaves at 06:40.', { keepNext: true }));
    { const ws = [1650, 1650, 1650, 1650, 1650, 1650];
      W.push(tbl(ws, [row(['1st bus', '2nd bus', '3rd bus', '4th bus', '5th bus', '6th bus'].map((s, i) => cell(s, ws[i], { bold: true, fill: 'EDEDED', h: 60 }))),
        row(['06:40', '', '', '', '', ''].map((s, i) => cell(s, ws[i], { h: 100, size: 24 })))])); }
    W.push(sub('a', 'Ravi reaches the interchange at 08:15. When is the next bus? How long does he wait?'));
    W.push(ans());
    W.push(sub('b', 'The bus ride to school takes 35 minutes. When does Ravi reach school?   ________'));
    return W;
  }
};
