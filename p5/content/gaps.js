// P5 enrichment features, rewritten in the fix pass (docs/audit/fixpass_p5.md):
//  sneak   = two "sneak-peek puzzles" at minutes 0-3: [0] an ACCESS question any child can try with objects, drawing or counting
//            (a guaranteed first win), [1] a thinking question. Ideas not yet taught; guessing and "I do not know" welcome; answers
//            are shown privately (own paper shown only to the tutor on camera, or all held up together); nobody is marked.
//  pic     = optional picture drawn on the slide beside the question (see rebuild/p5_gaps.py)
//  whatIf  = a second what-if question from the explore stage, for any child who is ready for more now (so nobody waits)
//  solo    = what to begin with on workbook page 2 (printed as a neutral line; the page is a menu, not a wall)
//  praise  = the strategy praise line used in the reflection script
// Open investigations live in inv.js. Every answer here was checked in Python (see docs/audit/fixpass_p5.md).
const INV = require('./inv.js');
const L = {
  1: {
    sneak: [
      ['Use the digit cards 3, 6, 7 and 9, each once, to make a 4-digit number as close to 7000 as you can. Try one that starts with 7 and one that starts with 6. Which is closer?', 'Starting with 7, the best is 7369 (369 above 7000). Starting with 6, the best is 6973 (27 below 7000). 6973 is closer, and it is the closest of all 24 numbers. A child who only tries numbers that start with 7 misses it: testing BOTH sides of a target is today\'s idea. Any honest try is a good start.'],
      ['Put ONE pair of brackets in  4 + 6 × 5 − 3  to make 47. How do you know no other place makes 47?', '(4 + 6) × 5 − 3 = 47. The other single pairs give 16 or 31 (and so does no bracket at all). Brackets first, then × and ÷, then + and −.']
    ],
    pic: 'cards',
    whatIf: ['A million seconds is about 11 and a half days. How long is 10 million seconds? Then guess first: how long is a BILLION seconds (1 000 000 000): days, months or years? Use your calculator.', '10 million seconds is about 116 days, nearly 4 months (10 times as long). A billion seconds is about 11 574 days, which is about 32 years: 1 000 000 000 ÷ 86 400 = 11 574.07 days; 11 574 ÷ 365 is about 31.7 years. A billion is a thousand millions, so 1000 × 11.6 days.'],
    pose: 'Write your own 7-digit number riddle with three clues. Swap with a partner and solve each other’s riddles.',
    p1: 'Q2 (a) (b) and Q3 (a) (b) (c); Q1 is take-home', take: 'Q1 (page 1); Q5 (c) (d) and Q6 (page 2)',
    solo: 'Q4 and Q5 (a) (b)', praise: 'You got unstuck by drawing it. That is a real mathematician move.'
  },
  2: {
    sneak: [
      ['Two pizzas are shared equally among 4 friends. Draw the pizzas and show how you would cut them. How much pizza does each friend get?', '1/2 of a pizza each. For example cut each pizza in half: that makes 4 halves, one for each friend. Any fair cutting is fine (for example cutting each pizza into quarters and giving each friend 2 quarters).'],
      ['Mei spends 1/3 of her money on a book. Then she spends 1/2 of the money she has LEFT on lunch. What fraction of her money has she spent altogether? Use the bar.', '2/3. After the book 2/3 is left; half of 2/3 is 1/3 (lunch); 1/3 + 1/3 = 2/3. The half is a half of what is LEFT, not of everything.']
    ],
    pic: 'bar3',
    whatIf: ['4 pizzas are shared among 5 children, 5 pizzas among 6 children, and 6 pizzas among 7 children. Who gets the biggest share? What do you notice as the group gets bigger?', '4/5, 5/6 and 6/7: the share grows each time (0.8, 0.83, 0.86). Each child is 1/5, 1/6, 1/7 short of a whole pizza, a smaller piece each time, so the shares creep up towards 1 pizza but never reach it.'],
    pose: 'Pick a fraction and write it as the sum of two different unit fractions. Challenge a partner to find your two.',
    p1: 'Q1 (a) (b) and Q2 (the worked example, (a) (b)); Q3 is take-home', take: 'Q3 (page 1); Q4 (b) (c) and Q6 (page 2)',
    solo: 'Q5 and Q4 (a)', praise: 'Drawing the bar again when it did not work is exactly right.'
  },
  3: {
    sneak: [
      ['Ben is 8 and his father is 32. (a) How old is Ben\'s father when Ben is 12? (b) How much older than Ben is his father now? How much older when Ben is 12?', '(a) 36. (b) 24 years older now, and 24 years older when Ben is 12: the gap does not change.'],
      ['Ali has 40 cards and Mei has 20. Ali gives Mei some cards and then they have the same number. How many cards did Ali give? What stays the same?', '10. The TOTAL stays 60, so each has 30 afterwards and Ali gives 40 − 30 = 10. Counters or a drawing help.']
    ],
    pic: 'bars2',
    whatIf: ['Ali has 19 counters and Mei has 6 (25 altogether). Ali gives Mei counters one at a time. Can Mei ever have exactly as many as Ali? Why or why not? Try 24 altogether too.', 'No for 25: equal shares would be 12 and a half each, so an odd total can never be shared equally. With 24 (18 and 6) it works: 12 each after Ali gives 6. The total never changes when they only swap counters.'],
    pose: 'Make up a before-and-after story in which the total stays the same. Draw its model, then swap with a partner.',
    p1: 'Q1 (a) (b) (c) and Q2 (a) (b)', take: 'Q3 and Q5 (page 2)',
    solo: 'Q4 (a) (b)', praise: 'You drew the before and after bars side by side. That is how you saw what stayed the same.'
  },
  4: {
    sneak: [
      ['Draw a rectangle 6 squares wide and 4 squares tall on squared paper. Count all the squares in it. Draw a line from one corner to the opposite corner and cut along it. Do the two pieces match exactly? What fraction of the rectangle is one piece?', '24 squares. The two triangles match exactly (turn one round and it fits on the other), so each is 1/2 of the rectangle: 12 squares.'],
      ['ABCD is a rectangle 12 cm long and 5 cm tall. P is a point on the top side AB. Join P to C and to D. Does the area of triangle PCD change if P slides along AB? What is the area?', 'No, 30 cm². The base DC = 12 cm and the height from P down to DC is always 5 cm, so the area is 1/2 × 12 × 5 = 30 cm² wherever P is. A guess of "it changes" is fine: we test it in the explore.']
    ],
    pic: 'grid64',
    whatIf: ['On squared paper draw THREE different triangles that each have an area of exactly 12 square units. Write the base and the height of each one. What do all three have in common?', 'For example base 6 and height 4, base 8 and height 3, base 12 and height 2, base 4 and height 6. Each time base × height = 24, which is double the area (12 × 2). Any triangle on the same base and height, leaning or not, is also fine.'],
    pose: 'Draw a rectangle, label its sides, and join points to make a shaded triangle. Work out its area, then swap with a partner.',
    p1: 'Q1 and Q2', take: 'Q3 (page 2)',
    solo: 'Q5 and Q4', praise: 'You split the shape into triangles when it was too big. That is a strong strategy.'
  },
  5: {
    sneak: [
      ['A box is 4 cubes long, 3 cubes wide and 2 cubes tall. Build it with cubes, or draw one layer and then the next layer. How many cubes fill the box?', '24 cubes: one layer is 4 × 3 = 12 cubes and there are 2 layers.'],
      ['A tank has a base 20 cm by 10 cm with water 6 cm deep. A 10-cm cube is dropped in and sinks. How far does the water rise? Draw the tank and shade the water first.', '5 cm. The cube is 1000 cm³ and the base is 200 cm², so the rise is 1000 ÷ 200 = 5 cm. The new depth is 11 cm, taller than the 10-cm cube, so the cube is completely covered.']
    ],
    pic: 'box432',
    whatIf: ['Try other numbers of cubes: 12, 16, 18, 20, 24 and 30. Which number gives the MOST different cuboids? Which numbers up to 30 give only ONE?', '24 gives the most, 6 cuboids (12, 16, 18 and 20 give 4 each; 30 gives 5). Only the prime numbers 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29 (and 1) give just one cuboid, a single row: 1 × 1 × n. Checked by listing every case.'],
    pose: 'Make up a tank puzzle with a stone: choose the base, the depth of the water and the stone. Swap and solve.',
    p1: 'Q2 (a) (b) and Q3 (the Start-here line, (a) (b)); Q1 is take-home', take: 'Q1 and Q3 (c) (page 1); Q5 and Q6 (page 2)',
    solo: 'Q4 (a) (b) (c)', praise: 'Thinking of the water as layers of cubes got you unstuck.'
  },
  6: {
    sneak: [
      ['A tap puts 12 litres into a tank in 4 minutes. Draw 4 buckets and share the 12 litres. How many litres go in each minute? How many litres go in during 6 minutes?', '3 litres each minute, so 18 litres in 6 minutes (6 × 3).'],
      ['Ali reads 12 pages in 4 minutes. Mei reads 20 pages in 5 minutes. Who reads faster? How can you be sure?', 'Mei. Ali reads 3 pages a minute (12 ÷ 4) and Mei reads 4 pages a minute (20 ÷ 5). Comparing the amount for 1 minute makes it fair.']
    ],
    pic: 'bar12',
    whatIf: ['Printer A prints 18 pages a minute and printer B prints 25 pages a minute. Together they print 430 pages in 10 minutes. How many pages should each printer be given so that both finish at exactly the same time?', 'Printer A gets 180 pages (18 × 10) and printer B gets 250 pages (25 × 10); 180 + 250 = 430. If both work for the whole 10 minutes they finish together.'],
    pose: 'Make up a better-buy puzzle with three packs of the same thing. Which pack is the best buy? Swap and check.',
    p1: 'Q1 (a) (b), Q2 (the Start-here line, (a) (b)) and Q3 (a)', take: 'Q3 (b) (c) (page 1); Q5 and Q6 (b) (c) (page 2)',
    solo: 'Q4 (a) (b) and Q6 (a)', praise: 'Making a table of 1, 2, 3 minutes got you unstuck.'
  },
  7: {
    sneak: [
      ['A 10 by 10 square has 100 small squares. Colour in 35 of them. How many are NOT coloured? What percentage is not coloured?', '65 squares, which is 65%. Percent means out of 100.'],
      ['A jacket costs $100. The shop takes 10% off, and then takes another 10% off the NEW price. Is that the same as 20% off? What is the final price?', 'No. $100 → $90 → $81. 20% off $100 would be $80. The second 10% is taken from $90, not from $100.']
    ],
    pic: 'hund',
    whatIf: ['A $200 price goes up 50% and then down 50%. What is the price now? Then try up 20% and down 20%. What do you notice about the final price each time?', 'Up 50% then down 50%: $200 → $300 → $150. Up 20% then down 20%: $200 → $240 → $192. The final price is always LESS than $200, because the "down" percentage is taken from the bigger new price.'],
    pose: 'Make up a price that goes up by a percentage and then down by the same percentage. Predict the final price, then test it.',
    p1: 'Q1 (a) (b) and Q3 (a) (b) (c); Q2 is done in the page 2 time', take: 'Q4 (d) and Q5 (page 2)',
    solo: 'Q2 (a) to (d) (it is on page 1) and Q4 (a) to (c)', praise: 'Using 10% as a stepping stone got you unstuck.'
  },
  8: {
    sneak: [
      ['The corner of your paper is a right angle, 90°. Draw a line from the corner so that it splits the right angle into two angles, and one of them is 30°. How big is the other angle?', '60° (30° + 60° = 90°).'],
      ['Two straight lines cross. One of the four angles is 38°. Find the angle next to it. Say which angle fact you used.', '142°. Angles on a straight line add up to 180°, and 180° − 38° = 142°.']
    ],
    pic: 'rt30',
    whatIf: ['Draw any five-sided shape and tear off its five corners. Fit them together. Do they fit on a straight line, or round a point, or neither? Predict first: how many degrees do the five corners make altogether?', '540°, which is one and a half turns (360° + 180°). A five-sided shape can be cut into 3 triangles from one corner, and 3 × 180° = 540°. A four-sided shape gives 2 triangles, 360°.'],
    pose: 'Draw a triangle and a parallelogram that share a side. Give two or three angles and ask for one more. Swap and solve.',
    p1: 'Q1 (a) to (d) and Q2 (a) (b)', take: 'Q2 (c) (page 1); Q3 (c) (d), and Q5 (page 2)',
    solo: 'Q3 (a) (b) and Q4 (a) (b)', praise: 'Writing the angle on the diagram as soon as you found it got you unstuck.'
  },
  9: {
    sneak: [
      ['Sticks make a row of triangles: 1 triangle uses 3 sticks, 2 triangles use 5 sticks, 3 triangles use 7 sticks. Build or draw 4 triangles. How many sticks does it use?', '9 sticks. Each new triangle shares a side with the one before, so it adds 2 sticks.'],
      ['Using the same pattern, how many sticks do 10 triangles need? How many triangles can you make with exactly 41 sticks? Say how you know.', '21 sticks for 10 triangles (3 + 9 × 2, or 2 × 10 + 1). 41 sticks make 20 triangles (take away the 1 extra stick, then 40 ÷ 2). Continuing the list also works.']
    ],
    pic: 'tri',
    whatIf: ['If 12 children each high-five every other child exactly once, how many high fives is that? Find a rule you could use for ANY number of children.', '66. With n children each high-fives (n − 1) others, but every high five is counted twice, so the number is n × (n − 1) ÷ 2. For 12 children: 12 × 11 ÷ 2 = 66. The table 1, 3, 6, 10, 15, 21 … also works.'],
    pose: 'Make up a growing pattern with dots or matchsticks. Draw figures 1, 2 and 3, and ask a partner for figure 10.',
    p1: 'Q1 (a) (b) and Q2 (a) (b)', take: 'Q1 (c) (d) and Q2 (c) (page 1); Q4 (b) and Q5 (page 2)',
    solo: 'Q3 and Q4 (a)', praise: 'Making a table of the first five figures got you unstuck.'
  },
  10: {
    sneak: [
      ['Ali, Mei and Ravi wear a red shirt, a blue shirt and a green shirt, one each. Ali is not wearing red or green. Mei is not wearing green. Who wears which colour? Move three cards or draw a small table.', 'Ali blue, Mei red, Ravi green. Ali can only wear blue. Mei is not green and blue is taken, so Mei wears red. Ravi has green.'],
      ['Ali spends half of his money on a book. Then he spends half of the money he has LEFT on lunch. He has $6 left. How much did he have at first? Draw a picture or work from the end.', '$24. Work backwards: 6 × 2 = 12 before lunch, 12 × 2 = 24 before the book. A bar cut into 4 equal units, 1 unit = $6, also works.']
    ],
    pic: 'logic3',
    whatIf: ['Card A has a twin: a number is TRIPLED, then 4 is taken away, then the answer is divided by 2, and the result is 7. What was the number? Then make up your own card of this kind whose answer is 10.', '6. Work backwards: 7 × 2 = 14, 14 + 4 = 18, 18 ÷ 3 = 6. Check: 6 × 3 = 18, 18 − 4 = 14, 14 ÷ 2 = 7. Any new card is fine if its working backwards gives a whole number and it checks when run forwards.'],
    pose: 'Make up a logic puzzle with three friends, three snacks and three clues. Swap and solve; does only one answer fit?',
    p1: 'Q1 and Q2; Q3 is done in the page 2 time', take: 'Q4 (b) (c), Q5 and Q6 (page 2)',
    solo: 'Q3 (it is on page 1) and Q4 (a)', praise: 'You tried a different way to start when the first one did not work. That is what we practised all holiday.'
  }
};
// short answers shown on the slide when the tutor clicks to reveal (full answers are in the notes and the guide)
const SHORT = {
  1: ['6973 (27 below 7000) beats 7369 (369 above).', '(4 + 6) × 5 − 3 = 47'],
  2: ['1/2 of a pizza each', '2/3 of her money'],
  3: ['(a) 36   (b) 24 older, then 24 older', '10 cards. The total stays 60.'],
  4: ['Yes, they match: 1/2 each, 12 squares', 'No. 30 cm² every time.'],
  5: ['24 cubes (12 in a layer, 2 layers)', '5 cm'],
  6: ['3 litres a minute; 18 litres', 'Mei: 4 pages a minute, Ali 3'],
  7: ['65 squares, so 65%', 'No. $81, not $80.'],
  8: ['60°', '142°'],
  9: ['9 sticks', '21 sticks; 20 triangles'],
  10: ['Ali blue, Mei red, Ravi green', '$24']
};
for (const n of Object.keys(L)) { L[n].inv = INV[n]; L[n].sneak.forEach((x, i) => x[2] = SHORT[n][i]); }
module.exports = L;
