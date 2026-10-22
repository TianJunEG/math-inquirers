/* Child sign-in STUB: family code + display name + PIN, checked by the child_sign_in() database function.
   It only proves "this child knows the PIN" and stores the child's name/level in sessionStorage for the placeholder
   practice page. It is NOT a real session: nothing server-side is authorised by it. See portal/README.md. */
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
      var r = await M.sb().rpc('child_sign_in', { p_family_code: code.value, p_name: name.value, p_pin: pin.value });
      if (r.error) throw r.error;
      var row = r.data && r.data[0];
      if (!row) { pin.value = ''; M.notice(box, 'err', 'That did not work. Check the family code, your name and your PIN. Too many tries pauses sign-in for a little while.'); }
      else { try { sessionStorage.setItem('mi-child', JSON.stringify({ id: row.child_id, name: row.display_name, level: row.level })); } catch (e) {} location.href = '/portal/practice/'; }
    } catch (e) { M.notice(box, 'err', 'Something went wrong. Please try again.'); }
    btn.disabled = false;
  } },
    h('p', null, h('label', { for: 'code', text: 'Family code (from your grown-up)' }), code),
    h('p', null, h('label', { for: 'name', text: 'Your name' }), name),
    h('p', null, h('label', { for: 'pin', text: 'Your PIN' }), pin), btn);
  M.mount(app, h('section', { class: 'card pop' }, h('h1', { text: 'Hi! Sign in to practise' }), form, box,
    h('p', { class: 'small muted' }, 'Grown-up? ', h('a', { href: '/portal/', text: 'Parent portal' }))));
})();
