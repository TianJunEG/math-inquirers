# Launch checklist: Fri 23 Oct to Tue 24 Nov 2026

First lessons: Tue 24 Nov (Levels 1 to 4), Thu 26 Nov (Level 6), Fri 27 Nov (Level 5). Week of Mon 23 Nov is the first week. Owner = Jasmine; Assistant = Claude (repo work). Dates are targets; tick as done. Links to detail: `docs/holiday_readiness.md` (blockers), `docs/printing/`, `portal/README.md`, `ops/README.md`.

## Critical dates
| Date | What |
|---|---|
| Fri 23 Oct | Today: kit built (calendars, reports, observation sheet, drafts); start lawyer and printer enquiries |
| Mon 9 Nov | **Printer order placed** (workbooks printed in black and white, posted before lesson 1) |
| Sun 15 Nov | Register-by date (suggested; owner sets `register_by` in `beta_schedule.json`) |
| Fri 20 Nov | All posted; families have Meet links and calendar files by Mon 23 Nov |
| Tue 24 Nov | First lessons |

## Week 1: Fri 23 to Sun 1 Nov
| Date | Task | Owner | Assistant |
|---|---|---|---|
| Fri 23 Oct | Decide the main open choices: PayNow-only beta or Stripe live; who pays postage (decided: included); parcel policy; recording storage (Drive) | Owner | Lists options |
| Fri 23 Oct to Mon 26 Oct | **Lawyer:** find and brief a Singapore lawyer; send `website/terms.html`, `website/privacy.html`, `docs/ops/tutor_agreement_draft.md`; ask for turnaround by Fri 6 Nov | Owner | Prepare brief and clean drafts of open brackets |
| Mon 26 Oct | **Printer:** send `docs/printing/quote_request.md` (black and white, 80 to 100 gsm, double-sided, bound; 6 levels, quantities per group up to 8) to 2 or 3 printers; ask lead time and courier days | Owner | Update quote with latest page counts, B&W specs |
| Tue 27 Oct | **Domain and email:** buy the domain, set up business email (replace placeholder `pypteltd@gmail.com` as data protection contact); decide Cloudflare DNS | Owner | List every page needing the new address |
| Wed 28 Oct | **WhatsApp Business** on +65 9880 5962: business profile, hours, greeting and away message, labels, quick replies from `docs/ops/message_templates.md`; link devices carefully | Owner | Load quick replies as copy-paste list |
| Thu 29 Oct | Tutor: confirm who teaches (owner or another tutor); if another, start `tutor_agreement_draft.md` with lawyer | Owner | |
| Fri 30 Oct | Confirm MOE 2026 school holiday dates against the MOE calendar | Owner | Re-check schedule file |
| Sat 31 Oct | **Decks:** republish stale decks / tutor console serve (blocker 4) | Owner: pick option | Republish |

## Week 2: Mon 2 to Sun 8 Nov
| Date | Task | Owner | Assistant |
|---|---|---|---|
| Mon 2 Nov | Choose the printer, approve the proof (one workbook per level), confirm lead time and postage | Owner | Check proof for B&W patterns (`print/check_bw.py`) |
| Tue 3 Nov | **Access lock plan:** decide the go-live date for removing the Cloudflare Access lock; then build with `--public` (removes noindex and robots Disallow) | Owner: decide | Run build, check |
| Wed 4 Nov | **Test Meet recording:** with a friend, record a 10-minute Meet in the business account; check what is recorded (tutor, shared screen, unmuted voices; cameras and names not shown), where it is stored (Drive), who can open the link, how long it takes to appear | Owner | Write the check list |
| Thu 5 Nov | **Trial lessons (dry runs) begin:** one full lesson per level with a friendly child, using `ops/out/tutor_observation_sheet.pdf` | Owner (teaches and observes) | Prints sheets, adjusts budgets from notes |
| Fri 6 Nov | Lawyer comments back; accept or reject changes | Owner | Apply to terms, privacy, fill brackets, remove draft banners |
| Sat 7 Nov | Dry run: Levels 1 and 2 (if not done) | Owner | |
| Sun 8 Nov | Print order files final: confirm quantities per register-by list | Owner | Export dispatch list template |

## Week 3: Mon 9 to Sun 15 Nov
| Date | Task | Owner | Assistant |
|---|---|---|---|
| **Mon 9 Nov** | **Place the printer order** and pay the deposit (workbooks plus Inquirer Kit; hold quantity for late registrations) | Owner | Send final print PDFs |
| Mon 9 Nov | **Consent versions:** after the lawyer review, bump `VERSIONS` in `portal/public/common.js` and `CONSENT_VERSION` in `website/interest_ui.py` to the reviewed text; rebuild | Owner: approve final text | Edit, rebuild, deploy |
| Tue 10 Nov | **Stripe / PayNow:** if Stripe: create the account for Preciouslyours Pte Ltd, test keys, Cloudflare secrets, webhook; apply `portal/supabase/stripe_migration.sql` after review; run a test payment. If PayNow-only: confirm the PayNow number and the reference format | Owner (accounts, keys) | Sandbox tests |
| Wed 11 Nov | Dry runs: Levels 3 and 4 | Owner | |
| Thu 12 Nov | Dry runs: Levels 5 and 6 (Level 6: Scratch check) | Owner | Adjust budgets from the notes |
| Fri 13 Nov | **Tutor agreement** reviewed and signed (if another tutor); tutor safeguarding briefing | Owner | |
| Sat 14 Nov | Recording storage ready: private Drive folder per group; confirm access rules | Owner | |
| Sun 15 Nov | **Register-by date.** Close registrations (late ones get the PDF to print at home) | Owner | Export confirmed list per group |

## Week 4: Mon 16 to Fri 20 Nov
| Date | Task | Owner | Assistant |
|---|---|---|---|
| Mon 16 Nov | Confirm places and payments with every family (message 1 or 2); send workbook courier details as the printer ships | Owner | Generate dispatch list (level, name, address, phone) |
| Tue 17 Nov | Create the Google Meet link per group; add to `ops/meet_links.json`; rerun `python3 ops/make_ics.py` and `python3 ops/test_ics.py` | Owner: creates links | Run script, check |
| Wed 18 Nov | Send calendar files and the one-page guide to each family (messages 5 and 6) | Owner | |
| Thu 19 Nov | Workbooks posted; send tracking (message 3). Chase any late parcel | Owner | |
| Fri 20 Nov | **Go-live:** remove Access lock; build with `--public`; check live pages (terms, privacy, sign-up, level pages), links, privacy banner | Owner: approve | Build, verify |

## Final days: Sat 21 to Tue 24 Nov
| Date | Task | Owner | Assistant |
|---|---|---|---|
| Sat 21 Nov | Check every family has: payment, consent, Meet link, calendar file, tracking number or PDF | Owner | Status list |
| Sun 22 Nov | Tech check: Meet, recording, screen share, tutor console, phone remote; print tutor notes sheets | Owner | |
| Mon 23 Nov | Send message 7 (reminder) for Tuesday lessons; check parcels arrived (message 4) | Owner | |
| **Tue 24 Nov** | **First lessons** (Levels 1 to 4). Start the recording first; send recording links after (message 11) | Owner / tutor | Standby for fixes |

## Not before launch (parked)
Extension workbooks and shop, school puzzle books, term-time 2027 grid and pricing (prices are on hold), practice pages for more lessons, B&W print for term books.

## Open decisions for the owner
Stripe live vs PayNow only; parcel policy (7 days, one free resend, second loss); register-by date; tutor status (employee or contractor); recording link availability period; whether all six levels open on 24 Nov or only those that fill.
