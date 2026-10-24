/* The child's practice list. Asks the database (child_session_overview) what THIS child may open, using the 4-hour token from the sign-in page,
   and shows a link for exactly those units. If the token is missing or has ended, the child goes back to sign in. No scores, no timers. */
(function () {
  var M = window.MI, h = M.h, app = document.getElementById('app');
  document.getElementById('top').appendChild(M.header('Practice'));
  var c = null; try { c = JSON.parse(sessionStorage.getItem('mi-child') || 'null'); } catch (e) {}
  if (!c || !c.token) { location.replace('/portal/child/'); return; }
  if (!M.configured()) { location.replace('/portal/child/'); return; }
  function bye(why) { try { sessionStorage.removeItem('mi-child'); } catch (e) {} location.href = '/portal/child/?ended=' + why; }
  var GROUPS = [['holiday', 'Holiday lessons'], ['term', 'Term lessons'], ['extension', 'Extension book']];

  async function load() {
    var r;
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
        h('h1', { id: 'hello', text: 'Hello, ' + o.name + '!' }),
        units.length ? h('p', { text: 'Pick a page to practise. You can skip a question and come back to it.' })
                     : h('p', { id: 'nothing-open', text: 'Nothing is open for you yet. Please ask your grown-up to look in the parent portal.' }),
        o.can_submit === false ? h('p', { class: 'msg info', id: 'no-send', text: 'Your grown-up has turned off sending answers, so your answers stay on this device.' }) : null,
        h('p', { class: 'small muted', text: 'Notice it. Test it. Explain why.' })),
      sections,
      h('p', null, h('button', { class: 'btn alt', type: 'button', id: 'bye', text: 'Sign out', onclick: async function () {
        try { await M.sb().rpc('child_end_session', { p_token: c.token }); } catch (e) {}
        bye('bye'); } })));
  }
  load();
})();
