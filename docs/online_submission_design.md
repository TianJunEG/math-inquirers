# Online submission to Math Inquirers: design and local prototype

Written 24 Oct 2026 on branch `claude/great-fermi-1hv4vc`. **Design plus a local prototype only.** Nothing is deployed, nothing is applied to the live Supabase project, nothing is published or sent, `website/dist` is untouched. Estimates are agent-hours. I am not a lawyer; privacy wording is a draft for the owner and a lawyer.

Owner decisions this design serves (`docs/terms/owner_decisions.md`): **SUBMIT-TO-TUTOR** (answers from the online workbooks are sent to us for reports), **auto-marking** ("the answers have to be auto marked too"), **D2** (holiday and term online practice only for enrolled families; extension only for the child it was bought for; a few open sample pages), **D8 amended** (paper-only questions stay online as self-checked), **extension books are bought online, one purchase = one child, with no enrolment needed**, and **extension books as a funnel to a trial class**. Related: `docs/online_versions_plan.md` (section 11), `docs/legal/online_submission_consent_draft.md`, lawyer question 11 in `docs/owner_kit/lawyer_email_draft.md`.

## 0. What is in the repo now

| File | What it is | Tested |
|---|---|---|
| `portal/supabase/practice_submissions.sql` | SQL draft, NOT applied: child sessions, units/tags/keys, submissions, extension orders and per-child access, tutors, trial requests, reports, retention, grants and RLS | `bash portal/supabase/test/run_sql_test.sh` runs `test/practice_submissions_test.sql` (about 100 assertions) on a throwaway local PostgreSQL 16 with the repo's Supabase stand-in. Not run on real Supabase. |
| `practice/submit/mark.js` | One marking module, used by the server and by tests (pure functions) | `node practice/submit/mark.test.mjs` (55 checks) |
| `practice/submit/handler.js` | `POST /api/practice/submit` handler (Web `Request`/`Response`), validation, re-marking, idempotency; `supabaseStore()` for production | `node practice/submit/handler.test.mjs` (34 checks, in-memory store) |
| `practice/submit/make_keys.py` | Builds the answer key and tags (JSON and an INSERT script) from a built online unit | run on `l2u01` |
| `practice/submit/stub_server.mjs`, `memory_store.mjs`, `test_submit.py` | Local stub endpoint + static server (one origin) and the browser test | `python3 practice/submit/test_submit.py`: all checks passed (Chromium) |
| `practice/ext/public/sheet.js` | Pilot runner with the send-to-tutor part **behind a flag that is OFF** | `python3 practice/ext/test_ext.py 2 1` still passes unchanged; flag tests in `test_submit.py` |
| `practice/submit/mock_report.py` and `docs/online_report_mock/` | Mock reports from synthetic data (HTML, PDF, phone screenshot) | rendered and looked at |

`worker/index.js` and `portal/functions` are **not** changed. Wiring is three lines at go-live (section 4).

---

## 1. Identity: reuse the portal's parent account and child profile

Owner direction: no new family code or link. What already exists (inspected): `portal/supabase/schema.sql` has `parents` (Supabase Auth user, `family_code`), `children` (parent-created: first name or nickname, level, PIN stored as a bcrypt hash, no child email), `groups`, `enrolments`, `consents` (append-only), `practice_attempts` (an unused placeholder), `admins`; `child_sign_in(family_code, name, pin)` (5 wrong PINs lock the child 15 minutes, identical silent failure); `portal/public/child/` is the child sign-in page and `portal/public/practice/` a placeholder; the portal README says outright that "child sign-in is a stub: when the practice area starts saving answers it must mint a real, short-lived token". `functions/`, `worker/` and the shop code hold no child data. `website/privacy.html` already lists "answers to practice questions" under photos of work and notes and names Supabase as a provider that may store data outside Singapore.

**How a child is identified when submitting**

