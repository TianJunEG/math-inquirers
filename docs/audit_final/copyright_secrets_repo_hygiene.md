# Audit: copyright, secrets, repo hygiene

Auditor: independent, read-only. Branch claude/great-fermi-1hv4vc. Audited at commit eb12b16 (HEAD moved to 4bf3f43 during the audit; other agents were editing term/l1/out/l31, portal, docs). Nothing was pushed or deleted.

## Verdict: Ready after minor fixes (no High finding on copyright or secrets; one High on repository weight)

Counts: High 1, Medium 7, Low 6.

## 1. Copyright / compliance

Method: 7-word shingles (lower-cased alphanumeric tokens) built from all 24 text files under docs/books/private_* and docs/sasmo/private_* (md, jsonl, txt, tsv; 339,616 shingles). Scanned every tracked text file (5,238 tracked files) and the extracted text (pdftotext) of every tracked PDF (397). 364 files had at least one shingle hit; 1,179 runs in total.

- Private files tracked: none. `git ls-files | grep private` = 0 results; `git log --all -- '*private_*'` = empty (never in any commit, so never in history). `git check-ignore -v` confirms .gitignore lines 12-13 cover them. PASS.
- Hit length distribution (merged runs): 996 runs of 7-8 words, 156 of 9-11, 21 of 12-19, 6 of 20+. The great majority are ordinary exam stems ("how much money did she have at first", "when rounded to the nearest thousand what is the smallest").
- Longest hits, all in analysis/planning docs, none in learner-facing term lessons:
  - docs/terms/level_1_year_plan.md and level_2_year_plan.md: 49 words, the project's own type-code legend (BACK, CTX, LIST...), copied from our own private notes. Not paper text.
  - docs/terms/l2_preflight.md: 31 words, the same legend; 20 words, a table of digits that matches private_solution_notes_g1.md (our own table).
  - docs/sasmo/k_analysis.md: 20 words and g3/g5/g2/g4_analysis.md: 12-18 words, book titles and series description ("sasmo primary 3 grade 3 gep practice 2019 and 2020 contest problems with full solutions") - bibliographic only.
  - docs/books/p2_school_paper_patterns.md:  22 words, "3.07 pm to 4.39 pm / 5.35 pm to 7.00 pm / 8.45 am to 11.23 am" (a verbatim time-pair list from a P2 paper), 15 words "what is the most number of friends she can give ... 20 cookies 3 each", and 14 words in school_paper_wording_patterns.md ("Box A weighs 800 g. Box A weighs 500 g more than Box B"). These are short quoted stems used as pattern evidence.
  - Learner-facing: p5/content/l9.js, p5 tutor guide, tutor/data/p5l9.notes.json: 13 words "Figure 1 has 4 sticks. Figure 2 has 7. Figure 3 has 10" (a generic stick-pattern, 3 numbers). p4/content/l2.js + p4/workbook_body.html + P4 workbook/question-bank PDFs: 11 words "...000 when rounded to the nearest thousand what is the smallest" (generic rounding stem). P2/P3/P5 question banks: 9-10 word stems.
  - term/ (all new term lessons, 92 files with any hit): maximum run 9 words; school/ maximum 7; extension/ maximum 7.
- Conclusion: no substantial verbatim reproduction of the private extracts in committed files. The few quoted fragments are 14-22 words and appear only in internal analysis docs.
- Limit: the scan can only detect overlap with the extracts. The original school and contest PDFs are not on this machine, and several extracts are lossy OCR, so verbatim copying of un-extracted papers is not detectable here.

