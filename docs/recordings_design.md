# Recorded live lessons: design for posting them to enrolled families (Google Meet)

Status: DESIGN AND DRAFT ONLY, written 24 Oct 2026. Nothing here is deployed, applied, sent or published. Owner decision that asked for it: `REC-DESIGN (Google Meet)` at the end of `docs/terms/owner_decisions.md`. I am not a lawyer; every legal point below is a question for the lawyer (see section 6), not advice.

Files that go with this design (all new, none wired in):

| File | What it is |
|---|---|
| `portal/supabase/recordings.sql` | Draft tables, access rule, functions, grants. NOT applied. Applies twice cleanly and passes the test below in a throwaway local Postgres. |
| `portal/supabase/test/recordings_test.sql` | Local test for it (by hand; not added to `run_sql_test.sh`). |
| `portal/public/recordings.html` | Static prototype with fake data, no script, marked PROTOTYPE. Not linked anywhere. |
| `docs/owner_kit/tutor_recording_sop.md` | One-page tutor routine. |
| `docs/owner_kit/lawyer_email_draft.md` | New question 12 added. |

Reuses the access model of the other agent's `portal/supabase/practice_submissions.sql` (parent account owns child profiles; `_has_consent()`; admin via `is_admin()`; optional child token later). `docs/online_submission_design.md` did not exist when I wrote this, so I could not read it; check the two agree.

---

## 0. The three facts that change the plan

1. **A free Gmail account cannot record Meet.** Recording needs a paid Google Workspace edition (or a 2 TB-or-larger Google consumer plan, not recommended, see 1.1). The cheapest suitable edition is **Business Standard, S$18.80 per user per month** on Google's Singapore page. **Business Starter does NOT include recording.**
2. **Meet cannot record "tutor and screen only".** Google records the *active speaker* and anything presented. Whenever a child with a camera on speaks, that child's video is the recording. The current privacy notice says "Children's cameras are not included in the recording, and children's names are not shown", and the tutor guides (`levels/reccues.js`) say to "turn off or exclude the other children's video (use active-speaker or screen-only recording)". Neither can be guaranteed by a Meet setting. The same file also says to turn captions on, which may print speakers' names; change it after the dry run (I did not edit `levels/`). The safe rule is **children's cameras off, plus a dry run to see what is actually captured** (names on tiles, captions). The privacy wording must change either way (section 5).
3. **The portal is not live for the beta start** (manual WhatsApp and PayNow; `docs/holiday_readiness.md` section 10). So the gated "Watch recording" button cannot be the only route for week 1. A manual fallback is designed (section 3.5), clearly weaker.

---

## 1. Google Meet: what recording needs (checked 24 Oct 2026)

### 1.1 Requirements and what the owner's account can do