1. The child opens the portal child page (`/portal/child/`), types the family code (the parent shows it in the portal, it is the existing code), the child's name and PIN: the existing flow.
2. The page now calls `child_start_session(code, name, pin)` (new, anon-callable like `child_sign_in`, which it calls inside, so the lockout and silent failure are the same). On success it returns a random 43-character token valid for **4 hours**; the database keeps only its SHA-256 hash. At most 5 live sessions per child. The token is held in `sessionStorage` (`mi-child`, which the placeholder practice page already uses for the name) and sent as `Authorization: Bearer ...` to the submit endpoint. No cookie, no password for the child, no child email.
3. A session is only issued if the parent currently has **contact + terms + online_practice** consents (section 8). Withdrawing one stops new sessions and new submissions at once (tested).
4. The token identifies exactly one child. The server looks the child up from the token hash; the browser never says which child it is.

**Families who are not in any group (extension book buyers).** Checked in the code: `add_child()` needs only a logged-in parent; `record_consents()` accepts any subset; only `enrol_child()` demands the four live-group consents. So a parent with no enrolment can sign up, add a child, give consents, buy a book and use it. Two changes are needed in the **portal UI** (not made): the "Agreements" card says the first four "are needed to join a live recorded group", which would scare off a book buyer; split it (section 8, matrix). `requiredOk()` should gate enrolling only. The SQL and RLS never require an enrolment or a group for a parent, the child or admin reports; only the **tutor** view needs a group (a tutor sees children with a confirmed enrolment in a group the tutor is assigned to). Children with no group are reported to the owner (admin view) and to their own parent.

**Reused:** `parents`, `children`, `groups`, `enrolments`, `consents`, `admins`, `is_admin()`, `child_sign_in`, `record_consents` (extended with 3 consent types), `practice_attempts` (becomes the per-question row: new columns instead of a second table), `delete_my_data()` (its `delete from children` now removes practice data through `ON DELETE CASCADE`; tested). **New:** `child_sessions`, `practice_units`, `practice_item_tags`, `practice_item_keys`, `practice_submissions`, `tutors`, `tutor_groups`, `ext_prices`, `ext_orders`, `child_book_access`, `trial_requests`, and the functions listed in the SQL header. The name `entitlements` is already used by `portal/supabase/delivery.sql` (expiring PDF download links), so per-child access is called `child_book_access`.

---

## 2. Data model (minimal) and row-level security

**Per submission** (`practice_submissions`, one row per child, unit and attempt; latest revision wins): child, unit key and version, the browser's attempt id (`client_sid`, makes a retry idempotent), revision number, first and latest server receive time, and counts (auto-marked, right, wrong, skipped, self-checked, ticked "got it", open). **Per question** (`practice_attempts`, extended): item id, `marking_mode`, `mark` (`right | wrong | skipped | self | open`), `answered`, the typed answer text (**auto items only**, at most 200 characters), partial credit detail for lists and boxes (`partial_found` of `partial_of`), the index of the listed wrong answer if it matched one of the item's `slips` (so reports can name the likely misconception), `self_result` (`got | not_yet | checked`), `correct` (kept for the old column: true, false, or null).

Decisions:
* **Name:** nothing new. The child profile's first name or nickname and level are the only identifiers; the parent is told to use a first name or nickname (existing rule). No photo, school, birth date, NRIC.
* **Right or wrong:** computed **on the server** from the stored key; the browser's mark is never read (the request has no field for it, and the handler rejects unknown fields; tested).
* **Time:** only the server's receive time. No per-question timers, no time on task, no client clock, nothing shown as pressure. If a tutor later wants a coarse "minutes spent" for planning, it can be added as one optional column; not collected now because it is not needed for the reports.
* **Free text is never stored** for self-check, paper-only and open items: only whether something was written (`answered`). Free text could contain anything; the reports do not need it.
* **`marking_mode`:** `auto` (marked by code), `self` (the child compares with the solution shown after Submit and may tick "I checked it / I got it / not yet"; includes the paper-only drawing, ruler and kit items from the D8 amendment), `none` (open items: many answers are right; never marked). Percentages and "right" counts use `auto` only.
* **Units are versioned:** `unit_version` = first 8 hex characters of the SHA-256 of the built data file; the page computes the same hash in the browser (tested equal), so a changed question can never be marked with an old key.

**Who can read and write (RLS, all tested locally)**

