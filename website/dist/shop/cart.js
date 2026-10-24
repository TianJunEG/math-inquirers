/* Math Inquirers shop cart ("Your list"). Loaded on every page (defer) so the Shop link in the nav can show how many items are on the list,
   and by the shop page, which draws the list and the notify/checkout buttons (shop.js).

   Storage: localStorage key "mi_cart_v1" = {"v":1,"items":[{"p":"ext-l1","f":"soft","q":1}, ...]}
     p = product id (products.json), f = "soft" | "physical", q = quantity (soft copy is always 1; physical 1 to MAX_QTY).
   Every localStorage read and write is wrapped in try/catch: a blocked or full store falls back to an in-memory cart for this page view.
   No personal data is ever stored here: only product ids, formats and quantities.

   API (window.MiCart):
     load() -> items            save(items)           add(p, f) -> items     remove(p, f) -> items
     setQty(p, f, q) -> items   has(p, f) -> bool     count() -> number      clear() -> items
     removeMany([{p,f}]) -> items     onChange(fn)   (also fires when another tab changes the list)
*/
(function () {
  var KEY = "mi_cart_v1", MAX_QTY = 10, MAX_LINES = 12, FORMATS = ["soft", "physical"];
  var mem = null, subs = [];

  function clean(list) {
    var out = [], seen = {};
    (Array.isArray(list) ? list : []).forEach(function (x) {
      if (!x || typeof x.p !== "string" || !/^[a-z0-9-]{1,24}$/.test(x.p) || FORMATS.indexOf(x.f) < 0) return;
      var k = x.p + "|" + x.f; if (seen[k] || out.length >= MAX_LINES) return; seen[k] = 1;
      var q = x.f === "soft" ? 1 : Math.max(1, Math.min(MAX_QTY, parseInt(x.q, 10) || 1));
      out.push({ p: x.p, f: x.f, q: q });
    });
    return out;
  }
  function load() {
    try {
      var raw = localStorage.getItem(KEY);
      if (raw === null) return mem ? clean(mem) : [];
      var d = JSON.parse(raw); mem = null;
      return clean(d && d.v === 1 ? d.items : []);
    } catch (e) { return mem ? clean(mem) : []; }
  }
  function save(items) {
    items = clean(items);
    try { localStorage.setItem(KEY, JSON.stringify({ v: 1, items: items })); mem = null; } catch (e) { mem = items; }
    changed(items); return items;
  }
  function find(items, p, f) { for (var i = 0; i < items.length; i++) if (items[i].p === p && items[i].f === f) return i; return -1; }
  function add(p, f) { var it = load(); if (find(it, p, f) < 0) it.push({ p: p, f: f, q: 1 }); return save(it); }
  function remove(p, f) { var it = load(), i = find(it, p, f); if (i >= 0) it.splice(i, 1); return save(it); }
  function removeMany(list) { var it = load(); (list || []).forEach(function (x) { var i = find(it, x.p, x.f); if (i >= 0) it.splice(i, 1); }); return save(it); }
  function setQty(p, f, q) { var it = load(), i = find(it, p, f); if (i >= 0) { it[i].q = parseInt(q, 10) || 1; } return save(it); }
  function has(p, f) { return find(load(), p, f) >= 0; }
  function count() { return load().reduce(function (n, x) { return n + x.q; }, 0); }
  function clear() { return save([]); }
  function onChange(fn) { subs.push(fn); }
  function changed(items) { badge(); subs.forEach(function (fn) { try { fn(items); } catch (e) {} }); }

  function badge() {
    var n = count();
    Array.prototype.forEach.call(document.querySelectorAll("[data-cartn]"), function (el) {
      el.textContent = String(n); el.hidden = !n;
      var a = el.closest && el.closest("a");
      if (a) a.setAttribute("aria-label", n ? "Shop, " + n + (n === 1 ? " item" : " items") + " on your list" : "Shop");
    });
  }
  window.MiCart = { load: load, save: save, add: add, remove: remove, removeMany: removeMany, setQty: setQty, has: has, count: count, clear: clear, onChange: onChange, MAX_QTY: MAX_QTY, KEY: KEY };
  window.addEventListener("storage", function (e) { if (e.key === KEY) changed(load()); });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", badge); else badge();
})();
