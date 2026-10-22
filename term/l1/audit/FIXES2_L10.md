# Second fix pass, Lesson 10 (Story Steps) and the end-of-term check, 22 Oct 2026

Inputs: `audit/GUIDE_DECK_AUDIT_L10.md`, `audit/HOME_PARENT_PRACTICE_AUDIT_L10.md`, L10 rows of `audit/TERM_WIDE_AUDIT.md` (F1, F5, F10, F12), `FIXES_L10.md`, owner decisions (20-minute check, about 8 questions, WhatsApp-only photo return, 90-day retention). Files changed: `lessons/l10.json`, `verify/l10_checks.py`, `out/l10/` (incl. check sheet, key, note), `AUDIT_L10.md`. Validator 0 FAIL, 548+ checks, leak check clean; slow-class script 87:52; check part 15:45 scripted, 18:33 slow; workbook fill 96, 91, 89, 97, 88%; check sheet 4 pages (88, 82, 56, 81%), printed bar 100.00 mm; home 94%; parent 87%; note 1 page.

| Finding | Sev | Action |
|---|---|---|
| G1 / F1 check does not fit 20 minutes | High | Cut from 10 to 8 questions (15 answer parts, was 22): Q2 shares Lessons 2 and 4, Q5 shares Lessons 6 and 7, so every lesson is still checked; digit cards cut to one blank; story has two step lines (last number is the answer). Modelled time: middle child about 16 minutes including reading, slower child 18.5 plus flex; asserted in `verify/l10_checks.py`. |
| G3, G2 exit ticket duplicates Q8, story lesson squeezed | Med | Exit ticket leaves the live lesson (optional flex slides); the freed 4 minutes go to the workbook (24 minutes, Start here finished in class); exit part is the check only, minutes 63 to 83. |
| G6 hold-ups, G15 safety | Med, Low | Sneak-peek hold-up removed; brain break leans, no stepping back; thumbs up in explore. |
| G5, L10-1, L10-4 photos and retention | Med | One rule everywhere (note, key, safeguarding, tutor prep, parent page): one photo per page to the business WhatsApp only, kept 90 days after the program ends then deleted, as privacy.html; WhatsApp named as a third-party service; "we" is the sender. Number removed from slide notes and never on slides. |
| G7 recording | Med | REC cue says the check is taken live or at the make-up slot. |
| G9 Q9 marking | Med | Ruler question accepts 5.5 to 6.5 cm, or right when part b is right. |
| F5 report claims | Med | Three areas instead of four (length and stories share one); term line no longer says "to say why". |
| L10-2, L10-3 | Med | Parent page says the check is optional; the sheet is sent a week before, no-printer route stated. |
| L10-5, L10-6, L10-8 | Med, Low | Home H1 and H3 have Step 1 and Step 2 lines; try-at-home has the "count everyone" example; Term 2 start date by the tutor, `next_materials` set. |
| F6 to F9, F29, P2 shared | Med | Recording statement, microphone routine, no first names, WhatsApp "still stuck" route, no paper to camera, beyond-P1 reminder, "do not hurry". |
| Named wrong working | Low | Talk slide says "a child says". |

Not fixed (shared tools or owner): `b_check.py` key text still says "one from each lesson", "Question 9" and "57% to 63%" (hard-coded; my key step says this means Question 7 and 5.5 to 6.5 cm), no draw box for the story question (id is fixed to C10), sheet cannot fit 3 pages, so it stays 4 pages with page 3 at 56%; look-back "(my tutor will come and help)"; Mi calculator image; no Term 1 console; `owner_decisions.md` and the plan still say 10 questions or 4/4/2 (owner to update); validator slow flag never OVER; s-end Mi bubble was avoided by shortening text.
