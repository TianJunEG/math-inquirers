# Portal UI and database draft: independent audit, round 1

Branch `claude/great-fermi-1hv4vc`, 24 Oct 2026. Reviewer role: security, privacy and UX. Read-only on existing source; only new files were added. I did not trust the builders' claims: every result below was run, not read off the status docs.

Verdict: **do not apply to a live Supabase project yet.** The access control core is sound (no cross-family read, no privilege escalation, no answer-key leak, no payment forgery, no XSS found). But the privacy promises are not yet kept by the code: "delete my data" leaves delivery addresses, phone numbers and child names behind, the 30-day address rule does not cover refunded or undelivered orders, and several retention jobs are manual only. Fix the High and Medium items in section 2 and re-run `audit_run.sh` before any real family data goes in.

## 1. Test suites run

| Suite | Result |
|---|---|
| `bash portal/supabase/test/run_sql_test.sh` (rls, interest, product_interest, practice_submissions, portal_ui) | all assertions passed |
| `run_delivery_test.sh`, `run_preview_test.sh` | passed |
| `python3 portal/tests/portal_ui_test.py` | ALL PORTAL UI TESTS PASSED |
| `python3 portal/tests/frontend_test.py` | ALL FRONT-END TESTS PASSED |
| `node portal/tests/delivery.test.mjs`, `functions.test.mjs` | 23 and 17 pass (`node --test portal/tests/` as a directory fails to load, harmless: run the files) |
| `practice/submit` handler (34), mark (147), `test_submit.py` | pass |
| **New:** `bash portal/supabase/test/audit_run.sh` (audit_00 to audit_07) | 209 PASS, 17 FAIL (each FAIL is a finding), 14 NOTE |
| **New:** `python3 portal/audit_shots/audit_frontend.py` | 25 PASS, 7 FAIL, 1 NOTE, 104 screenshots |

Caveat that applies to everything: all SQL was tested on a local PostgreSQL 16 with the repo's Supabase stand-in, not on real Supabase (PostgREST, JWT, the `extensions` schema, Auth rate limits untested). The front-end tests use a mock that re-implements the SQL, so they cannot prove the SQL.

## 2. Findings (severity High / Medium / Low)

### High
**H1. "Delete my data" leaves personal data in `ext_orders` and `trial_requests`.** `delete_my_data()` (schema.sql, finish_setup.sql) pre-dates extension orders and was not extended. After it runs: the delivery name, address, postal code and phone of an unpaid or undelivered book order stay; `child_label` keeps the child's nickname; a pending order stays `pending_payment` (the owner could still tick it paid); a trial request and its 300-character free-text note stay up to 12 months. This contradicts the privacy text ("removes your children ... strips your name, email and phone") and the consent draft section 5 item 3. Test: `audit_05_privacy.sql`. Fix: in `delete_my_data()` clear ship_*, child_label, cancel pending orders, delete the parent's trial_requests and recording_views; add a "refund due" signal for paid orders.

**Confirm item (not a defect): D2 family rule. A confirmed enrolment for one child opens holiday and term practice for every sibling at that level, whatever the sibling's own level or enrolment (`_can_access`, `_entitlements`). Matches the wording "family has a confirmed place", but the owner decision says "families with a confirmed enrolment", so I list it as a confirm item (NOTE in audit_03), not a defect.

No other High findings; section 3 lists what was attacked and held.

