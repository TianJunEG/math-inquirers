# Math Inquirers portal (first working version)

Parent accounts, child profiles (display name + PIN, no child email), beta group choice, PDPA consent records, payment status, a small owner admin page, and Stripe payment functions (Checkout). Static HTML/JS front end + Supabase (Auth, Postgres, row level security) + two Cloudflare Pages Functions.

```
portal/
  supabase/schema.sql, policies.sql, seed_groups.sql   run in this order in the Supabase SQL editor
  supabase/stripe_migration.sql                        REVIEW FIRST, then run once on a project created before 23 Oct 2026 (HitPay -> Stripe); not needed on a fresh install
  supabase/test/                                       local Postgres test (run_sql_test.sh)
  public/                                              the front end, served at /portal/ (index, child/, practice/, admin/)
  public/vendor/supabase.js                            supabase-js 2.45.4 UMD, vendored (MIT), so CSP needs no CDN
  public/config.js                                     SUPABASE_URL / ANON_KEY placeholders (public values only)
  functions/api/stripe-create-checkout.js, stripe-webhook.js   Cloudflare Pages Functions (+ functions/lib.js)
  tools/gen_groups_seed.py                             rebuilds seed_groups.sql from website/data/beta_schedule.json
  tests/                                               node test (functions), Playwright test (front end, mocked Supabase)
../functions/api/*.js                                  two one-line re-exports so Pages finds the functions at the repo root
```

## Owner setup, in order

