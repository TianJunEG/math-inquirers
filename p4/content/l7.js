// Math Inquirers P4 Holiday Program — Lesson 7: Area Architects II (Area and perimeter, rectangles and squares)
const tip = require('../tip.js');
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';

// ---------- drawing helpers (1 square on the grid = 1 cm) ----------
const svg = (w, h, label, inner) => `<svg aria-label="${label}" viewBox="0 0 ${w} ${h}" width="${w}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${inner}</svg>`;
const grid = (x0, y0, cols, rows, c) => {
  let d = '';
  for (let i = 0; i <= cols; i++) d += `M${x0 + i * c} ${y0} V${y0 + rows * c} `;
  for (let j = 0; j <= rows; j++) d += `M${x0} ${y0 + j * c} H${x0 + cols * c} `;
  return `<path d="${d}" stroke="${N}" stroke-width="1" opacity="0.22" fill="none"/>`;
};
const poly = (x0, y0, c, pts, fill = SKY, sw = 3) => `<polygon points="${pts.map(([a, b]) => `${x0 + a * c},${y0 + b * c}`).join(' ')}" fill="${fill}" stroke="${N}" stroke-width="${sw}" stroke-linejoin="round"/>`;
const tx = (x, y, s, size = 17, fill = N, anchor = 'middle', weight = 700) => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${s}</text>`;
const rect = (x0, y0, c, a, b, w, h, fill = SKY, sw = 3) => `<rect x="${x0 + a * c}" y="${y0 + b * c}" width="${w * c}" height="${h * c}" fill="${fill}" stroke="${N}" stroke-width="${sw}"/>`;

// Side-by-side block: question parts on the left, the figure on the right (saves a whole figure height on the printed page)
const side = (fig, w, inner) => `<div class="p sub" style="display:flex;gap:12px;align-items:flex-start;margin-bottom:4px;padding-left:0"><div style="flex:1;min-width:0">${inner}</div><div style="flex:none;width:${w}px">${fig}</div></div>`;

// Q1: L-shape, 9 cm by 7 cm with a 5 cm by 3 cm piece missing from the top right
const q1Svg = () => {
  const c = 16, x0 = 46, y0 = 6, ox = x0 + c, oy = y0 + c;
  let s = grid(x0, y0, 11, 9, c) + poly(ox, oy, c, [[0, 0], [4, 0], [4, 3], [9, 3], [9, 7], [0, 7]]);
  s += tx(ox + 2 * c, oy - 6, '4 cm') + tx(ox - 8, oy + 3.5 * c + 6, '7 cm', 17, N, 'end') + tx(ox + 4.5 * c, oy + 7 * c + 18, '9 cm');
  s += tx(ox + 9 * c + 8, oy + 5 * c + 6, '4 cm', 17, N, 'start');
  s += tx(ox + 6.5 * c, oy + 3 * c - 6, '? cm', 17, RED) + tx(ox + 4 * c + 6, oy + 1 * c + 4, '? cm', 17, RED, 'start');
  return svg(280, 156, 'An L-shaped figure on a 1 cm grid: top 4 cm, left side 7 cm, bottom 9 cm, right side 4 cm, and two step sides marked with question marks', s);
};
// Q3: blank grid to draw on
const blankGrid = (cols, rows, c, label) => svg(600, rows * c + 8, label, grid((600 - cols * c) / 2, 4, cols, rows, c));
// Q4: staircase, 11 cm wide and 6 cm high, layers 3, 7, 11 cm long and 2 cm high
const q4Svg = () => {
  const c = 18, x0 = 50, y0 = 4, ox = x0 + c, oy = y0;
  let s = grid(x0, y0, 13, 7, c) + poly(ox, oy, c, [[0, 0], [3, 0], [3, 2], [7, 2], [7, 4], [11, 4], [11, 6], [0, 6]]);
  s += tx(ox + 5.5 * c, oy + 6 * c + 17, '11 cm') + tx(ox - 8, oy + 3 * c + 6, '6 cm', 17, N, 'end');
  return svg(300, 134, 'A staircase figure on a 1 cm grid, 11 cm along the bottom and 6 cm up the left side, with three steps', s);
};
// Q5: 8 cm by 2 cm rectangle with a dashed cut line, and room to draw
const q5Svg = () => {
  const c = 20, x0 = 80, y0 = 4;
  let s = grid(x0, y0, 22, 5, c) + rect(x0, y0, c, 1, 1, 8, 2);
  s += `<line x1="${x0 + 5 * c}" y1="${y0 + 0.6 * c}" x2="${x0 + 5 * c}" y2="${y0 + 3.4 * c}" stroke="${RED}" stroke-width="4" stroke-dasharray="8 6"/>`;
  s += tx(x0 + 6 * c, y0 + 0.75 * c, 'cut', 16, RED);
  s += tx(x0 + 5 * c, y0 + 4.2 * c, '8 cm') + tx(x0 + 0.85 * c, y0 + 2 * c + 6, '2 cm', 16, N, 'end');
  s += tx(x0 + 16 * c, y0 + 0.75 * c, 'Draw the square here.', 16, TEAL);
  return svg(600, 108, 'An 8 cm by 2 cm rectangle on a grid with a dashed cut line down the middle, and empty grid space to draw the new square', s);
};
// Q6: photo 8 cm by 6 cm in a frame 1 cm wide
const q6Svg = () => {
  const c = 12, x0 = 6, y0 = 4, ox = x0 + c, oy = y0 + c;
  let s = grid(x0, y0, 12, 10, c) + rect(ox, oy, c, 0, 0, 10, 8, Y) + rect(ox, oy, c, 1, 1, 8, 6, SKY);
  s += tx(ox + 5.4 * c, oy + 5.6 * c, 'photo', 17, N);
  s += tx(ox + 5 * c, oy + 2 * c - 2, '8 cm', 16) + tx(ox + 1.2 * c, oy + 4 * c + 6, '6 cm', 16, N, 'start');
  s += tx(ox + 10 * c + 8, oy + 0.5 * c + 6, '1 cm', 16, TEAL, 'start');
  return svg(210, 130, 'An 8 cm by 6 cm photo inside a yellow frame that is 1 cm wide all round, on a 1 cm grid', s);
};

module.exports = {
  lesson: {
    n: 7, week: 4, session: 'A', title: 'Area Architects II', topic: 'Area and Perimeter',
    objective: 'Find the area of a composite figure by splitting it into rectangles or by taking away a missing piece, find its perimeter by pushing the steps out to a rectangle, find every rectangle with a given area and compare their perimeters, and explain what changes when a shape is cut and rearranged.',
    skills: 'Splitting and taking away, making a list in order, looking for a pattern, explaining why (area stays the same, perimeter can change)',
    materials: '1 cm square tiles or 24 paper squares per child (cut the Square grid page into squares), 1 cm grid paper, scissors, a 30 cm ruler, mini whiteboards, a paper strip 8 squares by 2 squares for cutting.',
    online: 'Children cut 24 paper squares and some 1 cm grid strips from the Square grid page before the lesson and build on camera; the tutor draws on the grid figures on the slides.',
    warmup: 'Area or Perimeter? The tutor reads a job (a fence round a field, carpet for a room, lace round a tablecloth). Children hold up A for area or P for perimeter and say why: area covers the inside, perimeter goes round the edge.',
    explore: 'Pairs use 12 square tiles to make every rectangle with an area of 12 square centimetres. For each one they record the length, the breadth and the perimeter, then find the longest and the shortest perimeter and say what they notice.',
    mini: 'Composite figures: find the missing lengths from the opposite sides, then find the area by splitting into two rectangles or by taking the missing piece away from a big rectangle (5 × 6 + 3 × 4 = 42 and 8 × 6 − 3 × 2 = 42). Perimeter: when a figure has only square corners and its steps go one way, push the steps out to make a rectangle, so the perimeter is the same as the big rectangle (28 cm). Fixed area: list the factor pairs in order (20 = 1 × 20, 2 × 10, 4 × 5); long and thin gives the biggest perimeter, close to a square gives the smallest. Before page 2: staircases, cutting and rearranging (the area stays the same, the perimeter can change), and borders (big rectangle take away the inside).',
    share: 'Ben says: "A bigger area always means a bigger perimeter." Do you agree? Use rectangles to test it.',
    exit: { q: 'A 7 cm by 5 cm rectangle has a 2 cm by 2 cm square cut from one corner. Find the area and the perimeter of the shape that is left.', a: 'Area 35 − 4 = 31 cm². Perimeter 24 cm, the same as the rectangle (push the corner back out).' },
    mistakes: [
      'Adding the given sides only and forgetting the unlabelled sides when finding the perimeter of an L-shape (or labelling a missing side with the wrong length because they did not use the opposite side).',
      'Thinking that the same area means the same perimeter, or that cutting a corner off a rectangle makes the perimeter smaller.',
      'Finding the area of a border by working out 2 × (length + breadth) and forgetting the 4 corner squares, instead of big rectangle take away the inside.'
    ],
    extension: 'Ravi has 24 m of fencing for a rectangular pen with whole-metre sides. One side is a wall and needs no fence. What is the largest area he can fence? (72 m²: 6 m, 12 m, 6 m.)',
    key: [
      ['Q1', '(a) The step across is 5 cm (9 − 4) and the step down is 3 cm (7 − 4).  (b) Split: 4 × 7 + 5 × 4 = 28 + 20 = 48 cm². Take away: 9 × 7 − 5 × 3 = 63 − 15 = 48 cm².  (c) 4 + 3 + 5 + 4 + 9 + 7 = 32 cm, the same as a 9 cm by 7 cm rectangle.'],
      ['Q2', 'Table: 1 by 24, perimeter 50 cm;  2 by 12, 28 cm;  3 by 8, 22 cm;  4 by 6, 20 cm (4 rectangles; 6 by 4 is the same as 4 by 6).  (a) Largest: 1 cm by 24 cm (50 cm). Smallest: 4 cm by 6 cm (20 cm).  (The 36 cm² question, answer: 6 cm by 6 cm, a square with perimeter 24 cm, is in the question bank.)'],
      ['Q3', '(a) 6 cm²  (b) Smallest: a 2 by 3 rectangle (the only shape with the smallest perimeter): 10 cm. Largest: for example a row of 6 squares, or any shape with no 2 by 2 block of squares in it: 14 cm.'],
      ['Q4', '(a) 34 cm. Push the steps out: they make an 11 cm by 6 cm rectangle, and 11 + 6 + 11 + 6 = 34.  (b) 3 × 2 + 7 × 2 + 11 × 2 = 6 + 14 + 22 = 42 cm².'],
      ['Q5', '(a) A 4 cm by 4 cm square (the two 4 by 2 pieces stacked).  (b) Rectangle: area 16 cm², perimeter 20 cm. Square: area 16 cm², perimeter 16 cm.  (c) No. The area stayed the same, but the perimeter changed from 20 cm to 16 cm.'],
      ['Q6', '(a) 10 cm by 8 cm  (b) 10 × 8 − 8 × 6 = 80 − 48 = 32 cm²  (c) Her 4 strips (8 + 8 + 6 + 6 = 28 cm²) leave out the 4 corner squares of the frame: 28 + 4 = 32 cm².']
    ]
  },

  script: {
    hook: ['Welcome, Area Architects! Architects must know two things about every room: how much floor it covers, and how far it is all the way round.', 'Today we find areas and perimeters of tricky shapes WITHOUT counting every square, and we test a big idea: does the same area always give the same perimeter? Notice it. Test it. Explain why.'],
    warmIntro: ['I will read out a job. If the job needs the space INSIDE, hold up A for area. If it goes ROUND THE EDGE, hold up P for perimeter.', 'Be ready to explain: "It covers the floor, so it is area." "It goes round the outside, so it is perimeter."'],
    predict: ['You have 12 square tiles. How many different rectangles do you think you can make with all 12? Will they all have the same perimeter? Write your guess in the corner of your whiteboard.'],
    exploreHints: ['Stuck: start with one long row of 12. Then try 2 rows. Then 3 rows.', 'Not sure if a rectangle is new: "Is it the same as one you have, just turned round?"', 'Finished early: try 16 tiles. Which rectangle has the smallest perimeter now?'],
    think: [
      '“An L-shape. I need every side. The bottom is 8 cm and the top part is 5 cm, so the step across must be 8 − 5 = 3 cm. The left is 6 cm and the right is 4 cm, so the step down is 6 − 4 = 2 cm.”',
      '“For the area I can split it into a 5 by 6 rectangle and a 3 by 4 rectangle: 30 + 12 = 42. Or I can draw the big 8 by 6 rectangle and take away the missing 3 by 2 piece: 48 − 6 = 42. Same answer, so I trust it.”',
      '“For the perimeter, I push the two step sides out. The 3 cm piece slides up to the top and the 2 cm piece slides across to the right. Now it is an 8 by 6 rectangle, so the perimeter is 8 + 6 + 8 + 6 = 28 cm.”',
      '“Area 20: I list the pairs in order. 1 × 20, 2 × 10, 3 does not work, 4 × 5, and 5 × 4 is the same as 4 × 5, so I stop. Perimeters 42, 24, 18. Long and thin is biggest; close to a square is smallest.”'
    ],
    circulate: ['Ask: “Which side is opposite this one? How can that help you find the missing length?”', 'Ask: “Can you find the area another way to check?”', 'Ask: “You cut the shape and moved a piece. What stayed the same? What changed?”'],
    hints: ['Hint 1: “Mark every side with its length before you start. Use the opposite sides.”', 'Hint 2: “Draw the big rectangle round the shape. What is missing?”', 'Hint 3: “Push the steps out. Does the outline become a rectangle?”'],
    talk: ['“Ben says a bigger area always means a bigger perimeter. Can you find two rectangles that prove him wrong?”', '“When we cut a shape and move the pieces, which stays the same, area or perimeter? Why?”'],
    talkAns: 'Ben is wrong. A 1 cm by 12 cm rectangle has area 12 cm² and perimeter 26 cm, but a 4 cm by 4 cm square has a bigger area (16 cm²) and a smaller perimeter (16 cm). When we cut and move pieces, nothing is added or lost, so the area stays the same; the outline changes, so the perimeter can change.',
    close: ['“Today you were real architects: you split shapes, took pieces away and pushed steps out instead of counting every square.”', '“Hand me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Find the area and perimeter of tricky shapes the smart way, and find out why the same area can have different perimeters.',
    warmGame: 'Area or Perimeter? The tutor reads a job. Hold up A if it covers the inside, P if it goes round the edge. Then explain why.',
    warmQs: [['Area of a rectangle 7 cm by 6 cm?', '42 cm²'], ['Perimeter of a square with sides of 9 cm?', '36 cm'], ['A rectangle has area 48 cm² and length 8 cm. Breadth?', '6 cm'], ['Perimeter of a rectangle 12 cm by 5 cm?', '34 cm'], ['A square has perimeter 28 cm. Its area?', '49 cm²']],
    expSetup: ['Take 12 square tiles. Each is 1 cm by 1 cm.', 'Use all 12 to make a rectangle. Write its length, breadth and perimeter.', 'Make every different rectangle you can.', 'Which has the longest perimeter? The shortest? What do you notice?'],
    expPic: 'twelve yellow square tiles next to a 1 cm grid with a 2 by 6 rectangle drawn on it, and a small table with the columns length, breadth and perimeter.',
    expAsk: [['How many different rectangles did you make?', '3: 1 by 12, 2 by 6 and 3 by 4 (turning one round does not make a new one).'], ['Which has the longest perimeter? The shortest?', '1 by 12 has 26 cm; 3 by 4 has 14 cm.'], ['What do you notice?', 'All have area 12 cm², but the perimeters differ. Long and thin is biggest; closest to a square is smallest.']],
    mini1: { head: 'Area of an L-shape: split or take away', body: ['An 8 cm by 6 cm rectangle with a 3 cm by 2 cm piece missing from one corner.', 'Split: 5 × 6 + 3 × 4.', 'Take away: 8 × 6 − 3 × 2.'], ans: '42 cm² both ways.' },
    mini2: { head: 'Perimeter: push the steps out', body: ['The same L-shape. Two sides have no labels.', 'Slide the step sides out to the edges.', 'It becomes an 8 cm by 6 cm rectangle.'], ans: '28 cm, the same as the rectangle.' },
    keyHead: 'Key idea: split, take away, push out', keyBig: 'Area: split into rectangles or take the missing piece away. Perimeter: push the steps out to make a rectangle.', keySmall: 'The same area can have different perimeters. Close to a square gives the smallest perimeter.',
    brk: 'Body shapes! "Long and thin": stretch your arms out wide. "Square": hug yourself tight. Which shape has the shorter way round?',
    ws1: 'Page 1, in pairs: Q1 the L-shape, Q2 every rectangle with area 24 cm², Q3 six tiles.',
    ws2: 'Page 2, on your own: Q4 the staircase, Q5 cut and rearrange, Q6 the photo frame.'
  },

  qbank: {
    core: [
      { q: 'Draw a rectangle 9 cm long and 7 cm wide on squared paper (1 cm squares). How many squares are inside it? That is its area in cm².', a: '63 cm² (7 rows of 9 squares).' },
      { q: 'A rectangle is 15 cm long and 4 cm wide. Walk your finger once round the edge, adding the sides as you go. How long is the way round (the perimeter)?', a: '38 cm (15 + 4 + 15 + 4).' },
      { q: 'Use 12 square tiles (each 1 cm by 1 cm). Make a rectangle using all of the tiles. Write its length and breadth. Can you make a different rectangle with the 12 tiles? Draw each one.', a: '1 by 12, 2 by 6 and 3 by 4 (a 6 by 2 is the same rectangle turned round).' },
      { q: 'A rectangle has an area of 56 cm². Its length is 8 cm. Find its perimeter. (Draw 8 squares in a row and add rows until you have 56 squares.)', a: '30 cm (the breadth is 7 cm; 8 + 7 + 8 + 7 = 30).' },
      { q: 'A figure is made of a 6 cm by 4 cm rectangle and a 3 cm by 2 cm rectangle joined together without overlapping. Draw it on squared paper. Find its area.', a: '24 + 6 = 30 cm²' },
      { q: 'On squared paper draw a 6 cm by 6 cm square. Cut a 2 cm by 2 cm square from one corner. How many squares are left (the area)? Walk round the edge of the new shape: is the perimeter more than, less than, or the same as the perimeter of the 6 cm by 6 cm square?', a: 'Area 36 − 4 = 32 cm². The perimeter is the same: 24 cm.' }
    ],
    stretch: [
      { q: 'List every rectangle with whole-cm sides and an area of 30 cm². Which one has the smallest perimeter?', a: '1 by 30 (62 cm), 2 by 15 (34 cm), 3 by 10 (26 cm), 5 by 6 (22 cm). Smallest: 5 cm by 6 cm, 22 cm.' },
      { q: 'A rectangle has whole-cm sides and a perimeter of 20 cm. List all the possible rectangles and their areas. Which has the largest area?', a: '1 by 9 (9 cm²), 2 by 8 (16 cm²), 3 by 7 (21 cm²), 4 by 6 (24 cm²), 5 by 5 (25 cm²). Largest: the 5 cm by 5 cm square, 25 cm².' },
      { q: 'A 3 cm by 3 cm square is cut from each of the four corners of a 12 cm by 8 cm rectangle. Find the area and the perimeter of the shape that is left.', a: 'Area 96 − 4 × 9 = 60 cm². Perimeter 40 cm, the same as the rectangle: each cut takes away 3 + 3 and adds 3 + 3.' },
      { q: 'Three squares with sides 2 cm, 3 cm and 4 cm stand side by side in a row on the same line, smallest on the left. Find the area and the perimeter of the figure.', a: 'Area 4 + 9 + 16 = 29 cm². Perimeter 26 cm: push the steps out to a 9 cm by 4 cm rectangle.' },
      { q: 'A path 2 m wide goes all round a lawn 10 m long and 6 m wide. Find the area of the path.', a: '80 m². The whole thing is 14 m by 10 m = 140 m²; take away the lawn 60 m².' },
      { q: 'Ali joins 8 square tiles, each 1 cm by 1 cm, edge to edge. What is the smallest perimeter his shape can have? The largest?', a: 'Smallest 12 cm (a 2 by 4 rectangle, or a 3 by 3 square with one corner missing). Largest 18 cm (for example a row of 8).' },
      { q: 'A 6 cm by 4 cm rectangle is cut into two 6 cm by 2 cm rectangles, which are put end to end to make a 12 cm by 2 cm rectangle. How much longer is the new perimeter?', a: '8 cm longer: 28 cm instead of 20 cm. The area stays 24 cm².' },
      { q: 'A rectangle has whole-cm sides, an area of 40 cm² and a perimeter of 26 cm. Find its length and breadth.', a: '8 cm by 5 cm. (List the pairs for 40: 1 by 40, 2 by 20, 4 by 10, 5 by 8; only 5 by 8 has perimeter 26 cm.)' },
      { q: 'Which rectangle with whole-cm sides and an area of 36 cm² has the smallest perimeter? What is its perimeter?', a: '6 cm by 6 cm, a square, with perimeter 24 cm (the others: 1 by 36 is 74 cm, 2 by 18 is 40 cm, 3 by 12 is 30 cm, 4 by 9 is 26 cm).' }
    ],
    challenge: [
      { q: 'A square is cut into two identical rectangles. Each rectangle has a perimeter of 24 cm. Find the area of the square.', a: '64 cm². Each rectangle is one whole side and one half side all round, which is 3 sides of the square. 24 ÷ 3 = 8 cm, and 8 × 8 = 64.' },
      { q: 'A gap is cut into the middle of the top side of a 10 cm by 6 cm rectangle. The gap is 2 cm wide and 4 cm deep, with square corners. Find the area and the perimeter of the shape that is left.', a: 'Area 60 − 8 = 52 cm². Perimeter 32 + 4 + 4 = 40 cm: the two 4 cm sides inside the gap cannot be pushed out.' },
      { q: 'Ravi has 24 m of fencing to make a rectangular pen with whole-metre sides. (a) What is the largest area he can fence? (b) Now one side of the pen is a wall and needs no fence. What is the largest area now?', a: '(a) 36 m², a 6 m by 6 m square. (b) 72 m²: the two sides from the wall are 6 m and the side opposite the wall is 12 m (6 + 12 + 6 = 24).' },
      { q: 'Two 8 cm by 2 cm rectangles cross at their middles to make a plus shape. Find the area and the perimeter of the plus shape.', a: 'Area 16 + 16 − 4 = 28 cm² (the 2 by 2 middle is counted once). Perimeter 32 cm: each of the 4 arms is 3 cm long, so each arm adds 3 + 2 + 3 = 8 cm.' },
      { q: 'Siti’s garden is a square with an area of 49 m². She makes it 1 m longer and 1 m wider. How much bigger is the area? Then try 2 m longer and wider, and 3 m. Write what you notice.', a: '+1 m: 64 − 49 = 15 m². +2 m: 81 − 49 = 32 m². +3 m: 100 − 49 = 51 m². Each time the new area is two strips of 7 m by the extra width, plus a small square in the corner: 14 × 1 + 1 × 1, 14 × 2 + 2 × 2, 14 × 3 + 3 × 3. The gains 15, 32, 51 grow faster each time.' },
      { q: 'Mei makes a rectangle with 36 square tiles (each 1 cm by 1 cm). Ben makes a different rectangle with 36 tiles. Ben’s perimeter is 16 cm longer than Mei’s. What are the two rectangles?', a: 'Mei 6 cm by 6 cm (24 cm), Ben 2 cm by 18 cm (40 cm). The perimeters for 36 are 74, 40, 30, 26 and 24; only 40 and 24 differ by 16.' },
      { q: 'Make up your own fencing puzzle like Ravi’s: choose a length of fence (a whole number of metres, more than 20) and say whether one side is a wall. Find the largest area the pen can have, and prove it by listing every whole-metre pen. Swap puzzles with a partner and check each other’s lists.', a: 'Puzzles will vary: check that every whole-metre pen is listed. Model: 30 m of fence, no wall: the sides add to 15, and 7 m by 8 m gives the largest area, 56 m². With a wall on one side: 7 m, 16 m, 7 m (or 8 m, 14 m, 8 m) both give the largest area, 112 m².' },
      { q: 'A garden is 10 m long and 8 m wide. Two paths 1 m wide cross it: one goes along its length and one goes across its width. What area of the garden is NOT path?', a: '63 m². Slide the paths to the edges: the grass makes a 9 m by 7 m rectangle. (Or 80 − 10 − 8 + 1 = 63, because the square where the paths cross was counted twice.)' },
      { q: 'A rectangle 9 cm long and 4 cm wide is cut into 2 pieces. The pieces fit together exactly to make a square. How long is a side of the square? Did the perimeter go up or down?', a: 'Area 36 cm², so the side is 6 cm. The perimeter went down from 26 cm to 24 cm.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.q(1, 'This figure has only square corners. Each small square on the grid is 1 cm by 1 cm.', { before: 40, keepNext: true }));
    W.push(side(q1Svg(), 280, [
      H.sub('a', 'Use the opposite sides to find the two missing lengths. Write them on the figure.'),
      H.sub('b', 'Find the area in TWO ways.', { after: 40 }),
      H.sub('', 'Split it into 2 rectangles:  ______________', { after: 40 }),
      H.sub('', 'Big rectangle take away the missing piece:  ______________', { after: 40 }),
      H.sub('c', 'Find the perimeter.   Perimeter:  ________')].join('')));
    W.push(H.q(2, 'Rectangles with whole-cm sides have an area of 24 cm². Find them all. Start with a length of 1 cm.', { keepNext: true }));
    W.push(H.tbl([2400, 1500, 1500, 1500, 1500, 1500], [
      ...['Length (cm)', 'Breadth (cm)', 'Perimeter (cm)'].map(r => H.row([H.cell(r, 2400, { bold: true, fill: 'EDEDED', h: 44 }), ...[0, 1, 2, 3, 4].map(() => H.cell('\u00a0', 1500, { h: 44 }))]))
    ]));
    W.push(H.sub('a', 'Largest perimeter:  ___ by ___ cm     Smallest perimeter:  ___ by ___ cm'));
    W.push(H.q(3, 'Mei joins 6 square tiles, each 1 cm by 1 cm, edge to edge (whole sides touching).', { keepNext: true }));
    W.push(H.fig(blankGrid(24, 3, 22, 'An empty 1 cm grid for drawing shapes')));
    W.push(H.sub('a', 'What is the area of any shape she makes?  ________', { after: 40 }));
    W.push(H.sub('b', 'Draw the shape with the SMALLEST perimeter and one with the LARGEST.   Smallest:  ______   Largest:  ______'));

    W.push(H.q(4, 'Ravi says, "I cannot find the perimeter of this staircase, because the steps are not labelled."', { pb: true, before: 0, keepNext: true }));
    W.push(side(q4Svg(), 300, [
      tip('put a finger on the top-left corner and walk along the edge of the staircase. How far did you go across? How far down?'),
      H.sub('a', 'Show Ravi how to find the perimeter WITHOUT measuring each step. Push the steps out: the shape then fits in a ___ cm by ___ cm rectangle.'),
      H.sub('', '___ + ___ + ___ + ___ = ___ cm.   Perimeter:  ________', { after: 40 }),
      H.sub('b', 'Think of the staircase as 3 rows. The rows are 3 cm, 7 cm and 11 cm long, and each row is 2 cm high. Area:  ________')].join('')));
    W.push(H.q(5, 'An 8 cm by 2 cm rectangle is cut along the dashed line. The two pieces are put together to make a square.', { keepNext: true }));
    W.push(H.fig(q5Svg()));
    W.push(H.sub('a', 'Draw the square on the grid.', { after: 40 }));
    W.push(H.sub('b', 'Area: rectangle ____ cm², square ____ cm².    Perimeter: rectangle ____ cm, square ____ cm.', { after: 40 }));
    W.push(H.sub('c', 'Ali says, "The area stayed the same, so the perimeter stayed the same too." Is he right? Explain.'));
    W.push(...H.lines(1));
    W.push(H.q(6, 'A photo 8 cm long and 6 cm wide is put in a frame. The frame is 1 cm wide all round.', { keepNext: true }));
    W.push(side(q6Svg(), 210, [
      tip('on squared paper, draw the photo 8 by 6, then the frame 1 cm wide round it. Count the frame squares.'),
      H.sub('a', 'How long and how wide is the whole thing (photo and frame)?  ____ cm by ____ cm'),
      H.sub('b', 'Find the area of the frame only.   Area of frame:  ________'),
      H.sub('c', 'Mei found the frame like this: 8 + 8 + 6 + 6 = 28 cm². What did she forget?  ________________')].join('')));
    return W;
  }
};

// ---- close_gaps + fix pass: sneak-peek puzzles, Investigation (with an easy first step), Looking back, Go further (docs/audit/close_gaps_p4.md, fixpass_p4.md)
module.exports.gaps = {
 "idea": "area and perimeter",
 "check": [
  {
   "q": "Look at the picture: a 5 by 3 rectangle of squares with one corner square cut out. Count the squares that are left. How many squares is the area?",
   "a": "14 squares (the full 5 by 3 rectangle is 15 squares, and 1 is cut out).",
   "s": "14 squares (15 − 1).",
   "kind": "access"
  },
  {
   "q": "The perimeter is the distance all the way round the edge. Is the perimeter of this shape longer than, shorter than or the same as the perimeter of the full 5 by 3 rectangle? Say why.",
   "a": "The same: 16 units for both. Push the cut-out corner back out. The two edges of the notch are just as long as the two edges of the corner they replace.",
   "s": "The same (16). Push the corner back out.",
   "kind": "think"
  }
 ],
 "why": "For area, count the squares or take away the piece that is missing. For perimeter, push the corner back out to a rectangle.",
 "invest": {
  "kind": "Is it always true? Test and explain.",
  "head": "Bigger area, bigger perimeter?",
  "intro": "Ali says: \"A rectangle with a bigger area always has a bigger perimeter.\"",
  "parts": [
   "Test Ali's idea. Find the area and perimeter of a 1 cm by 11 cm rectangle, and of a 4 cm by 4 cm square. Which has the bigger area? Which has the bigger perimeter?",
   "List ALL the rectangles with whole-cm sides and a perimeter of 24 cm. Write the area of each.",
   "Is Ali right? Which of your rectangles has the biggest area? What is special about its shape?"
  ],
  "lines": 5,
  "key": "(a) 1 by 11: area 11 cm², perimeter 24 cm. 4 by 4: area 16 cm², perimeter 16 cm. The square has the bigger area but the smaller perimeter, so Ali is wrong. (b) Two sides add up to 12 cm: 1 by 11 (11 cm²), 2 by 10 (20), 3 by 9 (27), 4 by 8 (32), 5 by 7 (35), 6 by 6 (36). Six rectangles (checked by brute force). (c) The 6 by 6 square has the biggest area. For the same perimeter, the closer to a square, the bigger the area. Look for an ordered list, and for children who see that the pair of sides adds up to half the perimeter.",
  "easy": "Draw a 4 cm by 4 cm square on the Square grid. Write its area and its perimeter."
 },
 "reflect": "Something I did well: I wrote the lengths on the picture. The hardest part was finding the missing lengths on the staircase. What helped me: writing every length I could work out on the picture.",
 "go2": {
  "q": "What if you use 24 tiles? Make every rectangle. Which has the smallest perimeter?",
  "a": "4 rectangles: 1 × 24 (perimeter 50 cm), 2 × 12 (28 cm), 3 × 8 (22 cm) and 4 × 6 (20 cm). The 4 by 6 has the smallest perimeter: it is the closest to a square."
 },
 "cap": "Page 2 is on your own. Aim for Q4 and Q5 first. Q6 is a choice for the last few minutes."
};
