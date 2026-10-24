# Soft-copy delivery: design (23 Oct 2026)

Owner, 23 Oct: "Soft-copy delivery is not built: it needs file storage with expiring download links, and a business email to send them from." This is the design. Setup steps for the owner are in `delivery_setup.md`. Nothing here has run against real Cloudflare R2, Resend or Supabase; see "Not tested".

## What it covers
- Soft copies of the extension workbooks (shop products `ext-l1` .. `ext-l6`, format `soft` in `website/data/products.json`, which is `pdf` here). Prices are on hold (owner); this system does not know or show prices.
- The late-registration fallback for the November beta: the colour PDF of the holiday workbook (`beta-workbook-l1` .. `l6`) for a family who registers too late for the posted printed copy.
- Printed workbooks stay black and white; soft copies stay colour (owner, 23 Oct). The manifest points soft copies at the colour print-layout PDFs in `outputs/print/`, never at `outputs/print/bw/`.

## Parts
| Part | Where | Notes |
|---|---|---|
| Private file store | Cloudflare R2 bucket `mi-delivery`, bound to the site as `DELIVERY_BUCKET` | Never public, no custom domain, no public r2.dev URL. Keys `files/<product>/v1/<name>.pdf`. |
| Manifest | `portal/data/delivery_manifest.json` | `product:format` -> R2 key, version, sha256, repository source. Checked by `portal/tools/delivery_manifest.py check`. |
| Upload | `portal/tools/upload_files.sh` | Checks the manifest, then `wrangler r2 object put --remote`. `--dry-run` first. |
| Entitlements | `portal/supabase/delivery.sql` (REVIEW FIRST, not applied) | Tables `entitlements`, `delivery_log`; RLS on, no policy, no grant to anon/authenticated. |
| Grant hook | `portal/functions/_shared/delivery.js` `grantEntitlements(env, session, items)` | Idempotent. Called from the Stripe webhook through one marked line (`MI-DELIVERY-HOOK`). |
| Download | `GET /api/download/<token>` (`portal/functions/api/download/[token].js`) | Validate, rate limit, count, stream from R2. |
| Success page | `/portal/order/?session_id=cs_...` + `GET /api/order-links` | Shows the links at once, so email is a convenience, not a dependency. |
| Email | `portal/functions/_shared/email.js` | `sendEmail` adapter, Resend implementation, plain + HTML template. |
| Admin | `POST /api/admin/delivery` (list, create one-off link, resend, revoke, purge log) and `portal/tools/make_link.mjs` | The function runs every database call as the logged-in admin; the SQL checks `is_admin()`. |

## Token model
- `link_nonce`: 32 random bytes (base64url), stored.
- `token = HMAC-SHA256(DELIVERY_TOKEN_SALT, "mi-dl-v1|" + nonce)`: 43 URL-safe characters, 256 bits, never stored.
- `token_hash = SHA-256("mi-dl-token|" + token)`: stored, unique, the lookup key.
- Why derived rather than purely random: the success page and "resend" must be able to show the same link again without the database holding it. A leak of the database alone gives hashes and nonces, which cannot rebuild a link without `DELIVERY_TOKEN_SALT` (a Cloudflare secret). A leak of the salt alone is useless without the database. **Rotating the salt invalidates every outstanding link** (do this only in an emergency, then resend).
- The lookup is by hash equality in Postgres, with a 256-bit unguessable input, so response timing reveals nothing usable. `verifyToken` (constant-time compare) is used wherever a presented token is compared to stored values in code.

## Download rules (all in `service_download_begin`, one database call)
1. Rate limit per IP: 30 requests per 10 minutes (wrong tokens count), plus 60 per minute per isolate in the Worker. The IP is stored only as a salted HMAC (32 hex chars), for 90 days.
2. Token unknown -> 404 page. Revoked or expired -> 410. `download_count >= max_downloads` (default 5) -> 410. Default expiry 14 days (`DELIVERY_EXPIRY_DAYS`, `DELIVERY_MAX_DOWNLOADS` override).
3. A request that starts at byte 0 (or has no Range, or an unusable Range) uses one download. A range starting after byte 0 (resume) is free, but only within 2 hours of a counted download, so ranges cannot be used to avoid counting. Suffix ranges (`bytes=-N`) count.
4. If the file cannot be read from R2 the download is given back (`service_download_release`) and the buyer sees "your download was not used".
5. `HEAD` is refused (link previews and scanners cannot burn a download). Responses: `Content-Disposition: attachment`, `Cache-Control: no-store, private`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `X-Robots-Tag: noindex`, `Accept-Ranges: bytes`, 206 + `Content-Range` for ranges, 416 for bad ranges.
6. The log row holds: time, entitlement id, order id, outcome, IP hash. No email, no name, no raw IP.