| Role | practice_submissions / practice_attempts | answer key (`practice_item_keys`) | other |
|---|---|---|---|
| anon, and the child's token | nothing directly | no grant | `child_start_session` only |
| Parent (Supabase Auth) | select own children's rows only | no grant | own orders, access rows, trial requests; no insert, update or delete anywhere (permission denied) |
| Tutor | select rows of children with a **confirmed** enrolment in a group assigned to that tutor (`tutor_groups`); a tutor of another group, or a child with no group, sees nothing; if the enrolment is not confirmed the tutor loses sight again | no grant | `tutor_group_practice`, `practice_child_detail` check the same rule |
| Admin (owner) | everything | no grant; reports never return keys | admin_* functions |
| service_role (the Worker only) | writes only through `service_practice_record`, which re-checks session, consent, access and row shape | read via `service_practice_keys` | |

The answer key lives in a table with RLS on, **no policy and no grant to anon or authenticated**, so no browser role (child token, parent, tutor) can read it through the API; the Worker reads it with the service role. `practice_item_tags` (strand, skill, tier, and the listed wrong answers with their kindly worded misconception) holds nothing that reveals a right answer and is only reachable through the report functions.

---

## 3. Who may practise what (entitlements), the purchase flow, and the shop mapping

| Unit kind | Access rule (enforced in the database, not only in the page) |
|---|---|
| Holiday and term (D2) | The family has a **confirmed enrolment** (any child of the parent) in a group at the unit's level. |
| Extension (D2, one purchase = one child) | A `child_book_access` row for **that child**, that book level, format `online` or `both`, status `active`. A purchase for child A does not unlock child B; a sibling needs a second purchase (tested). Whole book: all 10 units of the level. A `workbook`-only purchase gives no online access (tested). |
| Open sample pages | No sign-in. `service_practice_keys` refuses them (`unit`), so nothing is ever stored. |

`_can_access()` is called by both `service_practice_keys` and `service_practice_record`. The static page and its data file are public files on the static site, so the *page text* is not secret; see "gating the data file" at the end of this section.

