# Portal UI status (24 Oct 2026)

Branch `claude/great-fermi-1hv4vc`. Static front end under `portal/public`, built on the draft schema `portal/supabase/practice_submissions.sql`. **Not deployed, no live Supabase, Cloudflare or Stripe call, nothing sent, `website/dist` untouched.**

## What exists
1. **Sign-up / sign-in** (unchanged mechanics) and an **Agreements card per family type**: online (contact, terms, online_practice; printed-book delivery line), live group (contact, terms, recording, childs_work), both. marketing_contact and feedback_quotes optional, nothing pre-ticked. Wording from `docs/legal/online_submission_consent_draft.md`. `?for=online|live|both` presets the type. Version tags in `MI.VERSIONS` bumped to `...-2026-10d-draft`.
2. **Add child** (nickname, optional birth year, level, PIN), no enrolment needed (`/portal/children/`, `/portal/`).
3. **My children** dashboard: access per child, unit links, progress (answered / left for later / done on paper, "worth looking at together" from `practice_child_detail`), delete practice answers, quiet parent-only trial note.
4. **Child sign-in** via `child_start_session` (4-hour token in `sessionStorage 'mi-child'`, read by `practice/ext/public/sheet.js`).
5. **Practice list** from `child_session_overview(token)`: only entitled, published units; links `/practice/holiday/pN/NN/`, `/practice/ext/lNuNN/`, `/practice/term/lN/NN/`.
6. **Buy an extension book**: level, option, child, Singapore address (printed options), price from `list_ext_prices()`, order via `create_ext_order`, PayNow reference, cancel unpaid order. Stripe button hidden unless `PAYMENT_MODE=stripe`.
7. **Admin tabs**: Book orders (mark paid and give access, cancel, refund, posted/delivered, clear old addresses, owner price entry), Access (grant/revoke), Trials and previews, Funnel (+ children with no group), Group report (reading in words, alphabetical, paper column, common misconceptions).
8. **Trial class request** for any parent (`request_trial`), withdrawable.
9. SQL: `portal/supabase/portal_ui.sql` (new) and two fixes in `practice_submissions.sql` `create_ext_order` ("both" now needs online_practice; one unpaid order per child, level and kind).

## Tests (all pass locally)
`python3 portal/tests/portal_ui_test.py` (about 50 checks), `python3 portal/tests/frontend_test.py` (existing, updated), `bash portal/supabase/test/run_sql_test.sh` (includes the new `portal_ui_test.sql`).

## Mocked / not real
- `portal/tests/mock_supabase.js` re-implements the SQL functions' behaviour; only the SQL tests on local Postgres 16 with the repo's Supabase stand-in check the SQL, and not on real Supabase (PostgREST, JWT, `extensions` schema untested).
- `POST /api/stripe-create-ext-checkout` does not exist (the SQL helpers `service_ext_order_*` do). Card payment for books is therefore untested.
- The practice pages are not wired to the Worker (`practice/submit/handler.js` not routed); units exist in the database only after `make_keys.py` output is loaded and `published` set.
- Term practice URL pattern `/practice/term/lN/NN/` follows the plan; no term pages exist yet.
- Tutor login page not built: the group report is an admin tab (functions already allow the group's tutor).
- No email is sent anywhere (no order confirmations, no reminders).

## Needs the owner
- Supabase project and region (Singapore), then SQL order: `schema.sql`, `policies.sql`, `seed_groups.sql`, `practice_submissions.sql`, `portal_ui.sql` (scratch project first); optional `preview_class.sql`.
- Prices for the 18 book SKUs (enter in Admin > Book orders > Prices; none invented). Decision on the PDF format (PDF-DROP assumed).
- Approve privacy and consent wording; lawyer on the new optional **birth year** (the schema promised "no birth date"; a year is optional) and on Do Not Call for marketing_contact.
- Stripe account and the function above; Cloudflare secrets; the real domain (D9) for QR codes and Stripe URLs; `config.js` values.
- Short terms for extension books (one purchase = one child, refunds revoke access).
