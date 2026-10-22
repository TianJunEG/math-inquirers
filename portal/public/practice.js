/* PLACEHOLDER practice area. The real runner (practice/ in the repo) is not wired in yet. */
(function () {
  var M = window.MI, h = M.h, app = document.getElementById('app');
  document.getElementById('top').appendChild(M.header('Practice'));
  var c = null; try { c = JSON.parse(sessionStorage.getItem('mi-child') || 'null'); } catch (e) {}
  if (!c) { location.replace('/portal/child/'); return; }
  M.mount(app, h('section', { class: 'card pop' },
    h('h1', { id: 'hello', text: 'Hello, ' + c.name + '!' }),
    h('p', { text: 'Your practice area is coming soon. Level ' + c.level + ' puzzles will appear here.' }),
    h('p', { class: 'small muted', text: 'Notice it. Test it. Explain why.' }),
    h('button', { class: 'btn alt', type: 'button', id: 'bye', text: 'Sign out', onclick: function () { try { sessionStorage.removeItem('mi-child'); } catch (e) {} location.href = '/portal/child/'; } })));
})();
