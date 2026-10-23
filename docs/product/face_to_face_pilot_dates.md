# Face-to-face pilot: other dates that avoid the clash

Written Fri 23 Oct 2026 (planning only; nothing booked, sent, printed or changed). Answers the owner's question "is it possible to find other dates to avoid the clash?" for the Level 1 face-to-face pilot in `face_to_face_pilot_plan.md` (one group of at most 8 children, 10 lessons, two 90-minute lessons a session with a 15-minute break between them). The old default (Wed/Thu 2, 3, 9, 10, 16 Dec mornings) clashes with the held reserve groups R1 to R3.

**Short answer: yes.** Every Tue and Fri is taken by the online beta, every Wed and Thu morning by the reserve groups, Saturday morning by reserve R4 and Sunday morning by church. What is left is (1) Monday and Wednesday afternoons in December and (2) the week after the beta ends, 28 Dec to 2 Jan. Recommendation: Option 1 (section 3), with Option 2 as the fallback if the MOE reply, venue or insurance is not in by Fri 13 Nov.

## 1. Calendar facts relied on

| Fact | Date | Source / status |
|---|---|---|
| Last school day of 2026 (MOE primary and secondary) | Fri 20 Nov 2026 | Read on the official MOE press release "School Terms and Holidays for 2026" (moe.gov.sg, published 30 Jul 2025), opened 23 Oct 2026 |
| Year-end school holidays | Sat 21 Nov to Thu 31 Dec 2026 | Same MOE page (confirmed; earlier files called this "UNVERIFIED") |
| Deepavali | Sun 8 Nov 2026, so Mon 9 Nov 2026 is the public holiday | Same MOE page lists Mon 9 Nov 2026 as a public holiday |
| Christmas Day | Fri 25 Dec 2026 | Same MOE page |
| New Year's Day 2027 | Fri 1 Jan 2027 (fixed date; weekday checked by script) | The 2027 gazette was not opened: verify on mom.gov.sg |
| 2027 school year start | Mon 4 Jan 2027 is assumed | Not on the 2026 page: verify on moe.gov.sg. Treat 4 Jan as the end of the holiday window |
| Other public holidays Mon 30 Nov to Thu 31 Dec | none | MOE 2026 list (only Christmas Day falls in the window) |

Weekdays of every date in this file were generated or checked with a script (Python `datetime`), not by hand. Note that Mon 9 Nov, the day the launch checklist plans the printer order, is a public holiday.

Owner decisions applied (`docs/terms/owner_decisions.md`, 23 Oct 2026): R1 to R3 week-5 lessons move from Thu 24 Dec to Wed 23 Dec at the same times; R4 Sunday 2:00pm is not available (R4 needs a new slot, so only its Saturday 9:00am half is held here); Sunday church plus lunch blocks 10:30am to about 2:00pm (church ends about 11:15am); Saturday and Sunday lunch is 12:30 to 2:00pm; 15-minute breaks between classes. Other blocks from `beta_schedule.md`: Mon 7, 14, 21, 28 Dec 10:30am-12:30pm "P5M"; Wednesday 8:00-9:30pm "P5M"; Saturday 2:00-5:00pm orchestra.

Buffer rule used in the matrix: a pilot block counts as a clash if any beta lesson, reserve lesson or owner block is within 15 minutes of it. Morning block = 9:00am-12:15pm (two lessons). Afternoon block = Monday 1:30-4:45pm (after the P5M event and lunch) and every other weekday 3:00-6:15pm (after R3 ends 2:45pm).

## 2. Clash matrix, Mon 30 Nov to Thu 31 Dec 2026

Columns: (a) online beta lessons, all groups, from `website/data/beta_schedule.json` including the week-5 moves; (b) reserve groups R1 to R3 on Wed/Thu (Wed 23 Dec holds the moved week-5 lessons) and R4 Saturday, if released; (c) the owner's blocked times; (d) public holidays; then whether the morning and afternoon blocks above are free.

