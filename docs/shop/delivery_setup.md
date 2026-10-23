# Soft-copy delivery: owner's setup checklist

Do these in order. Nothing is secret in this file. **Never paste a key into chat, the repo or any page**: secrets go only into Cloudflare (step 6). Design and limits are in `delivery_plan.md`. Prices stay on hold; this setup does not need any.

## 0. Check how the site is deployed (5 minutes, important)
The site was set up as a Cloudflare Workers project with static assets (`wrangler.jsonc`, deploy command `npx wrangler deploy`). The delivery code (and the Stripe functions) are **Pages Functions** in `/functions`, which that setup does not run. Choose one:
- **A. Move to Cloudflare Pages** (simplest for the functions): Workers & Pages > Create > Pages > Connect to Git, same repository and branch; Root directory `/`, Build command `cd website && python3 lp_build.py && python3 build_site.py --with-portal`, Build output directory `website/dist`. Add your domain to the Pages project. Steps 3 and 6 below then use the **Pages** screens.
- **B. Stay on Workers**: ask for a small follow-up change (a Worker entry file that routes `/api/*` to these handlers, and an `r2_buckets` entry in `wrangler.jsonc`). Until then the links cannot be served.
Test after deploying: open `https://YOUR-DOMAIN/api/order-links?session_id=nope` -> it must answer `{"error":"bad session"}` (400). A normal 404 page means functions are not running.

## 1. Apply the database changes
1. Read `portal/supabase/delivery.sql` (or ask someone to). It adds two private tables and some functions; it changes nothing that exists.
2. Supabase > SQL Editor > New query > paste the file > Run. Safe to run twice.
3. Table Editor: `entitlements` and `delivery_log` must both show "RLS enabled".