1. **Supabase project.** supabase.com > New project (pick the Singapore region). Keep the database password somewhere safe.
2. **Run the SQL.** SQL Editor: paste and run `schema.sql`, then `policies.sql`, then `seed_groups.sql`. If you change `website/data/beta_schedule.json`, run `python3 portal/tools/gen_groups_seed.py` and run the new `seed_groups.sql` (safe to re-run; it never touches seats already taken).
3. **Auth settings.** Authentication > Providers: Email on. Keep "Confirm email" on. URL Configuration: Site URL = your domain, add `https://YOUR-DOMAIN/portal/` to Redirect URLs. Authentication > Rate limits: leave defaults or tighten. Set up an SMTP sender (Supabase's built-in mailer is heavily rate limited and for testing only).
4. **Make yourself the admin.** Sign up once at `/portal/` with your owner email, then in the SQL editor: `insert into public.admins (user_id, note) select id, 'owner' from auth.users where email = 'YOU@example.com';`. Then log in at `/portal/admin/`.
5. **Keys.** Project Settings > API: copy the Project URL and the `anon public` key. These two are public values. The `service_role` key is a secret: it goes only into Cloudflare Function env vars (step 7), never in the repo, never in `config.js`.
6. **Wire into the site.** In the Cloudflare Pages build settings use
   `cd website && python3 lp_build.py && python3 build_site.py --with-portal`
   and set build env vars `SUPABASE_URL`, `SUPABASE_ANON_KEY` (these are written into `dist/portal/config.js`), optionally `PORTAL_PAYNOW_TO` (your PayNow number/UEN shown to parents) and `PORTAL_PAYMENT_MODE` (`paynow_manual` is the default and the beta mode; `stripe` once the Stripe checklist below is done). Without `--with-portal` the build is unchanged. With it, `_headers` gets a stricter CSP for `/portal/*` allowing only `connect-src 'self'` plus your Supabase origin; Stripe needs no entry because the browser only navigates (top-level) to Stripe's hosted Checkout page; we do not load Stripe.js, so `js.stripe.com` is deliberately not allowed.
7. **Beta payment (manual PayNow).** Nothing more to set up. A parent reserves a place, sees a reference like `MI-7K3Q9X`, pays by PayNow with that reference in the comment, and you tick it off at `/portal/admin/` ("Mark paid") after checking your bank. The seat is held while payment is pending; cancel stale reservations from the SQL editor or ask the parent to cancel.
8. **Stripe (launch). Checklist for the owner.** Stripe replaced HitPay on 23 Oct 2026. The beta can run entirely on manual PayNow (step 7); do this when you want online payment.
   1. **Account.** Create a Stripe account for Preciouslyours Pte Ltd (country Singapore) and complete the business verification. Turn on 2FA.
   2. **Currency and PayNow.** Settings > Payment methods: make sure Cards and **PayNow** are enabled (PayNow needs a Singapore account and SGD; Stripe may ask for extra activation). Check Stripe's current Singapore pricing yourself before you launch; this repo states no fee numbers.
   3. **Test keys first.** Switch the dashboard to Test mode. Developers > API keys: copy the **secret key** (`sk_test_...`). Never paste it in chat, in the repo or in `config.js`.
   4. **Database.** Review `portal/supabase/stripe_migration.sql`, then run it once in the Supabase SQL editor (idempotent; it also retires the three old HitPay functions). A fresh install from `schema.sql` + `policies.sql` already has the Stripe functions.
   5. **Cloudflare secrets.** Cloudflare Pages > Settings > Variables and Secrets (Production and Preview), type **Secret**: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` (step 6), and `SITE_URL` (`https://your-domain`, no path). Redeploy after changing them.
   6. **Webhook.** Developers > Webhooks > Add endpoint: URL `https://YOUR-DOMAIN/api/stripe-webhook`; events `checkout.session.completed`, `checkout.session.async_payment_succeeded`, `checkout.session.async_payment_failed`, `checkout.session.expired`. Copy its **signing secret** (`whsec_...`) into `STRIPE_WEBHOOK_SECRET`. (Test mode and live mode have separate endpoints, keys and secrets.)
   7. **Test.** Build with `PORTAL_PAYMENT_MODE=stripe`, reserve a place, press Pay. Card: `4242 4242 4242 4242`, any future expiry, any CVC. Declined card: `4000 0000 0000 0002`. PayNow: choose PayNow on the Checkout page; in test mode Stripe shows a test QR page with an authorise/fail button instead of a bank app. Confirm the enrolment flips to confirmed and `payments` shows `method = stripe`, a `cs_...` `provider_ref` and a `pi_...` `provider_payment_ref`. In the Stripe dashboard the webhook endpoint should show 200s. Also try the PayNow fail and the cancel link.
   8. **Go live.** Complete activation, switch Test mode off, create the live key and a live webhook endpoint (new `whsec_`), replace `STRIPE_SECRET_KEY` and `STRIPE_WEBHOOK_SECRET` in Cloudflare, redeploy, make one small real payment of your own and refund it, then set `PORTAL_PAYMENT_MODE=stripe` for the public build.
   - **Refunds.** Refund from the Stripe dashboard (Payments > the payment > Refund). Then in the SQL editor set `update public.payments set status = 'refunded', note = coalesce(note,'') || ' | refunded in Stripe' where reference = 'MI-XXXXXX';` (there is no admin refund button yet; the payment note already flags "refund due" when a paid enrolment is cancelled). For a manual PayNow payment refund by PayNow as before.
   - **Fees.** Stripe charges per transaction and may differ for cards and PayNow; check Stripe's current Singapore pricing and decide whether the S$250 beta fee still covers it.
   - Pages Functions are read from `/functions` in the repo root (the Pages root directory). That folder only re-exports the code in `portal/functions`.
   - Unpaid reservations: a Checkout Session lasts 24 hours. If it expires, `checkout.session.expired` resets it and the parent can press Pay again (fresh idempotency key). The seat stays held while the reservation is pending.

## "Request another time" (timing interest)

The public site has an "Other times" area on each level card (placeholder slots, not open for enrolment, listed in `website/data/interest_slots.json`) and a "Request another time" form on the home page.

- **Apply `portal/supabase/interest_requests.sql`** in the Supabase SQL editor (after schema.sql and policies.sql; idempotent; re-run it after any re-run of policies.sql). It creates `public.interest_requests` (RLS on, no policy: anon and logged-in users cannot select), the anon-callable `submit_interest_request()` (validates lengths, one request per contact per 24 hours, 300 per hour site-wide, honeypot, no input echoed in errors) and admin-only `admin_interest_tally()`, `admin_list_interest_requests()`, `admin_set_interest_status()`, `admin_delete_interest_request()`, `admin_purge_expired_interest_requests()`.
- **Retention default: 12 months** (`expires_at`). It is a DEFAULT for the owner and a lawyer to confirm; if you change it, change the column default, the form wording (`website/interest_ui.py`) and `website/privacy.html`. Delete expired rows with the "Delete expired requests" button on the admin Interest tab, or schedule it with pg_cron (example in the SQL file).
- **Admin view:** `/portal/admin/` > Interest tab: tally by level and time, the list, mark contacted, delete. Without the portal, in the SQL editor: `select level, s as slot, count(*) from public.interest_requests, unnest(slots) s group by 1, 2 order by 1, 3 desc;`
- **Modes:** the form saves to Supabase only in a build made with `--with-portal` and `SUPABASE_URL` / `SUPABASE_ANON_KEY` set (the home page then loads `/portal/config.js`, and the site CSP `connect-src` allows your Supabase origin). Otherwise, or if saving fails, it builds a prefilled WhatsApp message to the business number. The anon key is public by design; nothing secret is in the page.
- **Tests:** `python3 website/tests/interest_test.py` (Playwright, RPC mocked), `bash portal/supabase/test/run_sql_test.sh` (includes `test/interest_test.sql`).

## Local tests

```
bash portal/supabase/test/run_sql_test.sh        # needs postgresql server binaries; starts a throwaway cluster
node --test portal/tests/functions.test.mjs      # Node 20+; Stripe + Supabase mocked (no network, no keys)
python3 portal/tests/frontend_test.py            # Playwright 1.56.0 + chromium; mocked Supabase client
python3 portal/tools/gen_groups_seed.py --check  # seed file matches beta_schedule.json
```

## How it works (security design)

- **No direct writes.** Browsers can only read their own rows (RLS) and call SECURITY DEFINER functions (`add_child`, `enrol_child`, `record_consents`, `delete_my_data`, ...). The one direct write is the parent's own name/phone.
- **PIN** is hashed in the database with bcrypt (`pgcrypto crypt`). `pin_hash`, `pin_failed`, `pin_locked_until` are not readable by any API role (column grants). `child_sign_in()` returns a row only on success, never says which part was wrong, and locks a child for 15 minutes after 5 wrong PINs. PINs are 4-6 digits: weak by nature, which is why the lockout exists.
- **Child sign-in is a stub.** It checks family code + display name + PIN and stores the name in `sessionStorage` for the placeholder page. It is not a server session; when the practice area starts saving answers, it must mint a real, short-lived token for the child.
- **Seats** are checked under a row lock in `enrol_child`, so two parents cannot take the last seat. Level must match the group.
- **Admin** is a row in `public.admins`. Every `admin_*` function checks it server-side; the admin page is only a viewer. An admin cannot read PIN hashes either.
- **Stripe.** The amount always comes from the database (`payments.amount_cents`, copied from the group fee at reservation). The create function checks the caller's Supabase token, then makes a Checkout Session (mode payment, SGD, card + PayNow, `client_reference_id` = payment id, idempotency key per payment and attempt). The webhook verifies `Stripe-Signature` (HMAC-SHA256 over `timestamp.rawbody`, 5 minute tolerance, constant-time compare), acts only on the four checkout events, and marks paid through a function only the service role can run, which checks the amount in cents and the currency. It is idempotent, so Stripe retries and replays are harmless. Card numbers never reach our pages or servers. Secrets live only in Cloudflare.
- **Consents** are append-only (trigger blocks update/delete). A withdrawal is a new row. Each row stores the terms and privacy versions (`MI.VERSIONS` in `public/common.js`: **bump them whenever terms.html / privacy.html change**). Enrolling requires the four needed consents to be currently granted.

## PDPA / security checklist (before real families use it)

- [ ] Lawyer reviews terms.html and privacy.html; remove draft banners; confirm the bracketed retention periods; name the data protection contact. The privacy notice already names Supabase and Stripe (Stripe may process data outside Singapore: wording in brackets for the lawyer): confirm it says where data is stored (Supabase region) and that transfers outside Singapore are covered.
- [ ] Bump `VERSIONS` in `public/common.js` to the reviewed text's version/date.
- [ ] Supabase: confirm region, turn on database backups (paid plan for PITR), keep "Confirm email" on, set an SMTP sender, restrict dashboard access to you (and 2FA on your Supabase, Cloudflare and Stripe accounts).
- [ ] Row level security is enabled on every table (check Table Editor shows RLS on). Never expose the service_role key; rotate it if it ever leaks.
- [ ] Retention: privacy.html promises payment/registration records for 12 months, recordings and work for shorter periods. `delete_my_data()` keeps only anonymised payment/consent rows. You must purge those after the retention period (consents has an append-only trigger: `alter table public.consents disable trigger consents_append_only;` for the purge, then enable again).
- [ ] Handle access/correction/delete requests within the promised days. A parent can self-serve delete in the portal; it does NOT refund: check the payment note "refund due" and refund per the terms (Stripe dashboard for online payments, PayNow for manual ones).
- [ ] Children's data stays minimal: display name (tell parents to use a first name or nickname), level, PIN hash. No photo, school, NRIC, birth date.
- [ ] Recordings and photos of work are not stored by this portal; store them privately elsewhere as the privacy notice says.
- [ ] Set `PAYNOW_TO` and check the instructions parents see.
- [ ] Data breach plan: PDPA requires notifying PDPC and affected people for notifiable breaches.

## Not tested / not verified (honest list)

- **Run against real Supabase: no.** The SQL ran and its assertions passed on a local PostgreSQL 16 with a small stand-in for Supabase's `auth` schema and roles (`test/stub_supabase.sql`). Real Supabase differences (e.g. how `auth.uid()` reads the JWT, the `extensions` schema, trigger on `auth.users`, `delete from auth.users` inside a function) are standard but unproven here. Run the SQL on a scratch project first.
- **Front end against the real supabase-js: no.** Playwright tests use an in-memory mock of the client and RPCs, so they prove the UI logic, not the network calls, the real email flows (confirm email, magic link redirect), or that column-limited `select` lists match your grants.
- **Stripe: never called with real keys.** The function logic, signature check, form encoding and the SQL are tested only with mocks and a local PostgreSQL. Unverified until you run the test-mode checklist: that Checkout accepts `payment_method_types[]=paynow,card` on your account, that the success/cancel redirects behave, the exact webhook payloads (`amount_total`, `currency`, `payment_status`, `payment_intent`, `client_reference_id`) and that `checkout.session.completed` for PayNow arrives with `payment_status` unpaid or paid as assumed. Endpoints used: `POST https://api.stripe.com/v1/checkout/sessions` (form-encoded, Bearer secret key, `Idempotency-Key`).
- **Cloudflare Pages Functions in the repo-root `/functions` re-export layout, and `_headers` path rules** (`/terms/*` matching `/terms/`, no double CSP on `/portal/*`) are untested on Cloudflare. Check response headers after the first deploy.
- Not built: password reset screen (use the magic link), instalments (terms mention them; one payment per enrolment here), waitlist, expiry of unpaid seat holds, emails/receipts to parents, real child session/practice data capture, admin refund button (set `refunded` by SQL), child-facing practice runner integration, rate limiting beyond Supabase defaults and the PIN lockout, accessibility audit.

## Posted workbook delivery (November beta)
The beta workbook is printed and posted to each family. The delivery name, address, postal code and phone, and the delivery consent, are collected on the WhatsApp registration form of the site (`website/lp_build.py`), not in this portal. The portal sign-up does not collect them yet: adding them needs new columns on `parents` (address, postal code), a delivery consent type and an admin view, so it is not a simple change. Until then, portal families send the delivery details on WhatsApp. Staff use `docs/printing/dispatch_list.md`. Terms and privacy versions in `public/common.js` were bumped for the new delivery wording.
