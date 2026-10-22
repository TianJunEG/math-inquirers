// Math Inquirers P5 — Lesson 5: Volume Vault (volume of cuboids, liquids, water levels, painted cubes)
// Every answer below was worked out with exact fractions and the cube counts were checked by listing every cube.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const WSIDE = '#BCD6EE', WTOP = '#EEF5FC';
const F = 'Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// Oblique drawing: x = length (right), y = height (up), z = breadth (back, at 30 degrees, half size).
const OB = (x0, y0, s) => (x, y, z) => [x0 + x * s + z * s * 0.433, y0 - y * s - z * s * 0.25];
const pts = (P, list) => list.map(([x, y, z]) => P(x, y, z).map(v => v.toFixed(1)).join(',')).join(' ');
const ln = (P, a, b, o = '') => { const [x1, y1] = P(...a), [x2, y2] = P(...b); return `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${NAVY}" ${o}/>`; };
const tx = (x, y, s, o = {}) => `<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" font-size="${o.size || 16}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.fill || NAVY}" font-family="${F}">${esc(s)}</text>`;

// A box L x B x H. o.grid: unit-cube grid lines; o.fill: [front, top, right]; o.water: water height (glass tank, open top); o.labels: [len, height, breadth]
function box(P, L, B, H, o = {}) {
  let s = '';
  if (o.water !== undefined) {
    const w = o.water;
    s += ln(P, [0, 0, B], [L, 0, B], 'stroke-width="1.5" stroke-dasharray="5 4"') + ln(P, [0, 0, B], [0, H, B], 'stroke-width="1.5" stroke-dasharray="5 4"') + ln(P, [0, 0, 0], [0, 0, B], 'stroke-width="1.5" stroke-dasharray="5 4"');
    if (w > 0) {
      s += `<polygon points="${pts(P, [[0, w, 0], [L, w, 0], [L, w, B], [0, w, B]])}" fill="${WTOP}" stroke="${NAVY}" stroke-width="1"/>`;
      s += `<polygon points="${pts(P, [[0, 0, 0], [L, 0, 0], [L, w, 0], [0, w, 0]])}" fill="${SKY}"/>`;
      s += `<polygon points="${pts(P, [[L, 0, 0], [L, 0, B], [L, w, B], [L, w, 0]])}" fill="${WSIDE}"/>`;
    }
  } else if (o.fill) {
    s += `<polygon points="${pts(P, [[0, 0, 0], [L, 0, 0], [L, H, 0], [0, H, 0]])}" fill="${o.fill[0]}"/>`;
    s += `<polygon points="${pts(P, [[0, H, 0], [L, H, 0], [L, H, B], [0, H, B]])}" fill="${o.fill[1]}"/>`;
    s += `<polygon points="${pts(P, [[L, 0, 0], [L, 0, B], [L, H, B], [L, H, 0]])}" fill="${o.fill[2]}"/>`;
  }
  if (o.grid) {
    const g = 'stroke-width="1.5"';
    for (let i = 1; i < L; i++) s += ln(P, [i, 0, 0], [i, H, 0], g) + ln(P, [i, H, 0], [i, H, B], g);
    for (let j = 1; j < H; j++) s += ln(P, [0, j, 0], [L, j, 0], g) + ln(P, [L, j, 0], [L, j, B], g);
    for (let k = 1; k < B; k++) s += ln(P, [0, H, k], [L, H, k], g) + ln(P, [L, 0, k], [L, H, k], g);
  }
  const e = 'stroke-width="2.5" stroke-linejoin="round"';
  s += `<polygon points="${pts(P, [[0, 0, 0], [L, 0, 0], [L, H, 0], [0, H, 0]])}" fill="none" stroke="${NAVY}" ${e}/>`;
  s += `<polygon points="${pts(P, [[0, H, 0], [L, H, 0], [L, H, B], [0, H, B]])}" fill="none" stroke="${NAVY}" ${e}/>`;
  s += `<polygon points="${pts(P, [[L, 0, 0], [L, 0, B], [L, H, B], [L, H, 0]])}" fill="none" stroke="${NAVY}" ${e}/>`;
  if (o.labels) {
    const [a, b, c] = o.labels;
    const ls = o.lsize || 16;
    if (a) { const [x, y] = P(L / 2, 0, 0); s += tx(x, y + ls + 6, a, { size: ls }); }
    if (b) { const [x, y] = P(0, H / 2, 0); s += tx(x - 8, y + 6, b, { a: 'end', size: ls }); }
    if (c) { const [x, y] = P(L, 0, B / 2); s += tx(x + 10, y + ls + 2, c, { a: 'start', size: ls }); }
  }
  if (o.water !== undefined && o.water > 0 && o.wlabel) {
    const [x1, y1] = P(L * 0.12, 0, 0), [, y2] = P(L * 0.12, o.water, 0);
    s += `<line x1="${x1.toFixed(1)}" y1="${(y1 - 3).toFixed(1)}" x2="${x1.toFixed(1)}" y2="${(y2 + 3).toFixed(1)}" stroke="${TEAL}" stroke-width="2.5"/>`;
    s += `<polygon points="${x1 - 6},${(y2 + 12).toFixed(1)} ${x1 + 6},${(y2 + 12).toFixed(1)} ${x1},${(y2 + 2).toFixed(1)}" fill="${TEAL}"/><polygon points="${x1 - 6},${(y1 - 12).toFixed(1)} ${x1 + 6},${(y1 - 12).toFixed(1)} ${x1},${(y1 - 2).toFixed(1)}" fill="${TEAL}"/>`;
    s += tx(x1 + 10, (y1 + y2) / 2 + 6, o.wlabel, { a: 'start', fill: TEAL });
  }
  return s;
}
const svg = (w, h, label, inner, dw, vb) => `<svg aria-label="${esc(label)}" viewBox="${vb || '0 0 ' + w + ' ' + h}" xmlns="http://www.w3.org/2000/svg" style="width:${dw || w}px;max-width:100%">${inner}</svg>`;