| Day | (a) Online beta | (b) Reserve groups | (c) Owner blocked | (d) Public holiday | Morning block 9:00-12:15 | Afternoon block |
|---|---|---|---|---|---|---|
| Mon 30 Nov | none | none | none | none | FREE | FREE |
| Tue 1 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4 |
| Wed 2 Dec | none | R1-R3 09:00-14:45 | P5M 20:00-21:30 | none | CLASH: reserve R1, reserve R2 | FREE |
| Thu 3 Dec | L6 18:15-19:45 | R1-R3 09:00-14:45 | none | none | CLASH: reserve R1, reserve R2 | CLASH: beta L6 |
| Fri 4 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30; L5 16:45-18:15 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4, beta L5 |
| Sat 5 Dec | L6 18:45-20:15 | R4 09:00-10:30 | lunch 12:30-14:00; orchestra 14:00-17:00; Sat 08:30-12:30 private tutoring in the 2027 grid (verify for holidays) | none | CLASH: reserve R4 | not tested (weekend) |
| Sun 6 Dec | L5 16:15-17:45 | none | church+lunch 10:30-14:00; Sun R4 14:00 not available | none | CLASH: own church+lunch | not tested (weekend) |
| Mon 7 Dec | none | none | P5M 10:30-12:30 | none | CLASH: own P5M | FREE |
| Tue 8 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4 |
| Wed 9 Dec | none | R1-R3 09:00-14:45 | P5M 20:00-21:30 | none | CLASH: reserve R1, reserve R2 | FREE |
| Thu 10 Dec | L6 18:15-19:45 | R1-R3 09:00-14:45 | none | none | CLASH: reserve R1, reserve R2 | CLASH: beta L6 |
| Fri 11 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30; L5 16:45-18:15 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4, beta L5 |
| Sat 12 Dec | L6 18:45-20:15 | R4 09:00-10:30 | lunch 12:30-14:00; orchestra 14:00-17:00; Sat 08:30-12:30 private tutoring in the 2027 grid (verify for holidays) | none | CLASH: reserve R4 | not tested (weekend) |
| Sun 13 Dec | L5 16:15-17:45 | none | church+lunch 10:30-14:00; Sun R4 14:00 not available | none | CLASH: own church+lunch | not tested (weekend) |
| Mon 14 Dec | none | none | P5M 10:30-12:30 | none | CLASH: own P5M | FREE |
| Tue 15 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4 |
| Wed 16 Dec | none | R1-R3 09:00-14:45 | P5M 20:00-21:30 | none | CLASH: reserve R1, reserve R2 | FREE |
| Thu 17 Dec | L6 18:15-19:45 | R1-R3 09:00-14:45 | none | none | CLASH: reserve R1, reserve R2 | CLASH: beta L6 |
| Fri 18 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30; L5 16:45-18:15 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4, beta L5 |
| Sat 19 Dec | L6 18:45-20:15 | R4 09:00-10:30 | lunch 12:30-14:00; orchestra 14:00-17:00; Sat 08:30-12:30 private tutoring in the 2027 grid (verify for holidays) | none | CLASH: reserve R4 | not tested (weekend) |
| Sun 20 Dec | L5 16:15-17:45 | none | church+lunch 10:30-14:00; Sun R4 14:00 not available | none | CLASH: own church+lunch | not tested (weekend) |
| Mon 21 Dec | none | none | P5M 10:30-12:30 | none | CLASH: own P5M | FREE |
| Tue 22 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4 |
| Wed 23 Dec | L5 16:45-18:15 | R1-R3 09:00-14:45 | P5M 20:00-21:30 | none | CLASH: reserve R1, reserve R2 | CLASH: beta L5 |
| Thu 24 Dec | L1 09:00-10:30; L2 10:45-12:15; L3 13:15-14:45; L4 15:00-16:30; L6 18:15-19:45 | none | none | none | CLASH: beta L1, beta L2 | CLASH: beta L4, beta L6 |
| Fri 25 Dec | none | none | none | Christmas Day (PH) | CLASH: public holiday | CLASH: public holiday |
| Sat 26 Dec | L6 18:45-20:15 | R4 09:00-10:30 | lunch 12:30-14:00; orchestra 14:00-17:00; Sat 08:30-12:30 private tutoring in the 2027 grid (verify for holidays) | none | CLASH: reserve R4 | not tested (weekend) |
| Sun 27 Dec | L5 16:15-17:45 | none | church+lunch 10:30-14:00; Sun R4 14:00 not available | none | CLASH: own church+lunch | not tested (weekend) |
| Mon 28 Dec | none | none | P5M 10:30-12:30 | none | CLASH: own P5M | FREE |
| Tue 29 Dec | none | none | none | none | FREE | FREE |
| Wed 30 Dec | none | none | P5M 20:00-21:30 | none | FREE | FREE |
| Thu 31 Dec | none | none | none | none | FREE | FREE |

