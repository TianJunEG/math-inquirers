/* Child sign-in: family code + name + PIN, checked by child_start_session() in the database. On success the database gives a short-lived (4 hours)
   random token for THIS child only; it is kept in sessionStorage ('mi-child', also read by the practice pages) and nothing else is stored.
   The same quiet message is shown whatever was wrong, so nobody can tell which part failed. */
(function () {
  var M = window.MI, h = M.h, app = document.getElementById('app');
  document.getElementById('top').appendChild(M.header('Child sign-in'));
  if (!M.configured()) { M.mount(app, h('section', { class: 'card pop' }, h('h1', { text: 'Not set up yet' }), h('p', { text: 'Ask a grown-up to finish setting up the portal.' }))); return; }
  var box = h('div'), code = h('input', { type: 'text', id: 'code', maxlength: 8, autocomplete: 'off', autocapitalize: 'characters', required: true }),
    name = h('input', { type: 'text', id: 'name', maxlength: 30, autocomplete: 'off', required: true }),
    pin = h('input', { type: 'password', id: 'pin', inputmode: 'numeric', pattern: '[0-9]*', maxlength: 6, autocomplete: 'off', required: true });
  var btn = h('button', { class: 'btn yel', type: 'submit', text: 'Sign in' });
  var form = h('form', { novalidate: true, onsubmit: async function (ev) {
    ev.preventDefault(); btn.disabled = true;
    try {
      var r = await M.sb().rpc('child_start_session', { p_family_code: code.value, p_name: name.value, p_pin: pin.value });
      if (r.error) throw r.error;
      var row = r.data && r.data[0];
      if (!row) { pin.value = ''; M.notice(box, 'err', 'That did not work. Check the family code, your name and your PIN. Too many tries pauses sign-in for a little while. If it keeps happening, ask your grown-up to check the agreements in the parent portal.'); }
      else {
        try { sessionStorage.setItem('mi-child', JSON.stringify({ id: row.child_id, name: row.display_name, level: row.level, token: row.token, expires_at: row.expires_at })); } catch (e) {}
        location.href = '/portal/practice/';
      }
    } catch (e) { M.notice(box, 'err', 'Something went wrong. Please try again.'); }
    btn.disabled = false;
  } },
    h('p', null, h('label', { for: 'code', text: 'Family code (from your grown-up)' }), code),
    h('p', null, h('label', { for: 'name', text: 'Your name' }), name),
    h('p', null, h('label', { for: 'pin', text: 'Your PIN' }), pin), btn);
  var ended = new URLSearchParams(location.search).get('ended');
  M.mount(app, h('section', { class: 'card pop' }, h('h1', { text: 'Hi! Sign in to practise' }),
    ended ? h('p', { class: 'msg info', id: 'ended-note', role: 'status', text: ended === 'bye' ? 'You are signed out. See you next time!' : 'Your sign-in has finished, which happens after a few hours. Please sign in again.' }) : null,
    form, box,
    h('p', { class: 'small muted', text: 'When you press Submit on a practice page, your answers are sent to your tutor at Math Inquirers so they can see what to help with.' }),
    h('p', { class: 'small muted' }, 'Grown-up? ', h('a', { href: '/portal/', text: 'Parent portal' }))));
})();