**Purchase flow for an extension book (portal, to build)**
1. The parent has an account, a child profile and the consents (`contact`, `terms`; `online_practice` for online or both; `book_delivery` for workbook or both).
2. Buy a book: choose the **level** (6 books), the **format**, and **which child** it is for. For workbook or both: delivery name, Singapore address and 6-digit postal code only (`website/data/beta_schedule.json` `delivery.singapore_addresses_only` is true; the SQL checks the postal code shape).
3. `create_ext_order(child, level, format, ship...)` creates a pending order with a reference `MI-XXXXXX`; the amount is read from `ext_prices` (the browser sends no price). **No price in `ext_prices` means no order** (`price_not_set`): prices are on hold and none appears in this repo (tests use obviously fake values inside a throwaway database).
4. Pay: during the PayNow beta the owner ticks the order (`admin_mark_ext_order_paid`, same pattern as enrolments). Later by Stripe: a new function `portal/functions/api/stripe-create-ext-checkout.js` modelled on `stripe-create-checkout.js` (validates the user's token, reads the order with `service_ext_order_for_checkout`, creates a Checkout Session with `client_reference_id` = order id, stores the session with `service_ext_order_attach_session`). `stripe-webhook.js` gets a branch for these sessions that calls `service_ext_order_paid(order, session, amount, currency)`, which checks amount and currency like `service_mark_paid` does and is idempotent (`provider_ref` unique, so a retried webhook cannot grant twice). Refunds: `service_ext_order_refunded` on the refund event, or `admin_refund_ext_order` by hand (the README says there is no refund button yet either).
5. Paid creates the `child_book_access` row. The child signs in and the 10 units of that book are available automatically. No printed code.
6. Shipping (workbook or both): `ship_status` `to_ship → shipped → delivered`, set by the admin. The name, address and phone are cleared 30 days after delivery (`admin_clear_delivered_addresses`, the same rule as the existing workbook delivery wording; to confirm).

**Admin screens (extend `/portal/admin/`, not built):** Orders (list from `admin_list_ext_orders`, mark paid, refund, ship status, parent email, child), Access (grant or revoke for a child: `admin_grant_book_access`, `admin_revoke_book_access`, for the beta before the shop is live), Practice reports (section 4), Trial requests and funnel counts (section 6). Refund: the order becomes `refunded` and the access `refunded` immediately; the child's past answers stay and are deleted by the retention rule (tested).

**Proposed SKUs for `website/data/products.json`** (not edited; `status` stays `coming-soon`; **prices are on hold, none are invented**). Today each product is `ext-lN` with `formats: ["soft","physical"]`. Proposal: replace by three products per level:

| `id` | name | what it is | needs |
|---|---|---|---|
| `ext-l1-workbook` ... `ext-l6-workbook` | Extension Workbook, Level N (printed) | printed book posted to a Singapore address | delivery consent + address |
| `ext-l1-online` ... `ext-l6-online` | Extension Workbook, Level N (online) | online practice for one named child, 10 units | child profile, `online_practice` consent |
| `ext-l1-both` ... `ext-l6-both` | Extension Workbook, Level N (printed + online) | both, for one named child | both of the above |

The `id` matches `ext_prices.product_id` and the generated `ext_orders.product_id`. The shop's "Tell me when it's ready" list (`product_interest`) keeps its own `{product, format, qty}`; its format values would change with the SKUs.

**Open question: the PDF "soft" format.** The owner described three options (printed, online, both) and did not mention the PDF. `products.json` has `soft` and `physical`, and `delivery.sql` already builds expiring download links for PDFs. Decide: drop the PDF, keep it as a fourth option, or include a PDF with the online option. Until then this design treats the PDF as separate and does not touch it.

**Gating the data file (optional, recommended before launch).** The online page's data file contains the answers (needed to mark instantly in the browser, as the owner wants), and it is a public static file, so a determined person with the URL can read questions and answers without paying. Database access, submissions and reports are protected; the page content is not. Option A (cheap): accept, as the plan's D4 did, since the printed answer key is also sold. Option B (6 to 8 hours): keep the data file private (R2 or a Worker asset) and serve it from `GET /api/practice/unit/<key>` only to a valid child session with access; the page shell stays public; open sample pages carry their data inline. This protects paid content and holiday/term content but not secrecy of answers from a paying child. Option C (a different product): "answers only on the server" mode where the browser never gets the key and the server returns marks and solutions after Submit; no instant marking, so it conflicts with the owner's wish for instant marking. Recommend B before the books go on sale.

---

## 4. Submission API, validation, abuse, retries

**Where it runs.** The repo already serves `/api/*` from `worker/index.js` (Cloudflare Workers static assets), with the Supabase service role key as a Worker secret and Pages-style handlers. The marking code is JavaScript shared with tests, so the endpoint is a Worker route, not a Supabase edge function (an edge function would run the same code but add a second platform and a second place for secrets). Wiring at go-live:

```js
// worker/index.js
import { onRequest as practiceSubmit } from '../practice/submit/handler.js';
const ROUTES = { /* existing */ '/api/practice/submit': practiceSubmit };
```

Same origin as the pages, so the site CSP `connect-src 'self'` already allows it and **no CORS header is sent**; the handler also rejects a request whose `Origin` is not its own.

**Request:** `POST /api/practice/submit`, `Authorization: Bearer <child session token>`, JSON `{v:1, unit, unit_version, sid, rev, answers:{itemId: string | [strings] | null}, self:{itemId:'got'|'not_yet'|'checked'}}`. No marks, no child id, no unknown fields (rejected).

**Server steps:** (1) method, content type, origin, token shape, size (20 000 characters), JSON; (2) validation: unit and version patterns, `sid` UUID, `rev` 1 to 200, at most 400 items, item ids by pattern, answers at most 200 characters or at most 12 boxes, every item id must exist in the unit; (3) `service_practice_keys`: session valid and not revoked or expired, parent not deleted, consents currently granted, unit published and not an open sample, `_can_access`, rate limit; (4) re-mark every item from the key with `mark.js` (an item the browser did not send is a skipped item; a self or open item can only ever be `self` or `open`, whatever was sent); (5) `service_practice_record`: re-checks session, consent, access, and that each row's `marking_mode` matches the item and the mark is allowed for that mode; recomputes the counts itself; upserts. Errors are fixed words (`session`, `consent`, `entitlement`, `unit`, `rate`, ...) and never echo input.

**Rate limiting and abuse (three layers).** (a) A Cloudflare rate limiting rule on `/api/practice/*` per IP (owner step in the dashboard, for example 30 requests per minute; not set up). (b) In the database: at most **20 submissions per child per hour** and **3000 per hour in all**; revisions of one attempt are capped at 200. (c) PIN guessing is bounded by the existing lockout (5 wrong PINs, 15 minutes); sessions last 4 hours; a session token is useless without the parent's consent and access. Spam rows cannot be created without a child session, so an anonymous visitor can store nothing. A child who submits garbage only affects their own report. The worst case for a stolen token is submissions under one child for at most 4 hours, which the parent can wipe with one button.

**Idempotency.** The page makes one `sid` (UUID) per attempt and a revision number that goes up each Submit or self-check tick. Same `sid` and same `rev` is a no-op (`duplicate`); a lower `rev` arriving late is ignored (`stale`); a higher `rev` replaces the earlier rows. One child, one unit and one attempt is always one submission row (tested: lost response then retry gives one row).

**Offline, retry, closing the tab.** Answers are already saved on the child's device (the pilot's `localStorage`). On Submit the page tries to send; on a network error or HTTP 429 or 5xx it shows "Your answers are saved on this device. Sending to your tutor again soon.", retries after 5 s, 30 s and 2 min, and again when the browser comes back online or the tab becomes visible; after that it says it will try later. If the child **closes the tab before the send succeeds**, the next time the page is opened (same device) it sees "submitted and not yet sent" and sends (tested: offline, tab closed, reopened, sent once). If the child closes the tab **before pressing Submit**, nothing is sent (there is no hidden draft upload, which also keeps this honest for privacy); a "send my progress so far" draft option could be added if tutors want it, but then the consent line needs to say so. On 401 (session ended) it asks the child to sign in again and keeps the answers; on 403 it says to ask a grown-up (consent or access problem); 400s do not retry. No timers or countdowns are shown to the child.