Findings
- C1 Low. docs/books/p2_school_paper_patterns.md (time-pair list, "most number of friends" stem) and docs/books/school_paper_wording_patterns.md (Box A/Box B) quote a whole question line. Fix: paraphrase or replace the numbers so the files hold patterns, not paper lines.
- C2 Low. docs/sasmo/*_analysis.md name the source books by exact title/years. Probably fine for an internal doc; if the repo is ever made public, drop the exact titles.
- C3 Medium. Learner-facing P4 and P5 items reuse stems with 11-13 words matching extracts (above). Generic phrasing, but the P5 "Figure 1 has 4 sticks / 7 / 10" pattern is identical to a P3 paper item. Fix: change the starting numbers and context in p5/content/l9.js (regenerate guide, notes) and p4/content/l2.js.
- C4 Low. docs/terms/level_*_year_plan.md hits are our own legend; no action.
- C5 Medium (compliance). Third-party licence for shipped fonts: Fredoka (64 woff2) and Nunito Sans (256 woff2) are tracked (practice/dist/fonts, term/l1/out/*/fonts), website pages load them, but no OFL.txt, no copyright line and no third-party notices file exists anywhere (`git ls-files | grep -iE 'ofl|licen|notice|credit'` = nothing; `git grep -i 'SIL Open Font'` = nothing). SIL OFL requires the licence text to accompany redistributed fonts. docs/legal/review.md L4 already flags it as unresolved. Fix: add fonts/OFL-Fredoka.txt, fonts/OFL-NunitoSans.txt (upstream copies) and a THIRD_PARTY_NOTICES.md covering also portal/public/vendor/supabase.js (MIT) and mascot/Mi artwork provenance; put a one-line credit in the site footer or colophon.

## 2. Secrets and personal data

- Working tree (tracked files, non-PDF): regexes for Stripe sk_/rk_/whsec_, Resend re_, AWS, GitHub, Slack, Google AIza, Supabase sbp_/sb_secret_, PEM private keys, JWTs (eyJ.eyJ.), `key = "long string"` assignments. Zero real secrets. Only hits: a password input (`portal/public/app.js:49`) and the minified supabase.js library. portal/public/config.js holds placeholders ('SUPABASE_URL', 'ANON_KEY'). No .env, .dev.vars, .pem, .key files tracked or present.
- Full history: all reachable blobs not under term/l1/out (19,943 objects, covering every commit on all branches) scanned with the same regexes: zero secrets, zero JWTs (so no anon key either), no service_role value anywhere (only the variable name SUPABASE_SERVICE_ROLE_KEY in code and docs, read from Cloudflare env). The 3.8 GB of term/l1/out history (generated decks/guides) was scanned only in the working tree (clean); a history scan of those blobs did not finish in the time budget (see "Not audited").
- GitHub secret scanning tool (mcp__github__run_secret_scanning) was loaded but is a content-snippet scanner; the full-history regex scan above stood in for it.
- Personal data in history: the business WhatsApp +65 9880 5962 (410 occurrences, owner's business contact, intended). Owner Gmail pypteltd@gmail.com appears in docs/legal/review.md, term/l1/audit, website/privacy.html and website/dist/privacy/index.html as a placeholder "to be changed later". jasmine@mncoholding.com appears once, in docs/audit_final/schedule_and_calendar.md (another agent's audit of the connected Google Calendar). All other addresses are example.com style. No children's or parents' names, phone numbers or emails found.
- S1 Medium. The placeholder contact on the PUBLIC privacy page (website/privacy.html:61, dist copy) is the owner's personal Gmail, flagged "to be changed later". It would go live as the data protection contact. Fix: replace with the business address before --public build; docs/owner_decisions has no decision on it.
- S2 Low. docs/audit_final/schedule_and_calendar.md exposes a calendar account email. Fix: redact to "the connected account".
- S3 Low. docs/audit_final/payments_and_database_adversarial.test.mjs.txt contains fake Stripe-looking test values (`sk_test_f...`); they are fakes, but would trip secret scanners on a public repo. Fix: build test values at runtime ('sk_' + 'test_' + ...).

## 3. Repository hygiene