const figQ1 = () => svg(300, 150, 'A solid cuboid built from 1-centimetre cubes: 4 cubes long, 3 cubes deep and 2 cubes high',
  box(OB(40, 130, 44), 4, 3, 2, { grid: true, fill: [YEL, '#FFE08A', '#F2B92E'] }));
const figQ3 = () => svg(440, 300, 'A glass tank 50 cm long, 30 cm wide and 40 cm high with water 18 cm deep, drawn to scale',
  box(OB(80, 260, 5), 50, 30, 40, { water: 18, wlabel: '18 cm', labels: ['50 cm', '40 cm', '30 cm'] }));
const figQ4 = () => {
  let s = box(OB(70, 230, 5), 40, 25, 30, { water: 15, wlabel: '15 cm', labels: ['40 cm', '30 cm', '25 cm'], lsize: 24 });
  const cubeAt = (x0, y0) => box(OB(x0, y0, 5), 10, 10, 10, { fill: ['#C9CED8', '#E3E6EC', '#AEB4C2'] });
  s += cubeAt(370, 120) + cubeAt(440, 120) + cubeAt(510, 120) + cubeAt(405, 210) + cubeAt(475, 210);
  s += tx(395, 140, '10 cm', { size: 22 }) + tx(480, 248, '5 metal cubes', { size: 22 });
  return svg(600, 260, 'A tank with base 40 cm by 25 cm and water 15 cm deep, and 5 metal cubes with edges of 10 cm, drawn to the same scale', s, 300, '-40 44 630 225');
};
const figQ5 = () => svg(250, 230, 'A 4 by 4 by 4 cube built from 64 small cubes, painted on the outside',
  box(OB(16, 200, 38), 4, 4, 4, { grid: true, fill: [YEL, '#FFE08A', '#F2B92E'] }), 175);
const figQ6 = () => {
  let s = box(OB(60, 200, 4), 30, 20, 24, { water: 24, labels: ['30 cm', '24 cm', '20 cm'], lsize: 24 });
  s += box(OB(330, 200, 4), 40, 30, 25, { water: 0, labels: ['40 cm', '25 cm', '30 cm'], lsize: 24 });
  s += tx(150, 52, 'Container A (full)', { size: 22 }) + tx(440, 52, 'Tank B (empty)', { size: 22 });
  return svg(600, 240, 'Container A, 30 cm by 20 cm by 24 cm, full of water, and empty tank B, 40 cm by 30 cm by 25 cm, drawn to the same scale', s, 300, '-40 28 640 215');
};

