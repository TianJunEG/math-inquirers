# Portal UI and database draft: round-1 fixes

Branch `claude/great-fermi-1hv4vc`, 24 Oct 2026. Nothing applied to a live database, nothing deployed, `website/dist` untouched. All SQL was edited in the draft files and run only on a throwaway local PostgreSQL 16 with the repo's Supabase stand-in (real Supabase, PostgREST, JWT and Cloudflare header behaviour are still untested).

## Results of the suites

| Suite | Before | After |
|---|---|---|
| `bash portal/supabase/test/run_sql_test.sh` | pass | pass (PINs in the tests changed to non-weak ones; one 90-day assertion rewritten for the new rule) |
| `run_delivery_test.sh`, `run_preview_test.sh` | pass | pass |
| `bash portal/supabase/test/audit_run.sh` | 209 PASS, 17 FAIL | **281 PASS, 0 FAIL** (new `audit_08_round1_fixes.sql`; `audit_04` online-address check rewritten to expect a rejection) |
| `python3 portal/audit_shots/audit_frontend.py` | 25 PASS, 7 FAIL | **33 PASS, 0 FAIL** (the idle NOTE became a check; `program` removed from the US-spelling list, see L8) |
| `python3 portal/tests/portal_ui_test.py`, `frontend_test.py` | pass | pass (10 new checks; the Stripe stand-in now answers on `https://checkout.stripe.com/`) |
| `node portal/tests/delivery.test.mjs`, `functions.test.mjs` | 23, 17 | 23, 17 |
| `practice/submit`: `handler.test.mjs`, `mark.test.mjs`, `test_submit.py` | pass | 53, 364, pass |
| `python3 website/tests/headers_test.py` (new, scratch `--out`) | n/a | 50 checks |

Previous screenshots in `portal/audit_shots/*.png` and the PDF are the audited state (before the fixes). The pre-fix log is kept as `frontend_audit_results_before_fixes.txt`; `python3 portal/audit_shots/audit_frontend.py` regenerates the pictures.

## Closed / not closed