Notes on the matrix:
- Levels: L1 9:00-10:30, L2 10:45-12:15, L3 1:15-2:45pm, L4 3:00-4:30pm (Tue, Fri; Thu 24 Dec last lessons), L5 Fri 4:45-6:15pm and Sun 4:15-5:45pm (Wed 23 Dec lesson 9), L6 Thu 6:15-7:45pm and Sat 6:45-8:15pm (Thu 24 Dec lesson 9).
- Reserve times: R1 Wed/Thu 9:00-10:30, R2 10:45-12:15, R3 1:15-2:45pm, R4 Sat 9:00-10:30. Reserves only exist if a group fills and one is released, so (b) is a potential clash, but one the owner has said must be kept.
- Nothing is free on Tue and Fri (beta), Wed/Thu mornings (reserves), or Sat/Sun mornings.
- Weekend afternoons were not tested: Sat 2:00-5:00pm orchestra and Sun beta L5 make them unsuitable.
- Not in the owner-blocked column because it is unknown: the day job in the holidays, and the "taken" private-tutoring slots of the 2027 grid (Mon 3:00-4:30pm, Wed 3:00-5:00pm and 5:30-7:00pm, Sat 8:30am-12:30pm). `beta_schedule.md` says both calendars were clear for 24 Nov to 27 Dec, but the options below that use those times must be confirmed by Jasmine.
- Days before the matrix window (21 to 23 Nov) were rejected: the launch checklist is at its busiest, printed workbooks would not be ready and MOE could not have answered.

## 3. Three options that avoid every clash

All three keep the pilot design: Level 1, one group of up to 8, 10 lessons in five two-lesson sessions, 15-minute break between lessons, Lessons 1 and 2 together and so on. Each date was checked against the matrix (free in the relevant block).

### Option 1 (recommended): Monday and Wednesday afternoons, 7 to 21 Dec

| Day | Lessons | Times |
|---|---|---|
| Mon 7 Dec | 1 and 2 | 1:30-3:00pm, break to 3:15pm, 3:15-4:45pm (children arrive 1:20pm) |
| Wed 9 Dec | 3 and 4 | 3:00-4:30pm, break to 4:45pm, 4:45-6:15pm (arrive 2:50pm) |
| Mon 14 Dec | 5 and 6 | 1:30-3:00pm, 3:15-4:45pm |
| Wed 16 Dec | 7 and 8 | 3:00-4:30pm, 4:45-6:15pm |
| Mon 21 Dec | 9 and 10 | 1:30-3:00pm, 3:15-4:45pm |

Clear of: all online beta lessons; R1 to R3 (Wed lessons start at 3:00pm, 15 minutes after R3 ends at 2:45pm); the Monday P5M event (ends 12:30pm); the Wednesday P5M (8:00pm); public holidays. Wed 23 Dec is deliberately not used (beta Level 5 at 4:45pm and the moved reserve lessons).
- Pros: mid-December is before Christmas week, so attendance risk is lowest; a venue is easy to book; the pilot ends before the beta's last week; every lesson is 2 to 5 days after the previous pair, close to the two-a-week online rhythm; starts a week later than the old default (more time for MOE and the venue).
- Cons: afternoons, not the online beta's morning times, so time of day is no longer held equal in the comparison (note it in the record); Wednesday finishes 6:15pm, long for 6-year-olds and into dinner time (a snack in the break if the venue allows food); needs Jasmine's Mon and Wed afternoons free, which the 2027 grid shows as private tutoring (confirm); the owner is teaching the beta at the same time.
- Parents: many families travel in the December holidays; a 7 to 21 Dec window sits before the usual Christmas travel peak, but ask on the interest form for any away dates. School-run traffic is not an issue in the holidays; Wed 6:15pm pickup needs a named adult. Christmas-week attendance risk is low (the last session is Mon 21 Dec).

### Option 2 (fallback): the week after the beta, Mon 28 Dec to Sat 2 Jan

