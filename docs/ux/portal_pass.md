# Portal UI/UX pass

Scope: `portal/public/` (parent portal, child sign-in, practice placeholder, admin incl. Shop interest, order/download page).
Method: Playwright + preinstalled Chromium, stubbed Supabase client and mocked `/api/order-links`. Screens rendered at 400px and 1280px, light and dark, with loading, empty, error, success, very long names and 25-30 rows. Screenshots were viewed, not just generated.

## Checked
Login/signup/magic link and their errors, not-configured page, load-failure, empty and full parent view, child sign-in and error, admin login, not-admin, enrolments, Interest, Shop interest (data, empty, missing-SQL error, generic error), order page (ready, pending, rate limited, error, no session id). No horizontal page overflow at 400px on any screen.

## Changed
- **Errors never leak internals.** `errText` used to pass through any message under 160 characters (e.g. "AuthApiError: Database error ... /auth/v1/signup"). Now only our own wording (`MI.say`) or known codes are shown; everything else becomes one plain "Something went wrong on our side... message us on WhatsApp". Added friendly text for already-registered, unconfirmed email, rate limit, short password, offline, expired session.
- **Parent next action.** "Next step" banner (pay / add child / save agreements / choose group) with a jump link; empty-children message; "Forgot it? Use Magic link" and password-length hints; a proper "could not load your account" screen with Try again / Log out (before, a load failure showed the login form again).
- **Admin tables on mobile** were horizontally scrolled with the Mark paid button off-screen. Under 640px every admin table is now one labelled card per row (`MI.stack`). Desktop unchanged.
- Admin: action errors now show as errors (red, alert) not blue info; "Loading..." on tab switch; empty state for filtered enrolments; payment method shown as "PayNow"; amount/group/pill no longer wrap mid-word; clearer "not an owner" text.
- **Order page**: each download is a large button with "Link works until <date>. N downloads left."; expired, used-up or withdrawn links say so and point to WhatsApp; WhatsApp fallback (public business number already on the site) with a pre-filled message containing the order number, shown on every failure state too; same header and card look as the rest of the portal; error states styled as errors.
- Accessibility: focus ring now navy/yellow (coral on white was about 2.5:1); danger button contrast fixed in both themes (white on red failed, and dark mode was worse); skip link; removed `aria-live` from whole `<main>` (re-announced entire pages); 44px tap targets for small buttons and tabs on touch devices; long names wrap.
- Test updates: `portal/tests/frontend_test.py` one selector (`.msg.ok` for admin success).

## Found, not changed
- Destructive actions already confirm (remove child, cancel reservation, mark paid, delete request, purge, delete my data needs typed DELETE). Kept; native `confirm()` is plain but reliable on mobile.
- "Reserve a place" is disabled with no hint until a group is picked. Left; low risk.
- No password-reset flow; magic link is the recovery path (now mentioned). A real reset flow touches auth config.
- Focus is not moved after a re-render (page redraws replace content); would need a larger refactor.
- Admin error cards for missing SQL still name `portal/supabase/*.sql` files. Owner-only screen, useful, so kept.
- Order links with `remaining` 0 are treated as unavailable client-side; the server remains the authority.
- `portal/supabase/test` SQL tests not run (need Postgres); no SQL touched. `node --test` on both `.mjs` files pass; front-end test passes.

## Owner decisions
1. Confirm the WhatsApp number +65 9880 5962 is the right fallback for download problems (hard-coded in `order/index.html` and `order.js`).
2. Replace native `confirm()` with in-page dialogs? Nicer, but more code.
3. Add a real "forgot password" flow, or keep magic link only?
4. Should "Awaiting payment" admin rows also offer a "cancel reservation" action?