### Medium
**M1. Address retention gap.** `admin_clear_delivered_addresses()` clears only `ship_status = 'delivered'` after 30 days. A refunded, lost, never-marked-delivered or forgotten order keeps name, address and phone for ever, against the 30-day consent line (`audit_04`). Also the function is manual; no pg_cron example exists, unlike the preview purge.
**M2. Retention jobs are all manual** (`admin_purge_expired_practice`, address clear, trial purge). The 12-month and 90-day promises depend on the owner remembering. Add scheduled jobs. The 90-day rule also counts from the submission date, not from when access ended as the consent text says.
**M3. Payment after cancel is lost.** If a parent cancels an order whose Stripe Checkout Session is already open, a later payment makes `service_ext_order_paid` raise `bad_status`: Stripe has the money, the database records nothing and flags nothing. The enrolment path handles this (`paid_enrolment_cancelled`); extension orders do not. `cancel_my_ext_order` should refuse when `provider_ref` is set, or the paid function should record a "late payment" for the owner.
**M4. `create_ext_order` stores an address for an online-only order** if an API caller sends one (the UI never does), and **accepts a NULL postal code** for a printed order (SQL NULL logic: `false or false or NULL` does not raise). Direct API calls bypass the UI checks.
**M5. Deleting a child who holds paid access is unguarded.** `delete_child` cascades the access row; the paid order keeps `child_id` NULL. The confirm dialog does not mention the purchase. Add a guard like `cancel_enrolment_first`, or warn.
**M6. Same `client_sid` can be reused for a different unit.** `service_practice_record` finds the submission by (child, sid) only, so a second call with another unit replaces the rows while `submissions.unit_key` stays the first unit; reports then join the wrong tags. The Worker takes unit and sid from the browser. Entitlement is still checked on the new unit, so no access bypass, only data integrity. Also a duplicate `item_id` inside one request raises a raw unique-violation instead of `bad_rows`.
**M7. PIN lockout does not escalate.** 5 wrong PINs lock for 15 minutes, the counter resets, so an attacker who knows family code and name gets 20 guesses per hour per child for ever (a 4-digit PIN falls within about 500 hours of patient guessing) and can keep a child locked out. Weak PINs (0000, 1234) are accepted. Suggest escalating lock times, a weak-PIN list, and telling the parent.
**M8. Agreements card says "Agreements saved." when needed boxes were left empty** (front end, `app.js`). Records contact=true, terms=false, online_practice=false and shows green success; the family then cannot use online practice and is not told why.
**M9. Keyboard focus is lost after every action.** The pages re-render by clearing the container, so focus falls back to `<body>` after add child, save, cancel, order. Keyboard and screen-reader users lose their place. Move focus to the result message or heading after each action.
**M10. Origin and headers architecture.** The portal (parent session in localStorage, owner admin session) shares an origin with the public site, whose CSP allows `'unsafe-inline'` scripts, and with `/practice/*`, for which `build_site.py` writes no CSP rule at all (only per site page and `/portal/*`). The child token is read from sessionStorage by the practice pages. Any script injection on a public or practice page can read the parent's or owner's session. Serve the portal on its own subdomain (or add strict CSP rules for `/practice/*`).
**M11. Birth year.** Optional in the portal (owner and lawyer to confirm; the original schema promised "no birth date"), but the preview class form requires a child birth year in the clear (2008-2022) for 30 days and keeps a hashed key 7 months. Two different treatments of one field; take both to the lawyer together. Verified: no other parent, tutor or child token can read it.
**M12. Long nickname breaks the 375px layout.** A 30-character nickname without spaces makes the "Buy a book for ..." button overflow (190px horizontal scroll at 375, 245px at 320). Let `.btn` wrap.

### Low
- L1. Payment redirect `location.href = j.url` (books.js, app.js) is not checked to be `https://checkout.stripe.com/`; a tampered `/api` reply would send the parent anywhere (demonstrated). The endpoint `/api/stripe-create-ext-checkout` does not exist yet either (status doc says so).
- L2. No rate limit on creating and cancelling orders (30 cycles made 30 rows). No postal-sector check beyond 6 digits (`000000` accepted). `admin_set_ship_status` has no status guard (unpaid or refunded orders can be marked posted).
- L3. Search_path hardening: all 103 SECURITY DEFINER functions pin `search_path`, but none lists `pg_temp` last. Not exploitable through PostgREST; harden anyway.
- L4. The Worker reply returns right/wrong for every item after each Submit, and up to 200 revisions of one attempt are allowed, so a determined child can read the key by trial. The 20-per-hour limit counts distinct submissions only and also blocks further revisions of an old attempt.
- L5. Preview class: anyone can fill a session with made-up emails (300/hour site brake, 8/day per email, honeypot, no captcha); "pending" vs "registered" is a small eligibility oracle.
- L6. No inactivity timeout for the child token on shared devices (4 hours or Sign out).
- L7. Footer links and "Go there" links are 19-22px tall (WCAG 2.2 target size 24px; inline-in-sentence links are exempt, standalone ones are not).
- L8. Wording: "program" (US) appears in the feedback consent line; Singapore usage is "programme". The "Order placed" page shows "No orders yet" in the list below the new order. The online practice consent is one long paragraph; consider a short summary line above it.
- L9. `request_trial` accepts unbounded-length slot strings (12 elements max) and saving the trial form silently overwrites the account phone.
- L10. Order page shows a placeholder PayNow target ("PayNow number or UEN (to confirm)") if `PORTAL_PAYNOW_TO` is not set at build.

