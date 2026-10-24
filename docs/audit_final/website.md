# Independent audit: public website (website/dist and sources)

Audited working tree on branch claude/great-fermi-1hv4vc at HEAD b81864f (several website files, including dist/, had uncommitted edits from other agents while auditing; the shop was mid-build). Method: served dist locally, rendered 14 pages at 1280 and 400 px, light and dark (no console errors, no horizontal scroll, all pages have one h1, no missing alt); stripped and read all page text; compared with website/data/beta_schedule.json and live Supabase `groups` (read-only SQL); ran website/tests/interest_test.py plus own form probes.

## Verdict: Not ready for public launch (fine as a private preview). Ready after fixing the High items and the Medium refund/price items.

## Findings

### High
1. **Refund policy contradicts itself across pages.** Home FAQ "What if we need to cancel?" (dist/index.html line ~99) and parent-questions hub (b-cancel answer) promise a refund within 60 days of paying, pro rata after lessons start. Home Price box (JS line ~380: "Beta fees are not refundable, see the terms") and terms.html section 5 say the November beta fee is NOT refundable; terms say regular program refunds need one month's notice before the first lesson. Three different rules for a legally binding promise, and consent box 2 makes parents agree to "the terms and refund policy". Fix: one policy, state beta vs regular separately, and replace the FAQ and hub text to match terms.
2. **Beta fee refund vs privacy withdrawal.** privacy.html "Your rights" says withdrawing recording/children's-work consent means "we will refund the lessons not yet held", which contradicts the non-refundable beta (terms s5). Fix: carve out or reconcile.
3. **Home says "Lessons start Mon 23 Nov"** (dist/index.html line ~276, from JSON `start` 2026-11-23) but no group meets on Monday: first lessons are Tue 24 (L1-4), Thu 26 (L6), Fri 27 Nov (L5), matching the cards, DB and JSON group data. Parents will be told the wrong start date. Fix: drop the sentence or derive from the earliest group.
4. **Register-by date is still a placeholder on live pages** ("[date to confirm]" in the register box, FAQ workbook answer, terms s3; JSON `register_by` is empty) although the posted workbook promise depends on it; the hub tells parents "register by the date shown on the home page", which shows no date. Blocks launch. Fix: owner sets `delivery.register_by` (about 9 Nov for a 24 Nov start).
5. **Bracket placeholders and draft banners live on terms and privacy** (listed below). Terms and privacy still say "Draft, not yet reviewed by a lawyer... Remove this note". Consent text parents agree to is unreviewed. Launch blocker by the DEPLOY.md rule.

### Medium
6. **Regular price S$65 a lesson / S$650 shown** on home Price box and FAQ ("What will the regular price be?"), and hub (b-price, JSON-LD FAQ) while only the S$25/S$250 beta fee is decided; owner_decisions lists term price as open and hold-prices decision of 23 Oct. Terms s7 says "[S$ per term]" so the site says two different things. Fix: remove S$65/S$650 everywhere until decided.
7. **Lesson 10 name**: owner decision keeps "Puzzle Day" for holiday Levels 1-4; Level pages 1-4 and home ("certificate signed on Challenge Day") say "Challenge Day".
8. **No email address anywhere**: CONFIG.email is empty so Email lines are hidden, but FAQ cancel says "message us on WhatsApp or email" and the WhatsApp fallback text says "or" + empty email (interest/registration copy: "send it to +65 9880 5962 or "). Privacy data contact is the personal gmail "[pypteltd@gmail.com, to be changed later]". Fix: set a business email or reword.
9. **"Free weekly puzzles by email" promise** (home "You get") has no sign-up form and the privacy notice lists no email-newsletter data or consent. Fix: remove or add consent and retention.
10. **Hero on the home page labels the whole program "Ages 6-8 (builds on Primary 1 maths)"** (eyebrow, FAQ "Who is it for?", footer "An Ages 6-8 ... holiday program"), although the page sells six levels. Misleading to Level 2-6 parents. Fix: neutral wording on home.
11. **Contradictory term-time statements**: terms s7 and FAQ describe the regular program as about 10 lessons per term of 90 minutes, no price; fine, but "Holiday courses... after a June course Term 3" is shown in terms while the owner's open item says Term 1 plans were rewritten: not a defect, but nothing on home says term classes exist, while the interest form lists "Term time (2027)" slots. Minor inconsistency in messaging; also term slots T27-* in interest_slots.json imply Level 5 on Thu 7:30pm and Sunday evenings ending 8:45pm for ages 10-12, unconfirmed.
12. **Printing/postage included in S$250**: stated consistently on home, terms and hub. The parcel policy (7 days, one resend) is stated but still tagged "[parcel policy: draft default, to confirm]" on home FAQ and terms. 30-day address retention is consistent on home consent, hub, privacy table and form wording, but privacy retention cell and wording line are bracketed.
13. **Tap targets under 44 px**: nav links 36 px high (every page), "Register" 39 px, syllabus country buttons 36 px, weekly-dose Check/Hint 41 px, back links 26-29 px; 98 undersized targets on home at 400 px (counting small inline controls). Fix: min-height 44px on nav, buttons, back links.
14. **Unlabelled inputs**: `#pzA` (home sample puzzle answer) and `#askq` (hub question box) have no label or aria-label.
15. **Syllabus page has no robots noindex meta** (all others do); only the header and robots.txt protect it. Fix in build_site.
16. **CSP uses `'unsafe-inline'` for scripts and styles** (all pages are inline); acceptable for static site but weakens XSS protection; consider hashes later. Headers otherwise good (nosniff, referrer, frame DENY, permissions, X-Robots-Tag, form-action wa.me). Note: _headers could only be checked statically (local server does not apply them); in a --with-portal build CSP connect-src must include the Supabase origin (build_site.py handles this) -- not tested live.
17. **Hub (parent-questions) states MOE is discontinuing GEP from 2027** citing a March 2026 press release; I could not verify this offline. Verify before public launch.
18. **Sample claims**: "Who teaches: an experienced Singapore primary school maths teacher" is an unverifiable claim to substantiate; the syllabus page claims lessons are "checked lesson by lesson against the MOE 2021 Primary Mathematics syllabus", fine with its disclaimer, but the owner decision says avoid "MOE-aligned" claims; wording "desk comparisons, not a claim of alignment" is acceptable.

