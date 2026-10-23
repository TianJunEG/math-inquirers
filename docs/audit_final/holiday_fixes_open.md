# Holiday program: fixes applied and items still open (23 Oct 2026)

Follows `docs/audit_final/holiday_program_final.md`. Scope: holiday, levels, outputs, print, k2, tutor data. Nothing under term/, school/, extension/, website/ or portal/ was touched.

## Fixed in the repo

| Finding | What was done |
|---|---|
| H1 P4 print: first cut-out page backed Lesson 10 Go further | `print/make_print_pdfs.py` now inserts one blank page before the first cut-out page when it would land on a back (even) page. P4 print: page 57 content, 58 blank, 59 Cut-outs, 60 blank. All six levels re-checked: every cut-out page is a front with a blank back. `print_spec.json` regenerated (P4 still 76 pages, 38 sheets, 10 blanks, but now 1 padding blank at p58 and no trailing blank pair). The B&W copies for P1 and P4 were rebuilt with `print/make_bw_print.py`. |
| H2 hold-ups to the camera (decision 9) | Wording changed in the SOURCE generators (`rebuild/*.py`, `p2..p6/content`, `p*/guide.js`, `hp/guide.js`, `hp/lessons.js`, `deck/`, `p2/gaps.json`, `p4/workbook_html.js`, `levels/reccues.js`). Replacement: tick your own work against the answer slide, say it together on three, fingers for choices, nothing held up to the camera. Decks regenerated (`gen_*` then `levels/restyle.py`), six tutor guides, weekly PDFs, P4 workbook (child page said "your tutor may look at it on camera if you hold it up") and `tutor/data` rebuilt. |
| M1 L1 "CHALLENGE DAY!" | `hp/workbook.js`, `hp/workbook_html.js` now "PUZZLE DAY!". L1 workbook (PDF, docx), print PDF (colour and B&W), weekly student pages rebuilt. Level 5 "Challenge Day" kept (decision). |
| M2 / price | `levels/mkextras.py` (P2-P6 What Learners Get) and the L1 What Learners Get (docx and PDF) now show only the beta fee: S$250 for all 10 lessons, S$25 a lesson, printed workbook and kit included. No regular or introductory price anywhere. The P2-P6 tutor guide "Fee" row (said S$500 introductory, regular S$650, 3 instalments) now shows the same beta fee. |
| M4 K2 readiness tiers | `k2/k2.py` reworded: no Core / Think Harder / Challenge / Group A; every child may choose any section. PDF rebuilt and copied to `outputs/designed/`. |
| M5 slide format | P2: the Go further slide id now equals its file name (`p2lN-challenge`); the generator `rebuild/p2gaps.py` no longer rewrites the id. P3 L2: column-sum pictures are inline SVG (`rebuild/gen_p3l2.py`), no `data:` images. |
| M6 L4 Go further numbering | `p4/guide.js` now says "Workbook Go further 5, 6, 7" like the workbook. L2, L3, L5, L6 already matched. |

## Not fixed, needs the owner or another team

1. **Republish the live decks.** The Claude Slides artifacts (all 60 decks) still carry the old text (hold-ups, P2 slide ids, P3 L2 `data:` images). The repo is fixed; the published copies need republishing and `outputs/deck_urls_all.json` refreshing. Not done here (publishing was not asked for).
2. **Decision 9 scope.** The audit asked the owner to confirm the rule covers the holiday program. I applied it everywhere, including whiteboard hold-ups ("whiteboards up together" is now "say the answer together on three"). Please confirm. Not changed: tutor-held props (a ruler, a cube) and children's hands (fingers, open palm for Buzz, "Hold up A or P"), and activities done "on camera" (folding, building, standing).
3. **Certificates.** Lesson 10 still says the tutor shows each certificate (child's name) on screen for about 12 seconds; the PDF is sent through the approved channel. Owner to say whether a named certificate on a recorded screen is acceptable.
4. **Private route in the parent note.** Decision 9 says the "I am still stuck" mark on the look-back page is photographed by the parent and sent to the business WhatsApp. The slides and guides now say this route exists but do not show the number (as decided). The parent-facing note that carries the number is not in the holiday folders I was allowed to edit; check the parent pack/taster wording.
5. **M3 L1 Free Taster placeholders** ("[Sign-up link or QR code]", "[Dates, fee and sign-up link]", "[Name, email or phone]"): the fee is known (S$250) but the sign-up link, dates and contact are owner facts. Not filled.
6. **Instalments.** The old guide row said "payable in 3 instalments". Dropped with the old price; owner to say whether instalments exist for the S$250 beta fee.
7. **M1(c) website and extension.** "Challenge Day" for Levels 1-4 remains in `website/data/level_lessons.json` (lines 50, 102, 154, 206), website level pages and dist copies, `weekly_dose_online.html`, `lp_build.py`, `mi_signup.html`, `referral.html`, `syllabus/index.html`, and `extension/config/levels.json:214`. Also the S$650 line on the website (decision log, line 21). Other agents own those areas.
8. **Published deck link names for Levels 2-4** still read "Challenge Day" (cosmetic, as logged in owner_decisions.md).
9. **M7 speaker notes hold answers.** Process point: keep deck links tutor-only. No change.
10. **Low findings** (L1 duplicate time pills, L2 question bank overlap, L3 to L6) not touched.

## Coordination note

Another agent is adding the Mi mascot to `split/` slides (uncommitted, `data-mi` images). My changes to those files were merged onto their versions, not overwritten; commit them together or re-run `rebuild/gen_*.py` then `levels/restyle.py` then `levels/normfoot.py`.
