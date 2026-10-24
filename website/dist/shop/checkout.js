/* Checkout hand-off: STUB INTERFACE ONLY. No payment is taken or implemented in this file.

   The shop cart ("Your list", cart.js) goes to checkout only for products that are status "available" AND have a price in
   website/data/products.json. While no product is available the Checkout button on /shop/ stays hidden and disabled.

   The payment code (Stripe, written by the payments work, see portal/README.md) must serve this endpoint on the same origin:

     POST /api/shop/checkout          Content-Type: application/json
     Request body:
       {
         "items":    [ { "product": "ext-l1", "format": "soft" | "physical", "qty": 1 } ],   // ids only, NEVER prices
         "contact":  { "email": "parent@example.com", "name": "Mei" },     // email is required whenever the order has a soft copy (download link goes there)
         "shipping": { "name": "Mei Tan", "line1": "Blk 1 Some Street #01-01", "postal_code": "123456", "phone": "91234567" },
                                                                            // required whenever the order has a physical copy; Singapore addresses only (6-digit postal code)
         "consent":  { "terms_version": "...", "privacy_version": "..." },  // same versions the registration form records
         "hp":       ""                                                     // honeypot, must be empty
       }
     The server MUST re-read the catalogue itself (products.json as deployed), reject any product that is not status "available" with a
     price, compute the total itself, and create the Stripe-hosted Checkout Session. A price sent by the browser is never trusted.
     Success (200):  { "ok": true, "url": "https://checkout.stripe.com/..." }      the browser then navigates to url (top-level navigation, so no CSP change)
     Failure (4xx):  { "ok": false, "error": "invalid_input" | "not_available" | "email_required" | "address_required" | "busy" }
     Not switched on (501): { "ok": false, "error": "not_enabled" }

   Turning checkout on later (owner/dev), see docs/shop/README.md:  1. set status "available" and a price on a product,
   2. deploy the /api/shop/checkout Pages Function, 3. set window.MI_SHOP.checkoutEnabled = true (build flag), 4. add the details form that calls
   MiCheckout.start(order) with the fields above. MiCheckout.validate(order) is already here so the form and the tests share the rules. */
(function () {
  var ENDPOINT = "/api/shop/checkout";

  /* Returns [] when the order is complete, else a list of {field, message}. */
  function validate(order) {
    var bad = [], items = (order && order.items) || [], c = (order && order.contact) || {}, s = (order && order.shipping) || {};
    if (!items.length) bad.push({ field: "items", message: "Add something to your order first." });
    var soft = items.some(function (x) { return x.format === "soft"; }), phys = items.some(function (x) { return x.format === "physical"; });
    if (soft && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(String(c.email || "").trim())) bad.push({ field: "email", message: "Soft copies are sent by email: enter your email address." });
    if (phys) {
      if (!String(s.name || "").trim()) bad.push({ field: "ship_name", message: "Enter the name for the parcel." });
      if (!String(s.line1 || "").trim()) bad.push({ field: "ship_line1", message: "Enter a delivery address in Singapore." });
      if (!/^\d{6}$/.test(String(s.postal_code || "").replace(/\s/g, ""))) bad.push({ field: "ship_postal", message: "Enter the 6-digit Singapore postal code." });
    }
    return bad;
  }

  /* Starts checkout. Resolves with {url} (and navigates there when opts.navigate !== false); rejects with {error: "..."}. */
  function start(order, opts) {
    var enabled = !!(window.MI_SHOP && window.MI_SHOP.checkoutEnabled);
    if (!enabled) return Promise.reject({ error: "not_enabled" });
    var bad = validate(order); if (bad.length) return Promise.reject({ error: "invalid_input", fields: bad });
    return fetch(ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(order) })
      .then(function (r) { return r.json().catch(function () { return null; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (x) {
        if (x.ok && x.j && x.j.ok && /^https:\/\//.test(x.j.url || "")) { if (!opts || opts.navigate !== false) location.href = x.j.url; return { url: x.j.url }; }
        return Promise.reject({ error: (x.j && x.j.error) || "failed" });
      });
  }
  window.MiCheckout = { start: start, validate: validate, ENDPOINT: ENDPOINT };
})();