## Hook contract with the shop and the Stripe webhook
The shop's checkout (shop agent) must create the Checkout Session with:
- `metadata[mi_items] = "ext-l1:pdf,ext-l3:pdf"` (product id : format, comma separated; physical items are not listed here). Stripe metadata values are limited to 500 characters; six items fit easily.
- optional `metadata[mi_order]` = short order reference (3 to 40 letters, digits, hyphen). Otherwise the order id is `MI-` plus the last 8 characters of the session id.
- `success_url = https://YOUR-DOMAIN/portal/order/?session_id={CHECKOUT_SESSION_ID}`
- Collect the buyer's email (Checkout does by default; `customer_details.email` is used).
The webhook (`portal/functions/api/stripe-webhook.js`) has one marked block, placed before the enrolment logic: for events carrying `metadata.mi_items`, it calls `maybeHandleShopOrder` and returns. Only `checkout.session.completed` / `async_payment_succeeded` with `payment_status = paid` grant links; unpaid PayNow waits for the async event; expiry events are ignored. A database failure returns 502 so Stripe retries; a repeat is harmless because the grant is unique on (session, product, format) and the email is claimed once under a 10 minute lease. A product missing from the manifest is logged as `NEEDS OWNER ATTENTION` and reported in the response; the other items still go out.

## Manual path (no payment): beta PDF fallback and WhatsApp
Admin API `create` or `node portal/tools/make_link.mjs --product beta-workbook-l1 --email ... --note "Tan family"`. Both write an entitlement with `source = manual`, order id `MANUAL-xxxxxxxx`, and print the link once. Without an email address nothing is sent: copy the link into WhatsApp. This is the interim procedure while email is not set up (see `delivery_setup.md` part 5).

## Watermarking: measured, NOT enabled
Test: pdf-lib 1.17.1, Node 22 (same V8 as Workers), stamp one line of footer text on every page, `portal/tools/watermark_measure.mjs`.
| File | Size | Pages | CPU | Wall | Extra memory |
|---|---|---|---|---|---|
| P2 workbook (colour print PDF) | 7.3 MB | 74 | about 470 ms | about 410 ms | about 38 MB |
| P3 workbook | 7.3 MB | 64 | about 520 ms | about 500 ms | about 37 MB |
A 10 MB file would take roughly 0.7 s CPU and 55 MB. Cloudflare's Workers Free plan allows 10 ms CPU per request; the Paid plan allows 30 s by default and 128 MB memory per isolate. So: impossible on Free, feasible but wasteful on Paid (every download burns about half a second of CPU and memory, it must buffer the whole file so range requests and the stored sha256 no longer apply, and a 20 MB book would be close to the memory limit). **Decision: not enabled.** Phase 2, if the owner wants it: stamp each file once per order at grant time (a Queue or an admin script) and store the stamped copy under `files/<product>/<order>/...`, which keeps the download path unchanged. Check the Cloudflare limits page for the current numbers before relying on the figures above.

## Not tested (needs real services)
R2 binding behaviour and `head`/`get` with ranges on a real bucket; Resend delivery, domain verification and the exact response shape; the repo-root `/functions` re-exports on Cloudflare; **the site is currently deployed as Workers static assets (`wrangler.jsonc`, deploy command `npx wrangler deploy`), which does not run `/functions`**. Pages Functions only run on a Cloudflare Pages project (the Stripe functions have the same dependency). Before launch the owner must either deploy through Pages, or the repo needs a Worker entry (`main`) that routes `/api/*` to these handlers and an `r2_buckets` binding in `wrangler.jsonc`. This is the first thing to check in `delivery_setup.md`.
Tested locally (no network): `node --test portal/tests/delivery.test.mjs` (22 tests: token generate/hash/verify, wrong-token constant-time compare, expiry, max downloads, revoked, rate limit, range requests, email payload shape, idempotent grant on repeated webhook, webhook hook, admin) and `bash portal/supabase/test/run_delivery_test.sh` (the SQL on a local PostgreSQL: idempotency, limits, RLS, admin checks, re-run safe).