---

## 5. Auto-marking

**Two markers, one rule set.** The child's browser marks instantly after Submit (the pilot behaviour, unchanged). The server marks again at submission with `practice/submit/mark.js` from the stored key; **reports use only the server mark**. For the pilot item types (number, boxes, list, choice) the server rules are the same as `sheet.js`'s `judge()`. The browser test compares the two on a mixed child (right, wrong, skipped, equivalent formats, lists in another order) and they agree on all 45 items; when the runner is generalised it should load `mark.js` itself so there is one implementation (Phase 0).

| Answer type | Right when | Notes |
|---|---|---|
| whole number | after removing spaces and thousands commas, equals the key: `1,000`, ` 1 000 `, `01000` accepted | `1000.0` and words are wrong (same as the browser). Wrong answers matching an item's listed `slips` get the misconception recorded |
| several boxes (`fields`) | every box right, in its box | detail records which boxes were right (partial) |
| choice | the chosen option text equals the key | never shuffled for `< = >` and True/False |
| list/set, any order | same numbers, same count, any order; typed with commas or spaces | partial: how many of the key's numbers were found; extras or duplicates make it wrong |
| list/set, ordered | same numbers in the same positions | |
| fraction (Phase 2) | equal value **and** lowest terms, unless the item says any equivalent fraction is right (`equivalent`); mixed or improper both read | `2/4` for key `1/2` is wrong with reason `not_simplest` (a kind message), `3/0` is wrong |
| decimal (Phase 2) | equal as a number: `0.5`, `0.50`, `.5`; a decimal comma is wrong (Singapore) | exact decimal comparison, no floating point |
| text (Phase 2) | equals any listed answer ignoring case, spacing, hyphens and a final full stop (`NW`, `north west`) | for directions, names, letters, days |
| self-check, incl. paper-only (`marking_mode` self) | **never auto-marked.** The child compares with the solution (and the figure of the correct drawing where there is one) and may tick "I checked it / I got it / not yet"; recorded as `self`, with the tick | reported separately as "checked on paper"; excluded from every percentage |
| open (`marking_mode` none) | **not marked**, flagged "not auto-marked", excluded from percentages | items whose book explanation starts "Open." |
| skipped / blank | `skipped` (not wrong). Some boxes blank and others filled: wrong with partial detail | |

