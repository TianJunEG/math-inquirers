# Face-to-face pilot plan (December 2026 school holidays)

Planning document, written Fri 23 Oct 2026. Nothing has been sent to anyone, booked, printed or changed. Website, portal and all materials are untouched. Every "default" below is a suggestion Jasmine can change. Anything marked UNVERIFIED comes from secondary sources or from files in this repository, not from an official page opened today.

Sources read: `docs/schedule/beta_schedule.md`, `docs/schedule/term_2027_t1_availability.md`, `docs/legal/review.md` (section 1.4 and L3), `docs/terms/owner_decisions.md`, `docs/ops/launch_checklist.md`, `docs/ops/tutor_agreement_draft.md`, `docs/ops/message_templates.md`, `docs/printing/*`, `docs/holiday_readiness.md`, `hp/budget.json`, `outputs/print/print_spec.json`, `website/data/level_lessons.json`, `docs/pedagogy/term_review.md` section 11 and `docs/pedagogy/holiday_review.md` section 11. There is no `docs/measurement/learning_record_spec.md` in the repository, so the learning-record rubric used here is the one in `term_review.md` section 11 (four observation prompts, explain ladder in section 2.4, optional three-word scale) plus the tutor signs A to F and the Form A / Form B idea in `holiday_review.md` section 11.

No claim of MOE, GEP or SASMO affiliation, approval or outcome is made or implied anywhere in this plan, and none should appear in anything sent to parents.

---

## 0. The short version

1. Run one group of up to 8 children, ages 6-8 (Level 1), for the 10 holiday lessons, in a hired community room (not a private home), with two adults in the room.
2. Keep the number of children at the venue under 10 at all times, and ask MOE the question in section 2.3 before taking any fees. Whether the owner contacts MOE first is her decision (section 6).
3. Default dates (updated 23 Oct 2026, owner asked for dates that avoid the Wed/Thu reserve-group clash): Option 1, two lessons a session on Mon 7, Wed 9, Mon 14, Wed 16 and Mon 21 Dec 2026, in the afternoon; fallback Option 2, Mon 28 Dec to Sat 2 Jan. The old Wed/Thu morning dates are dropped. Full clash matrix, day-by-day schedules and lead times: `face_to_face_pilot_dates.md`.
4. The pilot also tests the paper learning record: a rotating observation of 2-3 children a lesson on a paper tutor sheet, plus optional age-light timed items.
5. Biggest risks: the MOE question, workload (the launch checklist is full until 24 Nov), a venue and insurance that cannot be arranged in six weeks, and tutor/assistant availability. Section 3.8 lists them. The honest fallback is to move the pilot to the March 2027 holidays.

---

## 1. Recommended pilot design (all defaults changeable)

### 1.1 Which level and group

| Choice | Default | Why | Alternative |
|---|---|---|---|
| Level | Level 1, ages 6-8 | The most complete holiday and term materials (readiness file: "the most mature level"; 61-page designed workbook, 68 print pages, 93-page guide, K2 pack, readiness tracker). Six-year-olds are also where paper and hand-raising matter most. | Level 2 (ages 7-9) is the next most complete. Older levels read and write more on paper but have no stronger materials. |
| Group size | One group, at most 8 children | Stays under the 10-person line (section 2.1). | Fewer is fine. 5 or 6 is enough to learn from. |
| Who | Children new to Math Inquirers, not the online beta Level 1 families | Gives a clean comparison with the online pilot (section 4.5). A child in both would see each lesson twice. | Allow a sibling pair if the owner wants. |
| Tutor | The owner teaches; a second adult assists | See sections 2.4 and 3.5. | Another tutor only after the tutor agreement and screening are settled. |
| Fee | Blank, owner decides | Prices are on hold; the only decided price is the beta fee S$25 a lesson, S$250 for 10 lessons, with printing and posting included. Whether the face-to-face pilot charges the same, less, or nothing is not decided. | See section 3.1. |

The 10 lessons (Level 1 holiday, from `website/data/level_lessons.json`; Lesson 10 is "Puzzle Day" by owner decision, the data file still says "Challenge Day"):

| No. | Title | Topic |
|---|---|---|
| 1 | Count with the Frog | Number patterns |
| 2 | Number Bond Inquiry | Number bonds |
| 3 | Let's Plan the Fruit Party | Picture graphs |
| 4 | Pattern Inquiry | Repeating and growing patterns |
| 5 | Mystery Number | Working backwards |
| 6 | Coin Combos | Money |
| 7 | Shape Safari | 2D shapes |
| 8 | Logic Lab | Logic and sorting |
| 9 | Measure It! | Length |
| 10 | Puzzle Day | Mixed puzzles |

All 10 run face-to-face. Do not drop lessons: the pilot is also the first live test of the full 10-lesson flow for six-year-olds (readiness file: "the risk is the pace for six-year-olds, which only a pilot will show").

### 1.2 Time of day and structure of a lesson day

Each lesson is the usual 90 minutes (the `hp/budget.json` split: opening, warm-up, sneak-peek, explore, mini-lesson, brain break, worksheet, talk time, exit ticket, look-back, flex). Rules taken from the schedule documents: at least 15 minutes between consecutive classes, a 60-minute lunch break between 12:00 and 2:00pm on any day with several classes, nothing before 9:00am or after 9:00pm, no Sunday class before about 2:00pm (church and lunch), Saturday 2:00-5:00pm blocked (orchestra), Saturday 12:30-2:00pm lunch.

Default two-lesson morning (children go home for lunch; no lunch supervision, no food in the room, which also removes most allergen risk):

| Time | What |
|---|---|
| 8:30am | Room open for the adults: set-up (section 3.4) |
| 8:50am | Children arrive, sign-in, toilet, name tags |
| 9:00-10:30am | Lesson A (90 minutes) |
| 10:30-10:45am | 15-minute break: toilet, water, snack in a labelled box only if the venue allows food, free movement outside the room |
| 10:45am-12:15pm | Lesson B (90 minutes) |
| 12:15-12:30pm | Sign-out, one named adult hands each child to the authorised person |
| 12:15-1:15pm | Owner's lunch (the schedule's default lunch hour, kept even though no class follows) |