| Question | Answer | Source |
|---|---|---|
| Which editions record? | Business Standard, Business Plus, Essentials, Enterprise Starter/Standard/Plus/Essentials, Education Plus (staff licence), Teaching and Learning Upgrade, Workspace Individual, and Google One plans of 2 TB or more. A Workspace admin must also allow recording. | [Meet Help: Record a video meeting](https://support.google.com/meet/answer/9308681) |
| Is Business Starter enough? | **No.** Google's feature table says "This feature is not supported by this SKU" for Meeting recordings in the Starter column. | [Google Workspace pricing, Singapore](https://workspace.google.com/intl/en_sg/pricing?region=SG), read 24 Oct 2026 |
| Who can record? | The host; an outside user the host promotes to co-host; anyone in the host's organisation when host management is off. Joining only to present cannot record. Computer or Android only (not iPhone/iPad). | Meet Help, same page |
| Where is the file? | The **organizer's** Google Drive, in a "Google Meet" folder (older text: "Meet Recordings") with a sub-folder per meeting. | Same |
| Who gets it? | An email with the link to the organizer and the person who started the recording; the link is added to the Calendar event; attendees in the *organizer's own organisation* get access via the event, groups do not. Outside families get nothing automatically (good for us). | Same |
| Does everyone know? | Participants are notified when recording starts and stops. People outside the organisation and on mobile get the notice but cannot control it. | Same |
| What is in the file? | Active speaker and anything presented; other windows and notifications are not saved; pinning someone on your own screen does not change the recording. If continuous meeting chat is off, the chat is also saved as a `.SBV` file in the organizer's Drive. | Same |
| Captions? | "Record captions" embeds captions in the video; may appear hours after the file. | Same |
| Limits? | 8 hours total per meeting (we need 90 minutes). Both the personal Drive and the organisation's Drive need room, or recording is refused. | Same |
| Explicit consent prompt? | An admin can require participants to give consent (click Start / Join / Continue) before record, transcribe or AI notes are used. Off by default. A Workspace Updates post (April 2026) covers this for transcripts and recordings, and a May 2026 note says that rollout is **paused**. Edition coverage in that post lists Education Plus; I could not confirm Business Standard. Check the Admin console (Meet safety settings) at set-up. | [Admin Help: participant consent](https://knowledge.workspace.google.com/admin/meet/manage-participant-consent); [Workspace Updates, Apr 2026](https://workspaceupdates.googleblog.com/2026/04/require-explicit-consent-for-take-notes-with-Gemini-recordings-and-transcripts-in-Google-Meet.html) |
| Retention? | Google keeps the file until we delete it. Deleted Drive files go to Trash first (I believe 30 days, then purged: **not verified in this research; confirm at set-up**). No automatic expiry for Meet recordings that I could find. Meet Help does not state one. | Meet Help (silent) |
| Restrict to specific accounts? | Drive files can be shared to named Google accounts only (default "Restricted"). Families without a Google account need **visitor sharing** (email PIN; re-verify about weekly) which depends on the admin setting. Meet does not do this itself. | [Visitor sharing explainers](https://its.umich.edu/communication/collaboration/google/update/collaborate-users-drive-and-sites-who-don%E2%80%99t-have-google) (university IT pages, not Google's own; re-check in Drive Help) |
| Transcripts? | Separate "transcript" feature (editions per Google's page); creates a text record of everything children say. **Do not use.** Same for "take notes for me" (Gemini). | Meet Help; Admin Help |
| Minors, Education vs business? | Meet Help says nothing about recording under-18s. For Education accounts it says: Education Fundamentals/Standard users "can't record meetings they organize"; Education Plus can. Education editions are for eligible schools; a private tuition company probably does not qualify (**not verified**). **Children never need a Google account here**: they join from their parent's device through the link. We use a plain Business edition under the company, not Workspace for Education. | Meet Help; my reading |

### 1.2 Price (as Google states it)

Google's Singapore pricing page (read 24 Oct 2026, prices in SGD, "per user/month", page says "All plans billed monthly" and offers "Save 16% with one-year commitment"):

| Edition | Price on page | Records Meet to Drive? | Pooled storage |
|---|---|---|---|
| Business Starter | S$9.40 | No | 30 GB |
| **Business Standard** | **S$18.80** | **Yes** | 2 TB |
| Business Plus | S$29.40 | Yes | 5 TB |

- **Cheapest suitable edition: Business Standard, S$18.80 per user per month** (one user: the owner, who is the organizer). A one-year commitment saves "16%" per Google's page, which would be about S$15.80 (my arithmetic, not a Google figure). The page text is ambiguous about whether S$18.80 is the monthly-billing or the annual price; **the checkout screen is the authority**. GST treatment was not shown. A 14-day no-cost trial is offered, so the owner can run the dry run (section 8) inside the trial.
- One web search snippet showed S$4.70 beside a struck-through S$9.40 for Starter (a promotion). Irrelevant: Starter cannot record.
- The 2 TB Google consumer plan is listed by Google as able to record, but the plan is now sold as "Google AI Plus (2 TB)" at US$9.99 on the Singapore page (no SGD figure found). I do **not** recommend it: it is a personal account, with no company admin controls, no admin consent setting and no business terms for children's data.
- Sign-up for Workspace normally asks for a domain you own. **The business domain is still undecided (owner decision D9)**; settle the domain first or buy one for this.
- Seats: 1 (owner as organizer, tutor joins as promoted co-host). Add a seat only if the tutor must start recordings from a Workspace account of their own. This must be confirmed in the dry run (outside co-host can record per Google's page).

**What the owner's current account (a gmail.com address) can and cannot do:** it can host free Meets (time-limited for groups on free accounts, not checked), but it **cannot record** and cannot create the restricted-sharing folders under a company. It has to be replaced, for lessons, by a Workspace account under the company domain. The existing Gmail stays for contact.

---

## 2. Where the file lives: options and recommendation

### 2.1 Options compared

| | A. Drive only (restricted sharing) | B. Drive master + copy on Cloudflare Stream (signed tokens) | C. Drive master + copy in Cloudflare R2 behind a signed link |
|---|---|---|---|
| Cost | S$0 beyond Workspace | Stream (per [Cloudflare](https://developers.cloudflare.com/stream/pricing/), 24 Oct 2026): storage US$5 per 1,000 minutes per month (prepaid), delivery US$1 per 1,000 minutes watched. Beta estimate: about 6 groups x 10 lessons x 70 min = 4,200 minutes stored = US$25 per month at peak; if each family watches each lesson twice, about 67,000 minutes = about US$67; realistic US$20 to 40 delivery. Roughly US$45 to 90 for the whole beta, and the stored minutes fall as lessons expire. | R2 (per [Cloudflare](https://developers.cloudflare.com/r2/pricing/)): US$0.015 per GB-month, 10 GB free, **no egress fee**. 60 lessons of about 1 GB is well under US$1 a month. Needs our own player page and signing code. |
| Access control | Per file/folder to named Google accounts; non-Google families need visitor sharing with PINs; a link shared by a parent can reach anyone *signed in as an invited account only*. Manual work for every family. | Portal login decides. Video is `requireSignedURLs`; tokens expire in under an hour (Cloudflare caps at 24h); `allowedOrigins` limits where it plays; keys can be revoked. No Google account needed by families. | Same logic through a Pages Function that signs a short-lived link. No adaptive streaming; long downloads on bad wifi. |
| Link leaks | Low *if* "Restricted" is kept; high if anyone flips to "Anyone with the link". Easy to do by accident. | A leaked token dies within the hour; the video address alone is useless. | Same as B if the link is signed and short. |
| Deletion | Delete file, then it sits in Trash (verify days). Hard to prove deletion across shares. | API/dashboard delete is immediate; one place. | Delete object; immediate. |
| Player quality | Google viewer: good, but needs sign-in and blocks some school/work networks. | Adaptive bitrate, captions, works on phones with no sign-in. | Basic HTML5 video. |
| Build effort | None | One Pages Function (token) + the portal page. About 1 day. | Same plus a player. |
| Storage location | Google (outside Singapore; Workspace regional options are US or Europe as far as I know: **verify**) | Cloudflare global network (no Singapore-only choice that I verified) | R2 has jurisdiction/location hints (**verify**) |

### 2.2 Recommendation

**B, with Drive as the private master, and a manual version of A for the first week only.**

1. Drive is where Meet puts the file. Treat it as the **owner-only vault**. Nothing is ever shared by link. Tutors review in Drive view-only.
2. The copy families watch lives on Cloudflare Stream with signed tokens, shown only inside the logged-in portal. This is the only option where a leaked link does not leak the video and deletion is one call. R2 is the cheaper fallback if Stream's per-minute cost matters in the term program.
3. For week 1 (Tue 24 Nov), if the portal is not live, use the manual route in 3.5: a Drive sub-folder per group shared (Viewer, download off) to the named Google accounts the parents gave us. State the weakness to the owner: it depends on every family having a Google account, and on the owner not changing "Restricted".
4. Reject YouTube "unlisted" and any "anyone with the link": the link is the whole security, the audio contains children.

### 2.3 Drive folder structure (private, owner is the only editor)

```
MI Recordings (PRIVATE)            <- shared with nobody; "Restricted"
  L1A/                              <- one folder per group id (L1A..L6A, later R1.. and term groups)
    01_raw/                         <- Meet drops the file here after the owner moves it. Tutor: Viewer only (download disabled for viewers)
      L1A_L01_2026-11-24_raw.mp4
    02_ready/                       <- trimmed MP4 that is about to be uploaded. Owner only
    (03_published: not a Drive folder; the published copy is on Stream)
  _deleted_log.md                   <- date, group, lesson, who deleted raw/ready/Stream copy (no child names)
```

Naming: `{group}_L{nn}_{yyyy-mm-dd}_{raw|ready}.mp4`. Retention of the Drive master: **raw deleted 7 days after the published copy is live** (it holds untrimmed material); ready file deleted the same day as the Stream copy (below). Download copies on laptops are deleted at the same time (tutor agreement 6.5 already requires it).

---

## 3. End-to-end workflow per lesson

Timings are Singapore time (SGT). T = the end of the live lesson.

### 3.1 Before and during the lesson

| Step | Who | Detail |
|---|---|---|
| Meeting set up | Owner, once per group | One recurring Calendar event with a Meet link per group, created by the owner's **Workspace** account (so the owner is the organizer and the file lands in the owner's Drive). Link goes in `ops/meet_links.json` as already planned (`ops/make_ics.py`). |
| Tutor joins | Tutor | Joins 10 minutes early; owner (or the host) promotes the tutor to co-host. Tutor uses a **computer** (iPhone/iPad cannot record). |
| Host settings | Tutor | Turn on host controls; ask children's cameras **off** (if Meet's host controls let the host disable participants' video, use it; check in the dry run); chat off or "no personal info in chat". Captions: leave OFF until the dry run shows what they print (they may label speakers by name). |
| Start recording | Tutor | Meeting tools > Recording > Start recording. Check the red "recording" indicator. **Start before saying anything about the lesson content.** Google notifies everyone that recording started. |
| Spoken notice | Tutor | Within the first minute, once, same words every lesson: "This lesson is being recorded so that anyone who misses it can catch up. The recording has my voice, the screen and the voice of anyone who speaks. Please keep your cameras off. If you would rather not be heard, stay on mute and type nothing personal; I will repeat answers in my own words." Parents beside the child hear it too. |
| Who is on camera | Tutor only | Tutor camera on, shared screen on. Children's cameras off. A child whose camera is on will appear while speaking: tutor politely asks them to switch it off. Parents are asked not to appear in the background. |
| During | Tutor | The recording cues already in the guides apply (say the REC line, timers on screen, repeat answers). Never say a child's name with a right/wrong answer; no one holds work to a camera. |
| Stop | Tutor | Meeting tools > Recording > Stop recording > confirm, before saying goodbye chat. Recording also stops when everyone leaves. |

### 3.2 After the lesson (target: published within 24 hours of T; hard maximum 48 hours)

| When | Step | Who | Detail |
|---|---|---|---|
| T + 0 to 30 min | File appears | Google | Drive shows "Still processing" first. Email with the link goes to the organizer and the person who started it. Owner moves the file to `L1A/01_raw/` and renames it. If no file in 2 hours: see SOP "no file". |
| T + 1 day (by 12:00 SGT next day) | **Tutor review** (view-only in Drive, play at 1.5x to 2x but listen to all of it; scrub the video track to catch faces) | Tutor | Checklist below. Output: pass, or a cut list of `mm:ss-mm:ss` ranges with the reason (no child names in the reason). |
| Same day | **Trim** | Owner (default) | Cut the ranges and any dead time before the notice/after the goodbye. Stream-copy trim, no re-encode: `ffmpeg -ss 00:00:30 -to 01:12:10 -i raw.mp4 -c copy ready.mp4` (cuts land on keyframes; re-encode only if a cut must be exact). Anything needing a blur: cut it out instead. |
| Same day | **Upload and link** | Owner | Upload `ready.mp4` to Stream; set Require signed URLs = on, allowed origins = the site domain, downloads off. Add chapters and workbook page numbers/materials in the description (as `reccues.js` upload cues say). Record the Stream video id, then in the admin page (to be built; until then the SQL editor) call `admin_save_recording(...)` then `admin_publish_recording(..., review)`; the publish call refuses if the three review boxes are not true. |
| Publish | Families see it | Portal | "Watch recording" appears on the lesson row. The owner sends the group a WhatsApp saying "Lesson N recording is ready in your portal" (message 11 rewritten in 3.5, **no link inside**). |
| Raw cleanup | T + 7 days after publishing | Owner | Delete `raw` and `ready` in Drive and laptop copies. |

### 3.3 Tutor review checklist (all three required to publish; same keys stored in `recordings.review`)

1. **No private information** (`no_private_info`): no address, phone, school name, birth date, NRIC, passwords or email read aloud or visible; no parent or sibling talking in the background; no personal chat messages; no payment talk.
2. **No children's faces or names** (`no_child_names_faces`): no child's camera visible even briefly; no full names; no name shown with a right/wrong answer or with a behaviour comment; no child's paper held to a camera. Any first name that must stay is the owner's decision (the notice says names are not shown).
3. **On topic** (`on_topic`): no off-topic chat, complaints, tutor-parent private matters, other families' business, anything unsafe or embarrassing for a child; no technical meltdown the lesson does not need.
4. Trimmed (`trimmed`): dead time and the cut ranges removed (not required to publish).
5. Audio and screen usable (a child can follow the screen and hear the tutor).

If anything in 1 to 3 cannot be cut out, do **not** publish: tell the owner; the families keep the printed workbook and a makeup seat (section 4).

---

## 4. Makeup rules (from the terms) and how the recording supports them

Quoted from `website/terms.html` (read 24 Oct 2026):

| Rule | Where | What the recording does |
|---|---|---|
| Beta: child cannot attend: no refund; may make up **once** by joining the same lesson in another class of the same level if a seat is free; "Every lesson is also recorded, so your child can watch the recording and use the online practice. There are no separate make-up lessons." (s.5 table) | s.5 refunds table | The recording is the default catch-up; the live swap needs a free seat in another group (most levels have only one group in the beta, so for most families the recording is the only makeup: `holiday_readiness.md` s.10). |
| Withdrawal in the beta: fee not refunded; "your child can still watch the recordings of lessons already held" | s.5 table | Portal rule: a cancelled enrolment that was **paid** keeps access to recordings until they expire (in `_can_watch_group`). An unpaid, cancelled reservation does not. |
| Regular program withdrawal: remaining lessons move to a later cycle; can still watch recordings already held | s.5 table | Same rule. |
| Skipped lessons / exam periods: can watch the recording and use the online practice; may attend the same lesson in another class or holiday class if a seat is free; no refunds | s.7 "Missed lessons and exam periods" | The portal row shows the recording next to the workbook pages for that lesson. |
| Fee includes "access to the lesson recordings and online practice for your child's level" | Beta fee line | The paying family's access must exist for every held lesson that passes the review checklist. |

Gaps to fix in the terms (drafts, not applied): (a) **no end date for recordings** is stated in the terms while the privacy notice says 30 days after the group's last lesson (also noted in `docs/legal/review.md`); suggested text: "Recordings stay available to your group until 30 days after your group's last lesson, then they are deleted." (b) The make-up promise assumes a recording exists; add: "If a recording cannot be shared (for example, it captured something private), we will give your child the lesson slides and answers and, if a seat is free, a place in the same lesson in another class." (c) Section 12 should add: "Recordings may include other children's voices. Do not share, download or record them." (flagged T14 in `docs/legal/review.md`).

Optional later: an attendance table so the portal can show "you missed lesson 3: watch the recording" automatically. Not in this draft.

---

## 5. Portal: making recordings available only to enrolled families

### 5.1 Data model (`portal/supabase/recordings.sql`, NOT applied)

- `recordings(id, group_id, lesson_no 1..10, title, provider 'stream'|'drive'|'r2', provider_id, duration_min, recorded_on, status 'draft'|'in_review'|'published'|'withdrawn'|'expired', published_at, expires_at, review jsonb, reviewed_by, provider_deleted_at)`. One live row per group lesson (partial unique index).
- `recording_views(recording_id, parent_id, child_id, viewed_at)`: one row per successful playback request, deleted with the recording (and with `delete_my_data()`: line to add, in the SQL file footer).
- **Access rule** (`_can_watch_group`): the logged-in parent has a child enrolled in the recording's group with `status = 'confirmed'`, **or** `'cancelled'` with a **paid** payment (terms: can still watch recordings already held), **and** their latest `recording` consent is granted (`consents` table, append-only; withdrawing consent stops access at once).
- Clients have **no table grant at all**; `provider_id` (the video id) is never selectable. They use `my_recordings()` (no provider id) and `recording_playback(recording, child)` (returns provider id only when the rule passes, logs the view). Admin functions: list, save draft, publish (needs the 3 review keys true), withdraw, due-for-deletion, confirm-deleted. All check `is_admin()`.
- Local test (`recordings_test.sql`) proves: enrolled and paid sees it; other group, unpaid reservation, anon, direct table select, withdrawn consent: all refused; paid-then-withdrawn keeps access; publish refuses an incomplete review; deletion flow.

### 5.2 The "Watch recording" button

- Parent portal child/lesson page (the parent is the logged-in principal; the existing child sign-in is only a stub and not a session, so recordings use the **parent** login. The other agent's `child_start_session` token can be added later as a second path calling the same rule).
- Row per lesson: title, held on, length, "Available until" date, button **Watch recording** (prototype: `portal/public/recordings.html`). Status "Being checked by your tutor. Usually ready within 24 hours" until published.
- Click: browser POSTs `{recording_id, child_id}` with the Supabase JWT to a **new** Pages Function (to be written, e.g. `functions/api/recording-token.js`, not written now). It calls `recording_playback` **with the user's JWT forwarded** (so `auth.uid()` applies), returns 404 on empty, otherwise signs a Cloudflare Stream token for that video id with `exp` = now + 1 hour (Stream's maximum is 24 hours; shorter is safer) and `allowedOrigins` = the site, and returns the player URL. The video id and signing key never reach the page source. CSP for `/portal/*` will need a `frame-src`/`media-src` entry for the Stream player host (the current portal CSP allows only `self` and Supabase): that is part of the build step.

### 5.3 If Drive links are used anyway (week 1 fallback or if Stream is rejected)

- Never "Anyone with the link"; keep **Restricted** and share to named Google accounts (Viewer; untick "Viewers and commenters can see the option to download, print, and copy").
- Sharing is by group folder `L1A/families/` (not the raw folder), so a new recording needs no new share. Parents without a Google account: visitor sharing (PIN by email, re-verified about weekly, admin setting) or they create a Google account with the same email.
- The portal can still store the Drive file id in `recordings` and show the button, but then the button opens the Drive viewer; the portal cannot stop a family from forwarding a Drive link to another Google account **only if the owner granted "editors can share"**; keep sharing by owner only. A log is only what Drive's own "view activity" shows (Workspace editions vary: not verified).
- In this mode the portal adds nothing to security; it is a convenient list. State that plainly to the owner.

### 5.4 Message 11 rewritten (draft, not applied to `docs/ops/message_templates.md`)

> Hi everyone, the recording of lesson [N] for Group [Group] is ready. Log in at [portal address] > [Child] > Recordings and press Watch recording. It is for your family only and is deleted on [date: 30 days after the group's last lesson]. Please do not share, download or record it: it can include other children's voices.

Message 6 (day before first lesson) says "not cameras or names"; change after the dry run to: "The recording has the tutor, the shared screen and the voice of anyone who speaks. Please keep [Child]'s camera off." The tutor agreement 3.6 has the same sentence: change both together.

---

## 6. Retention, deletion, consent wording

### 6.1 Retention (suggestion)

| Item | Suggested period | Why |
|---|---|---|
| Published recording (Stream) | **30 days after the group's last lesson** (already in `privacy.html`; keep). E.g. Group L1A last lesson Thu 24 Dec 2026, so gone Sun 24 Jan 2027. | Matches the published notice. Long enough to catch up after the holidays. |
| Raw Drive recording | 7 days after publishing | Untrimmed. |
| Unpublished (blocked at review) | Delete within 7 days of the decision | No reason to keep. |
| Review checklist and view log | With the recording (view log deleted when the file is confirmed deleted) | Evidence of review/make-up while the recording exists; no long-term profile of who watched. |
| Withdrawn (found private content, or parent withdrawal) | Playback off immediately; file deleted within 7 days | |
| Google Drive Trash / Stream | Empty Trash immediately after delete (otherwise it lingers; verify) | |

Owner choice: 30 days is generous for a 10-lesson, 5-week program; 14 days after the last lesson is the stricter alternative.

### 6.2 Deletion process (every Monday, 10 minutes)

1. Run `select * from admin_recordings_due_for_deletion();` (also marks past-expiry rows `expired`). 2. Delete each listed video in Stream, then the Drive `ready`/`raw` files and laptop copies. 3. `select admin_confirm_recording_deleted('<id>');` for each. 4. Add a line to `_deleted_log.md`. A family that withdraws recording consent: the portal stops access at once (consent check); the child can no longer join a recorded group (privacy notice); the owner decides case by case whether to pull earlier recordings that include that child's voice (lawyer question).

### 6.3 What the existing `recording` consent says vs what Meet does

Consent text on the registration form (privacy.html, item 3): "I agree that live lessons are recorded as described in this notice, and that recordings are shared only with the enrolled families of my child's group."

| Statement in the current notice | Meet reality | Fix |
|---|---|---|
| "We record the tutor and the shared lesson screen. Children's cameras are not included" | Active speaker + presentation. A child with camera on is included while speaking. | Rewrite (below). |
| "children's names are not shown" | Unverified: may show a name label on the speaker; captions may name speakers. Test. | Test then state. |
| "A parent who does not want their child heard ... can ask us to mute the child" | Fine. | Keep; add "tell us when you register". |
| "We tell the group at the start of each lesson" | Google also shows a notice. | Keep. |
| "only the enrolled families of the same group, through a private link" | Sound if portal-gated; "private link" is wrong for the portal route. | "through your parent login". |
| Not mentioned | The tutor reviews and trims before posting; copy stored with Google and Cloudflare (outside Singapore); a view log. | Add. |
| Retention "30 days after your group's last lesson" | Matches the design. | Keep. |

### 6.4 Draft wording for `website/privacy.html` (DRAFT in docs only; not applied)

Replace the "How lessons are recorded" list:

> - We record the tutor, the shared lesson screen and the voice of anyone who speaks. Children are asked to keep their cameras off. If a child's camera is on while they speak, they may appear in the recording. If a name label is shown, it is the name the family typed when joining; we ask families to use a first name only. <span class="ph">[Confirm after the dry-run recording: whether names show]</span>
> - The tutor repeats children's answers in their own words wherever possible. A parent who does not want their child heard on the recording can ask us to keep the child muted; please tell us when you register.
> - We tell the group at the start of each lesson that it is being recorded. Google Meet also shows a notice when recording starts.
> - Before a recording is shared, your child's tutor watches it and we remove anything private (for example names, faces, addresses). If we cannot, we do not share it.

Replace in "Who can see it":

> - Recordings: only the logged-in parents of enrolled children in the same group, through the parent portal, for the time shown. We never post them publicly or send a link outside the portal. We record which parent account watched which recording and when, so that we can help with missed lessons and investigate misuse; we delete that log with the recording.

Add to "Who we share data with" (or equivalent): "Google (Google Meet and Google Drive) records and stores lesson recordings before we review them. Cloudflare stores the reviewed copy and delivers it to you. These services run outside Singapore. <span class="ph">[Lawyer to confirm PDPA transfer wording]</span>"

Replace consent item 3 (recording):

> **Recording (needed):** I agree that live lessons are recorded (the tutor, the shared screen and the voice of anyone who speaks; a child may appear if their camera is on), that the tutor checks and trims the recording, that it is stored with Google and Cloudflare outside Singapore, and that it is shown only to the logged-in parents of enrolled children in my child's group until 30 days after the group's last lesson, then deleted. I understand other children's voices may be on it and I will not share, download or record it.

If the consent text changes, bump `VERSIONS` in `portal/public/common.js` and re-collect consent from already-registered families (record_consents stores the version).

Terms: sentences in section 4 above (end date; recording unavailable; no sharing).

---

## 7. Lawyer question 12

Added as question 12 in `docs/owner_kit/lawyer_email_draft.md` (existing questions untouched). Note: that file currently has questions 1 to 10 only (no 11 yet), so 12 leaves a gap; renumber when 11 arrives from the other agent. The email also is titled for school booklets; question 12 belongs to the home-class business and could go in a separate email (`docs/legal/review.md` L3, L4 list the same area).

---

## 8. Owner checklist

### Decisions needed (owner)

1. **Buy Google Workspace Business Standard (one seat)?** S$18.80 per user per month on Google's SG page (24 Oct 2026); about S$15.80 on a one-year commitment if the 16% applies; confirm at checkout; trial 14 days. Yes/no, and **which domain** (D9).
2. **Storage choice:** B (Drive master + Cloudflare Stream signed; est. US$45 to 90 for the whole beta) or R2 (cheaper, more code), or Drive-only manual (free, weaker).
3. **Who reviews, who trims:** default tutor reviews view-only and owner trims/uploads. Or tutor does all (needs download rights; weaker for confidentiality).
4. **Review depth:** full listen to every lesson (about 45 minutes at 2x per 90-minute lesson; 60 lessons is about 45 hours in the beta) or full review of the first 3 lessons per group and spot checks. I recommend full review for the beta because children are involved.
5. **Retention:** keep 30 days after the group's last lesson, or 14.
6. **Cameras:** children's cameras off rule (my recommendation) and the privacy wording change; also whether first names may stay on screen.
7. **Publish within:** 24 hours target, 48 hours maximum (confirm).
8. **Week 1 route if the portal is not live:** manual Drive sharing to named Google accounts (needs parents' Google emails at registration) or hold recordings back until the portal is live. If recordings are late, the terms' catch-up promise is not met.
9. Approve the new consent wording and the privacy/terms edits (lawyer first).
10. Whether to let `portal/public/recordings.html` ship (it is copied by `--with-portal`): delete or exclude it from the first real portal build.

### Set up (owner, in this order)

1. Domain, then Workspace Business Standard; turn on 2-step verification for the owner account.
2. Admin console > Apps > Google Meet: allow recording; set Meet safety settings (consent prompt if available for your edition; host management on; who can join: invited or knock-and-admit); **Drive sharing: turn OFF "Anyone with the link"/public, restrict external sharing to named accounts; decide visitor sharing.**
3. Create `MI Recordings (PRIVATE)` and the group folders (2.3). Tutor Viewer on `01_raw` only.
4. Cloudflare Stream subscription (or R2); create a signing key; keep it in Cloudflare secrets only (never the repo).
5. Review then apply `recordings.sql` on a scratch Supabase project first; run `recordings_test.sql`; then live. Build the `recording-token` Pages Function and the real page from `recordings.html` (assistant task, after your approval).
6. Tutor agreement and tutor SOP signed/read (the tutor agreement says recordings are made by the company's Meet account only).

### Test (dry run, before Wed 4 Nov per `launch_checklist.md`)

Use the 14-day trial. Record a 10-minute Meet with the owner's own family: owner = organizer, a family member = tutor (promoted co-host, on a computer), two or three more people as "children" on phone, tablet and a signed-out browser (no Google account), some with cameras on, some off.

Check and write down: (1) can an outside co-host start the recording; (2) what the recording shows when a camera-on person speaks, when a camera-off person speaks, when someone is muted; (3) are **names** shown on the picture; (4) what captions show if turned on; (5) every participant got the "recording started" notice, including phone and signed-out guests; (6) where the file lands, how long until it plays, who is emailed; (7) who can open the link from another Google account and from a signed-out browser (must be nobody); (8) can a viewer download if download is disabled; (9) what the chat `.SBV` file contains; (10) host control to stop children turning cameras on (exists? where); (11) upload to Stream, signed token expires, link without token fails; (12) delete: how long until Drive Trash purge; (13) time taken to review, trim and upload a 90-minute lesson. Record the results in a short note, then fix the privacy wording items marked `[Confirm after the dry-run recording]`.

### Costs (summary)

| Item | Cost | Notes |
|---|---|---|
| Workspace Business Standard, 1 seat | S$18.80/month (about S$15.80 if annual 16% applies; verify) | Google SG page, 24 Oct 2026; GST not shown |
| Cloudflare Stream | about US$45 to 90 for the beta (US$5 per 1,000 stored minutes per month + US$1 per 1,000 minutes watched) | Cloudflare docs, 24 Oct 2026; my estimate |
| Cloudflare R2 (alternative) | under US$1 per month at this size | Cloudflare docs |
| Domain | to decide | D9 |
| Owner/tutor time | review ~45 min + trim/upload ~20 min per lesson | estimate; tutor hours not in the agreement yet |

---

## 9. Sources and dates

All read 24 Oct 2026.

- Google Meet Help, [Record a video meeting](https://support.google.com/meet/answer/9308681): editions, who can record, storage location, emails, notification, 8 hour limit, captions, education notes.
- Google Workspace pricing, Singapore: <https://workspace.google.com/intl/en_sg/pricing?region=SG> (S$9.40 / S$18.80 / S$29.40; recording not supported on Starter). The global page <https://workspace.google.com/pricing.html> shows recording "Not supported" for Starter and available for Standard and Plus but did not show prices.
- Google Workspace Admin Help, [Manage participant consent for Meet features](https://knowledge.workspace.google.com/admin/meet/manage-participant-consent) (found via search; contents summarised from the search result, not read in full).
- Google Workspace Updates blog, April 2026, [require explicit consent ... in Google Meet](https://workspaceupdates.googleblog.com/2026/04/require-explicit-consent-for-take-notes-with-Gemini-recordings-and-transcripts-in-Google-Meet.html) (a May 2026 note says the rollout is paused).
- Cloudflare Stream pricing <https://developers.cloudflare.com/stream/pricing/>; securing videos with signed URLs <https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/> (requireSignedURLs, tokens up to 24h, allowedOrigins, revocable keys); R2 pricing <https://developers.cloudflare.com/r2/pricing/>.
- Drive visitor sharing: university IT explainers (not Google's own page), e.g. <https://its.umich.edu/communication/collaboration/google/update/collaborate-users-drive-and-sites-who-don%E2%80%99t-have-google>.
- Google One 2 TB: <https://one.google.com/about/plans?hl=en_SG> (shown as Google AI Plus 2 TB, US$9.99; not recommended).

**Not verified and flagged:** Drive Trash purge period; Workspace data region options; Cloudflare storage location; whether Business Standard has the Meet explicit-consent prompt; whether Meet shows name labels in the recording; whether a host can disable participants' video; whether an outside co-host can record on our exact setup; the "Education eligibility" of a private tuition company; the exact Singapore billing basis (monthly vs annual) of S$18.80.