## 3. What was attacked and held (PASS)

SQL (local Postgres, 209 checks): anon and PUBLIC can execute only the reviewed allow-list of functions; no `service_*` or `_internal` function is executable by any API role; no API role can insert or delete any table, only `parents.full_name/phone` is updatable; RLS on every table; the answer key, sessions, pepper, admin and tutor tables are unreadable by anon, parents, tutors and admins-as-authenticated; the secret answer never appears in any parent, tutor or admin report or table read. Parent A cannot read or act on parent B's children, orders, trial requests, consents, access, submissions (every function re-tested with B's ids). Tutors see only children with a confirmed enrolment in their own groups, lose sight when the enrolment is cancelled, cannot call admin functions. Child tokens: 256-bit, stored hashed, expiry, revoke, deleted-parent and withdrawn-consent all stop them, no cross-child or cross-unit use, sibling gets nothing from another child's purchase. Lockout cannot be bypassed by case, spaces, wildcards or SQL text. Orders: no price means no order; consent gates per format; no access from a pending order; wrong amount, wrong currency and replays refused; refund revokes access and a late webhook cannot flip it back; the price is copied at order time. Marking: mode or mark lies, unknown items and oversized batches are refused; counts are recomputed from the rows. Retention: practice answers 12-month and 90-day purge work; `delete_child_practice` works; `marketing_contact` is never required and never recorded unless ticked.

Front end (Playwright): stored XSS payloads in parent name, nickname, address, phone and trial note do not execute on any parent page or any owner admin tab; reflected payloads in `for`, `paid`, `ended`, `from`, `child`, `session_id` are inert (no innerHTML anywhere in the code); no inline scripts or handlers; no third-party request and no CSP violation; no personal data in any URL or console line (only a child uuid in `?child=`); the child token is in sessionStorage only and the record holds no PIN or parent data; the built `_headers` gives `/portal/*` a strict CSP (`script-src 'self'`, `frame-ancestors 'none'`, `connect-src` own origin plus Supabase), `Cache-Control: no-store`, `X-Frame-Options: DENY` (clickjacking covered); contrast passes AA in light and dark on all parent and child pages; visible focus ring, skip link, labels, one h1; no score, rank, streak, percent or pressure wording; child pages say "grown-up", parent pages say "parent"; every agreement box starts un-ticked in all three family types; address fields only for printed options.

## 4. Privacy checklist against the consent draft

| Item | Result |
|---|---|
| Consent types gate the right functions | contact+terms+online_practice gate sessions and submissions; format gates orders (online, both, workbook); live consents only gate enrolment; trial needs contact+terms. OK |
| marketing_contact never pre-ticked, never required | OK (UI and SQL) |
| Address only for workbook options | UI OK; API accepts more (M4) |
| 30-day address deletion | works for delivered orders only, manual (M1, M2) |
| Retention / deletion paths exist | practice answers yes; account deletion incomplete (H1) |
| Consent draft says open-box text is never collected, SUBMIT-TO-TUTOR/EXPLAIN-TO-TUTOR says explanations go to the tutor | the Worker stores only typed answers of auto items (200 chars) and a 60-char mark note, never self or open text; the draft and the BLANKET default disagree, so the owner should say which is wanted |
| Birth year | M11, lawyer |

## 5. Screenshots

104 PNGs in `portal/audit_shots/` (name pattern `NN_screen_WIDTH_light|dark.png`, widths 375 and 1100, light and dark): parent sign-up, agreements card for each family type (online, live, both), add child, My children (empty, with progress), child sign-in (and error), practice list (unpaid and paid), buy flow (workbook form, no-price state), order pending, orders list, trial request and sent, admin tabs (enrolments, book orders, prices, access, trials and previews, funnel, group report), live-family home. Contact sheet with captions: **`portal/audit_shots/portal_screens.pdf`** (27 pages). Regenerate: `python3 portal/audit_shots/audit_frontend.py && python3 portal/audit_shots/make_contact_sheet.py`. Raw log: `portal/audit_shots/frontend_audit_results.txt`; all visible text: `visible_text_dump.txt`.

## 6. New files
`portal/supabase/test/audit_run.sh`, `audit_lib.sql`, `audit_00_fixtures.sql` to `audit_07_recordings_preview.sql`; `portal/audit_shots/` (script, contact-sheet builder, PNGs, PDF, logs); this report. No existing file was modified.
