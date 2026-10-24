/* "My children": per child, what they can open (enrolled levels, purchased extension books), links to the practice pages and a simple progress
   summary for the parent. No scores, no ranks, no streaks, no times: only what was done. All of it comes from database functions that check
   the parent (my_children_access / my_children_units / my_children_progress / practice_child_detail); this page only displays. */
(function () {
  var M = window.MI, h = M.h, P = M.P, app = document.getElementById('app'), S = P.state;
  document.getElementById('top').appendChild(M.header('My children'));
  var D = { access: [], units: [], progress: [], missing: false, open: {}, detail: {} }, flashMsg = null;
  function flash(kind, text) { flashMsg = text ? { kind: kind, text: text } : null; }
  function draw(nodes) { M.clear(app); [].concat(nodes).forEach(function (n) { if (n) app.appendChild(n); }); }
  async function run(fn, ok) { flash(null); try { await fn(); if (ok) flash('ok', ok); } catch (e) { flash('err', M.errText(e)); } await refresh(); }
  var by = function (list, id) { return list.filter(function (x) { return x.child_id === id; }); };

  async function refresh() {
    try {
      await P.load();
      D.missing = false;
      if (S.session) {
        var sb = M.sb(), res = await Promise.all([sb.rpc('my_children_access'), sb.rpc('my_children_units'), sb.rpc('my_children_progress')]);
        var bad = res.filter(function (x) { return x.error; })[0];
        if (bad) { if (P.isMissingSql(bad.error)) D.missing = true; else throw bad.error; }
        else { D.access = res[0].data || []; D.units = res[1].data || []; D.progress = res[2].data || []; }
      }
    } catch (e) { flash('err', M.errText(e)); }
    paint();
  }

  function entitlementLine(a) {
    if (a.kind === 'enrolled') return 'Holiday and term practice for Level ' + a.level + ' (your family has a confirmed place in a Level ' + a.level + ' group).';
    if (a.format === 'online') return 'Extension Workbook, Level ' + a.level + ': online practice.';
    if (a.format === 'both') return 'Extension Workbook, Level ' + a.level + ': printed workbook and online practice.';
    return 'Extension Workbook, Level ' + a.level + ': printed workbook only (we post it; online practice is not included).';
  }

  function progressRows(ch) {
    var rows = by(D.progress, ch.id);
    var box = h('div', { class: 'progress', 'data-progress-for': ch.id }, h('h4', { text: 'How it is going' }));
    if (!rows.length) {
      box.appendChild(h('p', { class: 'muted small', 'data-no-progress': '1', text: 'No answers have been sent yet. When ' + ch.display_name + ' presses Submit on a practice page, a short summary will show here.' }));
      return box;
    }
    box.appendChild(h('p', { class: 'small muted', text: 'This shows what ' + ch.display_name + ' has done, not a score. Every child learns at their own pace, and a skipped question is a fine choice.' }));
    rows.forEach(function (r) {
      var answered = Math.max(0, (r.n_auto || 0) - (r.n_skipped || 0));
      var bits = ['answered ' + answered + ' of ' + (r.n_auto || 0) + ' questions'];
      if (r.n_skipped) bits.push(r.n_skipped + ' left for later');
      if (r.n_self) bits.push(r.n_self + ' done on paper' + (r.n_self_got ? ' (' + r.n_self_got + ' ticked "I got it")' : ''));
      var key = ch.id + '|' + r.unit_key;
      var row = h('div', { class: 'unitrow', 'data-unit-progress': r.unit_key },
        h('strong', { text: M.unitLabel(r) }),
        h('div', { class: 'small', text: 'Last sent ' + M.dayText(r.last_received_at) + (r.tries > 1 ? ' (sent ' + r.tries + ' times)' : '') + ': ' + bits.join(', ') + '.' }),
        h('button', { class: 'linkbtn', type: 'button', 'data-detail': r.unit_key, 'aria-expanded': String(!!D.open[key]), text: D.open[key] ? 'Hide details' : 'Worth looking at together', onclick: function () { toggleDetail(ch, r, key); } }));
      if (D.open[key]) row.appendChild(detailBox(ch, key));
      box.appendChild(row);
    });
    return box;
  }
  async function toggleDetail(ch, r, key) {
    if (D.open[key]) { D.open[key] = false; return paint(); }
    D.open[key] = true; D.detail[key] = null; paint();
    try { D.detail[key] = await M.rpc('practice_child_detail', { p_child: ch.id, p_unit: r.unit_key }); } catch (e) { D.detail[key] = { error: M.errText(e) }; }
    paint();
  }
  function detailBox(ch, key) {
    var d = D.detail[key], box = h('div', { class: 'detail card', 'data-detail-box': key });
    if (d == null) return box.appendChild(h('p', { class: 'muted small', role: 'status', text: 'Loading...' })) && box;
    if (d.error) return box.appendChild(h('p', { class: 'msg err', role: 'alert', text: d.error })) && box;
    var look = {}, skipped = 0, paper = [];
    d.forEach(function (x) {
      if (x.mark === 'wrong' && x.misconception) { (look[x.skill || x.topic || 'Other'] = look[x.skill || x.topic || 'Other'] || []).push(x.misconception); }
      else if (x.mark === 'skipped') skipped++;
      else if (x.mark === 'self' && x.self_result) paper.push(x.self_result);
    });
    var skills = Object.keys(look);
    box.appendChild(h('h5', { text: 'Worth looking at together' }));
    if (!skills.length) box.appendChild(h('p', { class: 'small', text: 'Nothing stands out from this set. A good way to help is to ask ' + ch.display_name + ' to explain one answer out loud.' }));
    else {
      box.appendChild(h('ul', null, skills.map(function (k) { return h('li', null, h('b', { text: k }), h('ul', null, look[k].map(function (t) { return h('li', { text: t }); }))); })));
      box.appendChild(h('p', { class: 'small muted', text: 'A good way to help: ask your child to explain how they got one of these answers, and listen for the idea behind it. Please do not worry about the wrong answer itself.' }));
    }
    if (skipped) box.appendChild(h('p', { class: 'small', text: skipped + ' question' + (skipped === 1 ? ' was' : 's were') + ' left for later. That is fine; skipping is a good choice when something feels too hard right now.' }));
    if (paper.length) box.appendChild(h('p', { class: 'small', text: 'Checked on paper: ' + paper.map(function (x) { return x === 'got' ? 'I got it' : x === 'not_yet' ? 'not yet' : 'checked'; }).join(', ') + '. These are not counted as marked questions.' }));
    return box;
  }

  function childCard(ch) {
    var acc = by(D.access, ch.id), units = by(D.units, ch.id);
    var c = h('section', { class: 'card child-card', 'data-child-card': ch.id },
      h('div', { class: 'row' }, h('h2', { text: ch.display_name }), h('span', { class: 'pill', text: 'Level ' + ch.level }), ch.birth_year ? h('span', { class: 'small muted', text: 'born ' + ch.birth_year }) : null));
    c.appendChild(h('h3', { text: 'What ' + ch.display_name + ' can open' }));
    if (!acc.length) {
      c.appendChild(h('p', { class: 'muted', 'data-nothing-open': '1' }, 'Nothing is open yet. You can ', h('a', { href: '/portal/books/?child=' + ch.id, text: 'buy an extension book' }), ' for ' + ch.display_name + ', or join a live group from the ', h('a', { href: '/portal/#choose-group', text: 'home page' }), '.'));
    } else {
      c.appendChild(h('ul', { class: 'plain access' }, acc.map(function (a) { return h('li', { 'data-access': a.kind + '-' + a.level + (a.format ? '-' + a.format : '') }, entitlementLine(a)); })));
    }
    if (units.length) {
      c.appendChild(h('h3', { text: 'Practice pages' }));
      c.appendChild(h('p', { class: 'small muted', text: ch.display_name + ' signs in first (family code, name and PIN) so the answers can be sent to us. Without signing in, the pages still work but nothing is sent.' }));
      c.appendChild(h('ul', { class: 'plain units' }, units.map(function (u) {
        return h('li', null, h('a', { href: M.unitUrl(u), 'data-unit': u.unit_key, text: M.unitLabel(u) }));
      })));
    } else if (acc.some(function (a) { return a.kind === 'enrolled' || a.format === 'online' || a.format === 'both'; })) {
      c.appendChild(h('p', { class: 'small muted', 'data-no-units': '1', text: 'Practice pages are added week by week. None is ready for this level yet; we will tell you when they are.' }));
    }
    c.appendChild(progressRows(ch));
    c.appendChild(h('div', { class: 'row' },
      h('a', { class: 'btn sm', href: '/portal/child/', text: 'Open the child sign-in page' }),
      h('a', { class: 'btn alt sm', href: '/portal/books/?child=' + ch.id, text: 'Buy a book for ' + ch.display_name }),
      by(D.progress, ch.id).length ? h('button', { class: 'btn alt sm', type: 'button', 'data-delete-practice': ch.id, text: 'Delete practice answers', onclick: function () {
        if (confirm('Delete every practice answer we hold for ' + ch.display_name + '? The account and the access stay.')) run(function () { return M.rpc('delete_child_practice', { p_child: ch.id }); }, 'Practice answers deleted.'); } }) : null));
    if (by(D.progress, ch.id).length) {
      c.appendChild(h('details', { class: 'nextstep' }, h('summary', { text: 'For grown-ups: a possible next step' }),
        h('p', { class: 'small', text: 'If you would like to talk about a small group class, you can ask for a trial class whenever you like. There is no deadline and no obligation, and it does not change what ' + ch.display_name + ' sees on the practice pages.' }),
        h('a', { class: 'btn alt sm', href: '/portal/trial/?from=report&child=' + ch.id, text: 'Ask about a trial class' })));
    }
    return c;
  }

  function paint() {
    if (!M.configured()) return draw(P.notReady());
    var fb = h('div'); if (flashMsg) M.notice(fb, flashMsg.kind, flashMsg.text);
    if (!S.session) return draw([fb, P.signedOut()]);
    if (!S.parent) return draw([fb, h('section', { class: 'card' }, h('p', { text: 'We could not load your account. Please reload the page.' }))]);
    if (D.missing) return draw([P.nav('children'), P.missingSql()]);
    var out = [fb, h('div', { class: 'row' }, h('h1', { text: 'My children' }), P.signOutButton(function () { flash(null); refresh(); })), P.nav('children')];
    if (!S.children.length) {
      out.push(h('section', { class: 'card pop', id: 'first-child' }, h('h2', { text: 'Add your first child' }),
        h('p', { class: 'muted', text: 'You do not need to join a class. A child profile is what lets a book or a class be set up for the right child.' }),
        P.childForm({ run: run, title: 'Your child', submitText: 'Add my child' })));
    } else {
      S.children.forEach(function (ch) { out.push(childCard(ch)); });
      out.push(h('details', { class: 'card', id: 'add-another' }, h('summary', { text: 'Add another child' }), P.childForm({ run: run, title: 'Another child' })));
      out.push(h('p', { class: 'small muted' }, 'To change a name, level or PIN, go to ', h('a', { href: '/portal/#my-children', text: 'the home page' }), '. Child sign-in family code: ', h('span', { class: 'code', id: 'family-code', text: S.parent.family_code })));
    }
    draw(out);
    M.stack(app);
  }

  if (!M.configured()) return paint();
  M.sb().auth.onAuthStateChange(function (ev) { if (ev === 'SIGNED_OUT') refresh(); });
  refresh();
})();
