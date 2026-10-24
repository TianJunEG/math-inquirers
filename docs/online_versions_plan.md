# Online versions of the workbooks: plan and pilot

Written 24 Oct 2026 on branch `claude/great-fermi-1hv4vc`. Planning plus one pilot. Nothing is published, sent or deployed. Hours are agent-hours and are **estimates**.

Owner decisions this plan serves (`docs/terms/owner_decisions.md`): **ONLINE-VERSIONS** (holiday program 60 lessons, term lessons, extension workbooks 60 units; NOT school puzzle booklets) and **ONLINE-SKIP-SELECT-SUBMIT** (the child can skip and select any question, enters answers, submits, then sees marking and the online worked solutions).

Rules for every online page: no timers, scores, streaks or leaderboards; every answer verified by code; a variant can never be wrong; Singapore wording; no coin or note images; hints and worked steps; one-star and two-star tiers where the workbook has them (Start here, Think harder, Go further, Check yourself).

---

## 1. The requirement from ONLINE-SKIP-SELECT-SUBMIT, and what it changes

The existing runner (`practice/public/practice.js`, and its Term 1 copy `term/l1/runner/practice.js`) gives instant feedback on one question at a time. The owner wants a worksheet. So there is now a second runner, `practice/ext/public/sheet.js`, that works like this:

| Behaviour | How it works |
|---|---|
| Free selection | A question list (jump menu) shows every question by set. The child opens any question in any order. No forced order. "Previous" and "Skip to next" are only conveniences. |
| Markers | Before submit: filled dot = has an answer, hollow = no answer yet. After submit: tick = right, cross = look again, dash = no answer, pencil = self-check. Every marker has a symbol and a screen-reader label, so colour is never the only signal. |
| Autosave | Answers are saved in the browser's `localStorage` (every read and write in try/catch; the page works without it). A refresh does not lose answers or the submitted state. |
| Hints | Available before submit, on demand. |
| Solutions hidden until submit | The worked solution and the correct answer are not in the page DOM view until submit (tested). They are still in the data file, so this is a teaching device, not secrecy (see open decision D4). |
| Submit | "Submit my answers". If some questions have no answer: an in-page panel "N questions have no answer. Submit anyway?" with "Yes, submit" and "Keep working" (no browser `confirm`). |
| After submit | Marking per question (right / look again / no answer), a plain count line ("12 of 44 marked questions are right"), and for EVERY question, including skipped ones, the correct answer and the full worked solution. Open-ended questions are self-check: the example answer is shown, never marked. No percentage, no ranking, no comparison. |
| Review and retry | "Change my answers and submit again" hides the solutions again and unlocks the answers. "Start again with empty answers" clears. After submit each question with a variant family offers "Try a similar one" (instant check, a new question each time, answer computed). |
| Privacy | Submit is local. Nothing is sent to any server, there is no account, and the footer says so. |

**D5 RESOLVED 24 Oct 2026 as SUBMIT-TO-TUTOR (see section 11 and `docs/online_submission_design.md`): submitted answers are sent to Math Inquirers, re-marked on the server, and used for reports. The paragraph below is the earlier analysis, kept for the reasons it lists, which the design now answers.** Earlier recommendation: not at launch. It would need an account or a family code, a server table of children's answers, a privacy notice and consent, and a retention rule (the portal README already says the child sign-in is a stub). Offer instead a "Show this to your tutor" view (the marked page on screen) and, later, an optional opt-in "send my result" with counts only (not answers), if the owner wants it.

---

## 2. Status: what exists and what is missing