## 2. Cloudflare R2: create the private bucket
1. Cloudflare dashboard > left menu **R2 Object Storage** > Overview. R2 asks for a **payment method on the account** before you can use it (there is a free monthly allowance; check Cloudflare's current R2 pricing yourself, nothing is stated here). Add the card.
2. **Create bucket** > name `mi-delivery` (must match `bucket` in `portal/data/delivery_manifest.json`) > location: Asia-Pacific (or Automatic) > Create.
3. Open the bucket > **Settings**: leave "Public access" / "R2.dev subdomain" **Disabled** and add **no custom domain**. The files are only ever served by the download function.

## 3. Bind the bucket to the site as DELIVERY_BUCKET
- Pages project: Workers & Pages > your project > **Settings** > **Bindings** (Functions) > Add > **R2 bucket** > Variable name `DELIVERY_BUCKET` > Bucket `mi-delivery` > Save, for both Production and Preview. Then redeploy.
- (Option B only: the `r2_buckets` entry in `wrangler.jsonc`, done in the follow-up change.)

## 4. Upload the PDFs
On a computer with Node installed, in the repo folder:
1. `npx wrangler login` (opens the browser; log in to the Cloudflare account that owns the bucket).
2. `python3 portal/tools/delivery_manifest.py check` -> must say "0 problems". (If someone rebuilt a PDF it says the checksum differs: run `python3 portal/tools/delivery_manifest.py update`, change the `version` (v1 -> v2) and the matching part of `r2_key` for that entry, then continue. Never overwrite a key that buyers already have.)
3. `bash portal/tools/upload_files.sh --dry-run` then `bash portal/tools/upload_files.sh`.
4. Cloudflare > R2 > `mi-delivery` > Objects: the files appear under `files/...`. The extension workbooks are skipped until their PDFs exist; when each is built, put it at the `source` path in the manifest (adjust the placeholder path), run `update`, upload.

## 5. Interim procedure for the November beta: NO email needed
Use this for late registrants who need the PDF, and any time email is not ready.
1. Log in at `/portal/admin/` as admin. (Until an admin screen is added, call the API: ask for a one-line helper, or use the command below.)
2. On your own computer, in the repo folder, with the values typed into your own terminal (not into chat): 
   `export SUPABASE_URL=... SUPABASE_SERVICE_ROLE_KEY=... DELIVERY_TOKEN_SALT=... SITE_URL=https://YOUR-DOMAIN`
   `node portal/tools/make_link.mjs --product beta-workbook-l1 --note "Tan family, late registration"`
   (`DELIVERY_TOKEN_SALT` must be the same value you set in Cloudflare in step 6.) Product ids: `beta-workbook-l1` .. `beta-workbook-l6`.
3. It prints one link (valid 14 days, 5 downloads; change with `--days` and `--max`). Paste it into WhatsApp to the parent. Tell them to save the PDF and print it at home, in colour or black and white.
4. The link is recorded as `MANUAL-xxxxxxxx` under the Supabase table `entitlements` (Table Editor). To withdraw it: `update public.entitlements set revoked_at = now() where order_id = 'MANUAL-XXXXXXXX';`

## 6. Resend (the business email sender)
1. resend.com > Sign up with the business email > verify it.
2. **Domains** > Add Domain > enter your domain once you have bought it (a subdomain such as `mail.YOUR-DOMAIN` is fine) > region Singapore (ap-southeast-1) if offered.
3. Resend shows DNS records. In Cloudflare > the domain > **DNS** > Records > Add record, copy each exactly: the **SPF** (TXT, includes `amazonses.com`) and **MX** records Resend lists for its sending subdomain, the **DKIM** (TXT `resend._domainkey`), and add a **DMARC** TXT record at `_dmarc` with value `v=DMARC1; p=none; rua=mailto:YOU@YOUR-DOMAIN` (tighten to `quarantine` after a few weeks of clean sending). Set proxy status to **DNS only** for these. Back in Resend press **Verify** (can take minutes to hours).
4. Domain settings: leave **Open tracking** and **Click tracking** OFF.
5. **API Keys** > Create API Key > permission "Sending access" > domain: yours > copy it once.
6. Until the domain is bought and verified: Resend's test sender (`onboarding@resend.dev`) only delivers to **your own** Resend account email. Use it to test (set `EMAIL_FROM` to `Math Inquirers <onboarding@resend.dev>`), then switch `EMAIL_FROM` to `Math Inquirers <downloads@YOUR-DOMAIN>` once verified. Real buyers cannot get email before the domain is verified: use step 5's WhatsApp route or the success page (it always shows the links).

## 7. Secrets and settings in Cloudflare (never in chat)
Pages project > Settings > **Variables and Secrets** (Production and Preview) > Add:
| Name | Type | Value |
|---|---|---|
| `RESEND_API_KEY` | Secret | from step 6.5 |
| `SUPABASE_SERVICE_ROLE_KEY` | Secret | Supabase > Project Settings > API > service_role (already needed for Stripe) |
| `DELIVERY_TOKEN_SALT` | Secret | a long random string, at least 24 characters, e.g. generated by your password manager. Keep a copy there. Changing it later invalidates every link already sent. |
| `SUPABASE_URL`, `SUPABASE_ANON_KEY` | Text | as for the portal |
| `SITE_URL` | Text | `https://YOUR-DOMAIN` (no trailing slash; links are built from it) |
| `EMAIL_FROM` | Text | `Math Inquirers <downloads@YOUR-DOMAIN>` |
| `EMAIL_REPLY_TO` | Text (optional) | your support email |
| `SUPPORT_WHATSAPP` | Text | `+65 9880 5962` (the business number now in the site; change if different) |
| `DELIVERY_EXPIRY_DAYS`, `DELIVERY_MAX_DOWNLOADS` | Text (optional) | defaults 14 and 5 |
Redeploy after changing anything here.

## 8. Test (do all of these in Stripe test mode / test sender before going live)
1. **Manual link**: step 5 for `beta-workbook-l1`. Open the link in a private window: the PDF downloads and opens. Open it 6 times: the 6th shows "Download limit reached". Open `https://YOUR-DOMAIN/api/download/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` -> "Link not found".
2. **Expiry**: in Supabase run `update public.entitlements set expires_at = now() - interval '1 minute' where order_id = 'MANUAL-XXXXXXXX';` -> the link says expired. Revoke test: set `revoked_at = now()` on a fresh one.
3. **Paid order** (needs the shop checkout from the shop work, with `metadata[mi_items]`, see `delivery_plan.md`): pay with test card `4242 4242 4242 4242`; you land on `/portal/order/?session_id=cs_test_...` and the link(s) appear within a few seconds; the email arrives (to your own address while on the test sender); the Stripe dashboard shows the webhook 200. Re-send the webhook from Stripe (Developers > Webhooks > the event > Resend): no second email, same link.
4. **Privacy check**: in Supabase `delivery_log` has an `ip_hash` and an order id, no email. The bucket page shows no public URL.
5. Response headers of a download (browser dev tools > Network): `Content-Disposition: attachment`, `Cache-Control: no-store, private`.
6. Cloudflare R2 > Metrics: operations appear after the downloads.

## 9. If email is blocked or not working
- The buyer is never stuck: the success page shows the links; if they closed it, they message us on WhatsApp with the order number and we issue a link (step 5) or press resend.
- Check Resend > Logs for the failure (domain not verified, key wrong, recipient bounced). Common causes: `EMAIL_FROM` not on the verified domain; DNS records proxied (set DNS only); test sender used for a stranger.
- Gmail/Outlook spam folder: ask the buyer to check; keep DMARC in place; never add tracking links.
- If Resend itself is unavailable, switch provider by adding a function in `portal/functions/_shared/email.js` (the adapter has one entry per provider) and setting `EMAIL_PROVIDER`.
- Failed sends are logged in the Cloudflare function log as "delivery: email failed"; the order is still granted.

## 10. Later / admin
- `POST /api/admin/delivery` (admin login token) with `list`, `create`, `resend`, `revoke`, `purge_log`. There is no admin screen yet; ask for one when the volume justifies it.
- Retention: delete `delivery_log` rows after 90 days (run `select public.admin_purge_delivery_log(90);` monthly, or schedule with pg_cron, example in the SQL file). Purchase records (with buyer email) are kept [7 years] per the owner's records decision; see `privacy_additions.md`.
- A new version of a book: build the PDF, `delivery_manifest.py update`, bump version and key, upload; old links keep serving the version bought.
