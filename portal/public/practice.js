/* The child's practice list. Asks the database (child_session_overview) what THIS child may open, using the 4-hour token from the sign-in page,
   and shows a link for exactly those units. If the token is missing or has ended, the child goes back to sign in. No scores, no timers. */
(function () {
  var M = window.MI, h = M.h, app = document.getElementById('app');
  document.getElementById('top').appendChild(M.header('Practice'));
  var c = null; try { c = JSON.parse(sessionStorage.getItem('mi-child') || 'null'); } catch (e) {}
  if (!c || !c.token) { location.replace('/portal/child/'); return; }
  if (!M.configured()) { location.replace('/portal/child/'); return; }
  function bye(why) { try { sessionStorage.removeItem('mi-child'); sessionStorage.removeItem('mi-child-seen'); } catch (e) {} location.href = '/portal/child/?ended=' + why; }
  /* Shared tablets: after 30 minutes with no touch, key press or click on this page the child is signed out (token revoked in the database, removed from this tab),
     so the next person does not land inside the previous child's session. The token also lives in sessionStorage only, so closing the tab or window clears it.
     (The database also refuses a token that has been idle for 60 minutes.) */
  var IDLE_MS = 30 * 60 * 1000, lastTouch = 0, leaving = false;
  function seenAt() { try { return Number(sessionStorage.getItem('mi-child-seen')) || 0; } catch (e) { return 0; } }
  function touch() { var n = Date.now(); if (n - lastTouch < 5000) return; lastTouch = n; try { sessionStorage.setItem('mi-child-seen', String(n)); } catch (e) {} }
  async function idleOut() {
    leaving = true;
    try { await M.sb().rpc('child_end_session', { p_token: c.token }); } catch (e) {}
    bye('idle');
  }
  function idleCheck() { var t = seenAt(); if (!leaving && t && Date.now() - t > IDLE_MS) { idleOut(); return true; } return leaving; }
  if (idleCheck()) return;   // coming back to this page after a long time away: sign out before showing anything
  ['click', 'keydown', 'pointerdown', 'touchstart', 'scroll'].forEach(function (ev) { document.addEventListener(ev, touch, true); });
  document.addEventListener('visibilitychange', function () { if (!document.hidden) idleCheck(); });
  setInterval(idleCheck, 30000);
  touch();
  async function signOut() { try { await M.sb().rpc('child_end_session', { p_token: c.token }); } catch (e) {} bye('bye'); }
  var GROUPS = [['holiday', 'Holiday lessons'], ['term', 'Term lessons'], ['extension', 'Extension book']];

  async function load() {
    var r;
    if (leaving) return;
    try { r = await M.sb().rpc('child_session_overview', { p_token: c.token }); } catch (e) { r = { error: e }; }
    if (r.error) return M.mount(app, h('section', { class: 'card pop' }, h('h1', { text: 'Hello, ' + c.name + '!' }), h('p', { class: 'msg err', role: 'alert', text: 'We could not load your practice list. Please check the internet and try again.' }),
      h('button', { class: 'btn', type: 'button', text: 'Try again', onclick: load })));
    var o = r.data;
    if (!o) return bye('expired');
    var units = o.units || [];
    var sections = GROUPS.map(function (g) {
      var list = units.filter(function (u) { return u.product === g[0]; });
      if (!list.length) return null;
      return h('section', { class: 'card', 'data-group': g[0] }, h('h2', { text: g[1] }),
        h('ul', { class: 'plain units' }, list.map(function (u) { return h('li', null, h('a', { class: 'btn alt unitlink', href: M.unitUrl(u), 'data-unit': u.unit_key, text: M.unitLabel(u) })); })));
    }).filter(Boolean);
    M.mount(app,
      h('section', { class: 'card pop' },
        h('div', { class: 'row' }, h('h1', { id: 'hello', text: 'Hello, ' + o.name + '!' }),
          h('button', { class: 'btn alt sm', type: 'button', id: 'bye', text: 'Sign out', onclick: signOut })),
        units.length ? h('p', { text: 'Pick a page to practise. You can skip a question and come back to it.' })
                     : h('p', { id: 'nothing-open', text: 'Nothing is open for you yet. Please ask your grown-up to look in the parent portal.' }),
        o.can_submit === false ? h('p', { class: 'msg info', id: 'no-send', text: 'Your grown-up has turned off sending answers, so your answers stay on this device.' }) : null,
        h('p', { class: 'small muted', text: 'Notice it. Test it. Explain why.' })),
      sections,
      h('p', { class: 'small muted', text: 'Using a shared tablet? Press Sign out when you are done. You are also signed out after 30 minutes without touching the screen.' }));
  }
  load();
})();