| Product | Size | Machine-readable questions and answers? | Online today | Missing |
|---|---|---|---|---|
| **Extension workbooks** | 60 units (6 levels x 10), 1,330 items, 2,733 answered parts | **Yes.** `extension/data/lN_uXX.json`: text with markup (`{b}`, `{circ:a|b}`, `{ll}`), `answer.value` lists, `hint`, `explanation`, `figure` spec (drawn by `extension/tools/figs.py`), tier. `extension/verify/lN_uXX_checks.py` exists for all 60 units and `run_checks.py` passes (60 units, 2,733 answers independently recomputed). | **Pilot: L2 unit 1** (`practice/ext/`). | 59 units to build; gaps listed in section 4. |
| **Term lessons Level 1** | 40 lessons, 509 online items, 352 with a variant template | **Yes.** `term/l1/lessons/lNN.json` `online_practice.items` (types number 329, choice 108, selfcheck 39, set 9, fields 24); checks in `term/l1/verify/lNN_checks.py` (all 40 exist) and brute-force oracles for the templates. Pictures are drawn at build time (`b_practice.py`). | Built as per-question practice (`term/l1/out/lNN/practice`, git-ignored). Not linked from anywhere. | Switch to the worksheet runner (submit, solutions after submit); host; link; audit all 40. |
| **Term lessons Levels 2 to 6** | 200 lessons, not started | Will be, if the Level 2 to 6 term build (`docs/terms/levels_2_6_term_build_plan.md`) keeps `online_practice` in the lesson JSON. | None | Authoring `online_practice` per lesson inside that build (about 1.5 agent-hours per lesson, about 300 h; not counted again below). Decision: keep it in the plan so it is not dropped. |
| **Holiday program** | 60 lessons (6 levels x 10) | **No.** `pN/content/lN.js` `qbank` entries are `{q, a}` with prose answers ("54 (one more 9: 45 + 9)", "Both are 48: ..."). About 1,240 items in P2 to P6 plus 234 in `hp/qbank.json` (P1). No structured answer, no checks, no hints. Workbook pages are built from other sources (`hp/`, `levels/`), so the question bank is not guaranteed to be the workbook text. | Only `practice/build_practice.py` p3l3 (13 hand-authored items with brute-force checks). | A structured answer for about 1,470 items, independent checks, the link from workbook question to online item. The biggest job (section 5). |
| School puzzle booklets | n/a | n/a | n/a | **Excluded by the owner.** |

Other pieces that exist: `portal/public/practice/index.html` is a placeholder ("coming soon"), `website/weekly_dose_online.html` is a separate weekly teaser page (not part of this plan), `term/l1/README.md` documents the Term 1 practice build.

---

## 3. Architecture: generate online items from the same source data as the workbook

Principle: **one source file, two renderers.** The workbook and the online page both read the same JSON, and the online answer is taken from the independent check function that the workbook's answer key already has to pass. A pupil/key mismatch is then impossible by construction: the book answer, the checked answer and the online answer are the same value, and the build stops if they differ.

```
extension/data/lN_uXX.json  --+--> extension/tools/build.py  --> workbook PDF + answer key   (exists)
 (text, answers, hints,       |
  explanations, figures)      +--> practice/ext/build_ext.py --> practice/ext/dist/lNuXX/    (pilot)
extension/verify/lN_uXX_checks.py    (independent recomputation)  |
practice/ext/variants/lN_uXX.py      (variant families + oracles) -+
```

What `build_ext.py` does (pilot, works for any extension unit that has the same shapes):

1. Runs the unit's independent check functions and requires them to equal the JSON answers (same gate as `run_checks.py`); then uses the CHECKED value as the online answer.
2. Converts each item or part into an online question: `fields` (numbered boxes inside the sentence), `set` (a list typed with commas, ordered or any order), `choice` (the `{circ:...}` options become radio buttons, never shuffled for `< = >` or True/False), `selfcheck` (open items). The figure is drawn by the same `figs.py` and embedded as SVG. A part of a question becomes its own card (so `9(a)` is a card), numbered as in the book.
3. The worked solution is the book's `explanation`, split per part `(a) (b)` and per sentence. The hint is the book's `hint`.
4. Variant families (the sidecar): a template with variables and an arithmetic answer, plus an **independent oracle** (enumeration, digit strings, loops). The build runs the oracle over EVERY combination of the variables and at the authored numbers, and refuses to write anything on a single disagreement. In the browser the answer is computed by the template expression in JS; the test drives the page through the combinations and checks the question shown equals the template and the oracle's answer is accepted, so the JS evaluator is tested as well.
5. A sidecar policy that must be explicit: for every list answer, "any order" or "ordered" (a wrong guess would mark right answers wrong, so the build fails if it is missing), and wording overrides for text that only works on paper ("fill the table", "your list from the question before").