**What cannot be auto-marked, and the share** (from the plan's generator coverage, `docs/online_versions_plan.md` section 11): extension 10 open parts of 2,733 (0.4%) plus the paper-only drawing items, which are self-checked and need a solution figure rather than a checker; with the pilot rules 90.0% of extension parts are auto-marked, and 99.6% once the Phase 2 text, fraction and decimal rules are used; Term Level 1: 39 of 509 items are self-check (7.7%), 92.3% auto; holiday: about 75% expected auto, the rest self-checked or open (not yet structured).

**Tests** (`mark.test.mjs`, 55 checks): wrong, right, thousands comma, spaces, leading zero, `1000.0` wrong, words wrong, empty / spaces / null as skipped, negative numbers, choice right / wrong / skipped, several boxes (one wrong, one blank, all blank, swapped), lists in any order, spaces only, partial (2 of 3), extra, duplicate, ordered lists, fractions (simplest, equivalent, mixed, zero denominator, a decimal typed for a fraction), decimals (trailing zero, no leading zero, decimal comma, text), text (case, spacing, full stop, wrong, blank), self-check and paper-only never marked, open never marked, unknown type throws. `handler.test.mjs` (34 checks) proves a client claim of "correct" is ignored, a self or open item cannot become right, misconception slips and partial detail are stored, free text of self and open items is not stored, duplicates and stale revisions, rejected requests store nothing, consent and rate errors. `test_submit.py` is the end-to-end browser check.

---

## 6. Reports

Mock output from **synthetic** data: `docs/online_report_mock/mock_reports.pdf` (and `.html`, plus a phone screenshot). Regenerate with `python3 practice/submit/mock_report.py`.

* **A. Parent summary, per child** (parent portal, and by email only with the marketing/contact consent; section 7). Kind words: "What went well", "Worth looking at together" (the likely misconception in plain words, with a hint to ask the child to explain), "Left for later" (skipped questions, framed as fine), "Checked on paper" (separately), "A next step, if you would like one". **No scores, no percentages, no streaks, no ranking, no comparison with other children, no "behind"; no time.**
* **B. Tutor view of one child:** every question with the mark (right / to look at again / skipped / checked on paper / open), the likely misconception for mistakes (from the item's `slips`, matched on the server), partial credit for lists and boxes, and a by-skill table using the MOE strand and skill tags. Counts are for auto-marked questions only. Strand labels are tutor-facing (the term lessons' `moe.note` already forbids "MOE-aligned" claims on child or parent pages; the parent report uses plain skill names only).
* **C. Tutor view of a group:** one row per child, **alphabetical, never sorted by result**, each skill shown as words and a symbol (going well / some right and some to look at / worth practising together / not enough answers to say, needing at least 2 auto-marked answers), a "has not sent answers yet" row, and the most common misconceptions across the group for planning the next lesson. Tutors see only children with a confirmed enrolment in their own group.
* **D. Owner view** (admin page): the same reports for **children with no group** (extension-only families), and the funnel counts (section 7).

**Strengths and needs by topic** need per-item MOE strand and skill tags. The term lesson JSON carries `moe.strand` and topics; the extension JSON has only a unit topic, so `make_keys.py` falls back to the unit topic and accepts `practice/submit/tags/<unit>.json` for hand-written tags (about 1 minute per item for 1,330 items: 20 to 25 hours). The mock report uses synthetic tags.

---

## 7. Funnel to a trial class (extension book families; parents only, never children)

Owner decision: the extension book and its online practice invite parents to ask for a free trial class.

**1. Where the call to action appears**
* **In the printed extension book:** one page near the front or back with a QR code and a short link to the parent's trial request page. Needs a layout slot in each book (a reprint cost) and **the domain, which is still unknown (owner decision D9)**; until then the page cannot be printed with a real link.
* **On the post-purchase page** (portal, after paying): a short, plain parent-facing card.
* **In the online practice after Submit:** a **parent-facing panel only**, below the marked page and hidden from the child's flow (for example under "For grown-ups", or only on the parent's report), with no pressure and no mention of the child's mistakes. Never a pop-up, never on the question pages.
* **In the parent report** (section 6A) as a "next step, if you would like one": the suggestion is derived from the child's strengths and needs and the matching holiday or term level (for example "a small group class could help with place value and comparing numbers").

