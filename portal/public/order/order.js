// Order success page: /portal/order/?session_id=cs_...  (Stripe's success_url adds the session id).
// Asks /api/order-links for the download links of this checkout session. The webhook may take a few seconds, so it polls (every 3 s, up to 90 s).
(function () {
  var sid = new URLSearchParams(location.search).get('session_id') || '';
  var statusEl = document.getElementById('status'), list = document.getElementById('links');
  var note = document.getElementById('note'), help = document.getElementById('help');
  var tries = 0;
  function say(t) { statusEl.textContent = t; }
  function fmt(iso) { try { return new Intl.DateTimeFormat('en-SG', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Singapore' }).format(new Date(iso)); } catch (e) { return ''; } }
  function render(d) {
    say('Order ' + d.order_id + '. Your downloads are ready.');
    list.textContent = '';
    d.links.forEach(function (l) {
      var li = document.createElement('li');
      if (l.url && !l.revoked) {
        var a = document.createElement('a'); a.href = l.url; a.textContent = 'Download ' + l.name; a.rel = 'noopener noreferrer'; li.appendChild(a);
        li.appendChild(document.createTextNode(' (valid until ' + fmt(l.expires_at) + ', ' + l.remaining + ' download' + (l.remaining === 1 ? '' : 's') + ' left)'));
      } else li.textContent = l.name + ' (this link has been withdrawn, please message us)';
      list.appendChild(li);
    });
    note.hidden = false; help.hidden = false;
  }
  function poll() {
    tries++;
    fetch('/api/order-links?session_id=' + encodeURIComponent(sid), { cache: 'no-store', credentials: 'omit' }).then(function (r) {
      return r.json().then(function (d) { return { s: r.status, d: d }; });
    }).then(function (x) {
      if (x.s === 200 && x.d.status === 'ready') return render(x.d);
      if (x.s === 202 && tries < 30) { say('Confirming your payment... this can take a few seconds.'); return setTimeout(poll, 3000); }
      if (x.s === 202) { say('Your payment is still being confirmed. Please check your email in a few minutes, or message us on WhatsApp with your order number.'); help.hidden = false; return; }
      if (x.s === 429) { say('Too many tries. Please wait a few minutes and reload this page.'); return; }
      say('We could not load your links. Please check your email, or message us on WhatsApp with your order number.'); help.hidden = false;
    }).catch(function () { say('We could not load your links. Please reload, or message us on WhatsApp.'); help.hidden = false; });
  }
  if (!/^cs_(test|live)_[A-Za-z0-9]+$/.test(sid)) { say('This page needs the link from your payment confirmation. If you paid, check your email or message us on WhatsApp.'); help.hidden = false; return; }
  poll();
})();
