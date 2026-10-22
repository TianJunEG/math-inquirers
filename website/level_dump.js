// Dumps the real lesson titles and topics of the six levels to data/level_lessons.json (used by level_pages.py).
//   node level_dump.js
const R = require('path').resolve(__dirname, '..') + '/';
const out = {};
out[1] = require(R + 'hp/lessons.js').lessons;
for (const n of [2, 3, 4, 5, 6]) out[n] = require(R + 'p' + n + '/data.js').lessons;
for (const n in out) out[n] = out[n].map(l => ({ n: l.n, title: l.title, topic: l.topic }));
require('fs').writeFileSync(__dirname + '/data/level_lessons.json', JSON.stringify(out, null, 1) + '\n');
console.log('wrote data/level_lessons.json');