**2. The sign-up path for non-enrolled families.** What exists: the website's WhatsApp registration form and `mi_signup.html`; the anonymous "Request another time" form (`interest_requests`, for planning class times, no account); the shop's "Tell me when it's ready"; portal enrolment in a group (needs the live-group consents and payment). There is no trial class path. Reusing `interest_requests` would mix an anonymous planning list with named requests and lose the child and the source, so the draft adds **`trial_requests`** (parent account, optional child, level, preferred times, note, **source** = book / post_purchase / after_submit / report / website, status new → contacted → attended → enrolled / declined / withdrawn, 12-month expiry), `request_trial()` (parent only, needs `contact` and `terms`, at most 3 a day), `withdraw_trial_request()`, and the admin list and status functions (tested). Booking the actual trial slot stays a WhatsApp or email follow-up by the owner at first.

**3. Consent.** A request the parent makes themselves needs only `contact` and `terms`. A **separate, optional `marketing_contact` consent** (never pre-ticked, stored as an append-only consent row with versions, withdraw by unticking, with "stop" in every message) is needed before **we** start a message, such as the report email with a next-step line or a later reminder. Practice answers are **not** used for marketing beyond the parent-facing suggestion inside the parent's own report or portal; they are never used to message a parent who has not ticked `marketing_contact`, never shown to another family, never used to compare children, and never used for advertising. Singapore: the PDPA's Do Not Call provisions apply to marketing to Singapore telephone numbers (including WhatsApp and SMS), so ask the lawyer whether a clear written consent is enough or whether the registry must also be checked (question 11).

**4. Tone rules.** Honest and plain; no countdowns, scarcity or "limited seats" language; no scores or percentages; no comparison with other children; no "your child is behind"; never aimed at the child; a trial request is easy to withdraw; the child's flow never changes depending on whether a parent asks for a trial.

**5. Measurement for the owner.** `admin_funnel_counts()` returns counts from rows that already exist: books paid, families who bought, children who started the online practice, trial requests (total and by source), trial attended, enrolled afterwards. **No tracking cookies, no analytics scripts, no per-visitor records**; the source of a request is one field set by the page the parent clicked from. (Counts of "visited the page" are not available by design.)

---

## 8. Privacy and compliance checklist (PDPA Singapore)

Drafts of the exact consent lines, privacy page additions, retention and deletion are in `docs/legal/online_submission_consent_draft.md` (not applied to the live pages). Summary:

**Consent matrix** (consent type by family type; also in the draft file):

| Consent | Live group family | Extension, online or both, no group | Extension, workbook only |
|---|---|---|---|
| contact, terms | needed | needed | needed |
| recording, childs_work | needed | not asked | not asked |
| **online_practice (new)** | needed to send answers | needed | not asked |
| **book_delivery (new)** | not asked | needed if a posted book | needed |
| **marketing_contact (new, optional)** | optional | optional | optional |

| PDPA item | How the design handles it |
|---|---|
| Consent, children under 13 | The parent (who creates the child profile) gives a specific, withdrawable consent for this purpose; the child's own PIN sign-in is not a consent. The portal stores the consent as an append-only row with the terms and privacy versions (`MI.VERSIONS` must be bumped when the wording changes). |
| Notification and purpose limitation | Privacy page additions (what, why, who, how long); the data are used for marking, reports to the parent and tutor or owner, and improving materials; not for advertising; not for comparing children. |
| Data minimisation | First name or nickname and level only; no free text from open or paper items; no timers; no client clock; no photos, school or NRIC. |
| Retention (suggested, to confirm) | Answers: 12 months after the last submission, or 90 days after the child's online access ends or the program ends, whichever is sooner. Orders: 7 years, no address. Delivery details: cleared 30 days after delivery. Trial requests: 12 months. Sessions: 4 hours, removed within 7 days. `admin_purge_expired_practice()` does the first rule (tested) and runs from the admin page or pg_cron. The existing privacy page promises "work and answers 90 days after the program ends"; the draft keeps that and adds the 12-month cap. |
| Access, correction, withdrawal | The parent sees the same report in the portal; withdraw by unticking; "delete this child's practice answers" button (`delete_child_practice`, tested); account deletion cascades (tested). |
| Data protection officer contact | The privacy page still shows a placeholder Gmail address `[to be changed later]`; replace it before launch. |
| Overseas transfer | Supabase region: **the portal README says to pick Singapore**; confirm the real project's region (not checked here) and say it on the page. Cloudflare's Worker runs at edge locations worldwide and Stripe processes payments, so answers pass through servers outside Singapore even with a Singapore database: name them in the notice and have the lawyer confirm the transfer wording. |
| Security | RLS on every new table, no grants to anon or authenticated beyond selects with policies, keys unreadable by any browser role, hashed session tokens, service role only in the Worker secrets, fixed error words, no personal data in logs (the handler logs nothing). Run `get_advisors` on the scratch project. |
| Breach | The existing plan applies; PDPC and affected parents for a notifiable breach. |
| Lawyer | Question 11 added to `docs/owner_kit/lawyer_email_draft.md` (questions 1 to 10 untouched). |