| Day | Lessons | Times |
|---|---|---|
| Mon 28 Dec | 1 and 2 | 1:30-3:00pm, break to 3:15pm, 3:15-4:45pm (P5M event is 10:30am-12:30pm, so the morning is not used) |
| Tue 29 Dec | 3 and 4 | 9:00-10:30am, break to 10:45am, 10:45am-12:15pm |
| Wed 30 Dec | 5 and 6 | 9:00-10:30am, 10:45am-12:15pm |
| Thu 31 Dec | 7 and 8 | 9:00-10:30am, 10:45am-12:15pm (New Year's Eve; home before lunch) |
| Fri 1 Jan | none | public holiday |
| Sat 2 Jan | 9 and 10 | 9:00-10:30am, 10:45am-12:15pm (Saturday 8:30am-12:30pm is "taken" in the 2027 grid: confirm for the holidays) |

Clear of: every online beta lesson (the last is Sun 27 Dec) and every reserve lesson (week 5 ended Wed 23 Dec; R4 Sat 26 Dec); the only owner blocks (Mon 28 Dec P5M, Wed 30 Dec 8:00pm) are avoided; Fri 1 Jan holiday left empty.
- Pros: no clash with anything at all; mornings for four of five sessions, matching the online Level 1 time (9:00am); the owner is no longer teaching the beta, so attention is on the pilot; the most lead time of the three (D1 is 5 weeks after Option 1) for MOE, venue, insurance and printing; reserves can be released freely until 23 Dec.
- Cons: the last holiday week, with the least likely attendance (travel, relatives, New Year's Eve); some venues have reduced hours or are closed around 31 Dec to 2 Jan (ask); the Fri 1 Jan gap means Lessons 8 and 9 are 2 days apart through a holiday; the final lesson falls on Sat 2 Jan, just before school returns on Mon 4 Jan (assumed); results arrive after the term-time launch work; a Monday afternoon session breaks the all-morning pattern.
- Parents: this is the week many families are away or hosting. Ask the interest form for "free on all of 28 Dec to 2 Jan"; expect to lose more families than in Option 1 and keep a waitlist. Children are not in school, but parents may be at work between Christmas and New Year, so check collection arrangements.

### Option 3: Monday and Wednesday afternoons one week earlier, 30 Nov to 14 Dec

| Day | Lessons | Times |
|---|---|---|
| Mon 30 Nov | 1 and 2 | 1:30-3:00pm, 3:15-4:45pm (no P5M event on this Monday) |
| Wed 2 Dec | 3 and 4 | 3:00-4:30pm, 4:45-6:15pm |
| Mon 7 Dec | 5 and 6 | 1:30-3:00pm, 3:15-4:45pm |
| Wed 9 Dec | 7 and 8 | 3:00-4:30pm, 4:45-6:15pm |
| Mon 14 Dec | 9 and 10 | 1:30-3:00pm, 3:15-4:45pm |

Clear of: the same items as Option 1.
- Pros: finishes by 14 Dec, well before Christmas; the same weekly rhythm as Option 1.
- Cons: starts only 5 weeks from today and 6 days after the beta launch (first beta lessons Tue 24 Nov); the MOE reply, venue, insurance, forms and printing would all be squeezed into the busiest 4 weeks of the owner's year; same afternoon and Wed 6:15pm concerns as Option 1. Not recommended unless MOE answers very early.
- Parents: the earliest start; best if families mostly travel later; offers must go out around Fri 6 Nov.

### Recommendation

Choose **Option 1** and take the go/no-go on Fri 13 Nov. If by then the MOE reply, the venue or the insurance is still missing, switch to **Option 2** and move the go/no-go to Fri 27 Nov (the cost is higher Christmas-week attendance risk). Keep the March 2027 holidays (Option D in the plan) as the last fallback. The owner should confirm that Mon and Wed afternoons (Option 1) or the Mon 28 Dec afternoon and Sat 2 Jan morning (Option 2) are really free before anything is announced.

## 4. Lead-time reality

Today is Fri 23 Oct. The MOE question is the blocking item (nothing is announced to parents or fees taken until it is answered). Times below are the latest dates, working back from Day 1. Assumptions marked "assumed" are not from an official source.

| Step | Option 1 (D1 Mon 7 Dec) | Option 2 (D1 Mon 28 Dec) | Option 3 (D1 Mon 30 Nov) |
|---|---|---|---|
| Choose option, confirm owner availability | Mon 26 Oct | by Fri 30 Oct | Mon 26 Oct |
| Send the MOE enquiry (plan section 2.3) | Mon 26 Oct | by Fri 6 Nov | Mon 26 Oct |
| MOE reply must be in (go/no-go) | Fri 13 Nov (absolute last Fri 20 Nov) | Fri 27 Nov (absolute last Fri 4 Dec) | Fri 6 Nov (absolute last Fri 13 Nov) |
| Venue: enquire (ask about the exact dates and holiday hours) | by Fri 30 Oct | by Fri 13 Nov | by Fri 30 Oct |
| Venue: booked with a refundable deposit | Wed 11 Nov | Fri 20 Nov | Wed 4 Nov |
| Insurance quote and cover in place | quote Mon 2 Nov; cover by Fri 27 Nov | cover by Fri 11 Dec | cover by Fri 20 Nov |
| Parents: interest list ("dates and fee to be confirmed") | Mon 2 Nov | Mon 9 Nov (PH; send Tue 10 Nov) | Mon 26 Oct to Mon 2 Nov |
| Parents: offers, forms, fee, refund rule | Fri 13 Nov | Fri 27 Nov | Fri 6 Nov |
| Forms back | Wed 25 Nov | Fri 11 Dec | Wed 18 Nov |
| Seats confirmed in writing | Fri 27 Nov | Mon 14 Dec | Fri 20 Nov |
| Venue address and arrival information | Mon 30 Nov | Wed 16 Dec | Fri 20 Nov |
| Reminder to parents (day before) | Fri 4 Dec | Sun 27 Dec | Fri 27 Nov |
| Workbooks: add 10 Level 1 workbooks (and kit sheets) to the printer order | order due about 9 Nov | same order (preferred) | same order (mandatory) |
| Workbooks arrive and kits are cut and bagged | by Fri 20 Nov; kits Sat 28 to Sun 29 Nov | arrive by Fri 20 Nov; kits Mon 14 to Fri 18 Dec | arrive by Fri 20 Nov; kits 21 to 27 Nov |
| Day 1 | Mon 7 Dec | Mon 28 Dec | Mon 30 Nov |
| Last lesson | Mon 21 Dec | Sat 2 Jan | Mon 14 Dec |
| End-of-program notes | Fri 25 Dec is a holiday: send Mon 28 Dec | Tue 5 Jan | Fri 18 Dec |
| Delete personal data (30 days after) | Wed 20 Jan | Mon 1 Feb | Wed 13 Jan |

Notes on printing:
- The print deadline is about 9 Nov for the holiday workbooks (`owner_decisions.md`; `launch_checklist.md`). **Mon 9 Nov is a public holiday (Deepavali observed)**: ask the printer whether it works that day; otherwise place the order on Fri 6 Nov or Tue 10 Nov.
- Add 10 Level 1 workbooks to the same run for any option; the printed materials are the same as the beta's Level 1. This must be decided before the order, even though the MOE reply is not in; the cost of 10 spare books is small, and an unused pilot lot can be sold as beta stock. For Option 2 only, a small second run is possible if the printer's lead time is under about 3 weeks (assumed, not quoted); ask in the quote request.
- Printed kit pieces (cutting and bagging) need about a week of owner or assistant time.

Notes on Option 2: lead time is relaxed, but venue availability over 31 Dec to 2 Jan and parent replies in the Christmas week are the new risks; it needs the offer to go out before the holiday rush (Fri 27 Nov) and seats confirmed by Mon 14 Dec.

## 5. Open items for the owner

1. Which option, and confirmation that Monday and Wednesday afternoons (Options 1 and 3) or Mon 28 Dec afternoon plus Sat 2 Jan morning (Option 2) are free: day job in the holidays, the "taken" private-tutoring slots of the 2027 grid, the "P5M" events.
2. Whether a pilot in the afternoon is acceptable, given the online Level 1 comparison runs at 9:00am.
3. Whether the Mon 9 Nov printer order can be placed that day or must move.
4. Verify on moe.gov.sg the 2027 school start date and, for the fallback, the March 2027 holidays; verify the 2027 public holidays on mom.gov.sg.
5. Whether to release the reserve groups at all before the pilot, since Options 1 to 3 do not depend on it.
