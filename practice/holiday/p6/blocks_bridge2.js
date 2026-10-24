// Bridge to the Level 6 workbook's own code-block drawing used in lessons 3 and 4 (p6/content/l4.js blocksSvg; l3.js has the same function).
// Reads a JSON list of {prog, label, fs} on stdin (prog = [[indent, kind, text], ...], "[...]" in the text draws a value pill), writes a JSON list of svg strings.
const fs = require('fs'), path = require('path'), Module = require('module');
const root = path.join(__dirname, '..', '..', '..');
const file = path.join(root, 'p6', 'content', 'l4.js');
const req = Module.createRequire(file);
const src = fs.readFileSync(file, 'utf8');
const m = { exports: {} };
new Function('module', 'require', '__dirname', src + '\n;module.__blocksSvg=blocksSvg;')(m, req, path.dirname(file));
const reqs = JSON.parse(fs.readFileSync(0, 'utf8'));
process.stdout.write(JSON.stringify(reqs.map(r => m.__blocksSvg(r.prog, r.label || 'Code', r.fs || 15, 900))));