Why mornings: it matches the Level 1 online beta times (Tue/Fri 9:00am), so the time-of-day effect is not a difference between the two pilots. Why two lessons a day is the ask rather than a rule: it is 3 hours 15 minutes of work for a six-year-old. The alternative below spreads it out.

| Pattern | Days | Pro | Con |
|---|---|---|---|
| Default: 2 lessons a day, 5 days | 5 | Fewest days for parents and the venue; fits "holiday course" | Long mornings for 6-year-olds; two Lesson 1-type new ideas in one day |
| Alternative: 1 lesson a day, 10 days | 10 | Gentler; closer to the online two-a-week rhythm if spread over two weeks | Twice the venue bookings and fees; more days the owner must be free; more parent trips |
| Alternative: 2 lessons a day for the first and last day only, 1 a day otherwise | 7 | Compromise | Complicated to explain |

### 1.3 Default dates and options (updated 23 Oct 2026; NOT confirmed; owner to choose)

The old default (Wed 2, Thu 3, Wed 9, Thu 10, Wed 16 Dec mornings) clashed with the reserve groups R1 to R3, which hold Wed/Thu 9:00am, 10:45am and 1:15pm. A full clash matrix of every day from Mon 30 Nov to Thu 31 Dec against the online beta, the reserves, the owner's blocked times and public holidays is in `face_to_face_pilot_dates.md`, with the day-by-day schedules and lead times. Summary:

Facts the dates rest on: MOE 2026 school year ends Fri 20 Nov and the year-end holidays run Sat 21 Nov to Thu 31 Dec (read on the official MOE press release on 23 Oct 2026); Mon 9 Nov and Fri 25 Dec 2026 are public holidays; Fri 1 Jan 2027 is New Year's Day (verify on mom.gov.sg); the 2027 school start (Mon 4 Jan assumed) is to verify on moe.gov.sg. Tue and Fri are taken by the online beta, Wed/Thu mornings by the reserves, Sat morning by reserve R4, Sunday morning by church. The owner's holiday availability (day job, "taken" private-tutoring slots, "P5M" events) is still unconfirmed.

| Option | Dates | Lessons | Notes |
|---|---|---|---|
| 1 (default, recommended) | Mon 7, Wed 9, Mon 14, Wed 16, Mon 21 Dec; Mon 1:30-3:00pm and 3:15-4:45pm, Wed 3:00-4:30pm and 4:45-6:15pm | 1-2, 3-4, 5-6, 7-8, 9-10 | No clash with any beta lesson, reserve, owner block or public holiday. Afternoons, so time of day differs from the 9:00am online Level 1 group; Wednesday ends 6:15pm; needs Mon/Wed afternoons confirmed free. Ends before Christmas week. |
| 2 (fallback) | Mon 28 Dec (1:30-3:00pm, 3:15-4:45pm), Tue 29, Wed 30, Thu 31 Dec (9:00am-12:15pm), Sat 2 Jan (9:00am-12:15pm) | 1-2, 3-4, 5-6, 7-8, 9-10 | After the beta ends (27 Dec), so no clash with anything. Most lead time, mornings (four of five sessions). Risks: attendance in the New Year week, venue hours, Fri 1 Jan holiday gap, Sat morning confirm. |
| 3 | Mon 30 Nov, Wed 2, Mon 7, Wed 9, Mon 14 Dec (same times as Option 1) | 1-2, 3-4, 5-6, 7-8, 9-10 | Earliest, but only 5 weeks of lead time and it starts the week the beta launches. Not recommended. |
| D | Move the whole pilot to the March 2027 holidays (13-21 Mar, UNVERIFIED) | 10 | Last fallback. Most time for MOE, venue, insurance and screening. |

Recommendation: plan for Option 1; if the MOE reply, venue or insurance is missing by Fri 13 Nov, switch to Option 2 and move the go/no-go to Fri 27 Nov; keep Option D as the last fallback. Section 1.2's two-lesson morning (9:00am and 10:45am) is the pattern for Option 2 and the old default; for Options 1 and 3 the Monday and Wednesday afternoon times above replace it (same 90-minute lessons and 15-minute break; children eat lunch at home first).

### 1.4 What changes from the online version