For the term lessons the item format is already the runner format (`online_practice.items`, `tpl`, brute-force oracles); they only need the new page shell. For the holiday program the source has to be given a structured answer first (section 5).

Runner decision: **one worksheet runner for all three products** (`sheet.js`, about 190 lines, no framework, no network). It reads the same item shapes as the Term 1 runner (number, fields, set, choice, selfcheck, `tpl`, `svg`). Before Term 1 moves onto it, it must reach parity with `term/l1/runner/practice.js`: the template helpers `multiples`, `common`, `divisors`, the `{x|word}` `{x|ord}` `{x|usd}` `{x|c}` fillers, `pad` for clock minutes, templated choice and set variants, the "minutes 0 to 59" rule, and the slip messages (kept for after-submit feedback). About 12 to 16 agent-hours, listed as Phase 0.

---

## 4. Pilot result: extension Level 2 unit 1 "Digit detectives"

Files (all under `practice/ext/`, not deployed):

| File | Purpose |
|---|---|
| `build_ext.py` | generator: `python3 practice/ext/build_ext.py 2 1` writes `practice/ext/dist/l2u01/` (git-ignored) |
| `public/sheet.js` | the worksheet runner |
| `variants/l2_u01.py` | list policy, wording overrides, 5 variant families with oracles |
| `test_ext.py` | browser test and screenshots: `python3 practice/ext/test_ext.py 2 1` |
| `proof/*.png` | 7 screenshots (phone and desktop, light and dark) |

Serve and look: `python3 -m http.server -d practice/ext/dist/l2u01 8791`, open `http://localhost:8791/`.

Result of the run:

* 45 answers equal their independent check; 45 online questions (30 fields, 8 choice, 6 set, 1 self-check) from the 22 source items plus the "Your turn" item.
* 5 variant families, **1,000 combinations, every one equal to its independent oracle**.
* Browser test (Chromium, Playwright 1.56, installed browser): (1) the BUILT data file re-checked against fresh independent checks; (2) all 45 questions opened in reverse order, correct answer typed in each, confirm panel for the unanswered self-check, submit, every question marked right, 45 worked solutions shown, solutions hidden before submit and hidden again after "Change my answers"; (3) a second child answers wrongly, skips three, reloads (answers survive), submits: wrong and no-answer markers right, skipped questions show their solution, submitted state survives a reload; (4) 252 variant questions driven through the page (all combinations of the small families, 150 spread over S01(a)'s 900): question shown equals the template, oracle answer accepted; (5) no browser console errors. **RESULT: OK.**
* Screenshots checked by eye at 390 px and 900 px wide: no horizontal scroll, figures (digit cards, number line, 1000-chart pieces, base-ten blocks) drawn, markers readable, dark mode readable.

What the pilot found (all fixed or listed):

1. **Two-option questions trapped the child** in the existing runner (the "same answer as before" rule on True/False, only one wrong answer). Not an issue in the worksheet runner (there is no instant-feedback loop), but `term/l1/runner` has the bug: a True/False item can never reach the solution. Worth a one-line fix there (owner of term/l1 to do it; I did not touch it).
2. **Only 391 of 1,330 extension items have a hint** (the schema requires one only for Think harder and Go further). The online page falls back to "Read the question again slowly...". Hints for the 939 others must be written (Phase 2).
3. Some questions refer to the previous one ("Use your list from the question before") or to a table to fill in on paper: fixed with sidecar overrides that compute the list from the independent check (so it cannot disagree).
4. Parts of one book question are separate cards, so the card count (45) is higher than the book question count (22); labels keep the book number ("9(a)").
5. The solution is the book's `explanation` prose, split into sentences. It is accurate (same text as the answer key) but is not always step-by-step; for Think harder and Go further it is good, for Start here it is short. Acceptable at launch; richer steps are a Phase 2b option.
6. Coverage of the generator across all 60 units, counted from the data: **whole-number boxes 1,991 parts and whole-number lists 112 (77 percent), circle-a-choice 356 (13 percent), open 10, other text 167 (6 percent: fractions like `3/8`, letters, names, directions like `NW`, days), decimals 97 (3.5 percent)**. The pilot covers the first three. Phase 2 adds a `text` answer (case and spacing tolerant), a `fraction` answer (equivalent fractions accepted only if the book says so), and a `decimal` answer. Money answers use the cent sign in the source (no coin images are needed online, the book's coin figures are not rendered).
7. Figure types: about 100 different figure types appear across the 60 units; 15 or so are shared helpers and the rest are drawn by per-level plug-ins that the generator already reuses, so no figure is redrawn. Figures that contain the answer blanks (chart pieces, tables) work as read-only pictures plus a typed answer.

---

## 5. Holiday program: what has to be built first

The question bank is prose. Examples: `a: '54 (one more 9: 45 + 9).'`, `a: '10, 20, 30, 40 and 50. They all end in 0.'`, open-ended items with several possible answers. To get online versions with code-verified answers without guessing from text:

1. Add a structured answer next to each `{q, a}` (value list, type, order policy), written by the author of the lesson and recomputed by an independent check function per lesson (same pattern as `extension/verify`). The existing prose `a` stays as the worked solution.
2. Decide per item: auto-markable (about 75 percent by analogy with the extension count), self-check (open, drawing, "explain why"), or not suitable online (needs a physical kit: cut-outs, ruler, counters).
3. Confirm which workbook questions are the bank questions (the P1 workbook is built from `hp/` sources; P3 content files hold both the workbook SVGs and the bank). The online page should show the same questions as the workbook page of that lesson; where the workbook has questions the bank lacks, use the workbook source.
4. Hints and full steps are not in the data (the P3L3 pilot has them by hand). They need to be written for about 1,470 items, or the runner falls back to the generic hint and the prose answer as the solution (acceptable for launch, not good).

---

## 6. Hosting, URLs, and how the portal and website link to it

The site is static (Cloudflare Workers assets from `website/dist`, `wrangler.jsonc`), so every online page is a folder of static files. Nothing needs a server.

| Product | URL pattern | Folder in the repo (source of truth is the data, `dist` is built) |
|---|---|---|
| Extension | `/practice/ext/l{L}u{UU}/` e.g. `/practice/ext/l2u01/` | `practice/ext/dist/l2u01/` |
| Term | `/practice/term/l{L}t{T}/{NN}/` e.g. `/practice/term/l1/01/` | built from `term/l1/lessons/l01.json` |
| Holiday | `/practice/holiday/p{L}/{NN}/` e.g. `/practice/holiday/p3/03/` | built from the holiday sources |
| Index | `/practice/` lists the three products and levels | one generated page |

Each page folder is self-contained (index.html, `sheet.js`, `data/<key>.json`, fonts), with relative paths so it works under any prefix. The build copies the folders into `website/dist/practice/...` at release time. Shared `sheet.js` and fonts can be hoisted into `/practice/_shared/` once there are many pages (saves about 30 KB per page and means a runner fix reaches every page).

Linking:
* Website lesson and level pages: a "Practise online" button on each level page and in each syllabus entry, linking to `/practice/`. The extension and term book product pages say "Online practice included" (if the owner decides it is included, D2).
* Portal: replace the placeholder `portal/public/practice/index.html` with the product index filtered by the child's level; no sign-in is needed for the pages themselves (the child area only needs the link). Answers are sent to the server only after the child signs in with the existing child profile and PIN and the parent has agreed (section 11, D5 resolved); without that, nothing is saved or sent.
* Books: a short URL or QR code printed at the end of each workbook unit or lesson (`/practice/ext/l2u01/`). Needs a layout slot in the book (small, one line), and a decision on whether the QR goes in print (D1).

---

## 7. Phased order, effort, and order of delivery

Recommended order: **Phase 0 runner, Phase 1 term Level 1, Phase 2 extension, Phase 3 holiday**, with term Levels 2 to 6 riding on the term build.

| Phase | Work | Agent-hours (estimate) | Exit gate |
|---|---|---|---|
| 0. Worksheet runner parity | Bring `sheet.js` to parity with the Term 1 runner (helpers, fillers, pad, templated set and choice, slips after submit); shared test harness `test_ext.py` made generic (any product); accessibility pass (keyboard, screen reader labels, 44 px targets) | 12 to 16 | the Term 1 lesson 1 page produced by `sheet.js` passes the same browser test as the pilot |
| 1. Term Level 1 (40 lessons) | A builder that writes `sheet.js` pages from `online_practice`; the browser test for every item and every template combination (480 to 500 items, 352 templates); fix the True/False trap in the old runner; index page; link-up; second-reader audit of a 10 percent sample | 20 to 30 | all 40 pages pass the test; independent audit finds no wrong answer |
| 2a. Extension base (60 units) | Generalise the generator: `text`, `fraction`, `decimal` answers, list policy and wording overrides for 59 more units (about 5 per unit, 0.3 h each = 18 h), figure types verified, per-unit browser test | 50 to 70 | all 60 units build and pass; coverage report shows 0 unsupported parts |
| 2b. Extension quality | Write the 939 missing hints (about 1 min each, 15 h), 3 variant families per unit with oracles (180 families, about 0.5 h each = 90 h; this is optional and can ship unit by unit), richer steps for Start here items | 100 to 120 | every item has a hint; each unit has at least 2 variant families |
| 3. Holiday (60 lessons) | Structured answers and independent checks for about 1,470 items (about 4 min each = 100 h), hints and steps, workbook mapping, builder, tests | 140 to 180 | all 60 lessons pass; mapping report shows every workbook question online or marked "paper only" |
| Term Levels 2 to 6 | `online_practice` written with each lesson (inside the term build budget) | about 300 (already in that plan) | per lesson gate |
| Release | Copy to `website/dist/practice/`, index, links, portal page, QR in books, cross-product link check | 8 to 12 | owner approves |

Totals: about 200 to 290 agent-hours for the three products as asked (excluding Levels 2 to 6 term). Calendar: Phase 1 can be live in about 1 to 2 weeks of working time after Phase 0; extension base about 2 to 3 weeks; holiday about 4 to 6 weeks (the structured-answer authoring is the critical path and can run in parallel with Phase 2).

Why this order: term Level 1 is the only product whose data is already complete and in the right shape (most value for the least work, and it proves the runner on real children's content). Extension has complete data and checks but needs the generator to cover the 23 percent of non-whole-number answers and hints. Holiday needs new authoring first.

---

## 8. Open owner decisions

| # | Decision | Recommendation |
|---|---|---|
| D1 | Hosting URL: the main site (`/practice/...` on the current domain), a subdomain (`practice.<domain>`), or the portal path | The main site `/practice/...`: no extra setup, links in books stay short. Needs the real domain to print QR codes. |
| D2 | **RESOLVED (owner).** Holiday and term online practice: only families with a confirmed enrolment at that level, plus a few open sample pages that store nothing. Extension online practice: only for the CHILD profile a parent bought it for (one purchase = one child; options workbook only, online only, workbook + online per level). | Section 11. (Earlier options, kept for the record: Free to start for the holiday and term pages, with the solutions part linked from the book; revisit after launch. If paid-only is wanted, a short family code checked by the existing worker (`/api/*`) is enough; no accounts needed.) |
| D3 | Accounts | **Amended by D5.** No new account system: the existing portal parent account and child profile (name + PIN, no child email) are used. Nothing is sent from a page unless the child signs in and the parent has agreed. Open sample pages still need no sign-in and store nothing. |
| D4 | Are answers and solutions in the page data? They are in the JSON (needed to mark in the browser). A technically minded child could read them before submitting. | Accept it: the solutions are a teaching aid, and the workbook answer key is also sold. If it matters, move marking behind a worker call later (needs a server and logs). |
| D5 | Should submitted answers also be sent to the tutor or teacher? | **RESOLVED: SUBMIT-TO-TUTOR** (owner, 24 Oct). Answers are sent to us, auto-marked again on the server, and used for parent, tutor and owner reports. Goes live only after the privacy wording is reviewed (design doc section 8, lawyer question 11). |
| D6 | Is the online page included in the book price, or a separate product | **Implied by the owner's three options per extension level:** workbook only, online only, workbook + online (separate SKUs; prices on hold). Earlier thought: Include; it is a reason to buy the book, and costs nothing per child to host. |
| D7 | Do pages show the marked count ("12 of 44 right")? Counts are not a score or a ranking, but some owners will not want any number. | Keep the plain count; it is the same as a teacher marking, and the child sees which ones to redo. Can be removed in one line. |
| D8 | Holiday paper-only questions (kit cut-outs, ruler, drawing) | **RESOLVED (owner amended D8):** they are NOT left out. Show the question with a short note ("Do this on paper, then check your drawing against the answer shown on screen.") and, after Submit, the answer or worked solution (with a figure of the correct drawing where one exists). They are **self-checked** items (marking_mode `self`): the child may tick "I checked / I got it / not yet"; never auto-marked; reported separately as "checked on paper"; excluded from auto-marked counts. Effort consequence: these items need a **solution figure**, not a checker. |
| D9 | QR code or short link printed in the books (layout slot and reprint) | Add a one-line link at the end of each unit or lesson in the next print run. |

---

## 9. Verification and audit plan

Gates, in the order a page passes them (a failure stops the build; nothing is written):

1. **Source gate:** `extension/verify/run_checks.py` (or the term and holiday equivalent) passes for the unit.
2. **Answer identity:** the generator takes the online answer from the independent check function and fails if it differs from the book JSON (so the book key, the online answer and the check are one value).
3. **Variant oracles:** every combination of every variant family compared with independent code, and at the authored numbers; all slip messages (if any) are genuinely wrong answers.
4. **Built-file re-check:** the test reads the BUILT data file and recomputes every answer again from the check functions (catches generator bugs).
5. **Browser end-to-end:** each question answered correctly, in reverse order, then submit, then marking and solutions; a wrong-answer run with skips and a reload; variants driven through the real page; no console errors.
6. **Wording lint:** the same `wording_lint.py` on hints and solutions (Singapore wording, reading load), plus the "no coins, notes or timers" scan.
7. **Visual:** phone and desktop screenshots, light and dark, checked by a person or a second agent; for each product a 10 percent sample at first, 100 percent of figure types once.
8. **Independent audit:** a second agent that has not seen the generator solves a random 10 percent of the questions from the page text only, and compares to the marking; any difference is a fail for the whole product, not only the item.
9. **Link check:** every page is reachable from the index, from the website and from the book URL; no page is orphaned; no external requests at run time (fonts and script are local).
10. **Privacy check:** the page makes no network request after loading (tested in the browser test by blocking the network once the page is loaded), stores only in `localStorage`, no cookies.

Ongoing: a nightly or pre-release script runs gates 1 to 5 for every page; the build is reproducible from data, so nothing built is edited by hand. Every change to a data file rebuilds its page.

---

## 10. What is not decided or not done here

* Not done: any publishing, linking from the live site or portal, QR codes, changes to `term/l1/` (another agent is editing it) or to the old runner.
* Not verified: that every Term 1 check file covers the online items (their template oracles); Phase 1 starts by confirming this.
* The holiday question bank may not be the same text as the workbook pages (section 5, point 3).

---

## 11. Online submission to Math Inquirers (D5 resolved as SUBMIT-TO-TUTOR), added 24 Oct 2026

Design, SQL draft, prototype and tests: `docs/online_submission_design.md`. Nothing is deployed, applied or sent.

**What the owner decided and how the plan changes**

| Decision | Effect on this plan |
|---|---|
| SUBMIT-TO-TUTOR (D5) | Submitted answers go to a server table, for reports. Needs the existing portal child profile sign-in, a new parent consent (`online_practice`), PDPA notice, retention and deletion rules, and a lawyer question (question 11). Nothing goes live before the privacy wording is reviewed. |
| Auto-marking | The browser marks instantly (as in the pilot); the server marks again from its own answer key at submission and the reports use only the server mark. `practice/submit/mark.js` is the shared marking code. |
| D2 | Holiday and term: confirmed enrolment at that level. Extension: one purchase = one child (workbook only / online only / both, per level). Open sample pages store nothing. Extension buyers need no enrolment or group. |
| D8 amended | Paper-only items stay online as self-checked items (see D8 row above). |
| Funnel | Extension books lead parents (never children) to a free trial class request; separate optional marketing consent. |

**Generator coverage and what cannot be auto-marked** (counts from the plan's own data, section 4 point 6 and the Term 1 type counts):

| Product | Auto-marked now (pilot rules) | Auto-markable after Phase 2 rules (text, fraction, decimal, already written and tested in `mark.js`) | Never auto-marked |
|---|---|---|---|
| Extension (2,733 answered parts) | whole numbers 1,991 + lists 112 + circle-a-choice 356 = 2,459 (90.0%) | + other text 167 (6.1%) + decimals 97 (3.5%) = 2,723 (99.6%) | open items 10 (0.4%), plus paper-only drawing items, which are self-checked and need a solution figure |
| Term Level 1 (509 items) | number 329, choice 108, set 9, fields 24 = 470 (92.3%) | same | self-check 39 (7.7%) |
| Holiday (about 1,470 items, estimate) | none yet: needs structured answers first (section 5); about 75% expected auto-marked by analogy | about 75% | the remaining about 25%: self-checked (drawing, ruler, kit) or open |

**Added effort (agent-hours, estimates, on top of section 7):**

| Work | Hours |
|---|---|
| Per-item MOE strand and skill tags for the extension units (1,330 items, about 1 minute each) so reports can say strengths and needs by topic | 20 to 25 |
| Wire the worker route, Supabase scratch project trial, real-database tests of the SQL and the child-session flow (the SQL is only tested on local PostgreSQL) | 10 to 14 |
| Portal screens: child sign-in minting the session token, consent card split by family type, buy-a-book flow (child, format, address), parent report view, admin tabs (orders, grant or revoke, ship status, reports, trial requests, funnel counts) | 30 to 40 |
| Stripe: extension order checkout and webhook (reuse `portal/functions`), refund handling | 10 to 12 |
| Gating the practice data file behind the entitlement (optional, see design section 3) | 6 to 8 |
| Solution figures for paper-only items (holiday and extension), about 5 minutes each; count to be measured when the holiday items are structured | 20 to 40 |
| Tests, audit and owner walkthrough for the above | 15 to 20 |
| **Added total** | **about 110 to 160** |

**Phase placement:** Phase 0 gets the server prerequisites (sections 3 and 4 of the design) and the consent and privacy review in parallel, so that Phase 1 (term Level 1) can send answers when its privacy sign-off is done. Extension pages are sold only after the shop is live and the three SKUs and prices exist (prices are on hold).
