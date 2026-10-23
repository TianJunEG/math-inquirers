// Order success page: /portal/order/?session_id=cs_...  (Stripe's success_url adds the session id).
// Asks /api/order-links for the download links of this checkout session. The webhook may take a few seconds, so it polls (every 3 s, up to 90 s).
(function () {
  var sid = new URLSearchParams(location.search).get('session_id') || '';
  var statusEl = document.getElementById('status'), list = document.getElementById('links');
  var note = document.getElementById('note'), help = document.getElementById('help');
  var tries = 0;
  function say(t) { statusEl.textContent = t; statusEl.className = 'msg info'; }
  function fmt(iso) { try { return new Intl.DateTimeFormat('en-SG', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Singapore' }).format(new Date(iso)); } catch (e) { return ''; } }
  function wa(order) { var u = 'https://wa.me/6598805962'; if (order) u += '?text=' + encodeURIComponent('Hi, I need help with my download. Order number: ' + order); document.getElementById('wa').href = u; }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text) e.textContent = text; return e; }
  function render(d) {
    say('Order ' + d.order_id + '. Your downloads are ready.');
    statusEl.className = 'msg ok';
    list.textContent = '';
    d.links.forEach(function (l) {
      var li = el('li', 'dl'), exp = l.expires_at ? new Date(l.expires_at) : null;
      var gone = l.revoked || !l.url || l.remaining <= 0 || (exp && exp.getTime() < Date.now());
      if (!gone) {
        var a = el('a', 'btn', 'Download ' + l.name); a.href = l.url; a.rel = 'noopener noreferrer'; li.appendChild(a);
        li.appendChild(el('span', 'meta', 'Link works until ' + fmt(l.expires_at) + '. ' + l.remaining + ' download' + (l.remaining === 1 ? '' : 's') + ' left.'));
      } else {
        li.className = 'dl gone';
        li.appendChild(el('strong', '', l.name));
        li.appendChild(el('span', 'meta', l.revoked ? 'This link has been withdrawn. Message us on WhatsApp (below) and we will help.' : 'This link has expired or has no downloads left. Message us on WhatsApp (below) and we will send a fresh one.'));
      }
      list.appendChild(li);
    });
    wa(d.order_id); note.hidden = false; help.hidden = false;
  }
  function poll() {
    tries++;
    fetch('/api/order-links?session_id=' + encodeURIComponent(sid), { cache: 'no-store', credentials: 'omit' }).then(function (r) {
      return r.json().then(function (d) { return { s: r.status, d: d }; });
    }).then(function (x) {
      if (x.s === 200 && x.d.status === 'ready') return render(x.d);
      if (x.s === 202 && tries < 30) { say('Confirming your payment... this can take a few seconds.'); return setTimeout(poll, 3000); }
      if (x.s === 202) { say('Your payment is still being confirmed. Please check your email in a few minutes, or message us on WhatsApp with your order number.'); help.hidden = false; return; }
      if (x.s === 429) { say('Too many tries. Please wait a few minutes and reload this page.'); statusEl.className = 'msg err'; help.hidden = false; return; }
      say('We could not load your links. Please check your email, or message us on WhatsApp with your order number.'); help.hidden = false;
    }).catch(function () { say('We could not load your links. Please reload, or message us on WhatsApp.'); help.hidden = false; });
  }
  if (!/^cs_(test|live)_[A-Za-z0-9]+$/.test(sid)) { say('This page needs the link from your payment confirmation. If you paid, check your email or message us on WhatsApp.'); help.hidden = false; return; }
  poll();
})();
