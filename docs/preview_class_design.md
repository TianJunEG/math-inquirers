# Free preview class: design and prototypes

Written 24 Oct 2026 on branch `claude/great-fermi-1hv4vc`. **Design and prototypes only.** Nothing is deployed, applied to Supabase, sent, published or announced; `website/dist` is untouched; no Stripe, Cloudflare or Google account was touched. I am not a lawyer: every legal point is a question for the lawyer (new question 13 in `docs/owner_kit/lawyer_email_draft.md`), not advice.

Owner idea (`docs/terms/owner_decisions.md`, "FREE PREVIEW CLASS"): a free class of about 1 hour, open to everyone, lecture style (slides and chat, no workbooks), possibly built from the website daily teasers, funnelling families into the paid classes; weekly, with similar content each time so nobody needs to come twice; **new registrations only: anyone who attended in the past 6 months cannot attend again.**

## 0. Short answer, and what is in the repo

**Yes, we can do it.** The class itself is easy. The "not again within 6 months" rule can be enforced **well enough to stop honest repeat visits and casual repeats, but not a determined family** (section 1.3). That is acceptable because the lesson is the same every week (a repeat visitor gains nothing, and costs us one seat and one hour), so the rule is about protecting the funnel and the room, not guarding a secret. The one thing that changes the plan: **Google Business Standard does not give an attendance report** (section 6.1, checked 24 Oct 2026), so attendance comes from the host admitting people by name, which is also the safeguarding control.

| What | Where | State |
|---|---|---|
| This design | `docs/preview_class_design.md` | draft |
| Draft tables and functions (register, eligibility, cancel, attendance, close, purge, funnel) | `portal/supabase/preview_class.sql` | **NOT applied**; runs twice cleanly |
| Local test | `portal/supabase/test/preview_test.sql`, run with `bash portal/supabase/test/run_preview_test.sh` | passes on throwaway local PostgreSQL 16 with the repo's Supabase stand-in (`ALL OK`); not run on real Supabase; not added to `run_sql_test.sh` |
| Tutor one-pager | `docs/owner_kit/preview_class_sop.md` | draft |
| Lawyer question 13 | `docs/owner_kit/lawyer_email_draft.md` | added; 1 to 12 unchanged |
| Prototype deck, Level 3 band, 60 minutes, 16 slides | `split/preview_l3/` (generator `gen_preview_l3.py`, `project/deck.json`, `project/slides/*.html`) | **DRAFT, NOT PUBLISHED**; `levels/restyle.py` run twice (16 files, then 0); Mi rule checked |
| One-line change to a shared tool | `levels/restyle.py` `level_of()` also reads `preview_lN` so the deck gets the Level 3 green, not Level 1 teal | nothing else changes for other decks |

---

## 1. Feasibility, and the honest limits of the 6-month rule

### 1.1 What identifies a "new" attendee

A person on the internet is not a fixed thing. We never see a face, a passport or a Google account (families join through a link, not signed in). So "the same child" can only be guessed from what a parent types. The draft uses four things, each **normalised** first, then turned into a **keyed hash**:

| Identifier | Normalisation | Why it helps | Weakness |
|---|---|---|---|
| Parent email | lower case; drop `+tag`; for gmail and googlemail drop dots and map `googlemail.com` to `gmail.com` | most families use one email | free to make a new one |
| Parent phone (optional on the form, asked for WhatsApp) | digits only; a Singapore number written `+65 9123 4567` or `6591234567` becomes `91234567` | harder to change than an email; often the same family number | can be a different parent's number; optional, so can be left empty |
| Child first name | first word only, letters only, lower case ("Mei Ling", "mei-ling!" and "MEI" all give `mei`) | catches spelling and case changes | a nickname change gets through |
| Child birth **year** (not date, not age) | the year, 2008 to 2022 | stable (age changes, a year does not); low value for identifying a person | a lie or a typo |

**Hashed**: each value is run through HMAC-SHA256 with a secret key (the "pepper") kept in a table no API role can read. The long-term record of who attended holds **only the hashes** plus the birth year. If someone obtained only that table they could not read emails or names, and could not rebuild them without the key. This is **not** anonymisation: whoever holds the database and the key can test a guess, so the lawyer is asked (question 13a) to treat it as personal data. The key is generated at install (`preview_config`); on real Supabase move it to Vault. Losing or changing the key simply makes everyone "new" again.

**Match rules** (`_pv_eligibility()`, same function for the form and for the admin check):

1. **Blocked**: the **child key** (first name + birth year) matches someone who attended within 6 months **and** the **parent email or phone** matches too.
2. **A person decides** (`pending_review`, shown to the parent as "we will confirm by email"): same first name, birth year **within one year**, and same email or phone as a recent attendee (typo, or age typed as a year).
3. **A person decides**: the same child key registered **and never came** twice or more in the window (see 1.2).
4. **Allowed**: everything else. In particular a **sibling** (same parent contact, different first name) is a new child, and a stranger with the same first name and birth year but different contacts is allowed (common names exist; refusing them would turn away real new families).