module.exports = {
  lesson: {
    n: 5, week: 3, session: 'A', title: 'Volume Vault', topic: 'Volume',
    objective: 'Find the volume of a cuboid by counting layers of 1-cm cubes and by length × breadth × height; list every cuboid that can be built from a number of cubes; solve water-tank problems (cm³ and litres, new water levels, the rise when an object sinks, pouring from one tank into another); and count the painted faces of a cube cut into small cubes.',
    skills: 'Make a list in order, draw a diagram to scale, work backwards (height = volume ÷ base area), look for a pattern (painted cubes), check with a second method',
    materials: 'About 30 one-centimetre cubes (or dice, Lego bricks, sugar cubes), a ruler, squared paper, mini whiteboards. Tutor: a clear plastic box with a ruler taped to its side, water and a stone for the demonstration.',
    online: 'The tutor shows the water rise live on camera: a clear box, a ruler taped to the side, a stone dropped in. Children use dice or Lego for the Explore; with no cubes they draw layers on squared paper. Whiteboards are held up to the camera.',
    warmup: 'Missing Edge Match: six cuboid cards show the volume and two edges. Teams find the third edge and write the division they used, then show their answers together on three, two, one (nobody shouts, and speed does not matter). Then five quick questions on cm³, ml and ℓ.',
    explore: 'The 24-cube challenge: pairs build or draw every cuboid that uses exactly 24 one-centimetre cubes, record its length, breadth and height, and decide how they know they have found them all.',
    mini: 'Volume = cubes in one layer × number of layers = length × breadth × height. Water in a tank is a cuboid too: base area × water height, and 1000 cm³ = 1 ℓ. When water is added or an object sinks, the rise in level = extra volume ÷ base area. Worked examples: water added to a tank; a stone that makes the water rise.',
    share: 'Ali says: “A 1000 cm³ stone always makes the water rise 1 cm.” Is he right? Explain.',
    exit: { q: 'A tank has a base 30 cm by 25 cm and water 8 cm deep. A rock is put in and sinks. The water rises to 10 cm. (a) What is the volume of the rock? (b) How many litres of water are in the tank?', a: '(a) 1500 cm³ (30 × 25 × 2)  (b) 6 ℓ (30 × 25 × 8 = 6000 cm³)' },
    mistakes: ['Mixing units: dividing litres by a base area in cm² without changing litres to cm³ first (8 ℓ = 8000 cm³).', 'Using the tank’s full height instead of the water height, or giving the new water level when the question asks for the rise (or the other way round).', 'Painted cubes: counting the corner cubes again on the edges, or using n instead of n − 2 for the cubes along each edge.'],
    extension: 'Find every cuboid with whole-number edges and a volume of 60 cm³. (There are 10, from 1 × 1 × 60 to 3 × 4 × 5.) Which one is most like a cube?',
    key: [
      ['Q1', '(a) 24 cm³ (4 × 3 × 2)  (b) 40 cubes (the smallest cube it fits in is 4 × 4 × 4 = 64 cubes; 64 − 24 = 40)'],
      ['Q2', '(a) 8 cuboids: 1 × 1 × 36, 1 × 2 × 18, 1 × 3 × 12, 1 × 4 × 9, 1 × 6 × 6, 2 × 2 × 9, 2 × 3 × 6, 3 × 3 × 4  (b) only 3 × 3 × 4 (every other one has an edge longer than 5 cm)'],
      ['Q3', '(a) 27 ℓ (50 × 30 × 18 = 27 000 cm³)  (b) 33 ℓ (50 × 30 × 22 = 33 000 cm³)  (c) 12 cm (9000 ÷ 1500 = 6 cm lower; 18 − 6 = 12)'],
      ['Q4', '(a) 5000 cm³ (5 × 10 × 10 × 10)  (b) 5 cm (5000 ÷ 1000)  (c) 20 cm  (d) 3000 cm³ (40 × 25 × 3)'],
      ['Q5', '3 faces: 8 (corners)   2 faces: 24 (12 edges × 2)   1 face: 24 (6 faces × 4)   no paint: 8 (2 × 2 × 2 inside).  Check: 8 + 24 + 24 + 8 = 64'],
      ['Q6', '(a) 14.4 ℓ (30 × 20 × 24 = 14 400 cm³)  (b) 12 cm (14 400 ÷ 1200)  (c) 8 cm (14 400 ÷ (600 + 1200) = 8)']
    ]
  },

  script: {
    hook: ['Welcome to the Volume Vault, inquirers! Today everything is made of tiny 1-centimetre cubes: boxes, tanks, even water. If we can count cubes cleverly, we can work out how much a tank holds, how high the water goes and what happens when a stone sinks in.', 'Watch this clear box. I am going to drop a stone in. Before I do: what will happen to the water level, and could we work out the stone’s volume from it?'],
    warmIntro: ['Missing Edge Match! Each card shows a cuboid’s volume and two of its edges. Find the third edge and write the division you did. We show our answers together on three, two, one. Nobody shouts, and there is no prize for being first.', 'First card: 60 cm³, 5 cm and 4 cm. What is the third edge? How do you know?'],
    predict: ['You have 24 one-centimetre cubes. You must use all of them to build one cuboid. How many different cuboids do you think you can build? Write a guess: 2? 5? 10?'],
    exploreHints: ['Stuck: start with a flat cuboid, 1 cube high. Then try 2 cubes high: how many cubes are in each layer then?', 'Not sure if two are different: “Turn it round. If it is the same three edges, it is the same cuboid.”', 'Finished early: which of your cuboids is most like a cube? Can any of them be a cube? Why not?'],
    think: ['“A cuboid 5 cm by 3 cm by 4 cm. One layer on the bottom is 5 rows of 3: 15 cubes. There are 4 layers, so 15 × 4 = 60 cubes. That is 60 cm³. Length × breadth is the layer, and × height counts the layers.”', '“The water in the tank is a cuboid too: 40 by 25 by 12. That is 12 000 cm³. 1000 cm³ is 1 litre, so 12 litres. Now I pour in 8 litres: that is 8000 cm³. The base is 40 × 25 = 1000 cm², so each centimetre of height holds 1000 cm³. 8000 ÷ 1000 = 8 cm higher.”', '“A stone goes in and the water goes up 3 cm. The water did not change: the stone is pushing it up. The new slice of height is 30 by 20 by 3 = 1800 cm³. That slice is exactly the stone’s volume.”'],
    circulate: ['Ask: “Which number is the water height, and which is the tank height?”', 'Ask: “Is that in litres or in cm³? Change it before you divide.”', 'Ask: “How do you know your list is complete? What did you keep fixed?”'],
    hints: ['Hint 1: “Draw the tank. Shade the water. Write every length you know on the picture.”', 'Hint 2: “What is the base area? Each 1 cm of height holds that many cm³.”', 'Hint 3: “Is the object completely under the water? If not, the water only has the space around it.”'],
    talk: ['“Ali says a 1000 cm³ stone always makes the water rise 1 cm. Is he right?”', '“Why does a big tank’s water level rise only a little when a stone goes in?”'],
    talkAns: 'Ali is right only when the base area is 1000 cm² (for example 40 cm by 25 cm). The rise is the stone’s volume ÷ base area: in a 20 cm by 10 cm tank (200 cm²) the same stone makes the water rise 1000 ÷ 200 = 5 cm. A wide tank spreads the extra volume over a big base, so the rise is small. (And if the stone sticks out of the water, only the part under water counts.)',
    close: ['“Today you counted cubes in layers, listed every cuboid in order, and worked backwards from a water level to a volume. Notice it, test it, explain why: you did all three.”']
  },

  deck: {
    today: 'Count cubes in layers, find every cuboid from 24 cubes, and solve tank puzzles: litres, water levels and stones that make the water rise.',
    warmGame: 'Missing Edge Match. Six cuboid cards each show the volume and two edges. Teams find the third edge and write the division they used (60 ÷ (5 × 4) = 3). Show answers together on three, two, one.',
    warmQs: [['A cuboid is 7 cm by 5 cm by 2 cm. What is its volume?', '70 cm³'], ['1 ℓ = ? cm³', '1000 cm³'], ['3.2 ℓ = ? ml', '3200 ml'], ['A cube has a volume of 125 cm³. How long is each edge?', '5 cm'], ['4500 cm³ of water = ? ℓ', '4.5 ℓ']],
    expSetup: ['Take 24 one-centimetre cubes (or draw them on squared paper).', 'Build a cuboid that uses all 24 cubes. Write its length, breadth and height.', 'Build as many different cuboids as you can. Turning one round does not make a new one.', 'How do you know you have found them all? Which one is most like a cube?'],
    expPic: 'a pile of 24 small cubes next to two cuboids built from them: a flat 6 by 4 by 1 slab and a 2 by 3 by 4 block, with “24 cubes: how many cuboids?” written beside them.',
    expAsk: [['How many different cuboids can you build from 24 cubes?', '6: 1 × 1 × 24, 1 × 2 × 12, 1 × 3 × 8, 1 × 4 × 6, 2 × 2 × 6, 2 × 3 × 4.'], ['How do you know you have found them all?', 'List in order with the shortest edge first: shortest edge 1 (1 × 1, 1 × 2, 1 × 3, 1 × 4; after that the pairs repeat), then shortest edge 2 (2 × 2 × 6, 2 × 3 × 4). Shortest edge 3 would need 3 × 3 × something, and 24 ÷ 9 is not whole.'], ['Do they all have the same volume?', 'Yes: 24 cm³ each. Same volume, different shapes.']],
    mini1: { head: 'Water in a tank: 40 cm by 25 cm by 30 cm, water 12 cm deep', body: ['The water is a cuboid: 40 × 25 × 12 = 12 000 cm³ = 12 ℓ.', '8 ℓ more = 8000 cm³. Base area 40 × 25 = 1000 cm², so the water rises 8000 ÷ 1000 = 8 cm.', 'New depth 12 + 8 = 20 cm. To fill it: 40 × 25 × 10 = 10 000 cm³ = 10 ℓ more.'], ans: '12 ℓ of water; after 8 ℓ more the water is 20 cm deep; 10 ℓ more fills the tank.' },
    mini2: { head: 'A stone sinks: tank base 30 cm by 20 cm, water rises from 10 cm to 13 cm', body: ['The water does not change. The stone pushes it up.', 'The new slice is 30 × 20 × 3 = 1800 cm³: that is the stone’s volume.', 'Backwards: a 600 cm³ stone would make it rise 600 ÷ 600 = 1 cm.'], ans: 'The stone is 1800 cm³. Rise = object volume ÷ base area.' },
    keyHead: 'Key idea: volume = base area × height',
    keyBig: 'A cuboid, or the water in a tank, holds base area × height cubic centimetres. Anything added or sunk in raises the water by its volume ÷ base area.',
    keySmall: '1 ℓ = 1000 cm³ and 1 ml = 1 cm³. Change litres to cm³ before you divide by a base area.',
    brk: 'More or less than a litre? I name an object: a can of drink, a bathtub, a teacup, a fish tank, a big water bottle. Stand tall if it holds more than 1 ℓ, crouch if less.',
    ws1: 'Page 1, in pairs: Q1 count the cubes, Q2 every cuboid from 36 cubes, Q3 the fish tank.',
    ws2: 'Page 2, on your own: Q4 the metal cubes, Q5 the painted cube, Q6 pouring from A into B.'
  },

  qbank: {
    core: [
      { q: 'Build a box 3 cubes long, 2 cubes wide and 2 cubes high with 1-cm cubes (or draw it layer by layer). How many cubes are in the bottom layer? How many layers are there? How many cubes are used altogether?', a: '6 cubes in the bottom layer, 2 layers, 12 cubes altogether (12 cm³).' },
      { q: 'Use 12 cubes to build a flat rectangle, one cube high. How many different rectangles can you make? (Turning a rectangle round does not make a new one.) Write the length and width of each.', a: '3 rectangles: 1 by 12, 2 by 6 and 3 by 4.' },
      { q: 'A tank has a base of 10 cm by 10 cm. If the water is 1 cm deep, there are 100 one-cm cubes of water. How many cubes of water are there if the water is 3 cm deep? 10 cm deep? How many litres is the water when it is 10 cm deep? (1 ℓ = 1000 cm³.)', a: '300 cm³; 1000 cm³, which is 1 ℓ.' },
      { q: 'How many 1-cm cubes (dice) fill a box 5 cm long, 4 cm wide and 3 cm high? Use dice, or draw one layer and count the layers.', a: '60 cubes (a layer of 20, three layers).' },
      { q: 'A tank has a base 4 cm by 3 cm. The water is 2 cm deep. Twelve 1-cm cubes are dropped in and sink to the bottom. How much higher does the water rise? (Think of the cubes as one more layer of water.)', a: '1 cm (12 cubes fill exactly one layer of 4 × 3).' },
      { q: 'A bottle holds 2 litres of water. How many cm³ is that? How many ml is 2.5 ℓ? (1 ℓ = 1000 ml = 1000 cm³.)', a: '2000 cm³; 2500 ml.' }
    ],
    stretch: [
      { q: 'How many cubes with 2-cm edges can be packed in neat layers into a box 9 cm long, 6 cm wide and 5 cm high?', a: '24 (4 along, 3 across, 2 layers; not 270 ÷ 8, because the cubes cannot be cut)' },
      { q: 'A tank is 1/3 full of water. After 12 ℓ more is poured in, it is 3/5 full. How many litres does the tank hold when full?', a: '45 ℓ (3/5 − 1/3 = 4/15 of the tank is 12 ℓ, so 1/15 is 3 ℓ)' },
      { q: 'A cuboid has a square base and a height of 5 cm. Its volume is 245 cm³. How long is each side of the base?', a: '7 cm (base area 245 ÷ 5 = 49 cm², and 7 × 7 = 49)' },
      { q: 'A cuboid 3 cm by 4 cm by 5 cm is built from 1-cm cubes and painted on the outside. How many cubes have no paint at all?', a: '6 (the inside block is 1 × 2 × 3)' },
      { q: 'A tank is 60 cm long, 40 cm wide and 50 cm high. A bucket holds 8 ℓ. What is the fewest number of buckets of water needed to fill the tank at least 3/4 full?', a: '12 buckets (3/4 of 120 ℓ = 90 ℓ; 90 ÷ 8 = 11.25, so 11 buckets are not enough)' },
      { q: 'A tank has a base 40 cm by 30 cm. It holds 36 ℓ of water. How deep is the water?', a: '30 cm (36 000 ÷ 1200)' },
      { q: 'A cube-shaped container with 20-cm edges is full of water. All of it is poured into an empty tank with a base 50 cm by 32 cm. How deep is the water in the tank?', a: '5 cm (8000 ÷ 1600)' },
      { q: 'A tank with a base 50 cm by 20 cm has water 8 cm deep. Ali pours in 3 ℓ of water. Then he drops in a stone with a volume of 500 cm³, and it sinks. How deep is the water now?', a: '11.5 cm (3 ℓ = 3000 cm³ raises the water 3000 ÷ 1000 = 3 cm to 11 cm; the stone raises it 500 ÷ 1000 = 0.5 cm more).' }
    ],
    challenge: [
      { q: 'A big cube is painted on the outside and cut into small cubes of the same size. 96 small cubes have exactly one painted face. How many small cubes are there altogether?', a: '216 (each face has 96 ÷ 6 = 16 = 4 × 4 one-face cubes, so the cube is 6 cubes along each edge: 6 × 6 × 6)' },
      { q: 'How many different cuboids can be built with exactly 64 one-centimetre cubes, using all of them each time?', a: '7 (1 × 1 × 64, 1 × 2 × 32, 1 × 4 × 16, 1 × 8 × 8, 2 × 2 × 16, 2 × 4 × 8, 4 × 4 × 4)' },
      { q: 'A tank has a base 40 cm by 30 cm. A cube with edges of 10 cm sits on the bottom, and the water is 6 cm deep around it. How much water is in the tank?', a: '6600 cm³ = 6.6 ℓ (40 × 30 × 6 − 10 × 10 × 6 = 7200 − 600; the cube is taller than the water, so only 6 cm of it is under water)' },
      { q: 'Water in a tank is 15 cm deep. When 4 identical bricks are put in, the water rises to 18 cm. 6 more of the same bricks are put in. How deep is the water now? (The bricks stay under water.)', a: '22.5 cm (each brick raises it 3 ÷ 4 = 0.75 cm; 10 bricks raise it 7.5 cm)' },
      { q: 'Make up your own tank puzzle with a stone. Choose the size of the base, the volume of the stone and how the water changes, then give your partner the puzzle. Check your partner\u2019s answer. What if the base were twice as wide: how would the rise change?', a: 'Open-ended. Sample: a tank has a base 25 cm by 20 cm and water 10 cm deep. A stone of 1000 cm³ sinks. How much does the water rise? (1000 ÷ 500 = 2 cm, so the water is 12 cm deep.) If the base were twice as wide (1000 cm²), the rise would be half as much, 1 cm.' },
      { q: 'Bricks measure 2 cm by 3 cm by 4 cm. They are all placed the same way up to build a solid cube. What is the fewest number of bricks needed?', a: '72 (the smallest cube edge is 12 cm, the smallest common multiple of 2, 3 and 4: 6 × 4 × 3 = 72 bricks)' },
      { q: 'Three faces of a cuboid have areas 12 cm², 15 cm² and 20 cm². What is the volume of the cuboid?', a: '60 cm³ (edges 3 cm, 4 cm and 5 cm: 3 × 4 = 12, 3 × 5 = 15, 4 × 5 = 20)' },
      { q: 'A cuboid 3 cm by 4 cm by 5 cm is built from 1-cm cubes and painted on the outside. How many cubes have exactly 2 painted faces? How many have exactly 1?', a: '24 with 2 faces (4 × 1 + 4 × 2 + 4 × 3 along the edges); 22 with 1 face (60 − 8 corners − 24 − 6 inside)' },
      { q: 'A tank has a base 30 cm by 20 cm and water 10 cm deep. A block 10 cm by 10 cm by 15 cm is stood upright on the bottom. How deep is the water now?', a: '12 cm (the water now covers 600 − 100 = 500 cm² of floor: 6000 ÷ 500 = 12 cm; the block is 15 cm tall, so it sticks out. Not 12.5 cm!)' }
    ]
  },

  workbook: H => {
    const t = h => '<div style="text-align:left;font-size:16px;line-height:1.55">' + h + '</div>';
    const L = s => '<b style="color:#1F7A6F">' + s + '</b> ';
    const blank = w => '<span style="display:inline-block;width:' + w + 'px;border-bottom:2px dotted #8A94AD"></span>';
    const pw = [2700, 2400, 2400, 2400];
    const paintTbl = H.tbl(pw, [
      H.row(['Painted faces', '3 faces', '2 faces', '1 face'].map((s, i) => H.cell(s, pw[i], { bold: true, fill: 'D9D9D9', h: 50 }))),
      H.row([H.cell('Number of cubes', pw[0], { bold: true, h: 70 }), H.cell('8 corners', pw[1]), H.cell('12 edges × ____ = ____', pw[2]), H.cell('6 faces × ____ = ____', pw[3])])
    ]);
    return [
      H.p(['<b style="color:#1F7A6F">Words and signs.</b> cm³ means cubic centimetres (1 cm³ is one small cube). 1 litre (ℓ) = 1000 cm³. A cuboid has a length, a breadth (how wide) and a height.'], { after: 20 }),
      H.q(1, 'This solid cuboid is built from 1-cm cubes.', { before: 20, keepNext: true }),
      H.tbl([3600, 6300], [H.row([H.cell('<div>' + figQ1() + '</div>', 3600, { h: 20 }),
        H.cell(t(L('(a)') + 'What is its volume?   ' + blank(70) + ' cm³<br>' + L('(b)') + 'Mei adds more 1-cm cubes, without taking any away, until the solid is a cube. What is the fewest number of cubes she must add? Explain.'), 6300, { h: 40 })])]),
      ...H.lines(1),
      H.q(2, 'Ravi has 36 one-centimetre cubes. He uses all of them to build one cuboid. Turning a cuboid round does not make a new one.', { keepNext: true }),
      H.sub('a', 'List every cuboid he can build (length × breadth × height). Work in order. How many are there?', { keepNext: true }),
      ...H.lines(2),
      H.sub('b', 'Which of them can fit inside a box 5 cm long, 5 cm wide and 5 cm high?   ________________'),
      H.q(3, 'A glass tank is 50 cm long, 30 cm wide and 40 cm high. The water in it is 18 cm deep.', { keepNext: true }),
      H.p(['<b style="color:#1F7A6F">Start here:</b> the water is 18 layers of cubes. One layer is 50 × 30 = ______ cubes. 18 layers hold ______ cm³. Then 1000 cm³ = 1 ℓ.'], { after: 20 }),
      H.tbl([4400, 5500], [H.row([H.cell('<div>' + figQ3() + '</div>', 4400, { h: 20 }),
        H.cell(t(L('(a)') + 'How many litres of water are in the tank?<br>' + blank(110) + ' ℓ<br>' + L('(b)') + 'How many more litres are needed to fill it to the top?<br>' + blank(110) + ' ℓ<br>' + L('(c)') + 'Instead, 9 ℓ of water is let out. How deep is the water now?<br>' + blank(110) + ' cm'), 5500, { h: 40 })])]),

      H.q(4, 'A tank has a base 40 cm by 25 cm. The water in it is 15 cm deep. Ali drops in 5 metal cubes with edges of 10 cm. They sink to the bottom and are completely under water.', { pb: true, before: 0, keepNext: true }),
      H.fig(figQ4()),
      H.p(['<b style="color:#1F7A6F">Start here:</b> the base is 40 × 25 = ______ cm². A layer of water 1 cm deep over the base is ______ cm³. The cubes take up space, so the water has to rise.'], { after: 20 }),
      H.sub('a', 'Volume of 5 cubes: ______ cm³   (b) Rise: ____ cm   (c) Depth now: ____ cm'),
      H.sub('d', '(try this one if you like) Then Ali drops in a stone. The water rises another 3 cm. What is the volume of the stone?   ____________ cm³'),
      H.q(5, 'A 4 by 4 by 4 cube is built from 64 small cubes. The outside of the big cube is painted yellow. Then it is taken apart.', { keepNext: true }),
      H.tbl([3000, 6900], [H.row([H.cell('<div>' + figQ5() + '</div>', 3000, { h: 20 }),
        H.cell('<div>' + t('<b style="color:#1F7A6F">Start here:</b> every corner cube has 3 painted faces. Along one edge there are 4 cubes: 2 corners and ____ between them. On one face, the cubes not on an edge make a ____ by ____ square. Fill in the table.<br>How many small cubes have paint on exactly …') + paintTbl + t('How many small cubes have no paint at all?  ' + blank(60) + '<br>Check: do your four numbers add up to 64?') + '</div>', 6900, { h: 30 })])]),
      H.q(6, 'Container A is full of water. Tank B is empty.', { keepNext: true }),
      H.fig(figQ6()),
      H.sub('a', 'How many litres of water are in container A?   __________ ℓ'),
      H.sub('b', 'All of A is poured into B. How deep is the water in B?   ______ cm'),
      H.sub('c', '(try this one if you like) Then some water is poured back from B into A until the water in A and B is equally deep. How deep is it?', { keepNext: true }),
      ...H.lines(1)
    ];
  }
};

