# Tutor SOP: free preview class (one page) - DRAFT 24 Oct 2026

Full design: `docs/preview_class_design.md` (section 4 is safeguarding). 60 minutes, open to families we do not know, children 6 to 13 with a parent next to them. Nothing here has been tested in a real Meet yet; the owner's dry run (design section 6) confirms every setting marked (check).

**Roles.** Host = the owner's Workspace account (creates the meeting, admits people). Tutor = teaches and reads the chat. A **second adult (co-host)** must be in the room for the whole class: one teaches, one admits, watches the chat and handles reports. Never run it alone.

**Rules that never change**
- The class is **NOT recorded.** Nobody records, screenshots or photographs it (staff included). Do not turn on captions, transcripts or "take notes for me".
- **Children's cameras and microphones stay off.** Children answer by typing. No child is asked to speak.
- Names: first name or nickname only. Never ask for school, address, phone, surname.
- No private messages to any child or parent. No one-to-one calls.
- No promises about exams, schools or results. No pressure to buy.

**Before (T minus 30)**
1. Meeting settings (check): access **Restricted / host must admit** (waiting room on), host management ON, chat: **only the host and co-host read it aloud; disable direct messages if the option exists**, screen sharing: host only, children cannot unmute or start video (host controls). Reactions on.
2. Print or open the check-in sheet: `admin_preview_list` (join name = child first name + 4-character code, for example `Mei 7K3Q`). Confirmed rows only; pending_review and waitlisted do not get a place unless the owner says so.
3. Close other windows. Slides in presentation mode. Warm-up of the week slide updated (design section 3.5).

**Admit (T minus 10 to T plus 10)**
4. Admit a person only if the display name matches the sheet (child's first name + code) or is a parent using the same name followed by "parent". Anyone else stays in the waiting room; tell them kindly in the chat: "Please rename to your child's first name and the code from your email."
5. Tick each admitted join name on the sheet with the admit time. This list **is the attendance record**.
6. At **T plus 10 minutes close the door** (no more admissions). Late people: send "The room has closed; you are welcome to come to the next free class" (they are no-shows, not attendees).
7. Remove anyone who is not a registered join name or who shows a camera, a surname, a phone number or any inappropriate content. Do not argue in the room.

**During**
8. Say the rules slide aloud. Read chat answers by first name only. Delete any chat message with personal details at once ("Thank you! Please keep to first names"). Praise reasons, not speed. Never say who was wrong.
9. If an adult speaks to a child directly in a way that is unkind or unsafe, or an unknown person asks a child for private details or a link: the co-host removes that person, then see "Report" below.
10. The offer part (minutes 50 to 55) is soft. No countdown, no "last places", no price pressure, no comparison with other children. If a parent asks about a child's level in the chat, say "we will reply by email or WhatsApp" and do not discuss a child in front of others.

**After (within 1 hour)**
11. Co-host passes the owner the admitted join codes and for each the minutes present (admit time to end, minus any removal). Anyone present at least **15 minutes** counts as attended (owner runs `admin_preview_mark_attendance`, then `admin_preview_close_session`). A parent who joined with no child counts as not attended.
12. Write down numbers only: how many admitted, how many typed an answer in chat. Never write a child's name with a comment about them.
13. Do **not** message anyone. The owner sends the thank-you email with the take-home link, and only to parents who ticked the marketing box for anything beyond that. Delete anything you downloaded.

**Report (same day, to the owner)**: a person asked a child for private information or a link; an adult behaved unkindly to a child; a child said something that worries you (for example about safety at home); an unknown person joined; someone recorded or photographed the screen. Write the time (mm:ss), what happened and what you did, with no names beyond first names. Do not investigate. The owner decides the next step; the child protection route is in design section 4.6. If a child may be in danger now, call 999 and tell the owner.

**Being turned away.** If a parent says "it told me I cannot join": do not explain why. Say: "Thank you for your interest. This free class is for families who have not been to one in the last six months. We would love to help you with the next step; the owner will message you about a short chat or our enrolment page." Pass the name and contact to the owner; do not reveal what the system matched.
