# Public website UI/UX pass (23 Oct 2026)

Scope: website/ generators (lp_build.py, level_pages.py, shop_build.py, build_site.py, hub/build.py, hub/qa.py), lp_parts.txt (shared CSS), legal_style.txt, terms.html and privacy.html (navigation and layout only), weekly_dose_online.html, syllabus/index.html. dist was rebuilt, not hand-edited (private preview build, no --public, no --with-portal).

## What I checked
Playwright with the preinstalled Chromium, dist served locally, every page (home, 2 of 6 level pages, shop, parent questions, Weekly Dose, terms, privacy, syllabus, 404) at 400px and 1280px, light and dark, full-page screenshots viewed. Automated checks at 360px: no horizontal scroll on any page (light and dark); tap targets under 44px; unlabelled fields; heading order; small text; text contrast (computed, AA 4.5:1 / 3:1 large); images without alt. Walked the shop flow (add to list, Tell me when it's ready, field errors) and the home registration form errors. Existing tests: website/tests/shop_test.py and interest_test.py pass.

## Changed (before -> after)
- Prices: the home page, the parent-questions FAQ and the "Regular price" card showed S$65 a lesson / S$650. Now only the beta fee (S$25 a lesson, S$250 for 10) is shown; "After the beta" says the regular price is not set yet. Unused price/intro constants removed from the page script.
- First screen of home: eyebrow said "Ages 6-8, builds on Primary 1" although the site has six levels. Now "November beta - live online maths for ages 6 to 13"; the lead says who it is for and that you pick a level then a class time; primary button is "Choose your child's level" (was "Register now"). The lessons list is labelled "What Level 1 (ages 6-8) covers" (it was presented as the whole program). Footer and "Who is it for?" FAQ no longer say the program is only ages 6-8.
- Beta badge in the hero wrapped awkwardly ("S$25 a / lesson"); now stays on one line.
- Parent questions page: the top nav and logo were plain spans (not links). Now real links (Program, Levels, Parent questions, Puzzles, Shop, Register). At 400px the Ask box was squeezed into half width; now full width. "Ask a question" said "Thank you, we will add an answer" but sent nothing; it now opens WhatsApp with the question prefilled and says so. Textarea got a visible label; search placeholder shortened (was clipped).
- Weekly Dose and terms/privacy had no site navigation; added a small consistent nav bar / link row and Terms and Privacy links. Syllabus back link and country buttons enlarged. Legal wording untouched.
- Tap targets: nav tabs, buttons, small buttons, summaries, footer and crumb links, "Request another time", Weekly Dose buttons all >= 44px tall (home had 100+ elements under 44px, now only inline text links and the logo link at 40px was raised to 44).
- Text: small text raised (13.5 -> 14.5px, footer 14 -> 15px, lesson captions 13 -> 14px); body copy in sections capped at about 68 characters per line.
- Forms: input borders were about 1.5:1 against the page; now about 3:1 (WCAG 1.4.11). Registration errors now focus and outline the first missing field and are announced (aria-live). The taster puzzle answer box got a label. Required-field error styling added.
- Focus: visible coral focus ring on all links, buttons and summaries (yellow on the navy hero). Skip-to-content link on home, level pages, shop and parent questions.
- Contrast: the green "Open" pill was 4.32:1, now passes. No other AA failures found by the computed check at 360px in light or dark.
- Mi: was only on the shop. Added to the registration section (home) and the 404 page. 404 page also now links to home, levels, shop and parent questions and supports dark mode.

## Found, not changed (and why)
- Placeholder text visible to parents: "Register by [date to confirm]" on the home and level pages (owner must set delivery.register_by in data/beta_schedule.json); "[parcel policy: draft default, to confirm]" in the home FAQ; the red "Draft, not yet reviewed by a lawyer" banner on terms and privacy. These are owner/lawyer items; the site is a private preview.
- terms.html still contains money wording I did not alter (S$1 credit value, S$ per term bracket) because it is legal text; check it against the "no prices on hold" rule.
- Parent questions "Was this helpful?" buttons only change their own label; nothing is recorded. Left as is; either wire up or remove.
- Parent questions content is Primary 1 only while the site covers six levels (page title and hero).
- Registration is WhatsApp-only; the form cannot confirm that a message was sent. The level dropdown text is truncated on narrow phones (native select).
- Only two of six level pages were screenshotted; they share one template.
- portal/tests/frontend_test.py reported 3 failures (admin lists enrolments, delete my data, full group cannot be chosen). I did not touch portal/; not investigated further, probably pre-existing.

## Owner decisions
1. Set the register-by date. 2. Decide whether terms.html credit/instalment money wording stays while prices are on hold. 3. Decide whether the hero should keep the frog scene or use Mi. 4. Confirm the home page should lead with the level choice rather than "Register now" (Register stays in the nav and the band). 5. Hub scope (Primary 1 only or all levels).