- H1 HIGH. Repository weight. .git is 3.5 GB: 19,236 loose objects (3.28 GiB) plus a 198 MiB pack; reachable blobs total 5.2 GB uncompressed. term/l1 alone is 3.8 GB across 7,684 blobs in history (every lesson rebuild re-commits ~4 MB decks and ~500 KB PDFs; the "WIP checkpoint" commits from many agents amplify it). No single blob exceeds 20 MB; the largest tracked files are 14-17 MB PDFs (outputs/print/bw/*). Tracked working tree: ~429 MB; term/l1/out alone is ~520 MB of disk blocks (1,933 files). A push of this history will be very slow and may be rejected by the host (GitHub's push/repo recommendations: under 1-5 GB). Fix: see commands below.
- H2 Medium. Generated build output is tracked: term/l1/out (1,267 html, 246 pdf, 300 woff2 - the same 2 fonts copied into every lesson folder), website/dist, practice/dist, outputs/print twice (outputs/print and outputs/print/bw), p2-p6 workbook_body.html and workbook_full.html and root workbook_body.html (hp/workbook_*.html is in .gitignore but the same files for p2-p6 and the root are tracked: inconsistent). Fix: decide what is a deliverable (PDFs the owner prints/sells) and ignore the rest.
- H3 Medium. Stray files in repo root, untracked and not ignored: 7 Python wheels (ftfy, langcodes, locate, msgpack, regex, wcwidth, wordfreq .whl). `git add -A` by any agent would commit ~10 MB of them. Also tracked root workbook_body.html is a stray. Fix: delete the wheels, add `*.whl` to .gitignore, `git rm` root workbook_body.html (after checking nothing references it).
- H4 Medium. .gitignore is thin and partly contradictory: ignores `README.md`? No - but `fonts/fonts.css` is ignored while 300 copies of the same fonts are tracked; `*.jpg` is ignored with no jpg tracked (fine) but silently blocks future photos; `*.bak` ok; no entries for `.env*`, `.dev.vars`, `*.whl`, `*.log`, `.DS_Store`, `dist/`, `term/l1/out/*/fonts`. Fix: add them (below).
- H5 Medium. Seven zip files tracked (Weekly_PDFs zips 35-43 MB cumulative in history each, P6 scratch starters) duplicating PDFs also tracked individually. Fix: keep zips as release assets rather than tracked files.
- H6 Medium. README.md is out of date: it says the repo is "Primary 1 maths holiday program". It documents hp/, deck/, split/, taster/ but not p2-p6, term/ (2,232 files), school/, extension/, portal/, functions/, worker/, practice/, tutor/, rebuild/, print/, levels/, wrangler.jsonc, docs/ structure, the Stripe/Supabase/Cloudflare set-up, or the audit docs. Its backticked paths `project/deck.json` and `hub/` are relative to subfolders, not the root (ambiguous, not broken). Fix: rewrite README as a map of the repo (top-level folders, how to build, what is private/gitignored, where decisions live).
- H7 Low. Dead links: markdown relative-link check over README.md, portal/README.md, docs/** and website/*.md (150 files): 0 broken. PASS.
- H8 Low. docs/audit/scratch_check_p6 holds editor screenshots and result JSON (scratch). Fix: move out of the repo or ignore.
- H9 Low. No LICENSE file; the ownership/licence of the code and contents (Preciouslyours Pte Ltd) is not stated in the repo.
- H10 Low. Branches include origin/audit-fixes and origin/main; local branch is far ahead. Not a problem, but merge strategy for a 3.5 GB history should be settled before push.

## 4. docs/terms/owner_decisions.md consistency (145 lines)

Contradictions or stale entries, and which is current (later dated entry wins, unless the owner says otherwise):
1. Lesson length: "75 MINUTES" entry (23 Oct) is superseded by "stay 90 MINUTES (23 Oct, later)". Current: 90. The 2027 slot grid entry (75-minute slots) is therefore stale; docs/schedule/term_2027_t1_availability.md is flagged to be recomputed.
2. Payments: Decided item 8 still reads "originally HitPay"; "payment gateway is Stripe, replaces HitPay (23 Oct)" is current. Stripe code is not yet live (migration "review first, not yet applied"), PayNow by hand during the beta.
3. "Open" section still lists items resolved below it: Term 1 vs holiday course (resolved: Term 1 is new lessons), discount size (resolved: 5%). Still open: term price (website says S$65/S$650), content of the 10th lesson. Fix: move the resolved lines out of Open.
4. Decided item 2 says 10 lessons per term (40/level/year); other entries still talk about 9 of 10 and 20 written lessons (stale phrasing). Current: 10 per term.
5. End-of-term check: "takes 20 minutes" check with scores/WhatsApp photo return, then "Mi's Challenge Quest" (game, no scores, no word 'test'). Current: Challenge Quest; the "check" entries and the "photos of the check are returned via WhatsApp" default conflict with the Quest rule that the tutor keeps private notes only and with item 9 (no paper to camera; photograph look-back page after class).
6. Printed workbooks: "extension workbooks are not given" with payment vs later addenda (also an extra resource for enrolled students, optional add-on): not contradictory if read as "not included", but wording differs. Current: extension books are a separate paid add-on.
7. Extension workbook content: "original problems only, no contest-style" (early) vs "built from questions similar to holiday-program questions" (Addendum 3) vs "extend the holiday program, 10 units following the 10 holiday lessons" (23 Oct clarification). Current: latest (holiday extension, new questions).
8. Workbook delivery: "The workbook is a PDF you print yourself" (terms page) vs "beta workbook is POSTED (23 Oct)" - decision recorded, site text still to change (owner decision lists it as consequence; website/terms.html must match - see the website audit).
9. Printed workbooks colour: earlier "printable colour" plans vs "PRINTED workbooks are black and white; SOFT COPIES colour (23 Oct)". Current: B/W print, colour soft copy.
10. School puzzle books: Addendum 9 says 20 pages per level; earlier notes in the plan mention 40. Prices: "prices on hold (23 Oct)" overrides pricing_research.md placeholders; check no price appears on any page.
11. Address retention: 90 days vs 30 days: 30 days is current (owner chose).
12. Beyond-syllabus rule (every lesson has something beyond P1) vs "Start here stays school-range" - consistent, but the L1 "stronger arithmetic" decision is a standing conflict with any 'MOE-aligned' claim; keep the no-overclaim rule.

## Ranked top 10

1. H1 Repository 3.5 GB (3.28 GiB loose objects, 3.8 GB term/l1 history): gc and stop committing generated term/l1/out; decide before any push.
2. S1 Personal Gmail as public data-protection contact on the privacy page.
3. C5 No OFL / third-party licence texts for 320 shipped font files.
4. H3 Seven untracked .whl files in root with no ignore rule.
5. H2 Generated outputs tracked and duplicated (fonts x300, outputs/print twice, workbook_body/full inconsistently ignored).
6. H6 README describes only Primary 1 holiday program.
7. Owner_decisions: Open section holds resolved items; 75-minute grid and HitPay lines stale (list above).
8. C3 P4/P5 learner-facing items share 11-13 word stems with private extracts (change numbers/context).
9. H5 Tracked zips duplicating PDFs.
10. C1 Quoted 14-22-word paper lines in docs/books pattern files.

## Not audited
- History scan of term/l1/out blobs (3.8 GB) for secrets and emails (working tree is clean).
- Original school/contest PDFs (not present); overlap only versus the extracts. Image-only PDF pages (no text layer).
- Licences of mascot artwork, images, and the non-font libraries beyond noting the missing notices file.
- Live Supabase/Cloudflare/Stripe configuration; GitHub-side secret scanning alerts for the remote.
- External URLs (no link crawl, only relative markdown links).

## Proposed cleanup commands (NOT run)

```
# 1. stray wheels and ignore rules
rm -f /home/user/math-inquirers/*.whl
printf '%s\n' '*.whl' '.env' '.env.*' '.dev.vars' '*.log' '.DS_Store' 'website/dist/' 'practice/dist/' 'term/l1/out/*/fonts/' 'docs/audit/scratch_check_*/' >> .gitignore

# 2. stop tracking generated files (keeps them on disk)
git rm -r --cached term/l1/out/*/fonts p2/workbook_body.html p2/workbook_full.html p3/workbook_*.html p4/workbook_*.html p5/workbook_*.html p6/workbook_*.html
git rm --cached workbook_body.html

# 3. pack the 19k loose objects (no history rewrite)
git gc --aggressive --prune=now

# 4. only if the owner agrees to rewrite history before the first push (back up first: git clone --mirror . ../mi-backup.git)
git filter-repo --path term/l1/out --invert-paths      # then rebuild term/l1/out from term/l1 sources
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```