### Low
19. Placement text: "free 30-minute diagnostic" / "Placement Check" and "free 15-minute readiness check" are promised but no link or form exists on the site.
20. Level 6 has no "week 5" note while Levels 1-5 do (correct, no Friday), fine; first/last labels match JSON and DB.
21. Schedule (verified): all six groups' days, times, seats (8), first/last labels, fee 25000 cents match beta_schedule.json and live `groups` rows; all JSON lesson weekdays are correct and none falls on 25 Dec. DB `start_date` for L1A is 2026-11-24 while JSON `start` is 2026-11-23 (the Monday error in item 3).
22. Favicon and logo mark is "?" which can read as an error glyph; consider Mi.
23. 404 page lacks noindex meta (header applies).
24. Performance: no raster images, 10 woff2 fonts (155 KB, immutable cache), pages 12-92 KB. Fine. Home is 92 KB inline; acceptable.

## Placeholders still on live pages
Home: "[date to confirm]" x2 (register-by box, FAQ), "[parcel policy: draft default, to confirm]". Level pages 1-6: "[date to confirm]" x2 each. Terms: "[in brackets]" banner, "[registered address, to update later]", "[Wording for the lawyer to confirm]", "[date to confirm]", "[Register-by date: owner to set...]", "[Parcel policy: draft default...]", "[Confirm after the beta]", "[S$ per term]", "[Instalment amounts...]", "[amount and closing date to be set after the beta]", "[Liability wording...]". Privacy: "[in brackets]" banner, "[Confirm nothing else is collected]", "[Confirm the platform setting before the first lesson]", "[Printer and courier names to add once chosen]", "[Provider and location: owner to confirm]", "[pypteltd@gmail.com, to be changed later]", "[Retention and wording...]" x3 in the table and x5 in the wording list.

## Checks that passed
- 14 pages at 1280 and 400 px, light and dark: no console errors, no failed requests, no horizontal scroll.
- Posted-workbook promise is consistent across home, level pages, hub, terms, privacy (Singapore only, PDF fallback, included in S$250, 30-day retention, delivery consent box).
- Consent wording on the form matches privacy.html "wording used on the registration form" (contact, terms, recording, children's work, delivery, optional feedback).
- No-index stopgap present: robots.txt Disallow, X-Robots-Tag, meta on all pages but syllabus and 404.
- Request another time: website/tests/interest_test.py passes the 25 interest checks (validation, WhatsApp message to +65 9880 5962, level filter, selection count, honeypot, 1-minute throttle, portal mode with mocked RPC, duplicate and error handling); my own probe confirmed 5 validation messages on empty submit, per-field errors, and honeypot field present. Portal mode not tested live (dist built without --with-portal: WhatsApp fallback only).
- Sample puzzles checked: frog puzzle answer 11, 23, 35 is correct.
- No SASMO/MOE alignment promise or results promise on the home/level pages (explicit disclaimers present).

## Shop (exists, status: in progress by another agent)
dist/shop is a "coming soon" list page with no prices (consistent with price hold). Shop tests in tests/interest_test.py had 2 failures at audit time (physical quantity selector locator, and the 1-minute throttle message not shown for the shop form); likely mid-edit, re-check after the shop agent finishes.

## Ranked top 10
1. Contradictory refund rules (FAQ and hub 60-day refund vs terms non-refundable beta) (High)
2. Draft banners and bracketed placeholders on terms and privacy; no lawyer review (High)
3. Register-by date empty while workbook delivery depends on it (High)
4. "Lessons start Mon 23 Nov" is wrong; no group starts Monday (High)
5. Privacy withdrawal refund clause contradicts non-refundable beta (High)
6. S$65/S$650 regular price shown while prices are on hold and terms say "[S$ per term]" (Medium)
7. No business email while the cancel flow and fallbacks mention email; personal gmail as DPO contact (Medium)
8. "Free weekly puzzles by email" promised with no consent or sign-up (Medium)
9. Home page framed as Ages 6-8 only; "Challenge Day" vs owner's "Puzzle Day" (Medium)
10. Tap targets under 44 px and two unlabelled inputs (Medium)

## NOT audited
Live deployed site and real Cloudflare headers (checked _headers file only); portal mode against real Supabase (mocked only); screenshots were taken but visual contrast was not measured numerically; every sub-page of syllabus and weekly-dose content correctness; shop checkout flows (in progress); PDFs and portal pages; accessibility with a real screen reader; external link validity (MOE links not fetched).
