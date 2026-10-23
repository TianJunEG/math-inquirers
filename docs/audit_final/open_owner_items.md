# Open owner items (from the final audits, 23 Oct 2026)

Items below need the owner or live-system access. Everything else from the schedule, hygiene and payments audits was fixed in the repo.

## Payments and database
1. Apply `portal/supabase/stripe_migration.sql` (plus `delivery.sql`, `product_interest.sql`) to the live Supabase. NOT applied by anyone yet. It now also contains: duplicate/late payment flags, refunded payments can no longer flip to paid, and expiry of unpaid seat reservations (replaces `enrol_child`). Keep PAYMENT_MODE = paynow_manual until done and a Stripe test-mode payment works end to end.
2. Reservation expiry period: default 7 days (`_expire_stale_reservations`). Confirm or change. Optional: schedule `select public.expire_unpaid_reservations(7)` (pg_cron) so seats free even when nobody enrols.
3. Late payment after expiry returns `paid_enrolment_cancelled` and is logged "NEEDS OWNER ATTENTION": decide re-open the seat or refund. Same for `duplicate_payment`: refund the extra payment by hand in Stripe.
4. Shop prices are on hold, so the soft-copy amount check is a stub (`SHOP_PRICES_CENTS` in `portal/functions/_shared/delivery.js` is empty). When prices are decided, fill the table; until then correct Payment Link prices are the only protection.
5. Not done (need design or live access): F4 per-parent cap on open reservations and server-side email confirmation, F5 prorated fee/instalments/5% discount, F7 child PIN strength, F8 server-side child session, F9 checkout idempotency key, F10 interest-form abuse, L1 webhook body size cap, L2 Cloudflare rate rules, L4 CSPRNG for codes. Auth settings (email confirmation) must be checked in the live dashboard.

## Schedule
6. R1-R3 vs Levels 1-3 clash on Thu 24 Dec (reserve groups share the published last-lesson times). Decide the week-5 times for reserves (suggestion: Wed 23 Dec same times) and store them in `docs/schedule/beta_reserved.json`.
7. R4 (Sun 2:00pm) has no buffer after church/lunch: move to 2:15pm or confirm.
8. Thu 7:30pm and Sun 7:15pm 2027 options are offered to Level 5 (age 10-12): keep or make Level 6 only.
9. Verify MOE 2026 and 2027 term dates on moe.gov.sg (only secondary sources were available).

## Hygiene and legal
10. Repository weight (.git about 3.5 GB; term/l1/out history). Decide before any push: `git gc`, stop tracking generated `term/l1/out`, or rewrite history. Nothing was done to history.
11. Stray `.whl` files in the repo root are now git-ignored but still on disk: delete them if not needed (they were not removed).
12. Fredoka copyright line to confirm upstream; Supabase JS (MIT) notice and Mi artwork licence to attach (see `website/licenses/THIRD_PARTY_NOTICES.txt`). Add a footer credit/link to `/licenses/` if wanted.
13. Public privacy page still shows the owner's personal Gmail as contact (S1): replace before any `--public` build.
14. Tracked generated output (website/dist is deliberately tracked; term/l1/out, duplicate outputs/print, tracked zips, root workbook_body.html), LICENSE file, README full rewrite, P4/P5 stem rewording (C3), redaction of the account email in `schedule_and_calendar.md` and fake key-like strings in the adversarial test file: not changed here (outside allowed paths or need a decision).
