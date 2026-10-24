# Weekly Family Check-in: demand test (no app, no tracking)

Status: design draft for owner approval. Nothing here is sent or built yet.

## 1. Hypothesis, sample, success and failure

**Hypothesis.** Parents will, unprompted by any app, send us one weekly screen-time number and value a short reply (trend, one suggestion, a 5-minute puzzle) enough to keep doing it. If so, an app that automates this has demand; if not, we avoid building it.

**Sample.** Opt-in families from the November beta, target 10 to 20. Parents only; no child contact. Duration 6 weeks (4 weeks minimum; weeks 5 to 6 are slack for missed weeks and the interview).

**Measures and thresholds** (n = families who opted in and sent at least week 1; judge on n of 10 or more):

| Measure | Success | Weak | Failure |
|---|---|---|---|
| Submit at least 3 of the first 4 weeks | 60% or more | 40-59% | under 40% |
| Still submitting in week 4 | 50% or more | 30-49% | under 30% |
| "Would you keep doing this?" (yes/no at end) | 60% or more yes | 40-59% | under 40% |
| Opened/attempted the puzzle in 2+ weeks (self-report, one tick in the form) | 50% or more | 30-49% | under 30% |
| Parent names at least one concrete thing that changed (talk, routine, awareness) | 40% or more | 20-39% | under 20% |
| Would pay or would recommend (interview, 0-10, 8+) | 30% or more | 15-29% | under 15% |

With a sample this small, treat numbers as signals, not statistics; interviews outweigh the table when they disagree.

## 2. Weekly flow (plain steps)

Same day each week (suggest Sunday evening for the parent, reply by Monday evening).

1. **We remind** (WhatsApp from the business number or the Form link), Sunday 6pm: "Time for this week's check-in. It takes 2 minutes."
2. **Parent finds last week's total** on their own phone (menu names change; check on your device):
   - **iPhone:** Settings, then Screen Time, then See All Activity (or tap the device name). Choose "Last Week" or the weekly view and read the daily average or total. If the child has their own device set up through Family Sharing, the parent can view it from their own phone; otherwise use the child's device.
   - **Android:** Settings, then Digital Wellbeing and parental controls (check on your device), or the Family Link app for a supervised child. Open the dashboard, pick the child's device, and read the weekly total or daily average.
   - Always the same measure each week: please use the **total hours per week** (or daily average, but stay consistent).
3. **Parent sends** (recommended: a number only):
   - Weekly total (e.g. "17 h 30 m"), age band (6-8, 8-10, 10-13), optional one-line note ("exam week", "holiday").
   - No child's name, no screenshot, no app names. A screenshot is not needed and exposes more than we want; if a parent insists, we ask them to crop to the total and we delete it after replying.
4. **Where it goes.** Start: a Google Form (fields: family code, week number, total, age band, note, "did your child try the puzzle?") or a WhatsApp message to the business number. No new code. Later option: a portal page, only if the test succeeds.
5. **We reply within 24 hours** (WhatsApp or email, one short message, templates in section 3):
   - This week vs last week (numbers and difference).
   - A gentle trend line (up, down, steady; neutral tone).
   - One small suggestion the parent can choose to try.
   - A 5-minute original puzzle for the age band (with the answer at the bottom, parent-facing).
   - Never shaming, no medical claims, no claims about harm.

Week 1 has no comparison; ask for last week and the week before if available.

## 3. Message and puzzle templates

### Reply template (fill in)

> Hi [parent first name], thanks for this week's check-in.
> **This week:** [X h Y m]. **Last week:** [X h Y m]. [That is about N% more / less / about the same.]
> **Trend:** [One neutral line, e.g. "A little higher than last week, which is common in school holidays." or "Steady for three weeks."]
> **One small idea (optional):** [see suggestion bank]
> **5-minute puzzle for your child (ages [band]):** [puzzle]
> Answer is at the bottom, no pressure to finish. Reply with one word if it was fun, or skip it. Next check-in: Sunday.
> Answer: [answer]

### Suggestion bank (pick one; never more than one)

- Pick one meal a week that is screen-free and let your child choose the topic.
- Ask your child what they enjoyed most on screen this week; just listen.
- Agree one time of day your family keeps simple (e.g. the hour before dinner).
- Try the puzzle together on paper instead of on a screen.
- If the number is low or falling: "Nothing to change; thanks for tracking."

### Trend lines (neutral)

Up: "A bit higher than last week." Down: "A bit lower than last week." Steady: "About the same as last week." Holiday/exam note: acknowledge it.

### Puzzles by week and age band (originals, answers brute-force verified)

**Ages 6-8**

| Week | Puzzle | Answer |
|---|---|---|
| 1 | Two numbers add up to 10. One is 4 bigger than the other. What are they? | 7 and 3 |
| 2 | Mia has 3 bags with the same number of marbles in each, plus 2 loose marbles. She has 14 marbles in all. How many are in each bag? | 4 |
| 3 | Pick three different numbers from 1 to 5 that add up to 9, where the biggest is 4 more than the smallest. | 1, 3, 5 (only solution) |
| 4 | Make exactly 30 cents using exactly 4 coins, each a 5-cent or a 10-cent coin. | Two 10c and two 5c |

**Ages 8-10**

| Week | Puzzle | Answer |
|---|---|---|
| 1 | A two-digit number has digits that add to 11. It is 27 more than the number you get by swapping the digits. What is it? | 74 (74 - 47 = 27) |
| 2 | Sam has 8 stamps, some worth 2 cents and some worth 5 cents, worth 31 cents in total. How many of each? | Three 2c and five 5c |
| 3 | What is the smallest number bigger than 1 that leaves remainder 1 when divided by 2, 3, 4 and 5? | 61 |
| 4 | 6 friends each shake hands once with every other friend. How many handshakes? Try drawing dots and lines. | 15 |

