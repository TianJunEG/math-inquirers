# Shop (/shop/): extension workbooks, coming soon

The shop is a page of product cards plus a cart called **Your list**. While a product is "coming soon" it shows **no price**, and the cart collects interest ("Tell me when it's ready") instead of taking an order. Owner decision (23 Oct 2026): prices are on hold, nothing may show a price.

## Where things live

| What | File |
|---|---|
| Products (names, formats, status, price) | `website/data/products.json` (the only file you edit) |
| Page generator | `website/shop_build.py` (writes `website/shop/shop.html`) |
| Cart (browser storage, nav badge) | `website/shop/cart.js` |
| Page, list and interest form | `website/shop/shop.js` |
| Checkout hand-off (stub, not live) | `website/shop/checkout.js` |
| Database for interest requests | `portal/supabase/product_interest.sql` (review first, not applied) |
| Tests | `website/tests/shop_test.py` (run by `website/tests/interest_test.py`), `portal/supabase/test/product_interest_test.sql` |

## Setting products, prices and status

Edit `website/data/products.json`, then rebuild: `cd website && python3 shop_build.py && python3 build_site.py` (a full rebuild also needs `python3 lp_build.py && python3 level_pages.py` if you changed other pages).

Each product has:

- `id`: lowercase letters, digits and hyphens (for example `ext-l1`). It is stored with each interest request, so never reuse an id for a different product.
- `level` (1 to 6), `name`, `description`, `ages` (shown on the card).
- `formats`: `["soft", "physical"]`. `soft` is a PDF sent by email, `physical` is printed and posted to a Singapore address.
- `status`: `"coming-soon"` or `"available"`.
- `price_cents` (optional): whole cents. One number applies to every format, or give each format its own: `{"soft": 800, "physical": 1550}`.

**The price rule:** a price appears on the page **only if** `status` is `"available"` **and** `price_cents` is set (for every format the product offers). Anything else shows "Coming soon" with no price. A product marked `available` without a price is treated as coming soon. The price is never put into the page for a coming-soon product, so it cannot leak. The build prints a warning for every `price_cents` it finds (and says whether it will be shown), and the same warnings appear in the "To confirm before launch" list of `build_site.py`.

To add a seventh product, add an entry with a new id. No database change is needed.

## What the cart does

- Each card has an **Add to your list** button per format. Pressing it again removes it. Physical copies have a quantity (1 to 10) in the list; a soft copy is always one.
- The list is stored in the visitor's own browser (`localStorage`, key `mi_cart_v1`: product ids, formats and quantities only, no personal data). It survives reloads and shows as a small number beside **Shop** in the nav on every page. If the browser blocks storage the page still works for that visit.
- **Tell me when it's ready** opens a form: parent first name, a WhatsApp number or an email (at least one), which items from the list, an optional note, a consent tick (purpose: tell you when the product is ready; kept 12 months then deleted; no marketing beyond that notice) and a hidden honeypot. No child name is asked for.
- Submitting: in a `--with-portal` build with real `SUPABASE_URL` / `SUPABASE_ANON_KEY`, the form calls the database function `submit_product_interest` (after you apply the SQL). Otherwise, or if that call fails, it writes a WhatsApp message to +65 9880 5962 listing the items, which the parent sends. This is the same arrangement as the "Request another time" form. There is a one-minute limit in the browser, one request per contact per day and 300 an hour in the database.
- Sent items leave the list. Nothing is reserved, ordered or charged.

## Seeing the interest

After the SQL is applied (review it first; it does not touch existing tables): **/portal/admin/ > Shop interest** shows the tally by product and copy type, the list, "Mark notified" and "Delete". "Delete expired requests" removes anything older than 12 months. Without the portal, in the Supabase SQL editor:

```sql
select i->>'product' as product, i->>'format' as format, count(*) as requests, sum((i->>'qty')::int) as copies
  from public.product_interest, jsonb_array_elements(items) i group by 1, 2 order by 1, 2;
```

Change the 12 months in three places together: the `expires_at` default in the SQL, the wording in `website/shop_build.py` (CONSENT) and `website/privacy.html`.

## Turning on checkout later

Checkout is **not built**. The pieces are laid out so the payment work can plug in:

1. Set a product to `available` with a price (see the price rule). Its cards then show the price and **Add to cart**, and the list shows a **Ready to order** group with a total. The **Checkout** button appears but stays disabled.
2. The payment code serves `POST /api/shop/checkout` as a Pages Function (request, response and error shapes are documented at the top of `website/shop/checkout.js`). It must read the catalogue and price itself and never trust a browser price; physical items need a Singapore delivery address (name, address, 6-digit postal code), soft copies need an email.
3. Add a small details form (email, Singapore address) that calls `MiCheckout.start(order)`; `MiCheckout.validate(order)` already holds the rules.
4. Set `checkoutEnabled` to `true` in `shop_build.py` (the `shop` dict) and rebuild.
5. Update the terms (refunds for digital downloads and posted books), the privacy notice (delivery details and email for orders) and the CSP only if the payment flow needs a new host (hosted Stripe Checkout needs none).

Not decided yet (owner): prices, whether soft copies are in colour and physical copies in black and white, how soft copies are delivered after payment (download link), and bulk or school sales (a separate product).
