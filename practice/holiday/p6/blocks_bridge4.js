// Bridge to the Level 6 workbook's own figure code for lesson 7 (p6/content/l7.js): blocks() and cornerFig() as printed.
// Reads a JSON list of requests on stdin, writes a JSON list of results.  Nothing is copied: the workbook file is loaded and its functions are called.
const fs = require('fs'), path = require('path'), Module = require('module');
const root = path.join(__dirname, '..', '..', '..');
const file = path.join(root, 'p6', 'content', 'l7.js');
const req = Module.createRequire(file);
const src = fs.readFileSync(file, 'utf8');
const m = { exports: {} };
new Function('module', 'require', '__dirname', src + '\n;' + ['blocks', 'cornerFig'].map(n => `module.__${n}=typeof ${n}==="undefined"?null:${n};`).join(''))(m, req, path.dirname(file));
const reqs = JSON.parse(fs.readFileSync(0, 'utf8'));
const out = reqs.map(r => {
  switch (r.kind) {
    case 'blocks': { const b = m.__blocks(r.prog, { fs: r.fs || 15, h: r.h || 30 }); return { svg: b.svg, w: b.w, h: b.h }; }
    case 'corner': return m.__cornerFig();
    default: throw new Error('unknown kind ' + r.kind);
  }
});
process.stdout.write(JSON.stringify(out));
