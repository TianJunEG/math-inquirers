// Shared helpers for the screen and the remote.
window.MI = (function () {
  const fmt = (s) => { s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); };
  const fmtSigned = (s) => (s < 0 ? '+' : '') + fmt(Math.abs(s));
  const wsUrl = (room, role) => (location.protocol === 'https:' ? 'wss://' : 'ws://') + location.host + '/ws?room=' + encodeURIComponent(room) + '&role=' + role;
  // Reconnecting socket. on(msg) gets parsed JSON; status(ok) fires on every open/close.
  function connect(room, role, on, status) {
    let ws, closed = false, wait = 500;
    const open = () => {
      ws = new WebSocket(wsUrl(room, role));
      ws.onopen = () => { wait = 500; status && status(true); };
      ws.onmessage = (e) => { try { on(JSON.parse(e.data)); } catch (x) {} };
      ws.onclose = (e) => { status && status(false); if (!closed && e.code !== 4000) setTimeout(open, wait = Math.min(wait * 2, 5000)); };
    };
    open();
    return { send: (m) => { if (ws && ws.readyState === 1) ws.send(JSON.stringify(m)); }, close: () => { closed = true; ws && ws.close(); } };
  }
  const newCode = () => { const a = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; let c = ''; for (let i = 0; i < 4; i++) c += a[Math.floor(Math.random() * a.length)]; return c; };
  return { fmt, fmtSigned, connect, newCode };
})();