| ID | Finding | Status | Where / how |
|---|---|---|---|
| H1 | Delete my data leaves orders, notes | **Closed** | `delete_my_data()` in `practice_submissions.sql`: clears name, address, postal, phone and nickname on every book order, cancels unpaid orders, flags paid ones `refund_due`, deletes trial requests, recording views, preview registrations and attendance hashes (via `_pv_delete_person`); children and sessions cascade. Tests audit_05, audit_08 |
| H1b | Interest-form rows (`interest_requests`, `product_interest`) are not tied to an account | **Not closed** | They hold only a contact string, not a parent id; they keep their own delete buttons. Deleting them on "delete my data" would need matching by email/phone |
| D2 | Family rule: one confirmed place opens practice for every sibling | **Open (owner to confirm)** | Unchanged, noted in audit_03 |
| M1 | Address retention gap | **Closed** | `_purge_ext_addresses()`: delivered +30 d, shipped +30 d, cancelled/refunded at once, paid and never posted +90 d (flagged), unpaid +14 d cancelled |
| M2 | Retention manual; 90 days counted from submission | **Closed** (not enabled) | `run_retention_jobs()` + `_purge_*`; 90 days now count from when access ended; pg_cron lines in `portal/README.md`, **nothing scheduled by any file** |
| M2b | Live-group answers 90 days after the programme ends | **Not closed** | `admin_purge_practice_for_group()` stays manual; `groups` has no end date |
| M2c | Payments / consents / deletion_requests of deleted accounts | **Not closed** | Lawyer's period; no rule written |
| M3 | Payment after cancel lost | **Closed** | `service_ext_order_paid` records `paid_after_cancel_at`, sets `refund_due`, idempotent, grants nothing; admin "Refund due" tab, `admin_reinstate_ext_order` (online only), `admin_resolve_ext_refund` |
| M4 | Address on online order; NULL postal | **Closed** | `create_ext_order`: online + any ship field -> `bad_address`; printed needs 6 digits, sector 01-82 |
| M5 | Delete child drops paid access | **Closed** | `delete_child` refuses (`has_online_access`); `transfer_book_access`; `delete_child_and_access(child, true)`; UI panel with explicit tick; pending orders cancelled |
| M6 | `client_sid` reuse; duplicate `item_id` | **Closed** | `sid_unit` and `bad_rows` errors |
| M7 | PIN lockout flat; weak PINs | **Closed** | 15 min / 1 h / 6 h / 24 h, parent alert (`my_pin_alerts`), `_pin_check` weak list incl. birth-year patterns, mirrored in the form |
| M7b | Family code guessing has no per-IP throttle | **Not closed** | Supabase/Cloudflare rate limits only; code alone gives nothing |
| M8 | "Agreements saved." with empty boxes | **Closed** | Warning names the missing agreements |
| M9 | Focus lost after actions | **Closed** | Result message takes focus; focus restored to the same control on redraw; admin too |
| M10 | Shared origin, no `/practice/*` headers | **Partly closed** | Strict `/practice` and `/practice/*` headers in `build_site.py` (tested in a scratch dir); inline config scripts of the generators are moved to files by `--practice-dir`, otherwise the build warns. **Shared-origin risk remains**; recommendation (subdomains) in `portal/README.md`. The generators and the real Cloudflare header behaviour are untested |
| M11 | Birth year | **Partly closed** | Long-term preview store holds keyed hashes of year-1/year/year+1 only; readable year purged 30 days after the class. The preview form still requires a year (not made optional). Lawyer to decide both together |
| M12 | Long nickname overflow | **Closed** | `overflow-wrap`; checked at 375 and 320 |
| L1 | Stripe redirect not validated | **Closed** | `MI.goToStripe`: https, host `checkout.stripe.com`, no userinfo. The endpoint `/api/stripe-create-ext-checkout` **still does not exist** |
| L2 | Order rate limit; postal sector; ship status guard | **Closed** | 12 orders per parent per hour; sector check; only paid orders can be posted |
| L3 | `pg_temp` in `search_path` | **Closed** | All SECURITY DEFINER functions in all draft SQL files |
| L4 | Worker reply marks per item | **Closed** | `practice/submit/handler.js` returns only `ok, rev, duplicate, stale` (the page never used the marks). Revisions up to 200 and the 20 per hour count are unchanged |
| L5 | Preview class abuse / oracle | **Not closed** | No captcha; by design |
| L6 | Child token idle | **Closed** (partly client-side) | 30 min idle sign-out on the list page, Sign out at the top, server refuses a token idle for 60 min. Practice pages (`sheet.js`, other agent) have no idle timer of their own |
| L7 | Link tap targets | **Closed** | Portal links 24 px minimum in sentences, 44 px standalone. Site footer already 12 px padding |
| L8 | "program" spelling; "No orders yet" | **Decision** | The whole site (terms, privacy, sign-up) writes "program" and keeps "Programme" for the Gifted Education Programme; the consent line must match privacy.html, so it stays "program". "No orders yet" fixed. Long consent paragraph not summarised |
| L9 | Trial slots length; phone overwrite | **Closed** | 40-character labels; account phone only changed when empty or ticked |
| L10 | PayNow placeholder | **Closed** | Shows "message us for the PayNow details" until the build sets `PORTAL_PAYNOW_TO` |
| X1 | `practice_item_keys.rules`, `explain_text` | **Closed** (coordinator request) | `make_keys.py` SQL output and `service_practice_keys/record` carry them; explanation never returned to the browser; docs updated. Consent / footer wording **flagged for owner sign-off**, client text unchanged |

## Still failing or untested
No suite fails. Untested: real Supabase/PostgREST/JWT, Cloudflare `_headers` joining, the Worker wire-up, any Stripe call. Files outside my paths that were changed: `practice/submit/handler.js` and `handler.test.mjs` (reply without marks) and `make_keys.py` (SQL output), as requested.