---

## 9. The pilot runner flag (`practice/ext/public/sheet.js`)

Default OFF. Nothing is sent unless **both** are true: the page sets `window.MI_SUBMIT = {endpoint: '/api/practice/submit'}` (the built pilot page does not) **and** a child token exists (`MI_SUBMIT.token` or `sessionStorage 'mi-child'.token` from the portal sign-in). Without the flag, or with the flag but no token, the page behaves exactly as before and makes **no** request other than loading its own files (tested twice, including that no tutor note is shown). With it on: a plain line before Submit ("When you press Submit, your answers are also sent to your tutor."), the send after Submit with the retry behaviour in section 4, optional "I checked it / I got it / not yet" buttons on self-check items, and a status line ("Sent to your tutor."). It sends answers only, never a mark; for self-check items it sends "(written)" instead of the text. The existing test `python3 practice/ext/test_ext.py 2 1` passes unchanged after the edit.

How to run everything locally: `python3 practice/ext/build_ext.py 2 1 && python3 practice/submit/make_keys.py 2 1 && python3 practice/submit/test_submit.py`; `node practice/submit/mark.test.mjs`; `node practice/submit/handler.test.mjs`; `bash portal/supabase/test/run_sql_test.sh`.

## 10. What the owner must decide or do

1. **Approve the privacy wording** (consent lines, page additions, retention) and send question 11 to the lawyer; nothing goes live before that. Name the **data protection contact** (replace the stand-in Gmail).
2. **Supabase region:** confirm the real project is in Singapore (README step 1) and tell the lawyer about Cloudflare edge and Stripe.
3. **Domain (D9):** needed for the QR code and short link in the printed book and for the Cloudflare route and Stripe URLs.
4. **Prices** for the 18 SKUs (3 per level) or for the formats you keep; `ext_prices` stays empty until then, so no order can be made. Decide **the PDF "soft" format** (drop, keep, or bundle with online).
5. **Who sees which reports:** this design says parent: own child; tutor: children in their own groups; owner: all, including children with no group. Confirm, and name the tutors to add to `tutors` and `tutor_groups`.
6. **Retention periods** (12 months, 90 days, 30 days for addresses, 12 months for trial requests).
7. **Gate the data file?** (section 3, option A, B or C; recommended B before sale.)
8. **Trial class path:** confirm booking is a manual follow-up at first, and who answers `trial_requests`; whether a Do Not Call registry check is done by you.
9. **Terms for extension books** (one purchase = one child, refunds revoke access, printed book returns): a short new section or page (the lawyer decides).
10. **Shop and portal build:** approve building the buy flow, the consent card split, parent report page and admin tabs (about 110 to 160 agent-hours in total, plan section 11). Owner-side steps when you are ready: create a scratch Supabase project to run the SQL, set Worker secrets, the Cloudflare rate limit rule, the Stripe checklist in the portal README.

## 11. Not verified (honest list)

* The SQL ran only on local PostgreSQL 16 with the repo's stand-in for Supabase's auth schema and roles, not on real Supabase (how `auth.uid()` reads the JWT, the `extensions` schema, definer functions called through PostgREST). Try it on a scratch project first.
* The Worker route has not run on Cloudflare; the `supabaseStore()` calls to PostgREST are untested against real Supabase (the tests use an in-memory store). The generated key SQL from `make_keys.py` has not been loaded into a database.
* No portal page, consent card, purchase flow or admin tab exists yet; the Stripe functions are described, not written.
* The mark rules for fractions, decimals and text are tested in isolation but no built unit uses them yet.
* Only L2 unit 1 has a built online page and keys; strand and skill tags for it fall back to the unit topic.
* The mock reports are synthetic and have not been shown to a tutor or a parent; wording is a first draft.
