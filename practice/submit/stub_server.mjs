// LOCAL STUB of the submit endpoint + a static file server, ONE origin (like the real site). Test use only; stores in memory.
//   node practice/submit/stub_server.mjs <distDir> <keys.json>      prints {"port":N,"token":"..."} then serves until killed.
// Test controls (not present in production code): POST /__arm {mode:'503'|'store503', n}  GET /__state  -> {requests, submits, stored}
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
import { handle, sha256Hex } from './handler.js';
import { memoryStore } from './memory_store.mjs';
const [dist, keysFile] = process.argv.slice(2);
const K = JSON.parse(fs.readFileSync(keysFile, 'utf8'));
const TOKEN = 'S'.repeat(43);
const store = memoryStore({ tokenHash: await sha256Hex(TOKEN), keys: K.keys, unit: K.unit, version: K.version });
const st = { requests: [], armed: null, n: 0, submits: 0, duplicates: 0 };
const realRecord = store.record;
store.record = async (th, p) => { const r = await realRecord(th, p); if (r.duplicate) st.duplicates++; return r; };
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.css': 'text/css', '.woff2': 'font/woff2', '.woff': 'font/woff', '.svg': 'image/svg+xml' };
const srv = http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://x');
  const chunks = []; for await (const c of req) chunks.push(c); const body = Buffer.concat(chunks);
  if (url.pathname === '/__state') { res.setHeader('content-type', 'application/json'); return res.end(JSON.stringify({ requests: st.requests, submits: st.submits, duplicates: st.duplicates, stored: Object.fromEntries([...store.data].map(([k, v]) => [k, v])) })); }
  if (url.pathname === '/__arm') { const a = JSON.parse(body.toString()); st.armed = a.mode; st.n = a.n; return res.end('ok'); }
  if (url.pathname === '/api/practice/submit') {
    st.requests.push({ method: req.method, body: body.toString() }); st.submits++;
    const arm = st.n > 0 ? st.armed : null;
    if (arm === '503') { st.n--; res.statusCode = 503; return res.end('{"ok":false}'); }
    const r = await handle(new Request('http://' + req.headers.host + req.url, { method: req.method, headers: req.headers, body: req.method === 'POST' ? body : undefined }), {}, store);
    if (arm === 'store503') { st.n--; res.statusCode = 503; return res.end('{"ok":false}'); }   // stored, but the answer is lost on the way back
    res.statusCode = r.status; res.setHeader('content-type', 'application/json'); return res.end(await r.text());
  }
  const f = path.join(dist, url.pathname === '/' ? 'index.html' : decodeURIComponent(url.pathname));
  if (!f.startsWith(path.resolve(dist)) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.statusCode = 404; return res.end('no'); }
  st.requests.push({ static: url.pathname });
  res.setHeader('content-type', TYPES[path.extname(f)] || 'application/octet-stream'); res.end(fs.readFileSync(f));
});
srv.listen(0, '127.0.0.1', () => console.log(JSON.stringify({ port: srv.address().port, token: TOKEN })));
