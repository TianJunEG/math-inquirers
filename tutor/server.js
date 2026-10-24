// Tutor console server (development). Production: static files + a WebSocket room relay (Cloudflare Pages + a
// Durable Object), with the tutor area behind Cloudflare Access. This file is the reference for the protocol.
//
//   node server.js            then open  http://localhost:8787/screen.html?lesson=<id>
//
// Rooms: the laptop ("screen") owns the clock and the slide; the phone ("remote") shows notes and sends commands.
// The screen only ever receives public lesson data. Notes and answers are served to the remote only.
const http = require('http'), fs = require('fs'), path = require('path');
const { WebSocketServer } = require('ws');

const PORT = process.env.PORT || 8787;
const ROOT = __dirname;
const SPLIT = path.join(ROOT, '..', 'split');
const FONTS = path.join(ROOT, '..', 'website', 'dist');
const KEY = process.env.TUTOR_KEY || '';           // dev guard for the notes endpoint; production uses Cloudflare Access
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.woff2': 'font/woff2', '.png': 'image/png', '.svg': 'image/svg+xml' };

function send(res, code, body, type) { res.writeHead(code, { 'Content-Type': type || 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' }); res.end(body); }
function file(res, p) {
  fs.readFile(p, (e, b) => e ? send(res, 404, 'Not found') : send(res, 200, b, TYPES[path.extname(p)] || 'application/octet-stream'));
}
const safe = (base, rel) => { const p = path.normalize(path.join(base, rel)); return p.startsWith(base) ? p : null; };

const server = http.createServer((req, res) => {
  const u = new URL(req.url, 'http://x'); let p = decodeURIComponent(u.pathname);
  if (p === '/') p = '/index.html';
  if (p === '/fonts.css' || p.startsWith('/fonts/')) { const f = safe(FONTS, p); return f ? file(res, f) : send(res, 400, 'Bad path'); }
  // Slide fragments: /slides/<deck>/<slideId>.html
  let m = /^\/slides\/([\w-]+)\/([\w-]+)\.html$/.exec(p);
  if (m) return file(res, path.join(SPLIT, m[1], 'project', 'slides', m[2] + '.html'));
  if (p === '/data/index.json') return file(res, path.join(ROOT, 'data', 'index.json'));
  // Lesson data: public for the screen, notes only for the remote
  m = /^\/data\/([\w-]+)\.(public|notes)\.json$/.exec(p);
  if (m) {
    if (m[2] === 'notes' && KEY && u.searchParams.get('key') !== KEY) return send(res, 403, 'Notes need the tutor key');
    return file(res, path.join(ROOT, 'data', m[1] + '.' + m[2] + '.json'));
  }
  const f = safe(path.join(ROOT, 'public'), p);
  return f ? file(res, f) : send(res, 400, 'Bad path');
});

// ---- rooms --------------------------------------------------------------------------------------------------
const rooms = new Map();           // code -> { screen, remotes:Set, state }
const wss = new WebSocketServer({ noServer: true });
server.on('upgrade', (req, sock, head) => {
  const u = new URL(req.url, 'http://x');
  if (u.pathname !== '/ws') return sock.destroy();
  wss.handleUpgrade(req, sock, head, (ws) => wss.emit('connection', ws, u));
});
wss.on('connection', (ws, u) => {
  const code = (u.searchParams.get('room') || '').toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 8);
  const role = u.searchParams.get('role') === 'remote' ? 'remote' : 'screen';
  if (!code) return ws.close(1008, 'room required');
  const r = rooms.get(code) || { screen: null, remotes: new Set(), state: null }; rooms.set(code, r);
  const tell = (to, msg) => { if (to && to.readyState === 1) to.send(JSON.stringify(msg)); };
  if (role === 'screen') {
    if (r.screen && r.screen.readyState === 1) r.screen.close(4000, 'replaced');
    r.screen = ws; r.remotes.forEach((x) => tell(x, { type: 'screen', online: true })); tell(ws, { type: 'remotes', n: r.remotes.size });
  } else {
    if (r.remotes.size >= 2) return ws.close(1008, 'room full');          // the code is visible on the shared screen until a phone joins
    r.remotes.add(ws); tell(ws, { type: 'screen', online: !!(r.screen && r.screen.readyState === 1) }); if (r.state) tell(ws, r.state);
    tell(r.screen, { type: 'remotes', n: r.remotes.size });
  }
  ws.on('message', (raw) => {
    let msg; try { msg = JSON.parse(raw); } catch (e) { return; }
    if (role === 'screen' && msg.type === 'state') { r.state = msg; r.remotes.forEach((x) => tell(x, msg)); }
    else if (role === 'remote' && msg.type === 'cmd') tell(r.screen, msg);
  });
  ws.on('close', () => {
    if (role === 'screen' && r.screen === ws) { r.screen = null; r.remotes.forEach((x) => tell(x, { type: 'screen', online: false })); }
    else { r.remotes.delete(ws); tell(r.screen, { type: 'remotes', n: r.remotes.size }); }
    if (!r.screen && !r.remotes.size) rooms.delete(code);
  });
});

server.listen(PORT, () => console.log('Tutor console on http://localhost:' + PORT));