**Ages 10-13**

| Week | Puzzle | Answer |
|---|---|---|
| 1 | Three consecutive whole numbers multiply to 990. Find them. | 9, 10, 11 |
| 2 | Two whole numbers add to 20 and multiply to 96. Find them. | 8 and 12 |
| 3 | How many 3-digit numbers have digits that add to exactly 5? | 15 |
| 4 | What is the last digit of 7 multiplied by itself 2026 times? Hint: write the last digits of 7, 49, 343, 2401... | 9 (last digits cycle 7, 9, 3, 1; 2026 is 2 more than a multiple of 4) |

Verification: each answer was checked by exhaustive search (Python, 2026-10-23), including uniqueness where the text says "only". The puzzles are new, in the style of our school puzzle books (short, answer-in-hand, one idea each), not copied from them.

## 4. Family agreement card (one page, optional)

Printable A5, parent-set, nothing enforced by us. Layout:

- Title: "Our Family Screen Agreement". Date and family-chosen name (no personal data collected by us).
- "We agree to (pick 1 to 3, or write your own):" screen-free dinner; devices charge outside the bedroom at night; one family activity per week; ask before installing something new.
- "When we break our own agreement, we talk about it; we do not punish." One line: "Adults follow it too."
- "We will look at it again on: ____."
- Signatures (child and parent) optional. No points, no rewards, no penalties.

We do not require it and never ask whether a family used it beyond the interview.

## 5. Privacy and consent

**Tell parents (plain words):** we ask for one weekly number and your child's age band only. No child names, no screenshots, no app names, no device access, no tracking. We use it only to write your reply and judge whether this idea is useful. We do not share it with anyone, ever. Joining is optional and you can stop any time.

**Minimal data:** family code (not the child's name), parent contact (already held from the beta), age band, weekly total, optional note.

**Retention:** delete submissions and our tracking sheet 30 days after the test ends, unless the parent opts in to continue. Interview notes: anonymise (family code only) within the same 30 days.

**Withdrawal:** parent says "stop" by WhatsApp or email; we delete their data within 7 days and confirm.

**PDPA basics (Singapore):** get consent for a stated purpose, collect only what is needed, keep it secure (access limited to the owner), retain only as long as needed, honour access and withdrawal requests, no transfer to third parties. Parent provides data about their own child; we collect no data directly from children. Google Form data is stored with Google: say so in the notice. Check the wording with the existing privacy notice in docs/legal/ before launch.

**Opt-in wording draft:**

> I would like to join the Math Inquirers Weekly Family Check-in for 6 weeks. I understand that I will send one number each week (my child's total screen time from my phone's built-in report) and my child's age band. I will not send my child's name or screenshots. Math Inquirers will use this only to reply to me and to decide whether to build a tool like this. My data will not be shared, will be deleted 30 days after the test ends unless I choose to continue, and I can stop at any time by messaging "stop". [ ] I agree.

**Pending owner item:** consent for the weekly puzzle email is still undecided. Until the owner approves it, the weekly reply goes only through WhatsApp/email to parents who ticked this separate opt-in, and nothing is sent without it.

## 6. Running it with almost no work

**Roles.** Owner (or one helper): sends reminder, writes replies, runs interviews. Claude can draft the replies and puzzles for the owner to review and send; nothing is sent automatically.

**Time per family per week:** about 5 minutes (read number, fill template, send). 15 families = about 75 minutes weekly. Parents: 2 minutes.

**Tracking sheet** (one row per family per week):

| family_code | age_band | week | submitted (Y/N) | total_h | prev_total_h | change | reply_sent (date) | puzzle_tried (Y/N/NA) | parent_note | opt_in_date | withdrawn |
|---|---|---|---|---|---|---|---|---|---|---|---|

Summary tab: submitting 3 of 4, still active in week 4, continue yes/no.

**End-of-test parent interview (10 minutes, phone or WhatsApp call):**

1. What did you do with the reply each week?
2. Did anything change at home (conversations, routines, awareness)? What exactly?
3. What was annoying or hard about getting the number?
4. Which part was most useful: the trend, the suggestion, the puzzle, none?
5. Did your child do the puzzles? What did they say?
6. Would you keep doing this? What would make you stop?
7. If an app did the number part for you, would you want it? Why or why not?
8. What do the built-in reports on your phone not tell you that you wish they did?
9. How much would you pay per month, if anything (0 is fine)? Who would you recommend it to?
10. Did anything about it feel uncomfortable (privacy, tone)?

## 7. Decision guide

- **Build a prototype** if at least 4 of the 6 measures hit success and none fail, and interviews show parents want the number step automated. Prototype = a portal page where parents type the number, no device access.
- **Try a different angle** if the puzzle/reply is valued but submission is weak (the number step is the friction), or the number is valued but not the puzzles. Test: puzzles-only weekly, or monthly check-in, or a different audience.
- **Stop** if 3 or more measures fail, or interviews show the built-in reports already suffice and there is no pull. Keep the puzzle content for other use.
- Mixed results: run a second 4-week round with the changes before deciding; do not build.

## 8. What we are not claiming

- No health, sleep, vision, mental-health or developmental claims.
- No claim that screen time causes harm or that any amount is "right"; no benchmarks or "too much" labels.
- No promise that families will reduce screen time; this is awareness only.
- No claim that puzzles replace or counter screen time, or improve school results.
- No monitoring, blocking, or access to the child's device.
