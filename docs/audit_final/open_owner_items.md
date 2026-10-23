# Open owner items (from the final audits, 23 Oct 2026)

Items below need the owner or live-system access. Everything else from the schedule, hygiene and payments audits was fixed in the repo.

## Payments and database
1. Apply `portal/supabase/stripe_migration.sql` (plus `delivery.sql`, `product_interest.sql`) to the live Supabase. NOT applied by anyone yet. It now also contains: duplicate/late payment flags, refunded payments can no longer flip to paid, and expiry of unpaid seat reservations (replaces `enrol_child`). Keep PAYMENT_MODE = paynow_manual until done and a Stripe test-mode payment works end to end.
2. Reservation expiry period: default 7 days (`_expire_stale_reservations`). Confirm or change. Optional: schedule `select public.expire_unpaid_reservations(7)` (pg_cron) so seats free even when nobody enrols.
3. Late payment after expiry returns `paid_enrolment_cancelled` and is logged "NEEDS OWNER ATTENTION": decide re-open the seat or refund. Same for `duplicate_payment`: refund the extra payment by hand in Stripe.
4. Shop prices are on hold, so the soft-copy amount check is a stub (`SHOP_PRICES_CENTS` in `portal/functions/_shared/delivery.js` is empty). When prices are decided, fill the table; until then correct Payment Link prices are the only protection.
5. Not done (need design or live access): F4 per-parent cap on open reservations and server-side email confirmation, F5 prorated fee/instalments/5% discount, F7 child PIN strength, F8 server-side child session, F9 checkout idempotency key, F10 interest-form abuse, L1 webhook body size cap, L2 Cloudflare rate rules, L4 CSPRNG for codes. Auth settings (email confirmation) must be checked in the live dashboard.

## Schedule
6. DECIDED 23 Oct 2026: R1-R3 week-5 lessons move from Thu 24 Dec to Wed 23 Dec at the same times (stored in `docs/schedule/beta_reserved.json`). STILL OPEN: their own Wednesday lesson of week 5 is the same day and time, so one of the two needs another slot.
7. DECIDED 23 Oct 2026: Sunday 2:00pm is not available; R4 withdrawn. PROPOSED R4B (Sat 9:00-10:30am + Sun 6:00-7:30pm, Levels 5-6) awaits the owner's yes.
7a. REPLACE LATER: pypteltd@gmail.com is the business and data-protection contact FOR NOW (owner, 23 Oct 2026). It appears in `website/privacy.html` and `website/terms.html` (marked with a bracket note). Replace it with the business address when the owner gives one, and give the registered office address (still a placeholder in `website/terms.html`).
8. Thu 7:30pm and Sun 7:15pm 2027 options are offered to Level 5 (age 10-12): keep or make Level 6 only.
9. Verify MOE 2026 and 2027 term dates on moe.gov.sg (only secondary sources were available).

## Hygiene and legal
10. Repository weight (.git about 3.5 GB; term/l1/out history). Decide before any push: `git gc`, stop tracking generated `term/l1/out`, or rewrite history. Nothing was done to history.
11. Stray `.whl` files in the repo root are now git-ignored but still on disk: delete them if not needed (they were not removed).
12. Fredoka copyright line to confirm upstream; Supabase JS (MIT) notice and Mi artwork licence to attach (see `website/licenses/THIRD_PARTY_NOTICES.txt`). Add a footer credit/link to `/licenses/` if wanted.
13. Public privacy page still shows the owner's personal Gmail as contact (S1): replace before any `--public` build.
14. Tracked generated output (website/dist is deliberately tracked; term/l1/out, duplicate outputs/print, tracked zips, root workbook_body.html), LICENSE file, README full rewrite, P4/P5 stem rewording (C3), redaction of the account email in `schedule_and_calendar.md` and fake key-like strings in the adversarial test file: not changed here (outside allowed paths or need a decision).