| Online (current) | Face-to-face |
|---|---|
| Child's own screen; shared deck; tutor remote on a phone | A projector or a large screen or a whiteboard for the deck (venue permitting). Or the tutor works from printed lesson notes and a whiteboard with no deck. The deck is built for screen sharing; test it on the venue's screen in the room visit. |
| Workbook posted to the home before lesson 1 | Workbook printed in black and white, handed out at the room (default) so no delivery addresses are collected. Owner decision: post instead if she prefers the beta routine (then PDPA delivery consent applies). |
| Inquirer Kit cut-outs cut at home by the family | Kit pages cut in advance by the owner or assistant and bagged per child (section 3.3), so lesson time is not spent on scissors. |
| "Hold paper to the camera" | Does not apply. Online, this is already forbidden (owner decision; tutor agreement 3.3). Face-to-face the tutor walks round and looks at paper where the child allows it. Children tick their own work against the answer slide and give choral answers, exactly as online. |
| Mute, unmute, chat, raise hand on screen | Hand-raising, a "show me with fingers" signal, whole-group choral answers "on three", partner talk. |
| Brain break at home | Movement breaks in the room: standing stretches, a counting walk, a "stand up if" game. Plan a safe space (section 3.4). |
| Recording for catch-up (Meet) | NOT applicable. Do not record. A child who misses a lesson gets the pages and a short catch-up note from the owner, not a recording link (message 10 in `message_templates.md` refers to a recording and would need a face-to-face version, not drafted here). |
| Google Meet link, calendar files | Calendar file for the dates (`ops/make_ics.py` creates online ones; a face-to-face one would need the venue address and no Meet link) and a printed map and arrival note. |
| Parents out of the room | Parents drop off and collect. Decide whether a parent may sit in lesson 1 (default: no, for the children's privacy and to keep the room count clear). |
| Photos of child's work only via the business WhatsApp | Same rule: the tutor takes no photos of children. If the owner wants any photos of the room or work, she needs separate written parent consent (section 2.6). |
| Break: 5 minutes inside the lesson | Same 5-minute brain break inside the lesson; plus the 15-minute break between lessons. Watch the six-year-olds' stamina (readiness file names the 5-minute break as a structural risk). |

### 1.5 What stays the same

The 90-minute lesson structure and budget; the strategy card and look-back routine added to the holiday workbooks (owner decision of 23 Oct, being done before 9 Nov); private paper; no scores shown to children; no ranking; tutor notes private; tiers anyone may choose; "pass" always allowed and the "I am still stuck" tick; answers never shown to children before the checking moment; Mi appears only where already placed; a maximum of 8 children; the same workbook files; and the tutor agreement rules on conduct.

Pages to print are the black-and-white files only (`outputs/print/bw/Math_Inquirers_P1_Workbook_PRINT.pdf`), never the colour print PDFs (owner decision 23 Oct).

---

## 2. Legal and regulatory checklist

Honest status: none of this is legal advice and none of it has been verified with the regulator or a lawyer. The repository's legal review (`docs/legal/review.md`, sections 1.4 and L3) already flags the registration question as unverified. Online lessons raised children's recording and safeguarding; face-to-face adds premises, physical safety and insurance, which the existing documents do not cover.

### 2.1 The registration threshold (the blocking item)

What the research says (UNVERIFIED, search results, last updated dates as shown there):
- MOE's "Register a private school" page says a private school must register its school, courses and teachers if it offers education for 10 or more persons, and that this includes tuition and enrichment centres teaching subjects taught in mainstream schools (`legal/review.md` 1.4).
- The Education Act section 21 is cited as "a place where 10 or more persons are being or are habitually taught, whether in one or more classes". Exact wording and the current edition have not been opened here.
- Registration is described as including premises and fire-safety requirements, a school management committee and registered teachers.
- A 2026 consultant guide says a centre teaching fewer than 10 may fall outside the rule, with advice to confirm with MOE.
- Sources disagree on whether the Committee for Private Education (CPE, under the Private Education Act) or MOE regulates enrichment centres. For a maths enrichment business for primary-age children, MOE appears the more likely, but this is not established.

Default rule for the pilot: **keep the total number of children at one venue under 10 at all times, and ensure no more than 8 children are ever taught there in a day or on the same premises across a week, unless the owner has confirmed the position with MOE in writing.** Practical reading:
- One group of at most 8 children only.
- Do not run a second group, a taster session or a "bring a friend" class at the same venue in the same period.
- Do not put sibling observers, parents or other children in the room to be "taught".
- Count children enrolled or on a waitlist who attend a trial lesson. The 8-child cap includes them.
- The assistant and the tutor are adults and not "persons taught", but ask MOE to confirm that.

What is not known, and is part of the question to MOE: whether "habitually taught ... in one or more classes" is counted per venue, per day, per business or across all the owner's groups including the online ones (about 12 groups of up to 8 online during the beta).

### 2.2 Online-only treated differently? (UNVERIFIED)

The repository's legal review did not find anything on how online-only classes are treated. The face-to-face pilot makes this more urgent, because a regulator that treats the pilot as a "place where persons are taught" may also ask about the online groups. The question below asks this directly. Do not assume that the online operation is exempt, and do not assume that the pilot being small makes it exempt.

### 2.3 The exact question to ask MOE (draft email, NOT SENT)

The recipient address and form are to be found on MOE's private education page ("Register a private school") or via GoBusiness, which has a guide titled "Notification for Private Tuition Enrichment" that could not be opened (HTTP 403) when researched. The owner should read that guide first, and decide whether she or a lawyer sends it. The lawyer brief in the launch checklist (term 23-26 Oct) is a natural place to add this question.

> Subject: Enquiry: does a small holiday maths enrichment class need MOE registration?
>
> Dear Sir/Madam,
>
> I run a small business, Preciouslyours Pte Ltd (UEN 201507566K), trading as Math Inquirers. We teach enrichment mathematics to primary-school-age children in small groups. We are not a school and we do not claim any affiliation with MOE.
>
> We currently teach online only, in groups of at most 8 children, 90-minute lessons. We are considering a single face-to-face class during the December 2026 school holidays: one group of at most 8 children, aged about 6 to 8, 10 lessons over about 5 mornings, in a hired community room or library meeting room, taught by one tutor with one adult assistant.
>
> We would be grateful for your written guidance on these points:
> 1. Under section 21 of the Education Act (a place where 10 or more persons are being or are habitually taught), does a single face-to-face class of at most 8 children at one venue require registration?
> 2. Is the number of persons counted per venue, per class, per day, or across all our classes and venues, including classes held online? If we run one group of 8 on some days and a different group of 8 at the same venue on other days, would that count as 16?
> 3. Are online-only classes (groups of at most 8, taught from the tutor's home) treated differently from classes at a physical place? Do they need any notification or registration?
> 4. Are the tutor and an assistant counted as "persons taught"? Are parents or guardians who stay for part of a lesson counted?
> 5. Is any notification, permit or approval needed for fewer than 10 children (for example under the GoBusiness "Notification for Private Tuition Enrichment" guide)? If so, which agency and form?
> 6. Does the Committee for Private Education / Private Education Act apply to a business like ours, or only MOE?
> 7. Whether we may charge fees for the pilot, and whether there are requirements on tutor qualifications, screening, fire safety or insurance for a class under 10 children.
>
> We have not taken any fees or registered any child for the face-to-face class. Please let us know if you need further details.
>
> Thank you,
> [Name], Preciouslyours Pte Ltd, [business email], +65 9880 5962

Notes: the draft says "not taken any fees" so the owner must not take fees before sending. It deliberately mentions the online groups. Ask MOE also whether a reply by email is acceptable evidence (keep it for seven years with the other company records, as the legal review proposes for agreements).

### 2.4 Venue

| Item | Detail |
|---|---|
| Type | A hired community room, library meeting room or church hall. **Not a private home**: no fire-safety checks, no separate toilets, unclear insurance and a safeguarding red flag. |
| Check with the venue | Maximum occupancy and the number the room is licensed for; that a children's paid class is allowed (some halls forbid commercial classes or tuition, some forbid fees); fire exits, extinguishers and assembly point; accessible toilets close by and whether children go alone; a water source; whether a locked cabinet or room is available for materials between days; air-conditioning; quiet and not a thoroughfare; booking cancellation rules and deposit; whether the venue requires its own insurance certificate or a hirer's indemnity; whether the booking is non-religious (a church hall may have rules about use). |
| Access | Door that does not let a child walk out unseen; a place for parents to wait. Check CCTV and whether the venue records, because that creates personal data of the children (PDPA, section 2.6). |
| Walk-through | Visit once with the assistant before booking. Take a floor plan, note exit routes and the nearest AED/first-aid box, and count desks and chairs. |
| Church constraint | The owner's own church and lunch block (Sunday to about 2:00pm) does not affect weekday mornings but matters if a church hall is used on a Sunday. |

### 2.5 Insurance, safeguarding, first aid and medical

| Item | What to do | Status |
|---|---|---|
| Public liability insurance | Get a quote for a children's educational class of 8 children, 10 sessions at a hired venue. Ask whether it covers one tutor and one assistant, a participant's injury, and whether the cover requires registration with a regulator. Ask the venue whether it requires a certificate. Also ask whether accident cover for the children is available per-session. | Not done. Cost blank. |
| Employer or worker cover | If the assistant is an employee or contractor: check requirements. The tutor agreement is still a draft with employee vs contractor undecided. | Open |
| Limit of liability wording | `terms.html` has no liability clause yet (safer than a bad one). Death or personal injury caused by negligence cannot be excluded (UCTA s 2(1), UNVERIFIED section numbers in `legal/review.md` L1). Face-to-face terms need their own physical-safety wording, to be reviewed with the lawyer. | Open |
| Two adults present | Default: at least two adults in the room at all times (tutor plus assistant). Never one adult alone with one child. If the assistant is delayed, the lesson waits or a parent stays. Toilet trips: children go in pairs or with a named adult at the door; the owner decides the exact rule. | Decide |
| Tutor and assistant screening | The tutor agreement draft (3.10) leaves the criminal-records/background check open "owner and lawyer". No screening requirement was found in the research (`legal/review.md` P-section). Ask the lawyer and MOE. Do not claim background checks to parents unless they are done. At minimum: ID check, two references, a signed conduct and safeguarding acknowledgement, and a conversation about any past work with children. | Open, UNVERIFIED |
| Incident procedure | A one-page written procedure: record who, what, when, where and what was done; tell the parent the same day by phone for anything beyond a minor scrape; tell the owner immediately if she is not the tutor; keep an incident book at the venue; the tutor agreement 3.9 sets the concern-reporting rule (tell the owner the same day, write only facts, no investigation). A lost or hurt child and a safeguarding concern need separate steps. | To draft |
| First aid | A stocked first-aid kit; at least one adult with a current first-aid certificate (CPR/AED) would be ideal. Cost and course date blank. Know the venue's AED and the nearest clinic and emergency number (995 for ambulance, 999 for police; confirm). | To arrange |
| Allergy and medical form | Per child: allergies (food, latex, plasters), medication, asthma or epilepsy, anything staff should know, doctor's contact, consent to give first aid and to call an ambulance. Default: no food shared; snacks are the child's own and not swapped. | To draft |
| Emergency contacts | Two adults per child, with phone numbers and a note of who can collect. | To draft |
| Pickup and drop-off | Written authorisation per child naming who may collect; adults sign children in and out; a collection password for anyone not on the list; what happens if no one arrives (call, wait with two adults, never send a child home alone). Decide whether children aged 6-8 may ever leave unaccompanied: default no. | To draft |
| Behaviour and bullying | Short rules; the tutor agreement's conduct rules adapt. | Adapt |
| Toilets and changing | Venue's toilets only; adults do not enter a cubicle. Decide the plan for an accident. | Decide |

### 2.6 Data (PDPA), forms and consent

The PDPA applies from the first registration. Existing consent boxes cover online recording and delivery data; face-to-face needs separate wording. A lawyer should review the final forms (they are children's data and photos). Items:

- Registration consent for the pilot (contact, child's name, level, age, health information) with a stated purpose and retention. Health information is more sensitive: collect only what is needed, store it securely, and delete it after the pilot (default: 30 days, matching the delivery-address rule; the owner decides).
- Learning-record consent: the paper tutor sheet records observations of a child's strategies, explanations and persistence, and possibly marked-paper accuracy. Say what is written, who sees it (tutor only, then a parent summary), how long it is kept, and that nothing is shared with other families or published. This is the new thing and needs its own consent line. The owner's rules still apply: no ranking, no scores shown to children, no test, no marketing percentages.
- Photo consent: default no photos of children at all. If the owner wants any photos (room, work, marketing), ask separate, optional, written consent per use, with a way to withdraw. The tutor agreement says tutors make no photos or recordings of their own; keep that for the pilot.
- Recording: Meet recording does not apply. Do not record audio or video. Check the venue's CCTV and tell parents about it.
- Sign-in sheets and forms are personal data: keep them in a locked bag, not left in the room, and delete them on the date promised.
- Data Protection Officer contact: the existing launch item (replace the placeholder Gmail address) applies equally here.
- Parent consent form for participation, covering: the dates and venue; the rules; medical and first-aid consent; authorised collectors; the learning record; photos (default none); the refund rule; the complaint route.
- Do not collect more than needed. The existing sign-up flow collects delivery addresses for postage; the face-to-face pilot, if workbooks are handed out, can skip the address entirely.

### 2.7 Money, refunds and tax

| Item | Detail |
|---|---|
| Refund policy | The online beta fee is "not refundable" in the draft terms, but the legal review recommends exits if the organiser changes times by more than a set amount, removes a child, or cancels (`legal/review.md` T6). A face-to-face class has extra risk: a late MOE answer, a venue cancelling, a tutor illness, a child's illness. Default proposal for the pilot, for the owner to change: full refund of unheld lessons if the owner cancels or changes the dates or venue; full refund before a stated date (for example 14 days before the first day); after the first lesson, refund unheld lessons only if the child cannot continue for a medical reason or the owner removes the child; otherwise no refund. Write this on the consent form and have the lawyer review it. Nothing is finalised. |
| Price and payment | Blank. Beta fee is S$25 a lesson, S$250 for 10; face-to-face price not decided; prices are on hold. Payment route: manual PayNow is the beta default; Stripe is not yet live. |
| Taking money before the MOE answer | Don't. Collect an expression of interest and a waitlist only (section 3.7). |
| GST | Status unknown. The repository does not state whether Preciouslyours Pte Ltd is GST-registered; the owner must confirm with her accountant before quoting any fee, and the fee page should say whether prices include GST. |
| Insurance cost, venue deposit, first-aid course | Cost checklist in section 3.1. |
| Business licence | UNVERIFIED whether a hire of premises for classes needs any other licence. Ask the venue and MOE. |

### 2.8 Not applicable to this pilot

Google Meet recording and its settings, camera and mute rules, the Meet link and recording-link messages, the stuck-photo WhatsApp route for sending photos of paper (replaced by the tutor looking at paper in the room), and postal delivery (if workbooks are handed out).

---

## 3. Logistics

### 3.1 Cost checklist (amounts left blank on purpose)

| Line | Notes | Amount |
|---|---|---|
| Venue hire | Five mornings of 3.5 hours with set-up; deposit; cleaning fee | |
| Public liability insurance | Per event or per period | |
| Accident insurance for children (if any) | | |
| Printing: 8 workbooks plus spares (P1, 68 print pages, black and white, double-sided) | Quote from the printers asked in `quote_request.md`; add to the 9 Nov order if the timing fits | |
| Printing: tutor answer key, tutor notes sheet, observation sheets, timed item sheets | Office or library printing | |
| Printing: forms, sign-in sheets, name tags | | |
| Kit cutting supplies and bags/envelopes | Section 3.3 | |
| Stationery: pencils, erasers, rulers, crayons, counters, coins (play), tape, clipboards, whiteboard markers | Section 3.4 | |
| First-aid kit and course | | |
| Snacks/water (if the owner provides) | Default: none, children bring their own | |
| Assistant fee | Hours: 2 x 3.5 hours x 5 days plus set-up and a briefing session | |
| Tutor's own time | The owner; value is for the owner to decide | |
| Screening/background check fees | | |
| Travel and parking | | |
| Lawyer time for the consent forms and refund wording | Add to the existing lawyer brief | |
| Accountant (GST) | | |
| Contingency | | |
| Total cost against total expected income | Income depends on the fee and on how many of the 8 seats fill | |

### 3.2 Materials and printing list

Everything printed is black and white and double-sided (owner decision; `docs/printing/README_bw.md`). Use only files in `outputs/print/bw/`.

| Item | Source file | Quantity (default) |
|---|---|---|
| Level 1 student workbook with kit pages | `outputs/print/bw/Math_Inquirers_P1_Workbook_PRINT.pdf` (68 print pages, 34 sheets; kit/cut-out pages are source pages 56-61) | 8 plus 2 spare |
| Tutor answer key | Level 1 tutor guide (`hp/Math_Inquirers_P1_Tutor_Guide.pdf`); check the print-ready black-and-white option with the printer | 1 for the tutor, 1 for the assistant |
| Lesson decks | Decks are built for screen sharing | A screen or projector, or printed slide notes |
| Tutor observation sheet | `ops/out/tutor_observation_sheet.pdf` (built as a dry-run timing sheet; the learning-record sheet in section 4 is a new layout, not yet built) | 10 copies of the learning-record sheet, 5 timing sheets |
| Tutor notes sheet | `ops/out/tutor_notes_sheet.pdf` | 1 a lesson |
| Parent materials | Parent pack and weekly outputs exist for Level 1 (`readiness file`); they are written for the online program and may mention Meet; check before printing | 8 |
| Forms | Consent form, medical form, authorised-collector form, sign-in/out sheet, incident book, emergency contact list | 8 each plus spares |
| Timed fluency items (only if approved, section 4.4) | Age-light sheet, to be written | 8 plus spares per use |
| End-of-program report | `ops/out/end_of_program_report_L1.pdf` or `.docx` | 8 (filled in by hand or edited) |

Printing timeline: the beta printer order is Mon 9 Nov (launch checklist). A pilot workbook run can join that order if quantities are agreed, or be printed separately on a smaller run. The 9 Nov deadline also means the strategy-card and look-back routine edits should be done before the file goes to the printer; the owner decided to make them before about 9 Nov, and any change to PDFs already sent to printers needs a printer-status check.

Who cuts the kit pieces: default, the owner and the assistant cut and bag the kit pages for each child before day 1 (a child's six cut-out pages into one labelled envelope). Estimate the time by cutting one workbook's kit as a test and timing it, then multiply by 10. The children then spend no lesson time on scissors. The owner may prefer that the children cut the simple pieces in the room as a calm warm-up; check the budget before agreeing (lesson time is already full).

### 3.3 Kit and equipment per child

Check each lesson's materials line in the tutor guide for the final list; the following are likely from the lesson topics and are not confirmed: a pencil, an eraser, a ruler (Lesson 9), play coins or the kit coins (Lesson 6), counters or the kit cut-outs, crayons or colour pencils, a scrap of blank paper (private paper), and a small container for kit pieces. Mi appears only where already placed.

### 3.4 Room set-up and supplies

- Tables and chairs in a U or in two small clusters so every child can see the board and the tutor can walk round without stepping over bags; 8 children plus 2 adults.
- A board or a projector with a visible countdown timer; a bell or chime for transitions.
- A table at the door for sign-in, a labelled bag for each child, a place for shoes and bags.
- A cleared movement space for brain breaks.
- A first-aid kit, the incident book and the emergency contact list within reach but not on a child's table.
- Water, tissues, hand sanitiser, a bin, a wet cloth.
- Name tags with first names only.
- Posted rules (hands up, kind words, "pass is allowed", "I am still stuck" tick).
- Answer slides shown only at the checking moment, never on a screen children can read in advance.
- A clock visible to the tutor, because no lesson has been stopwatch-timed yet and this pilot is the first time anyone times the full sequence in a room.

### 3.5 Staffing

| Role | Default | Notes |
|---|---|---|
| Tutor | Jasmine | Her availability in the holiday weeks is unknown (day job, "P5M" Monday events, private lessons). |
| Assistant | One adult, aged 18 or older, screened and briefed (section 2.5) | Runs sign-in/out, toilet trips, first aid, kit bags, timing and 2-3 child observations per lesson (so the tutor is free to teach). A second pair of eyes is also the safeguarding rule. |
| Backup | One named relief adult | If the assistant is ill, the lesson waits or the day is postponed. |
| Tutor agreement | The draft in `docs/ops/tutor_agreement_draft.md` was written for online tutors (rooms, laptops, Meet). Face-to-face wording is not written. If the assistant is paid, the employee/contractor question applies. |

### 3.6 Run-of-day sheet for a two-lesson morning

| Time | Who | Task |
|---|---|---|
| 8:15 | Tutor, assistant | Arrive, open room, check exits and first-aid kit, set tables, test screen/board, put kit bags and workbooks at places |
| 8:45 | Assistant | Door: welcome, check the sign-in sheet, check the authorised-collector list |
| 8:50-9:00 | Assistant | Children settle, name tags, toilet visit; late arrivals noted |
| 9:00-9:04 | Tutor | Opening: greet, hands up rule, today's strategy card |
| 9:04-9:42 | Tutor | Warm-up, sneak-peek, explore, mini-lesson (follow the lesson's own budget in `hp/budget.json`) |
| about 9:42-9:46 | Tutor | Brain break (movement) |
| 9:46-10:16 | Tutor | Worksheet; tutor and assistant walk round; assistant records observation for today's 2-3 children |
| 10:16-10:30 | Tutor | Talk time, exit ticket, look-back (the common look-back routine), flex |
| 10:30-10:45 | Both | 15-minute break: toilets, water, movement; adults supervise in the room |
| 10:45-12:15 | Tutor | Lesson B in the same shape; assistant records the next 2-3 children |
| 12:15-12:30 | Assistant | Collection: call each child by name to the authorised adult, tick sign-out, note anything to tell a parent |
| 12:30-12:45 | Both | Reset room, lock forms, collect lost property, write incident notes, finish the tutor sheet |
| 12:15-1:15 | Owner | Lunch (default rule, if the owner is also teaching later in the day or online) |

The `hp/budget.json` timings for Lesson 1 are shown above only as an example; each lesson has its own split and the numbers have not been stopwatch-timed with children.

### 3.7 Registration and waitlist (existing flow)

- The existing interest and registration flow collects interest from parents on the website (`website/interest.js`, `website/interest_ui.py`, `website/data/interest_slots.json` with placeholder slot ids, and the sign-up page `mi_signup.html`; interest requests are held for 12 months). A face-to-face slot is not on the site and does not exist in `interest_slots.json`; adding one is a later task for the owner to approve and was not done here.
- Until MOE and the venue are settled, use the existing "Request another time" interest route or the business WhatsApp (+65 9880 5962) to collect only first name, contact, child age band and an expression of interest. Say plainly that it is an interest list for a pilot, that no seat is held, and that nothing is charged.
- Eight places; a waitlist after that. If the owner later learns the 10-person line applies, the waitlist must not be taught in the same venue.
- Confirm a seat only after: MOE answer (or owner's decision), venue booked, insurance in place, consent and medical forms returned, fee received or waived.
- Parents of the online Level 1 beta groups may also ask for a seat; keep the comparison clean (section 1.1).

### 3.8 Parent communication timeline (working back from the first day, Option 1: Mon 7 Dec; Options 2 and 3 are in `face_to_face_pilot_dates.md` section 4)

| When | Send | Via |
|---|---|---|
| Mon 26 Oct to 30 Oct | Nothing to parents. First, decide and send (or not) the MOE email, ask the venue | Owner |
| Mon 2 Nov | Interest list opens (only if the owner agrees): "a small face-to-face holiday pilot, dates and fee to be confirmed" | WhatsApp / interest form |
| Fri 13 Nov | Go/no-go decision. If go: offer places to the first eight; send the pilot information sheet, consent form, medical form, authorised-collector form, refund rule, fee and payment details | WhatsApp, email |
| Wed 25 Nov | Forms returned by this date; chase gaps | WhatsApp |
| Fri 27 Nov | Confirm the seat in writing once forms and payment are in (the existing message 1 needs a face-to-face version: venue, no Meet) | WhatsApp |
| Mon 30 Nov | Venue address, map, arrival and parking, what to bring, what to wear, no valuables | Message and PDF |
| Mon 30 Nov | Remind families that the posted-workbook route does not apply: workbooks are handed out at the room (if so decided) | Message |
| Fri 4 Dec | Reminder for Mon 7 Dec: time, place, collector rule, illness rule ("do not come if unwell") | WhatsApp |
| Mon 7 Dec | Day 1 | |
| After each day | A short message to each parent: arrival/collection confirmed and one specific kind observation (the existing message 9 style) | WhatsApp |
| After the last day (Mon 21 Dec; send Mon 28 Dec, not on the Christmas holiday) | End-of-program note using the template (`ops/out/end_of_program_report_L1`) and the learning-record observation lines (section 4.6) | Email/PDF |
| Wed 20 Jan 2027 (30 days after) | Delete sign-in sheets, medical forms and any remaining personal data per the promised date | Owner |

### 3.9 Risk list

| Risk | Likelihood / impact | Mitigation |
|---|---|---|
| MOE says registration is needed or a notification is required | Unknown / high | Ask first; cap at 8; fall back to Option D (March 2027) or a registration process; do not take fees before the reply |
| MOE does not reply in time | Medium / high | Set the go/no-go date at Fri 13 Nov; fall back to March 2027 |
| Venue unavailable, or its rules forbid paid children's classes | Medium / high | Ask 2-3 venues in the first week; book with a refundable deposit |
| Insurer will not cover, or is expensive | Medium / medium | Get quotes early; note blanks in the cost checklist |
| Owner overload: the beta launch runs to 24 Nov | High / high | Do not start parent work before the checklist items clear; keep the interest list light |
| Reserve groups R1-R3 are released for the online beta and collide with the pilot dates | Low-medium / medium | Choose the pilot dates before releasing reserves; record the hold in `beta_schedule.md` (not done here) |
| Assistant ill or screening incomplete | Medium / high | Named backup; the lesson waits rather than one adult alone |
| Six-year-olds tire in a 3-hour-15-minute morning | Medium / medium | Offer the one-lesson-a-day alternative; watch the day-1 stamina; shorten the second lesson's optional parts (flex and stretch slides) |
| Pace: lessons have not been stopwatch-timed | High / medium | Treat the pilot as the first timing; record actual minutes per part on the sheet |
| Child injury, allergy reaction, a lost or uncollected child | Low / high | Forms, two adults, collection password, incident book, first aid |
| Safeguarding concern | Low / high | Two adults, no one-to-one, concern rule (report to owner the same day) |
| Children's data breach (lost forms) | Low / medium | Locked bag, minimum data, delete on schedule |
| Fewer than eight enrol | Medium / low | Pilot still valuable at 4-5; set a minimum and say what happens below it |
| Christmas and travel clashes | Medium / medium | Ask families their travel dates before fixing dates |
| Misreading the rubric on paper (it was designed for screen-free notes) | Medium / low | That is what the pilot tests |

---

## 4. The learning-record pilot

### 4.1 What is tested

The rubric in `term_review.md` section 11 and `holiday_review.md` section 11 was written for a tutor watching on a screen with a private paper rule. Can a tutor and an assistant, with no software, record it reliably and cheaply in a live room, and does the record say something useful to parents without scores or rankings? Everything is observation, not assessment: no test, no marks shown to children, no ranking, tutor notes private.

### 4.2 The paper tutor sheet (one page per lesson)

Rows are children (up to 8); columns are the habits. In a lesson the assistant or the tutor watches only 2-3 named children, rotating so each child is watched about once every three to four lessons (10 lessons give each child 3 to 4 observations). Draw the rotation in advance:

| Lesson | Children observed (example for 8 children A-H) |
|---|---|
| 1, 2 | A, B, C (and D) |
| 3, 4 | D, E, F |
| 5, 6 | G, H, A |
| 7, 8 | B, C, D |
| 9, 10 | E, F, G, H (for the second look and the end-of-pilot picture) |

Each observation, in words (the optional three-word scale below is an owner decision because the Quest privacy checklist rules out tallies):

| Field | What the observer writes |
|---|---|
| Tool used | Which strategy the child used to start (picture, objects, list, table, pattern, working backwards, "in my head"), and whether they named it from the strategy card, or only used it |
| Explain-ladder rung | The highest rung seen (1 say what I did; 2 say why with objects or a picture; 3 test a claim; 4 give a reason that covers every case; 5 pose and defend), with the child's own words in a short quote. At Level 1 expect rungs 1-3 |
| Checked | Prompted, partly, or on their own; which kind of check (a second method, add back, estimate, an example) |
| Persisted | What the child did when stuck (waited, tried another tool, asked, used the "I am still stuck" tick, gave up), and roughly how long they stayed with it |
| Help level (optional) | with help, with a prompt, on their own |

The tutor prompts are the ones already written: "How did you start? Which tool did you use?", "What did you try first? What did you try next?", "Is that always true? Can you find one that breaks it?", "How could you check that?", "Tell me why, in one sentence", and "Show me, don't tell me" for a child who finds writing hard. Thirty seconds a child is the budget; the sheet is filled in after the break or at the end of the day so it does not interrupt teaching.

A single sheet design (children down the side, the five fields across, a space for one quote, and the lesson number and date at the top) can be made by the assistant on a later task once the owner approves this design. It does not exist yet.

### 4.3 Other paper evidence

- The child's own workbook is the main record: the look-back box, the "pass" and "I am still stuck" ticks, and the self-check against the answer slide.
- Do not take or keep photos of the children's pages; read them in the room and note what is seen, or ask parents to keep the workbook and bring it back for a look at the end.

### 4.4 Timed fluency items on paper (age-light; ONLY if the owner approves)

This is not in the existing rubric and is new: the owner has to decide whether a timed element belongs in a program whose design says no tests and no marks. If approved, keep it light and never public:
- Short, 2-3 minute, number-fact sheets (for example number bonds to 10 and 20 for Lesson 2, adding within 20), done on the child's own paper as a game, "beat your own last time", never compared with another child.
- Run twice only: in Lesson 1 and Lesson 10, so the change per child is the only comparison. The sheets are not marked in front of the child.
- The tutor records, privately, the number attempted and the number correct, and the child's reaction (calm, rushed, upset). Stop the activity for any child who is distressed.
- Item selection and wording would be written and verified by the assistant later; none exists yet.

### 4.5 Marked-paper accuracy

For each child, the owner or assistant marks the Lesson 1 and Lesson 10 timed sheet (if approved), plus, optionally, the "exit ticket" and a few chosen workbook items, after the lesson. Record right / not yet, separately from the process notes (as `holiday_review.md` proposes: score the process, record the answer separately). Keep the marked pages only until the end-of-pilot summary is written, then return them to the family. State in the parent consent that the child's paper may be read and marked.

### 4.6 What to compare with the online pilot

Same Level 1 holiday workbook, same strategy card and look-back routine, different delivery, different children. Compare, with all the limits below:

| Thing | Face-to-face (paper sheet) | Online (screen) |
|---|---|---|
| Timing | Actual minutes per part, per lesson, from a clock | The dry-run sheets and the beta lessons |
| Tool, rung, checked, persisted | Paper tutor sheet from 2-3 children a lesson | The online beta observation (tutor observation sheet; Form A / Form B if used) |
| Whether the tutor can record the four prompts without losing teaching time | Time cost, missing entries, which fields get skipped | Same |
| Parent report line quality | Could the observation lines in `term_review.md` 11.3 be written for each child? | Same |
| Stamina and pace for 6-year-olds | A two-lesson morning against a single lesson | Online 90-minute lesson with a 5-minute break |
| Paper practicalities | Pencil work, cutting, kit use, whether hands-up works with 8 children | Not applicable |
| Sources of confusion | Where the sheet confused the observer, and what to change | |

Limits (stated in `holiday_review.md` and `term_review.md`): at most 8 children, no control group, the same tutor teaching and judging, one short window, children may differ between groups. The comparison shows how the instrument works in a room, not that face-to-face teaching is better or worse. Report no percentages; "often, sometimes, starting to" is enough. Do not publish or compare groups. Make no outcome claims about marks, MOE, GEP or SASMO.

### 4.7 Success criteria for the tutor sheet (suggested, owner to set)

- The assistant can record 2-3 children per lesson without missing teaching.
- At least a few quotes per child by the end.
- The look-back and parent line can be written from the notes alone.
- The owner can say what she would change in the sheet.

---

## 5. Dated timeline from today (Fri 23 Oct 2026) to the last day (Option 1: Mon 21 Dec; Options 2 and 3 in `face_to_face_pilot_dates.md` section 4)

Existing beta dates are in `docs/ops/launch_checklist.md`. The owner's workload to 24 Nov is already high, so this timeline puts only decisions and questions in October, and only parent-facing work after the beta launches.

| Date | Step | Decision or owner action needed |
|---|---|---|
| Fri 23 Oct | This plan written | Read it; answer the questions in section 6 |
| Mon 26 Oct | Decide whether to contact MOE first | Owner chooses: send the MOE email (section 2.3) herself, add it to the lawyer brief, or skip the pilot. Read the GoBusiness guide "Notification for Private Tuition Enrichment" |
| By Fri 30 Oct | Check dates | Owner confirms the December dates (Option 1 default: Mon/Wed afternoons, 7-21 Dec) against her calendars and day job; confirm MOE school holiday dates (already on the launch checklist for Fri 30 Oct); decide Option 1, 2, 3 or D |
| By Fri 30 Oct | Venue enquiries | Ask 2-3 venues the questions in section 2.4; book nothing without the rules in writing |
| By Fri 30 Oct | Assistant | Name a candidate assistant and a backup |
| Mon 2 Nov | Insurance quotes | Ask an insurer or broker; owner decides whether cover is affordable |
| Mon 2 Nov | Interest list (optional) | Owner approves a short message; no fees and no seats |
| Fri 6 Nov | Lawyer comments back (existing) | Add pilot consent forms and refund wording to the lawyer's scope |
| Mon 9 Nov (public holiday: Fri 6 or Tue 10 Nov if the printer is closed) | Printer order (existing) | Add 10 Level 1 workbooks to the order if the pilot is still on, or ask for a small separate run |
| Wed 11 Nov | Venue decision | Book the venue with a refundable deposit (or choose Option D) |
| Fri 13 Nov | Go/no-go | Owner decides with the MOE reply (if any), venue, insurance, assistant and screening |
| Fri 13 Nov | Forms to parents | Send information sheet, consent, medical, collector forms, refund rule, fee (if go) |
| Mon 16 Nov to Fri 20 Nov | Cut and bag kits (can begin once workbooks arrive) | Owner and assistant |
| Tue 24 Nov | Online beta begins | Pilot waits; the owner is teaching online |
| Wed 25 Nov | Forms returned by this date | Chase gaps |
| Fri 27 Nov | Confirm seats | Only for complete forms and payment |
| Sat 28 to Sun 29 Nov | Cut and bag kits | Owner and assistant (workbooks arrive by about Fri 20 Nov) |
| Mon 30 Nov | Venue and arrival information to parents; assistant briefing and room walk-through; incident-book and first-aid check | |
| Fri 4 Dec | Reminder to parents; print forms and sheets; test the room's screen | |
| Mon 7 Dec | Day 1: Lessons 1 and 2 | |
| Wed 9 Dec | Day 2: Lessons 3 and 4; first end-of-day review of the sheet | |
| Mon 14 Dec | Day 3: Lessons 5 and 6 | |
| Wed 16 Dec | Day 4: Lessons 7 and 8 | |
| Mon 21 Dec | Day 5: Lessons 9 and 10; final timed items if approved | |
| Mon 28 Dec | End-of-program notes to parents | |
| By Fri 8 Jan 2027 | Debrief: compare with the online pilot (section 4.6); decide whether to repeat | |
| By Wed 20 Jan 2027 (30 days) | Delete personal data per the promised schedule | |

Note: Mon 9 Nov is a public holiday (Deepavali observed); confirm with the printer whether the order can be placed that day or place it on Fri 6 Nov or Tue 10 Nov.

If Option D (March 2027) is chosen, shift every date later by the same lead time; the first parent-facing step moves to about January 2027, which also lets MOE answer.

---

## 6. What could not be determined; what is needed from the owner

1. Dates: which option (1, 2, 3 or D) and whether she is available on those days (day job, private lessons, the "P5M" events, any December travel). MOE 2026 school holidays and the March 2027 holidays still need verifying on moe.gov.sg.
2. Whether the owner wants MOE contacted first, and whether she, a lawyer, or the assistant sends the question. Her answer decides whether the pilot can go ahead in December.
3. Venue: which, and whether she has contacts. Whether the venue can take a paid children's class and what capacity and fire-safety rules apply.
4. Group size and level: confirm Level 1, one group of at most 8, and the minimum to run.
5. Tutor and assistant availability and screening: who, paid or unpaid, employee or contractor, what checks (the lawyer item), a first-aid certificate.
6. Budget and fee: the amount (or free), the refund rule, payment route, and GST status.
7. Whether workbooks are handed out at the room or posted, and who cuts the kit pieces.
8. Whether she approves the timed fluency items (section 4.4), the optional three-word scale, and the new tutor sheet design.
9. Whether parents may sit in on any lesson, and whether any photos at all are wanted.
10. Insurance: what the insurer will cover, and whether the venue demands a certificate.
11. Whether the online-only operation needs any notification (UNVERIFIED) and whether the Education Act section 21 wording and threshold are as stated here (UNVERIFIED: the section was not opened).
12. Whether the two pilots should use different children (default) or the same.
13. Whether to add a face-to-face option to the website and sign-up flow, or keep it WhatsApp-only. The site, the portal and the materials have not been touched.

Nothing in this plan has been sent, booked, printed or published.