A refused parent sees one sentence whatever matched (section 1.5), so nobody can probe "did this family attend?" by trying variations; attempts are rate-limited (8 a day per parent email, including refused attempts, stored as hashes for 2 days).

### 1.2 What counts as "attended"; no-shows

* **Registered is not attended.** Registration never writes to the exclusion record. This also means nobody can use up someone else's free class by registering their email.
* **Attended = the host admitted the child's join name and the child stayed at least 15 minutes** (a quarter of the class). The check is from the host's check-in sheet (section 6.1), not from a Google report, because Business Standard has none. A parent who joined with no child does not count; someone who arrived after the door closed (10 minutes) is a no-show.
* **No-show policy (recommended): a no-show does not use up the free class, and may try again.** Two no-shows are fine; a third registration for the same child within 6 months is held for a person ("repeat no-show"), usually to ask if something is wrong with the time. A child who joined for under 15 minutes (a technical failure, a wrong room) also keeps the free class.
* The 6 months run from the **day attended**, not the registration day. The exclusion record is kept 7 months (6 plus 1 month of grace for the weekly purge, which is also why a late purge never gives an extra visit: the window is checked on the date, not on whether the row still exists).

### 1.3 How easily it is got round

| Way round | Stopped? | Notes |
|---|---|---|
| Same family, same details, tries again | **Yes** | blocked at the form |
| Different case, dots or `+tag` in a gmail address, `+65`, spaces in the phone, "Mei Ling" for "Mei" | **Yes** | normalised |
| New email, **same phone** | **Yes** | child key + phone |
| New email **and** new phone, same child name and birth year | **No** | cannot be detected: nothing links the two registrations. This is the cheap circumvention. |
| The other parent registers (their own email and phone) | **No** | same as above |
| A nickname, a different name, a wrong birth year (more than 1 off) | **No** | fuzzy matching on names without storing names is weak, by design |
| A sibling attends under the first child's code | **No** | we cannot see who is behind the name tag |
| A friend of an attendee registers their own child | allowed (correct) | a new child |

**What we can reasonably do:** (1) the normalising and the rules above; (2) a **sensible person-in-the-loop** for near matches; (3) the **tutor sees a child's first name** in the room and may recognise a repeat (a soft check, never accuse); (4) keep it light: no ID, no OTP by SMS, no face checks, no photo, no tracking cookies, no device fingerprinting (all disproportionate for a free maths class, and they would collect more data than the class is worth); (5) **measure the leak rather than chase it**: a repeat visitor sees the same lesson with a different warm-up; if two weeks in the tutor notices 3 repeat names, we learn how big the leak is. The risk of the opposite error (turning away a genuinely new family) is small, because a block needs a first name, a birth year **and** a matching parent contact.

**Honest summary for the owner:** "once per child per 6 months" is a **policy we apply to honest families and say clearly on the page**, backed by a record that catches the simple repeats. It is not a lock. Do not promise it as a guarantee anywhere, and do not tell parents how it works in detail.

### 1.4 What the family is told they agree to

A **required** line (never pre-ticked; wording in 2.3): "I understand this free class is for children who have not attended a Math Inquirers free class in the last 6 months. To apply this, Math Inquirers keeps a coded record (not my name or email in readable form) for 7 months after my child attends." Whether a required tick for a free service is a valid consent is a question for the lawyer (13a), so I list the alternative bases there.

### 1.5 Being turned away: policy and tone

* **On the form** (same wording whether the cause is a match or a full-and-blocked case; no reason given): "Thank you for your interest. We are not able to offer a place in this free class for your family right now. The free class is for children who have not joined one in the last 6 months. If you would like, we can help you with the next step: a short chat with us, or our enrolment page. [Chat with us on WhatsApp] [See the classes]"
* **If it is a person deciding** (pending): "Thank you. We will confirm your place by email within one working day."
* **If a parent writes, upset:** never say what matched or "our system says you came". "Thank you for telling us. I am sorry for the confusion. The free class is once per child in six months, so I cannot add your child this time. Here is something better for you: [a 15 minute chat with a tutor about which level suits your child] or [the free Placement Check]". Offer a warm next step and move on.
* **A mistake (a genuinely new child blocked):** the owner runs `admin_preview_check()` with the details; if wrong, add by hand with `admin_preview_decide(...,'confirm')`. Apologise and move on; never argue.
* **No lecture, no suspicion, no mention of other families, no mention of "circumvention".** A family that tried a second time is more likely forgetful than devious; the next step offered is the same one we want them to take.

---

## 2. Registration flow and data

### 2.1 The flow