// ---- figures for the printed Think harder (A1, A4) and Go further (B2, B3) items ----
{
  // A1: the box 9 cm long, 6 cm wide and 5 cm high (no grid: the 2-cm cubes are for the child to imagine)
  module.exports.qbank.stretch[0].fig = svg(260, 150, 'A box 9 cm long, 6 cm wide and 5 cm high',
    box(OB(40, 130, 15), 9, 6, 5, { fill: [WTOP, '#FFFFFF', '#DCE6F2'], labels: ['9 cm', '5 cm', '6 cm'], lsize: 15 }), 230);
  // A4 and B2: a 3 by 4 by 5 cuboid made of 1-cm cubes, painted on the outside
  const cub = () => svg(250, 170, 'A cuboid 5 cubes long, 4 cubes wide and 3 cubes high, built from 1-centimetre cubes and painted on the outside',
    box(OB(20, 150, 30), 5, 4, 3, { grid: true, fill: [YEL, '#FFE08A', '#F2B92E'] }), 180);
  module.exports.qbank.stretch[3].fig = cub();
  module.exports.qbank.challenge[module.exports.qbank.challenge.length - 2].fig = cub();
  // B3: tank 30 x 20 with water 10 cm deep and a block 10 x 10 x 15 standing on the bottom
  let g = box(OB(30, 200, 5), 30, 20, 25, { water: 10, wlabel: '10 cm', labels: ['30 cm', '', '20 cm'], lsize: 17 });
  g += box(OB(30 + 5 * 10, 200, 5), 10, 10, 15, { fill: ['#C9CED8', '#E3E6EC', '#AEB4C2'], labels: ['10 cm', '15 cm', ''], lsize: 15 });
  g += tx(285, 80, 'block 10 × 10 × 15', { size: 15, a: 'start' });
  module.exports.qbank.challenge[module.exports.qbank.challenge.length - 1].fig = svg(400, 230, 'A tank with base 30 cm by 20 cm and water 10 cm deep. A block 10 cm by 10 cm by 15 cm stands upright on the bottom.', g, 260);
}
