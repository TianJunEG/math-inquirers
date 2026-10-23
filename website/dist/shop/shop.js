/* /shop/ page behaviour: add-to-list buttons on the product cards, the "Your list" panel, and the "Tell me when it's ready" interest form.
   Expects window.MI_SHOP (embedded by shop_build.py: products, wa, waShow, consent, checkoutEnabled) and window.MiCart (cart.js).
   Prices: only products that carry `prices` are priced, and shop_build.py only emits `prices` when status is 'available' AND a price is set.
   Two submit modes, chosen at load (same as the "Request another time" form, interest.js):
   - portal: window.MI_CONFIG (/portal/config.js, only in a --with-portal build with real Supabase values) holds a Supabase URL + anon key (public by
     design). The request goes to the SECURITY DEFINER function submit_product_interest via PostgREST. No key is hard-coded here.
   - WhatsApp: otherwise (or if the call fails), a prefilled WhatsApp message to the business number is built for the parent to send. */
(function () {
  var S = window.MI_SHOP, C = window.MiCart;
  if (!S || !C) return;
  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  var P = {}; S.products.forEach(function (p) { P[p.id] = p; });
  var FMT = { soft: "Soft copy", physical: "Physical copy" };
  var MC = window.MI_CONFIG || {};
  var SB = /^https:\/\/[a-z0-9-]+\.supabase\.co$/.test(MC.SUPABASE_URL || "") && MC.ANON_KEY && MC.ANON_KEY !== "ANON_KEY" ? { url: MC.SUPABASE_URL, key: MC.ANON_KEY } : null;

  function money(c) { return "S$" + (c % 100 ? (c / 100).toFixed(2) : String(c / 100)); }
  function priceOf(p, f) { return p.status === "available" && p.prices && p.prices[f] > 0 ? p.prices[f] : null; }
  function lines() {   // cart lines that still match a product on the page
    return C.load().filter(function (x) { return P[x.p] && P[x.p].formats.indexOf(x.f) >= 0; }).map(function (x) { return { p: P[x.p], f: x.f, q: x.q }; });
  }
  function isReady(l) { return l.p.status === "available" && priceOf(l.p, l.f) !== null; }
  function label(l) { return l.p.name + " (ages " + l.p.ages + "): " + FMT[l.f].toLowerCase() + (l.f === "physical" && l.q > 1 ? " x" + l.q : ""); }

  /* ---- product cards ---- */
  function drawCards() {
    each(document.querySelectorAll(".addbtn"), function (b) {
      var p = P[b.dataset.add]; if (!p) return;
      var on = C.has(p.id, b.dataset.format), ready = p.status === "available";
      b.hidden = false; b.setAttribute("aria-pressed", on ? "true" : "false");
      b.textContent = on ? (ready ? "In your cart: remove" : "On your list: remove") : (ready ? "Add to cart" : "Add to your list");
      b.setAttribute("aria-label", (on ? "Remove " : "Add ") + p.name + ", " + FMT[b.dataset.format].toLowerCase() + (on ? " from" : " to") + (ready ? " your cart" : " your list"));
    });
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".addbtn"); if (!b) return;
    if (C.has(b.dataset.add, b.dataset.format)) C.remove(b.dataset.add, b.dataset.format); else C.add(b.dataset.add, b.dataset.format);
  });

  /* ---- the list ---- */
  function lineHtml(l) {
    var pr = priceOf(l.p, l.f), key = l.p.id + "|" + l.f;
    var qty = l.f === "physical" ? '<span class="qty" role="group" aria-label="Quantity for ' + esc(l.p.name) + ', physical copy"><button type="button" data-qty="-1" aria-label="One fewer"' + (l.q <= 1 ? " disabled" : "") + '>&minus;</button><output aria-live="polite">' + l.q + '</output><button type="button" data-qty="1" aria-label="One more"' + (l.q >= C.MAX_QTY ? " disabled" : "") + '>+</button></span>' : "";
    return '<li class="lline" data-line="' + esc(key) + '" data-p="' + esc(l.p.id) + '" data-f="' + l.f + '"><div class="lname"><b>' + esc(l.p.name) + '</b><br><span class="small muted">' + FMT[l.f] + (pr ? " · " + money(pr * l.q) : "") + '</span></div>' +
      '<div class="lact">' + qty + '<button type="button" class="linkbtn2" data-remove aria-label="Remove ' + esc(l.p.name) + ', ' + FMT[l.f].toLowerCase() + ', from your list">Remove</button></div></li>';
  }
  function drawList() {
    var ls = lines(), ready = ls.filter(isReady), soon = ls.filter(function (l) { return !isReady(l); }), h = "";
    if (!ls.length) h = '<p class="muted small" id="listEmpty">Nothing on your list yet. Tap <b>Add to your list</b> on a workbook.</p>';
    if (soon.length) h += '<h3>Coming soon: we will tell you when ready</h3><ul id="soonList">' + soon.map(lineHtml).join("") + '</ul>';
    if (ready.length) {
      h += '<h3>Ready to order</h3><ul id="readyList">' + ready.map(lineHtml).join("") + '</ul>';
      var tot = ready.reduce(function (n, l) { return n + priceOf(l.p, l.f) * l.q; }, 0);
      h += '<div class="total"><span>Total</span><span id="listTotal">' + money(tot) + '</span></div>';
    }
    $("listBody").innerHTML = h;
    $("notifyBtn").hidden = !soon.length;
    $("checkoutBtn").hidden = !ready.length;                       /* hidden while no product is available */
    $("checkoutBtn").disabled = !(ready.length && S.checkoutEnabled);
    var n = C.count(), bar = $("listBar"); $("listBarN").textContent = String(n); bar.classList.toggle("on", n > 0);
    drawCards(); drawItems();
  }
  $("listBody").addEventListener("click", function (e) {
    var li = e.target.closest && e.target.closest("[data-line]"); if (!li) return;
    var q = e.target.closest("[data-qty]");
    if (q) { var cur = C.load().filter(function (x) { return x.p === li.dataset.p && x.f === li.dataset.f; })[0]; if (cur) C.setQty(li.dataset.p, li.dataset.f, cur.q + parseInt(q.dataset.qty, 10)); return; }
    if (e.target.closest("[data-remove]")) C.remove(li.dataset.p, li.dataset.f);
  });
  C.onChange(drawList);

  /* ---- checkout button (stub: see checkout.js) ---- */
  $("checkoutBtn").addEventListener("click", function () {
    var order = { items: lines().filter(isReady).map(function (l) { return { product: l.p.id, format: l.f, qty: l.q }; }) };
    if (!window.MiCheckout) return;
    window.MiCheckout.start(order).catch(function (err) {
      $("listMsg").innerHTML = '<div class="msg info">' + (err && err.error === "not_enabled" ? "Checkout is not open yet." : "We could not start checkout. Please try again.") + "</div>";
    });
  });

  /* ---- interest form ---- */
  var form = $("nfForm"), unticked = {};
  $("nfModeNote").textContent = SB ? "Your request is stored securely and used only to tell you when these products are ready." : "Sending opens WhatsApp with your message written out, so you can check it before you send it to " + S.waShow + ".";
  function soonLines() { return lines().filter(function (l) { return !isReady(l); }); }
  function drawItems() {
    each(form.querySelectorAll('#nfItems input'), function (c) { unticked[c.value] = !c.checked; });
    var ls = soonLines();
    $("nfItems").innerHTML = ls.length ? ls.map(function (l) {
      var k = l.p.id + "|" + l.f;
      return '<label><input type="checkbox" name="nfitem" value="' + esc(k) + '"' + (unticked[k] ? "" : " checked") + '><span>' + esc(label(l)) + "</span></label>";
    }).join("") : '<p class="muted small">Your list is empty. Add a workbook from the cards above.</p>';
  }
  function openForm() {
    var n = $("notify"); n.hidden = false; drawItems();
    try { n.scrollIntoView({ behavior: "smooth" }); } catch (e) { n.scrollIntoView(); }
    setTimeout(function () { try { $("nfName").focus({ preventScroll: true }); } catch (e) {} }, 350);
  }
  $("notifyBtn").addEventListener("click", openForm);
  function checkedLines() {
    var keys = Array.prototype.map.call(form.querySelectorAll('input[name="nfitem"]:checked'), function (c) { return c.value; });
    return soonLines().filter(function (l) { return keys.indexOf(l.p.id + "|" + l.f) >= 0; });
  }
  function fieldErr(id, text) { var el = $(id); el.setAttribute("aria-invalid", "true"); var p = el.parentNode, m = p.querySelector(".err"); if (!m) { m = document.createElement("span"); m.className = "err"; m.setAttribute("role", "alert"); p.appendChild(m); } m.textContent = text; }
  function clearErrs() { each(form.querySelectorAll(".err"), function (n) { n.parentNode.removeChild(n); }); each(form.querySelectorAll("[aria-invalid]"), function (n) { n.removeAttribute("aria-invalid"); }); }
  function digits(s) { return String(s).replace(/\D/g, ""); }
  function normWa(s) { var d = digits(s); if (d.length === 10 && d.slice(0, 2) === "65") d = d.slice(2); return d; }
  function valid() {
    clearErrs(); var bad = [];
    var v = { items: checkedLines(), name: $("nfName").value.trim().replace(/\s+/g, " "), note: $("nfNote").value.trim(), wa: $("nfWa").value.trim(), email: $("nfEmail").value.trim() };
    if (!v.items.length) bad.push(["nfItems", "Tick at least one workbook from your list."]);
    if (!v.name) bad.push(["nfName", "Please add your first name."]);
    var wd = normWa(v.wa);
    if (v.wa && !/^\d{8,15}$/.test(wd)) bad.push(["nfWa", "Enter a WhatsApp number with 8 or more digits."]);
    if (v.email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v.email)) bad.push(["nfEmail", "That email does not look right."]);
    if (!v.wa && !v.email) bad.push(["nfWa", "Give a WhatsApp number or an email."]);
    if (!$("nfConsent").checked) bad.push(["nfConsent", "Please tick the box so we may use your details to tell you when it is ready."]);
    bad.forEach(function (b) {
      if (b[0] === "nfItems") { var el = $("nfItems"), m = el.parentNode.querySelector(".err"); if (!m) { m = document.createElement("span"); m.className = "err"; m.setAttribute("role", "alert"); el.parentNode.appendChild(m); } m.textContent = b[1]; } else fieldErr(b[0], b[1]);
    });
    if (bad.length) { $("nfMsg").innerHTML = '<div class="msg no">Please fix the ' + bad.length + " item" + (bad.length > 1 ? "s" : "") + " marked in red.</div>"; try { var f = $(bad[0][0]); (f.focus ? f : form.querySelector("input")).focus(); } catch (x) {} return null; }
    v.wd = v.wa ? wd : ""; return v;
  }
  function message(v) {
    return "Hi! Please tell me when these Math Inquirers products are ready:\n\n" + v.items.map(function (l) { return "- " + label(l); }).join("\n") +
      "\n\nParent: " + v.name + "\nContact: " + [v.wa ? "WhatsApp " + v.wa : "", v.email ? "email " + v.email : ""].filter(Boolean).join(", ") + (v.note ? "\nNote: " + v.note : "") +
      "\nI agree you may use these details only to tell me when these products are ready (kept for 12 months, then deleted). This is not an order.";
  }
  function waOut(v, intro) {
    var msg = message(v), url = "https://wa.me/" + S.wa + "?text=" + encodeURIComponent(msg);
    $("nfMsg").innerHTML = '<div class="waout"><div class="msg ok">' + esc(intro) + '</div><pre id="nfPre">' + esc(msg) + '</pre><div class="row"><a class="btn teal" id="nfWaLink" href="' + url + '" target="_blank" rel="noopener">Open WhatsApp</a><button class="btn alt sm" type="button" id="nfCopy">Copy message</button></div><p class="small muted">If WhatsApp does not open, copy the message and send it to ' + esc(S.waShow) + ". Nothing is reserved or charged by sending it.</p></div>";
    $("nfCopy").addEventListener("click", function () { var b = this; if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(msg).then(function () { b.textContent = "Copied"; }, function () { b.textContent = "Select the text above to copy"; }); else b.textContent = "Select the text above to copy"; });
  }
  var KEY = "mi_shop_interest_last";
  function recentlySent() { try { var t = parseInt(localStorage.getItem(KEY), 10); return t && Date.now() - t < 60000; } catch (e) { return false; } }
  function markSent() { try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {} }
  function done(status, v) {
    $("nfMsg").innerHTML = '<div class="msg ok" role="status">' + (status === "already_received" ? "Thank you. We already have a request from this contact today, so we have kept that one." : "Thank you. We have your request.") + " We will message you when the workbooks are ready. This is not an order: nothing is reserved or charged. We have taken them off your list.</div>";
    form.reset(); unticked = {}; C.removeMany(v.items.map(function (l) { return { p: l.p.id, f: l.f }; }));
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if ($("nfHp").value) return;                                   /* honeypot: a person never sees this field */
    var v = valid(); if (!v) return;
    if (recentlySent()) { $("nfMsg").innerHTML = '<div class="msg info">You just sent a request. Please wait a minute before sending another.</div>'; return; }
    if (!SB) { markSent(); waOut(v, "Almost done. Tap the button to send this on WhatsApp."); return; }
    var btn = $("nfSubmit"); btn.disabled = true; btn.textContent = "Sending…";
    var body = { p_first_name: v.name, p_whatsapp: v.wd || null, p_email: v.email || null,
      p_items: v.items.map(function (l) { return { product: l.p.id, format: l.f, qty: l.f === "physical" ? l.q : 1 }; }),
      p_note: v.note || null, p_consent: true, p_consent_version: S.consent, p_hp: $("nfHp").value || null };
    function reset() { btn.disabled = false; btn.textContent = "Tell me when it's ready"; }
    fetch(SB.url + "/rest/v1/rpc/submit_product_interest", { method: "POST", headers: { "Content-Type": "application/json", apikey: SB.key, Authorization: "Bearer " + SB.key }, body: JSON.stringify(body) })
      .then(function (r) { return r.json().catch(function () { return null; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (x) {
        reset();
        if (x.ok && x.j && x.j.ok) { markSent(); done(x.j.status, v); return; }
        var m = x.j && x.j.message;
        if (m === "invalid_input" || m === "consent_required") { $("nfMsg").innerHTML = '<div class="msg no">Some details were not accepted. Please check the form and try again.</div>'; return; }
        waOut(v, "We could not save your request here. You can send it to us on WhatsApp instead.");
      }, function () { reset(); waOut(v, "We could not reach our server. You can send your request on WhatsApp instead."); });
  });

  drawList();
  if (location.hash === "#notify" && soonLines().length) openForm();
})();
