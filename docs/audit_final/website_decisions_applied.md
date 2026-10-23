# Website and schedule: owner decisions applied (23 Oct 2026, late batch)

## 1. Refund rule (answer 13)
One rule everywhere: the November beta fee is NOT refunded; a child may make up a missed lesson ONCE by joining the same lesson in another class of the same level (seat permitting). If we cancel a lesson or group and cannot reschedule, we refund lessons not held (unchanged). The old "cancel within 60 days, pro-rata refund" wording is gone from all sources.
Changed: website/lp_build.py (FAQ "What if we need to cancel, or miss a lesson?", "missed a lesson" FAQ, price-box note), website/hub/qa.py (hub parent question), website/terms.html (section 5 table), website/privacy.html (consent withdrawal: data rights stay, fees not refunded, no legal conclusions), website/referral.html (prototype enrol note). Generated: website/mi_signup.html, website/hub/parent_questions.html, website/dist/ (index, terms, privacy, parent-questions). The register-form tick text ("terms and refund policy") and the shop page needed no change; portal/ non-public files only mention refunds in the Stripe admin steps (not touched). Not edited: terms section 5 regular-program rows and section 7 (term-time draft, not the beta).

## 2. Contact email (answer 9)
pypteltd@gmail.com added in website/terms.html (section 14) and kept in website/privacy.html as the data-protection contact, both marked "for now, to be changed later". Registered office address placeholder stays; both "Draft, not yet reviewed by a lawyer" banners kept. Reminder added to docs/audit_final/open_owner_items.md (item 7a).

## 3. Schedule (answers 15, 16, 17)
- R1-R3 week-5 lessons: Thu 24 Dec to Wed 23 Dec, same times (docs/schedule/beta_reserved.json `week5`, docs/schedule/beta_schedule.md). Published groups (L1-L4 on Thu 24 Dec) unchanged. ops/make_ics.py reads only website/data/beta_schedule.json (no reserves), so calendar output is unchanged; regenerated, ops/test_ics.py ALL OK.
- R4 (Sun 2:00pm) removed. PROPOSED R4B: Sat 9:00-10:30am + Sun 6:00-7:30pm, Levels 5-6 (follows Level 5 at 4:15-5:45pm with a 15 minute break, ends before 9pm, clear of church and lunch). Alternative: Sun 2:15-3:45pm. Files: website/data/interest_slots.json (id R4B, old id gone), docs/schedule/beta_reserved.json, beta_schedule.md, website/tests/interest_test.py.
- Thu 7:30pm and Sun 7:15pm 2027 options: already Levels 5 and 6 only in interest_slots.json; locked by new website/tests/slots_data_test.py. docs/schedule/term_2027_t1_availability.md section 8 added. No SQL source holds slot ids or levels, so no SQL changed (nothing applied to Supabase).

## 4. Build and tests
Rebuilt lp_build, level_pages, shop_build, hub/build, build_site (private preview, no --public). Passed: website/tests/interest_test.py, shop_test.py, slots_data_test.py, ops/test_ics.py. Screenshots at 400 and 1280 px (terms, home FAQ, parent questions, Level 5 page) viewed; no horizontal scroll.

## Could not do / open
- R1-R3 clash: their own Wednesday lesson of week 5 is also Wed 23 Dec at the same time, so applying the decision literally puts two lessons in one slot. Flagged in the data and open_owner_items.md item 6; owner must choose another slot.
- R4B is a proposal awaiting the owner.
- Beta pages say nothing yet on how many make-ups apply if a child misses two lessons beyond "once"; wording follows the owner's answer exactly.
- Some source edits were already swept into another agent's WIP commit.