1. Owner (or an admin form) creates the weekly session (`admin_preview_create_session`): date, **band A, B or C** (section 3.1), capacity 40 confirmed, 30 live, warm-up reference. Sessions are published about 3 weeks ahead; registration opens when listed, closes 1 hour before the start.
2. The website "Free class" page lists open sessions from `preview_open_sessions()` (date, band, full or not; no counts). The parent picks the session that matches the child's **school year** (P1 to P2 band A, P3 to P4 band B, P5 to P6 band C; a wrong band gets a friendly "that class is for P4 to P5; the next one for your child is on ...").
3. The form (all fields below) calls `register_preview()` (anonymous, no account; a honeypot field; no cookies; no tracking). One of: **registered** (a 4-character join code is shown and emailed), **waitlisted**, **pending** (a person decides), **not available**, **already registered**, **closed**, **wrong band**.
4. Confirmation email (immediately), reminder 24 hours before, reminder 1 hour before (wording 2.4). The email carries the Meet link and the **join name** the family must use ("Mei 7K3Q": child's first name and the code). The Meet link is **not** shown on the web page and is never public.
5. The parent can cancel with the code and email (`cancel_preview`), which frees a seat; the admin promotes the waitlist (`admin_preview_promote_waitlist`) and mails the promoted parents.
6. After the class: the co-host gives the owner the admitted codes and minutes; `admin_preview_mark_attendance` writes the hash-only exclusion rows; `admin_preview_close_session` marks no-shows and stores counts.
7. Thank-you email with the take-home link (3.8). Follow-up only to parents who ticked the marketing box, or who asked.

**Reuse of existing tables.** `interest_requests` is an anonymous planning list (parent first name, age band, no child name); `trial_requests` needs a signed-in portal parent and a child profile. Neither fits an anonymous family who has not made an account, so the draft adds `preview_registrations` (contact in clear, 30 days) and `preview_attended` (hashes only, 7 months). **The bridge to the funnel** is the manual `followup_status` column (none, contacted, trial_booked, trial_attended, enrolled, declined) and the "How did you hear about us?" option "free preview class" on the trial and enrolment forms; a one-line change to `trial_requests.source` (add `'preview'` to the check in `practice_submissions.sql`) is recommended when both are built. Not edited here.

### 2.2 Fields (data minimisation)

Parent first name; parent email (required); parent mobile (optional but recommended, used only for the WhatsApp reminder); child **first name or nickname**; child **birth year**; child **school year** (P1 to P6); chosen session. **Not collected:** surname, school, address, birth date, NRIC, photo, child email, a child account. Tick boxes (never pre-ticked):

| Box | Required | Stored as |
|---|---|---|
| "A parent or guardian will be with my child for the whole class." | yes | `parent_present` |
| Contact: "Math Inquirers may email me, and WhatsApp me if I gave a number, about this class (link, reminders, a thank-you with the practice page)." | yes | `consent_contact` |
| Class rules: "I have read the free class rules (no recording or screenshots, cameras and microphones off, first names only)." | yes | `consent_terms` |
| Coded record: the text in 1.4 | yes | `consent_exclusion` |
| **Marketing (optional):** "I would like to hear from Math Inquirers about trial classes and new classes, by email or WhatsApp. I can say STOP at any time." | no | `consent_marketing`; with this the contact is kept 6 months, otherwise 30 days |

`consent_version` records the wording version; the page and the privacy notice must change together (`MI.VERSIONS` pattern in the portal).

### 2.3 Draft wording (for the lawyer, not live)

* Page note (small print under the form): "This free class is for families who have not been to one of our free classes in the last 6 months. We keep a coded record for 7 months after attendance to apply this, and your contact details for 30 days after the class (6 months if you tick the last box). Nothing is recorded, and we do not use cookies or advertising trackers."
* Required "coded record" tick: see 1.4. Optional marketing tick: see 2.2. The privacy notice needs a new row (purpose: run the free class and apply the once-per-6-months rule; data: as 2.2; provider: Supabase and Google Meet may store data outside Singapore; retention: 30 days, 6 months, 7 months; contact: the data protection contact, still a placeholder).

### 2.4 Message drafts (nothing is sent; owner or a later tool sends)

Rules (PDPA and Do Not Call, to be confirmed by the lawyer, question 13d): confirmations and reminders are **logistics about a class the parent asked for**, so they carry no promotion; the email is the default channel; a WhatsApp reminder only when the parent gave a number and ticked the contact line; every WhatsApp message names Math Inquirers and says "Reply STOP and we will not message you again"; **no promotional text** is added to a reminder; after the class, anything beyond the thank-you and the practice link goes only to parents who ticked the marketing box (or asked).

1. **Confirmation (email), at registration:** "Hello [parent first name], thank you for registering [child first name] for our free class: *The Mystery Number*, [day date], [time] to [time+1h] (Singapore time). Your join name is **[child first name] [code]**. Please use exactly that name when you join, so we can let you in. Join here: [Meet link, sent only by email]. A parent or guardian must sit with your child. Children answer by typing in the chat; cameras and microphones stay off. Nothing is recorded. Need to cancel? Reply to this email with your code. This free class is once for each child every 6 months. Math Inquirers (Preciouslyours Pte Ltd)."
2. **Waitlist (email):** "You are on the waiting list for [date]. If a place opens we will email you. You are welcome to try the free practice page meanwhile: [link]."
3. **24-hour reminder (email, and WhatsApp if allowed):** "Reminder: [child first name]'s free class is tomorrow at [time]. Join name: [child first name] [code]. We open the room 10 minutes early and close it 10 minutes after the start. Reply STOP to stop messages."
4. **1-hour reminder (WhatsApp, if allowed, else email):** "[child first name]'s free class starts in 1 hour. Join with the name [child first name] [code]: [link]. A grown-up should sit with your child. Reply STOP to stop messages."
5. **Held for review (email):** "Thank you for registering. We will confirm your place within one working day." (No reason given.)
6. **Thank-you (email, after class, to every attendee; no promotion beyond the link):** "Thank you for joining *The Mystery Number*. Here is the free practice page for [child first name]: [link]. It has two puzzles with answers and worked solutions, needs no login and saves nothing. If you would like to ask us anything, just reply. Math Inquirers."
7. **Follow-up (email or WhatsApp, only for marketing-ticked parents or if the parent asked):** "If you would like to see how a full class works, you can ask for a free trial class here: [link] (no obligation). Reply STOP to stop messages."

### 2.5 Eligibility function, attendance, enforcement

* `portal/supabase/preview_class.sql`: `register_preview()` (validation, honeypot, 300 an hour sitewide, 8 attempts a day per email, `_pv_eligibility()`, capacity and waitlist, join code), `preview_open_sessions()`, `cancel_preview()`, and admin-only `admin_preview_create_session`, `admin_preview_list` (check-in sheet and reminder list), `admin_preview_decide`, `admin_preview_promote_waitlist`, `admin_preview_mark_attendance(session, codes[], minutes[], min 15)`, `admin_preview_close_session`, `admin_preview_set_followup`, `admin_preview_check` (the owner answers "can this family come?"), `admin_preview_exclusion_count`, `admin_preview_funnel`, `admin_preview_delete_person` (PDPA request), `admin_purge_preview`. Anonymous roles can read no table (tested); every error is a fixed word; no input is echoed; hashes are 64-character hex and contain no plain identifiers (tested).
* **Attendance after class:** primary route is the **co-host's check-in sheet** (codes admitted, minutes present). If the owner ever has a Meet attendance CSV (needs Business Plus, 6.1), the join names in the CSV contain the codes, so the same function takes the pairs (code, minutes) from it; no email matching is needed. Tutors mark; nobody imports names.
* **The 6-month rule enforcement query** (the admin sees the answer, not the data): `select public.admin_preview_check('parent@example.com','91234567','Mei',2016);` returns `ok`, `blocked`, `review_similar` or `review_no_show`. The count of live exclusion rows is `admin_preview_exclusion_count()`.
* **Retention:** contact details in `preview_registrations` are deleted at `expires_at` = session start + 30 days (6 months if the marketing tick); `preview_attended` rows at attendance + **7 months** (6 months of exclusion, plus a month so a weekly or late purge never allows an early repeat; the window itself is checked by date); attempt log 2 days; counts per session (`stats`: registered, attended, no-show, waitlisted, declined, cancelled) are kept for measurement without personal data. `admin_purge_preview()` (button or `pg_cron`, example in the file). A parent may ask for deletion at any time (`admin_preview_delete_person`), which also lets them attend again; lawyer question 13e.

---

## 3. The class itself

### 3.1 One lesson per band: 3 bands, not 6 (recommended)

| Band | School years | Levels it feeds | Warm-up taken from teaser level |
|---|---|---|---|
| A | Primary 1 to 2 (ages 6 to 8) | 1 and 2 | Level 1 |
| B | Primary 3 to 4 (ages 8 to 10) | 3 and 4 | Level 3 |
| C | Primary 5 to 6 (ages 10 to 13) | 5 and 6 | Level 5 |

Why 3: (a) **audience size**: a free class draws about 15 to 30 live families per week in total (an assumption, see 6.3); six bands would leave about 3 to 5 children each, which feels empty and gives no chat energy, and two bands for the same week doubles the tutor hours; (b) **build and upkeep**: 3 decks, not 6, each needing an independent check; (c) the "notice, test, explain" puzzle lesson already serves a three-year age range with **Start here, Think harder, Go further** moments inside one lesson, so pairing two adjacent levels works; (d) the bands match the three-year bands the website already uses. Cost: a P3 and a P4 child sit together; the "Go further" slide serves the stronger one, and the free **Placement Check** (already in the funnel) is the proper tool for the level choice. A sibling pair in two bands registers for the older child's band. If demand later shows a band is too mixed, split to 6 and reuse the band decks. **Schedule recommendation:** one weekly slot, rotating A, B, C (each band every third week, 3 weeks of future sessions always visible). Add a second weekly slot when a band regularly fills. The weekday and time are the owner's choice (suggested: Saturday 10:00 to 11:00 Singapore time, outside the paid classes in `website/data/beta_schedule.json`; the paid beta groups run daytime and early evening weekdays, Friday and Sunday evenings, and Saturday 18:45, so Saturday 10:00 is free).

### 3.2 "Same lesson each week, fresh to staff"

* **Fixed content per band** (the 16 slides, never edited between weeks): repeat visitors learn nothing new, which is the point; it also means the lesson can be rehearsed to a polished 60 minutes.
* **Rotating warm-up (slide 3 only, 5 minutes):** the tutor drops in that **session date's** daily teaser for the band's warm-up level from `website/teasers/batches/mNN/bank.json` (puzzle, hint, worked answer; already verified by `verify_bank.py`). The slide shows the puzzle, a type-your-answer prompt and a click-to-reveal answer. Staff meet a new puzzle each week; families who read the website see the same puzzle that day, which links the class to the site. Rotation depends on a released month (Nov and Dec 2026 are released; Jan to Oct not yet written, `website/teasers/README.md`), so until then reuse a released month. A tiny script that writes slide 3 from the bank (about 2 hours) is on the build list.
* **No-new-lesson safety:** if the owner ever wants a second lesson per band for those who are curious, that needs a different rule (section 7, decision 6).

### 3.3 Lesson plan (Level 3 prototype; the other bands use the same shape)

Total **60 minutes**. Same pace as the 90-minute lessons: short bursts, a break, typed answers.

| Min | Slide | What happens | Chat or poll |
|---|---|---|---|
| 0 to 2 | Title (Mi hello) | Welcome by first name; "no workbooks, no recording"; cameras off | none |
| 2 to 4 | How we answer | House rules; practise typing a nickname and an emoji | type nickname + 👍 |
| 4 to 9 | **Warm-up of the week** (rotates) | daily teaser, 90 s of silent thinking, reveal | typed answer |
| 9 to 14 | Notice it: "I am thinking of a number" | mystery number puzzle, guesses | typed guesses; emoji vote (guess and check or something cleverer) |
| 14 to 19 | Test it: guess and check, or undo? | table of guesses, then the undo way | type "what undoes + 6?" |
| 19 to 23 | Key idea: undo in reverse order | undo machine diagram | none (say together) |
| 23 to 28 | Your turn 1 | one-step-pair puzzle | typed number; reveal |
| 28 to 31 | Brain break (Mi stretch) | stand, stretch, water | none |
| 31 to 36 | Spot the mistake | wrong working; three options | emoji vote A, B or C; type a reason |
| 36 to 42 | Your turn 2 | order is different (add then multiply) | typed number |
| 42 to 48 | Go further | three-step mystery; "can the answer ever be 39?" | typed number and why |
| 48 to 50 | What we did today | notice, test, explain | one-word chat |
| 50 to 53 | If you would like more (offer 1) | what a class is like | none |
| 53 to 55 | Your next step (offer 2) | grown-ups only; no pressure | questions in chat |
| 55 to 58 | Take-home | free practice page link pasted in chat | type one thing to tell someone |
| 58 to 60 | Thank you (Mi goodbye) | close | none |

Answers (checked by a script and by hand): 8, 7, 9, 5, 6; warm-up 87 minutes; "39 is impossible": 39 − 6 = 33 and 33 ÷ 4 is not a whole number. All puzzles are original and kept out of the teaser bank.

### 3.4 Chat-interaction script (what the tutor says, in order)

1. "In the chat box, type your **first name or a nickname** and a 👍. Please never type a surname, a school or a phone number. If you type one, I will delete the message, and that is okay."
2. "I will ask a question. **Do not answer yet.** Think. I will say go." (a silent 60 to 90 seconds)
3. "Go. Type your answer. I will read some out by first name. I will not say who was right or wrong."
4. Reading answers: "Sam says 8. Mei says 10. Let us test both." Always test, never judge.
5. Polls with emoji: "👍 means A, ❤️ means B, 😮 means C." Count aloud. (We do **not** rely on Meet's poll feature: its availability on Business Standard is not verified, 6.1.)
6. If the chat floods: "Let us slow down. Type your answer once, then wait for me."
7. If a parent types: "Thank you, grown-ups. Please let your child type their own answer if they can."
8. Never: ask a child to speak or turn on a camera; ask a child's school; name a child who was wrong; promise a result.

### 3.5 Slides spec (follows the repo's deck conventions; `split/preview_l3/` is the worked example)

* Structure: `project/deck.json` + one `project/slides/<key>-<name>.html` per slide, ids `pv3-title`, `-rules`, `-warm`, `-notice`, `-test`, `-key`, `-try1`, `-break`, `-spot`, `-try2`, `-challenge`, `-recap`, `-class`, `-offer`, `-takehome`, `-end`; 1920 x 1080, Fredoka for headings and Nunito Sans for text, `data-theme="modern2"` after `levels/restyle.py` (light slides on `#F3F6FB`, navy or accent title and break slides, a time pill "n–m MIN" top right, accent bar), level accent from the folder name (Level 3 green).
* **One idea per slide.** At most one question, one reveal; large type (32 to 46 px body); reveals use `data-build-in="pop"`; emoji used only for votes; no workbook page numbers anywhere.
* **Speaker notes** in `<aside>`: minute range, what to say, what to expect in chat, the answer, and "DRAFT, NOT PUBLISHED" on the draft.
* **Mi the dolphin on title, break and last slide only**, never on a question slide (`levels/mi_deco.py` pose rule: `hello_wave`, `stretch`, `goodbye_wave`). The last slide is a thank-you, not a question. Mi's real image ids exist per published deck (`mascot/blob_ids.json`); the prototype carries `/_blob/PENDING-<pose>` placeholders because nothing was uploaded. `levels/mi_deco.py` does not touch this deck (its folder name does not match its key pattern), so the placeholders survive restyle; when the deck is built for real, extend `key_level()` (and add the blob ids at the republish step) so Mi is applied like other decks.
* No calculator, no scores, no timers on screen, no "test" or "exam" wording, no claim about schools or exams, no price on the slides.
* Every deck states "DRAFT, NOT PUBLISHED" in a footer until the owner approves; remove with the generator's `FOOT` text.

### 3.6 How teasers feed the interactive moments

1. **Warm-up of the week** is the date's daily teaser (puzzle, hint after a wrong try, worked explanation).
2. **Spot the mistake** can use a teaser's recorded wrong answers (each teaser in `bank.json` has a `wrong` list of plausible slips, for example 88 or 86 for 87): "Which of these answers is most likely a slip, and what slip?" This makes the poll slide feel new in the band-A and band-C decks too.
3. **The thank-you email and the take-home page** use the same teaser family, so the class, the website and the practice page feel like one thing.
4. Rotating only the warm-up keeps the "same lesson" promise (3.2).

### 3.7 The 5-minute offer segment (minutes 50 to 55): soft, honest, no pressure

* **What it says (parents, not children):** a plain description of a Math Inquirers class (live, up to 8 children, 90 minutes, workbook posted to the home, the same four steps); that the free **Placement Check** exists; that a trial class can be requested; that questions are welcome in chat or by reply; "no obligation; if this was not for you, that is fine."
* **What it never does:** countdowns, "last places", discounts that end tonight, comparison with other children, remarks about a child's level in front of others, claims about exams or schools or results, prices on slides (prices are on hold; the website carries them when decided), pressure on a child.
* **What is offered must exist.** Today the repo has: the free 30-minute Placement Check, the "Request another time" form, and a trial request path in the portal draft. **What a "trial class" is (free? one lesson? paid?) is not decided**; the offer slide says "ask us" until the owner decides (section 7, decision 3).

### 3.8 Take-home: a free sample practice page

A one-page "Mystery Number" practice sheet per band: two puzzles, answers and worked solutions, in the existing online-practice runner style (`practice/public`): **open, no login, nothing saved, no timer or score** (the "open sample pages that store nothing" in D2 of `docs/online_versions_plan.md`). **It does not exist yet** (section 6 build list). Until then the take-home slide says "[link to be added]". The link has no per-family token, so we cannot tell who opened it (no tracking, by design).

### 3.9 What was checked for the prototype deck

16 slide files plus `deck.json`; contiguous minute pills 0 to 60; the five puzzle answers and the warm-up by script; every slide rendered at 1920 x 1080 in Chromium (with the deck's reset) and the flow content stops above the footer; Mi only on `pv3-title`, `pv3-break` and `pv3-end`; no calculator mention; `python3 levels/restyle.py split/preview_l3` run twice: 16 files changed, then 0. Not done: an independent second checker, a timed rehearsal with a real tutor (the 60-minute plan is untested: in particular the two typed-answer pauses and the offer segment), Mi artwork upload.

---

## 4. Safeguarding an open class with unknown children

### 4.1 Decisions

| Question | Recommendation | Why |
|---|---|---|
| Who joins | A **parent or guardian sits with the child** and joins from one device; the parent is on the sheet by the child's join name | we do not know these families; a parent present is the main safeguard |
| Entry | **Waiting room**: meeting access Restricted / host admits; the host admits **only** a name that matches the check-in sheet (`child first name + code`); the room closes at T + 10 min | keeps strangers out; the same list is the attendance record |
| Who admits | The **co-host**, a second adult present for the **whole class** | one adult cannot teach and guard the door |
| Cameras and microphones | **Off for children**; children cannot unmute or start video (host controls, to be checked); the tutor does not ask a child to speak | the teaching works by typing; nobody's face or voice leaves the home |
| Chat | Open for typed answers (so chat is **visible to all**); **moderated live** by the co-host: delete personal details at once; direct messages disabled if the option exists; links are removed | Meet cannot pre-approve chat messages (to verify in the dry run, see 6.1); the real control is people |
| Recording | **No recording of the class at all** (decision, recommended) | `docs/recordings_design.md` shows Meet cannot record "tutor and screen only"; a recording of unknown children needs consent, review and a retention duty for no benefit, because the class is free and repeated. If a promo video is wanted, record the tutor **alone**, with no audience, in a separate session. |
| Names | First name or nickname only; the join name is `first name + code` | minimal; no surname |
| After class | No private messages, no one-to-one chat, no "stay behind"; questions are answered to the parent by email | tutor agreement 3.2 already bars one-to-one with a child |
| Captions, transcripts, AI notes | **Off** | would create a text record of children's words |

### 4.2 Rules shown to families (the "How we answer" slide, the confirmation email and the page)

Parent stays with the child; first names only; type, do not speak; cameras and microphones off; no recording or screenshots; be kind in chat; the tutor may remove anyone who breaks these rules, kindly and without argument.

### 4.3 Who may be removed, and how

The co-host removes (1) a name that is not on the sheet, (2) anyone who shows a camera, a surname, a phone number, a link or unkind chat, (3) an adult who speaks to a child in a way that is unkind or unsafe. Then: leave the room as normal, no debate, record time and what happened (SOP).

### 4.4 Tutor SOP

`docs/owner_kit/preview_class_sop.md` (one page): roles, rules, before (settings, check-in sheet), admit, during, after (attendance minutes, no messages), report, and how to speak to someone who was turned away.

### 4.5 Policies that do not exist yet (owner decision)

A written **child safeguarding policy** and a named **designated person** (suggested: the owner) do not exist in the repo. Needed before the first class: a half-page policy, a staff declaration (tutors and co-host), and a decision on police or background checks for tutors who teach a public class (the tutor agreement is a draft and does not say). Asked of the lawyer in 13c.

### 4.6 Report procedure

Same day, to the owner, written, first names only: what happened, when (mm:ss), what the tutor did. The owner decides: warn, remove from future classes, or involve an outside body. If a child may be in immediate danger: call **999**. Reports about a child's safety or welfare go to Singapore's child protection services (MSF Child Protective Service and the national helplines); **I have not verified the current numbers: the owner should write the right ones into the SOP before the first class.** Do not investigate, do not confront, do not delete the evidence (a note is enough, no recording exists).

---

## 5. Funnel, measurement and tone

### 5.1 The funnel (counts only, no tracking cookies)

`registered → attended → asked for follow-up → trial attended → enrolled`. Counts come from rows we already hold: `admin_preview_funnel()` (per band, from registrations still stored) plus `preview_sessions.stats` for older sessions. Trial and enrolment status are set by the owner (`admin_preview_set_followup`) and by the self-reported "How did you hear about us? Free preview class" on the trial and enrolment forms. **No cookie, no pixel, no analytics script, no link tokens, no device ID.** The take-home link carries no identifier (we do not count who opened the practice page). What we cannot see: how many *looked at* the registration page.

What to look at weekly: registered, attended, show rate (attended ÷ confirmed), the offer-time chat questions, asks for trial, trial attended, enrolled; per band. Decide after 6 sessions whether the class earns its tutor hour.

### 5.2 Consent wording for marketing follow-up (draft)

Optional box on the form (never pre-ticked): "I would like Math Inquirers (Preciouslyours Pte Ltd) to contact me by email or WhatsApp about trial classes and new classes. I can say STOP at any time and you will stop. This does not affect my child's place in the free class." Stored with a version and time. Withdrawn by replying STOP or by email; removing the tick shortens retention to 30 days after the class. **Questions for the lawyer (13d):** whether the thank-you with the practice link is marketing; whether Do Not Call rules apply to a WhatsApp message to a Singapore mobile number that was given and ticked, and whether the Registry must be checked as well; what each message must say; how long a contact may be kept if the parent never replies.

### 5.3 Tone rules (same as the extension-book funnel in `docs/online_submission_design.md` section 7)

Honest and plain; no countdown or "limited seats" language (the page may say a plain fact: "the class has room for 40 families; if it is full you can join the waiting list"); no scores, no percentages, no comparison with other children; no "your child is behind"; never aimed at the child; one clear next step; "no obligation"; a parent who says no is thanked; a family turned away is treated kindly (1.5). Nothing is sent without the owner's approval.

---

## 6. What to build, effort, order, dependencies, decisions

### 6.1 Dependency on Google Workspace (checked 24 Oct 2026; not tested in a real Meet)

| Question | Answer | Source |
|---|---|---|
| Participant limit of Business Standard? | **150** per video meeting (Starter 100, Plus 500) | [Google Workspace pricing, Singapore](https://workspace.google.com/intl/en_sg/pricing?region=SG), read 24 Oct 2026. Enough: 30 children plus parents is about 60. |
| **Attendance report in Business Standard?** | **No.** Google's Admin Help lists attendance reporting only for Business **Plus**, Enterprise Standard and Plus, Education Plus and the Essentials editions; the pricing page shows "attendance tracking" on Plus only. Business Plus is S$29.40 per user per month on the same page (as read in `docs/recordings_design.md`); I do not recommend buying it for this: guests appear by the **name they type**, so the report would not identify anyone better than our check-in sheet. | [Admin Help: attendance reports](https://knowledge.workspace.google.com/admin/meet/let-organizers-get-reports-on-meeting-attendance-and-live-stream-views?hl=en), read 24 Oct 2026 |
| Does an admin audit log show joins? | Possibly (Admin console, Meet log events) and might be a backup check; **I could not verify** which editions give it or what it shows for guests. Check in the dry run. | not verified |
| Waiting room and host admit | Meeting access can be Restricted and the host controls who may knock; host management lets hosts or co-hosts accept knocks and lock chat, screen sharing, microphone and video | [Workspace Updates, June 2025](https://workspaceupdates.googleblog.com/2025/06/google-meet-host-management-control-for-asking-to-join-a-meeting.html); Admin Help on host management (via search snippet). Behaviour for a **guest without a Google account** typing a name is **not verified**: test it. |
| Recording | Not used for this class; Business Standard can record, Starter cannot (`docs/recordings_design.md` section 1.1) | |
| Polls, Q&A | Availability and host moderation on Business Standard **not verified**; the design uses typed chat and emoji reactions instead | |
| Can a child (no Google account) join from a parent's device by link? | Assumed, as in `docs/recordings_design.md`; **not tested** | |

So **attendance reports are not available** on the owner's planned edition; the design is built so that they are not needed. The dry run (a short Meet test with 2 to 3 helpers on different devices, no real children) must answer: restricted access with a typed guest name; can children's video and microphone be locked; can chat be limited; does the host see the join time of each person (People panel); can a second co-host be assigned; what a person who is removed sees.

### 6.2 What to build, with effort and order (agent-hours, estimates)

| # | Item | Effort | Depends on |
|---|---|---|---|
| 0 | Owner decisions (6.4) and lawyer question 13 sent; **Meet dry run** | owner 1 to 2 h | nothing |
| 1 | Review and run `preview_class.sql` on a **scratch** Supabase project; adjust | 3 to 4 | scratch project (owner) |
| 2 | Registration page (static form posting `register_preview`, list from `preview_open_sessions`, wrong-band and refusal messages, honeypot, consent boxes, no cookies), in the style of `website/interest_ui.py` | 8 to 12 | 1, lawyer text |
| 3 | Admin tab: sessions, check-in sheet, mark attendance, close, promote waitlist, funnel | 6 to 8 | 1 |
| 4 | Decks: **2 more** (band A, band C) from the same generator (about 4 to 6 each), independent check of all 3 (about 3) | 11 to 15 | owner approves the Level 3 prototype |
| 5 | Mi artwork for the three decks (publish step; not done here) | 1 to 2 | owner OK to publish |
| 6 | Free sample practice pages x 3 (open, no storage, answers and worked solutions) | 8 to 10 | online runner |
| 7 | Reminder and thank-you templates in `docs/ops/message_templates.md` style; manual send procedure (mail merge from the admin list) | 2 to 3 | owner OK |
| 8 | Warm-up slide builder from the teaser bank | 2 | released teaser month |
| 9 | Free-class terms page and privacy rows (lawyer text) | 3 | lawyer |
| 10 | First small **pilot**: one session, 15 invited families, 2 adults; then open | 3 (tutor time) | 1 to 9 |
| | **Total** | **about 50 to 70 agent-hours** plus the owner's time | |

**Order:** 0, 1, 2 and 3 together with 4, 6, 7, 9, then 10. Nothing opens before the lawyer replies and the owner approves the wording and the safeguarding policy.

**Automatic email.** Reminders and confirmations can be sent by hand from the admin list at first (40 a week). An automatic sender (a Worker plus an email provider) is a **separate choice** not made anywhere in the repo yet; owner decision 7.

### 6.3 Honest assumptions that need a first real session to test

* Registered-to-live show rate for a free class (I assumed roughly half; capacity 40 confirmed and 30 live is set from that; not measured).
* 15 to 30 live families a week (not measured; no marketing plan exists for this class).
* A parent will sit with the child (stated, not enforceable).
* Typing answers works for the youngest band (P1 to P2): reading and typing speed vary; band A may need larger type and a parent reading aloud.

### 6.4 Owner decisions needed

1. **Go or hold** until the lawyer answers question 13 (recommended: hold).
2. **The one-per-6-months rule and its strictness**: keep the recommended rule (child key + contact, near matches to a person), or the simpler "email only", or stricter (add phone verification, not recommended). Whether a "no-show" counts (recommended: no; 2 free, third reviewed).
3. **What the offer is**: trial class (free, one lesson, paid), the free Placement Check, a first-lesson discount? Prices are on hold; the offer slide says "ask us" until you choose.
4. **Bands and times:** 3 bands rotating weekly (recommended) or three weekly slots; day and time (suggested Saturday 10:00).
5. **No recording** (recommended) versus a host-only recording.
6. **Do repeat visitors ever get a second, different lesson?** (No: it breaks the 6-month rule's logic.)
7. **How reminders go out:** manual email and WhatsApp from the admin list at first (recommended), or an automatic sender (new account, new provider, cost).
8. **Safeguarding:** name the designated person; approve the half-page policy, tutor declarations and whether checks are required for tutors in a public class; supply the real child-protection numbers.
9. **Staff:** who is the co-host each week (a second adult is a hard requirement).
10. **Google edition:** stay on Business Standard (recommended; attendance from the check-in sheet) or Business Plus for the report (not recommended).
11. **Domain (D9)** for the registration page and the take-home link; the real **data protection contact** (still a placeholder).

### 6.5 Not verified (honest list)

* The SQL ran only on local PostgreSQL 16 with the repo's stand-in for Supabase's `auth` schema, never on real Supabase (pgcrypto in the `extensions` schema, definer functions called through PostgREST, `pg_cron`).
* Nothing in Google Meet was tested: guest knocking, host controls for video, microphone and chat, People-panel join times, removal behaviour. The Google facts in 6.1 come from Google's own help and pricing pages read on 24 Oct 2026; Google changes these pages.
* No real tutor has rehearsed the 60-minute lesson; the timings are a plan.
* The PDPA, Do Not Call and children's-data points are questions for the lawyer, not answers. The child-protection numbers are not given because I did not verify them.
* The registration page, admin tab, sample practice pages, reminder sending, the other two decks and Mi's uploaded artwork do not exist.
