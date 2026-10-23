# Learning record: design spec (draft, 23 Oct 2026)

Status: DESIGN ONLY. Nothing here is built, applied to Supabase, or promised to parents. Owner and a lawyer must confirm the items marked **[OWNER]** and **[LAWYER]**. Nothing here edits lessons, the schema or the live database; the SQL in section 7 is a sketch to review.

Sources read: `docs/pedagogy/term_review.md` (toolbox 2.2, explain ladder 2.4, checking 2.5, mini-check 11, Quest section 9), `docs/pedagogy/holiday_review.md` (Thinking Check 11.1, observation 11.2, parent lines 11.3), `docs/gifted_research.md`, `docs/terms/owner_decisions.md` (Quest, spine, recording, retention), `docs/legal/review.md`, `website/privacy.html`, `portal/supabase/schema.sql` and `policies.sql`, `portal/public/practice.js`, `term/l1/runner/practice.js`.

---

## 0. The idea in one paragraph

Lessons are live (Google Meet, up to 8 children, 90 minutes), so we can see how each child works, not just whether the page is right. We keep a small, structured record of three things the owner has adopted as the spine: (a) which strategy from the toolbox the child chooses, (b) giving a reason (the 5-rung explain ladder), and (c) checking and persistence. Digital answers add pace (time on accurate answers) and accuracy, which show fluency and confidence. The record produces one thing parents see (a short block report in plain words), one thing tutors use (a view that tells them whom to ask what next), and one thing the owner uses (to find out whether the program is working). Time taken on accurate answers (pace) is used as a real measure of fluency and confidence, in short labelled Quick sets only, against the child's own baseline. It never produces a public rank, a score shown to a child, or a prediction.

## 1. Purpose and honest limits

**Purpose.** (1) Tell a parent something specific and true about how their child is growing as a problem solver. (2) Help the tutor notice quiet children and choose the next prompt. (3) Let the owner see, in aggregate and without names, whether the spine is being taught and picked up.

**Honest limits (these also go in the parent report footer and tutor guide).**
- **Growth indicators, not measurements of ability.** The record shows what a child did in the sessions we watched. It does not show what they know in general.
- **Small groups.** Up to 8 children, 10 lessons per block. Any count is anecdotal. We never publish percentages or compare groups (term_review 11.4).
- **Tutor subjectivity.** The same tutor teaches and judges. Ratings are a professional judgement on a 1-5 / yes-no sheet, taken live, and will vary between tutors and days. Section 8 reduces this; it cannot remove it.
- **Not norm-referenced.** There is no population to compare against. Everything is a child against their own earlier self.
- **Not predictive.** The record says nothing about exams, competitions, GEP or any school outcome. No MOE, GEP or SASMO claim, no exam-result promise (gifted_research section 3; owner decisions on the spine).
- **Not causal.** No control group; the course cannot be shown to have caused a change.
- **Observed, not total.** A child is observed 2-4 times per block by rotation. A report line says "in the lessons we watched".
- **Digital capture is partial.** Children answer on their own devices; a slow answer may be a phone call, a sibling, a dropped connection, or thinking. Pace is read together with accuracy, checks and hints (section 3).
- **Today the runner records nothing server-side.** `term/l1/runner/practice.js` keeps only a done flag in the browser's localStorage (`mi-practice-<lesson>`), counts tries in memory, does not count hints, stores no times, and has no child identity. `portal/public/practice.js` is a placeholder. The `practice_attempts` table exists (`child_id`, `lesson_key`, `item_key`, `correct`, `hints_used`) but nothing writes to it. So every digital number in this spec is new build work (phase 1).

## 2. What is captured, by whom, when

### 2.1 Automatic capture from digital activities (the runner)

One row per item per child, written when the item is finished (answered correctly, or the worked solution is shown), plus a partial row if the child leaves. Fields:

| Field | Meaning |
|---|---|
| answer | What was typed or chosen on the final attempt (short text, capped at 200 characters; free text "selfcheck" items are stored as written). |
| correct, first_try_correct | Final result, and whether the first attempt was right. The runner already has the states `ok` and `shown` (shown = the worked solution was revealed after two tries). |
| attempts | 1, 2 (the runner allows two tries, then shows the solution). |
| hints_used | Count of "Give me a hint" presses (not counted today). |
| active_ms | Time the item was on screen AND the tab was visible AND the child interacted within the last 60 s; pauses over 60 s are cut. Capped at 20 minutes. |
| wall_ms | Opened to finished, uncapped except for the same 20-minute ceiling. Kept so a bad `active_ms` can be understood. |
| tier | core / stretch / challenge (already in the item data). |
| tool_chosen | Only on items that ask "Which tool did you use?" (tool cards introduced so far, plus "I just knew" and "I'm not sure"). Optional to answer; skipping is recorded as null, not as a failure. |
| checked | Only on items that ask "Did you check?" (a tick, as in the paper look-back). |
| mode, skill | `mode` is `depth` (untimed) or `fluency` (a labelled Quick set); `skill` is a short tag such as `add-2digit`. Only `fluency` items feed pace (section 3). |
| context | `live` (during a Meet lesson, from a link the tutor shared) or `home` (practice link at home). Live time includes listening to the tutor and is used as context only unless it is in a labelled Quick set (section 3.6). |

Rules for the child's screen, unchanged from the runner's header: **no timer shown, no score, no streak, no leaderboard.** The only change is that time and hints are noted in the background; Quick sets (3.4) are labelled and may be skipped. Because the practice page currently says "There is no score and no timer", the wording must be changed to something true: "We do not show a timer or score. With your parent's agreement we note how long you spend on a question, to understand how you think. It is never used to compare you with anyone." **[OWNER]** to approve that this background timing is acceptable at all (see decision D3).

### 2.2 Quick tutor capture in the live lesson

Per lesson the tutor observes **2-3 children in rotation** (section 3.5 explains the rotation and why it protects quiet children). For each observed child, one capture of six things, taking under 20 seconds:

| Field | Values |
|---|---|
| Tool used | One toolbox tool for that level (Draw it, Act it out, Find the pattern, List every case, Make a table, Work backwards, Guess and check then improve, Try a simpler case; only those introduced so far), or "none visible", plus "named it unprompted: Y/N" |
| Explain rung | 1 Say what I did; 2 Say why it works, with objects or a picture; 3 Test a claim; 4 A reason that covers every case; 5 Pose and defend (rungs from term_review 2.4); or "not observed" |
| Checked | Y / N / not observed (a second method, add back, estimate, example, or checking someone else's working) |
| Persisted | Y / N / not observed (stayed with the problem past the first stuck moment, by trying another way or asking a good question) |
| Prompted? | Unprompted / after a prompt (a single toggle that applies to the whole entry; this is the term_review 11.2 three-word scale "on their own / with a prompt" simplified) |
| Note | One free-text line, 200 characters, describing what was seen or said. Not an opinion about the child ("quiet", "weak" are not allowed in the guide; see 8). |

"Not observed" is a first-class value and is never converted to a low rating.

### 2.3 Mock-up: tutor screen, sized for mid-lesson use

Design for a tablet or second laptop, **never the screen shared into Meet**. Large targets (minimum 48 px), one child at a time, no typing except the optional note, whole entry completable in about six taps. The screen shows only a child's first name, as in the lesson.

```
+--------------------------------------------------------------+
|  Group P3-Sat-10:30     Lesson 4     Tools so far: 3         |
|  Observe next:  [Mei]  [Ravi]  [Siti]    (least recently     |
|                                           seen first)        |
+--------------------------------------------------------------+
|  MEI                                         (seen 1 time)   |
|                                                              |
|  TOOL USED                                                   |
|  [Draw it] [List every case] [Make a table] [None visible]   |
|  Named it unprompted?                 [ Yes ]   [ No ]       |
|                                                              |
|  EXPLAIN RUNG                                                |
|  [1 What I did] [2 Why, with objects] [3 Test it]            |
|  [4 Always, because] [5 Pose + defend]  [Not observed]       |
|                                                              |
|  CHECKED        [ Yes ]  [ No ]  [ Not observed ]            |
|  PERSISTED      [ Yes ]  [ No ]  [ Not observed ]            |
|  PROMPTED?      [ On own ]  [ After a prompt ]               |
|                                                              |
|  Note (optional, 200 chars)  [______________________________]|
|                                                              |
|  [ Save and next child ]                [ Skip, not seen ]   |
+--------------------------------------------------------------+
|  This lesson: Mei saved   Ravi -   Siti -     [Finish lesson]|
+--------------------------------------------------------------+
```

Behaviours: selecting a rung or tool is one tap and stays highlighted; "Save and next child" saves and moves on; an entry can be edited until "Finish lesson" (and for 24 hours after, for the tutor only); the phase-0 paper sheet (section 9) is the same layout on one A5 page per lesson. The screen shows no digital time or accuracy numbers during the lesson; the tutor sees those only after the lesson (section 5.2), so a number does not steer the live rating.

## 3. How TIME (pace) and ACCURACY are used

**Owner correction (23 Oct 2026).** Contests and school exams are timed, and a child who answers accurately and quickly is usually a confident child. So pace is a real measure here, of **fluency and confidence**, alongside the three spine outcomes. It is not a hidden extra and it is not forbidden. What stays forbidden is turning pace into a public rank or a verdict on a child.

**Two honest views, both kept.** `docs/gifted_research.md` rates "depth over speed" as a core design feature (few problems, long think time, rewarding explaining over finishing) and notes that competitions reward speed and accuracy on closed-answer items, while math circles and depth programmes differ. We do not settle that argument. We keep two modes so the data can hold both: **Depth mode** (untimed) and **Fluency mode** (timed, short, labelled). Neither is "the real one". The research note gathered no evidence that speed practice transfers to contest or exam results, and none that it does not; this spec makes no such claim.

### 3.1 Principles
1. **Pace counts only on accurate answers.** Pace = time taken on items answered correctly. Time on wrong answers is read for the quadrant (3.3) but is not "pace".
2. **Two modes, never mixed.** Depth tasks are untimed and are never used for pace. Fluency sets are short, labelled, and are the only items used for a pace statement (3.4).
3. **A child against their own baseline first.** For Levels 4-6, pace is reported as movement against the child's own earlier sets (3.5). Optional indicative target ranges are secondary and are never shown as a pass or fail.
4. **No public leaderboards, no ranking or comparison between children,** on screen, in reports, in exports, or aloud. Group figures go to the owner only as counts, never per child, and only for cohorts of 5 or more (5.3).
5. **Speed is never the headline for a young child, and never praised on its own.** The tutor praises the use of a tool, a check or a reason, and says "quicker" only about a skill, not about the child.
6. **Pace never replaces tutor judgement.** The quadrant is a prompt; the tutor decides what it means for this child on this day.

### 3.2 Depth mode and Fluency mode

| | Depth mode | Fluency mode |
|---|---|---|
| Purpose | Strategy, reasoning, checking, persistence (the spine) | Fluency and confidence on a skill the child already has |
| Items | Think harder, Go further, investigations, the Quest gates | Short closed-answer items on one skill (for example multiplication facts, fractions of a quantity, converting units) |
| Time | Untimed; no timer; think time is protected | Short set, clearly labelled "Quick set"; a soft clock the child can see only if they choose (3.4) |
| Recorded | Tool, rung, checked, persisted, hints, attempts, time kept as context only | Per item: correct, time, first-try, plus the set's skill tag |
| Used for | The three outcomes | Pace on accurate answers, the quadrant, the fluency line in the report |
| Who | All children | All children may do a Quick set; anxious children can opt out (3.6) |

The item field `mode` (`depth` or `fluency`) and `skill` (a short skill tag such as `add-2digit`) are stored on every digital item (section 7). The runner's current rule "no timers, no scores, no streaks, no leaderboard" stays for depth items; Fluency mode needs an explicit change to that header, which the owner has decided for Levels 4-6 only (3.4); D3 still covers the background-timing consent.

### 3.3 The speed-accuracy quadrant (per child, per skill)
"Fast" and "slow" are relative to the child's own baseline for that skill and item type (3.5); until a baseline exists the tutor view shows only accuracy and hints.

| | Fast | Slow |
|---|---|---|
| **Accurate** | **Fluent / confident.** The skill is secure. Offer a Think harder item rather than more of the same. Evidence for fluency and confidence. | **Careful.** Two different stories, told apart with the check and hint data: (a) *persisting*: long time, a check done or a second method tried, few hints, correct: evidence for outcome (c); say "stayed with it". (b) *needs fluency practice*: little checking, steady hesitation across the whole set, hints at the start: a short Quick set on that skill, with an easier entry. |
| **Wrong** | **Rushing.** Prompt to slow down: "How could you check that before you press Check?" Also look for tapping through (many very short, all wrong). | **Needs re-teaching.** Long time, wrong, often with hints: go back to the tool card or an easier item (the item's "Try an easier one first"), not more time. |

Checks on the quadrant: a single item never classifies a child; the quadrant uses at least 6 items on the skill in a set or across 2 lessons. The tutor can mark an item invalid (device problem, interruption). The labels are computed when the tutor opens the view and are not stored as facts about the child.

### 3.4 Quest Sprint (Fluency mode): DECIDED by the owner, 23 Oct 2026
**Decision.** Timed sets are allowed only as an **optional "Quest Sprint" for ages 9-13 (Levels 4, 5 and 6)**. **None for Levels 1-3 for now.** Children aged 6-10 (Levels 1-3, and the younger Level 4 children) get no timed-set experience at all. For them, pace is only background context from ordinary digital items (tutor view, 3.3 note below), never a Sprint result and never a number in a report. Rules that stay: accurate answers only count towards pace; own baseline first, with optional indicative targets that are not exam or contest norms; no leaderboards or ranking; anxious children may opt out; depth tasks stay untimed; online timing is noisy (3.6). This supersedes the earlier proposed age bands and options A-C and closes D12. The owner should still note this changes the earlier "no visible timer" Quest rule for these levels.

**Design of the Sprint.**
- **Where.** The last part of the Challenge Quest at Levels 4-6 (lessons 10, 20, 30, 40), after the gates and never replacing one. It is a separate, clearly marked, optional part, so the rest of the Quest stays a game with no scores.
- **Format.** One short set of 8-10 closed-answer items on one skill the block has taught, about 4-5 minutes, typed or chosen answers (typing is allowed from about age 9; a practice item first). Level 4: 8 items, about 4 minutes. Levels 5-6: 10 items, about 5 minutes.
- **Labelling.** "A Quick set: just to see how smoothly you can do this skill today. It is the only part where time is noted. Press Skip any time." No "test", "exam", "score", "race" or "best time". No time or score shown to the child at the end. A soft clock is visible only if the child chooses it.
- **Opt-out.** A Skip button on screen, a parent switch (a separate consent tick, 8.3), and a tutor option to skip a child without reason. Skipping is recorded as "skipped", never as a low result.
- **What is recorded.** The items are `mode = 'fluency'` with a `skill` tag. Pace is computed from correct answers only (3.5).
- **Younger children (Levels 1-3).** Ordinary digital items are `mode = 'depth'`. Their time is stored as context (3.6). The tutor view may show the quadrant (3.3) as a prompt about an item pattern, but it needs the full caveats, no report line quotes pace, and no timed set is offered.

### 3.5 Pace against the child's own baseline, and optional target ranges
- **Own baseline (primary).** Baseline = the child's own median time on correct answers for that skill and item type in their first Quick set, then their previous two sets as it moves. The report compares the latest set with the child's earlier set ("quicker", "about the same", "slower while checking more"). No flags until there are at least 6 correct items on the skill.
- **Item-type baselines.** Different item types have different overhead (tap vs typing vs handwriting). Baselines are per item type: tap, typed number, several fields, written working. Compare like with like only.
- **Indicative target ranges (secondary, optional, our own).** Derived by the tutor team from the item type, not from a population: time-to-answer is split into (a) a reading time (words in the question), (b) an input time (a tap is about 2 s, a typed 1-2 digit answer about 4 s, a 3-4 digit about 6 s for a child who has settled in; longer for ages 6-8) and (c) a thinking time that depends on the skill. A working range for a single-step item on a secure skill is "reading + input + 3 to 10 seconds of thinking" for Levels 4-6 (the only levels with a Sprint). These are rough starting points to be tuned by observing the first sets; they are **our own indicative targets, not norms, and not a prediction of any contest or exam**. A child above the range is shown nothing; the tutor sees "inside / above range" only to decide whether to offer more of that skill. No range is shown to a parent as a number. No MOE, GEP or SASMO claim is made or implied.
- **Never:** compare a child with another child, with the group median, or with a "typical" child, in any view a parent or child sees.

### 3.6 Measurement caveats (what pace does and does not tell)
- **Online timing is noisy.** It includes typing, mouse or finger accuracy, handwriting transcribed onto the screen, device speed, and network latency; the noise is greatest at ages 6-8 whose typing and mouse control are still developing. Mitigations: no timed sets below Level 4; for the Sprint use choice or short typed items and a practice item; exclude the first 3 seconds of each item (reading and settling) or measure from first interaction; use item-type baselines (3.5); keep only `home` or labelled Quick-set `live` items for pace; drop items flagged invalid; never read pace from fewer than 6 items.
- **Live time is not pace.** Time during a live lesson includes listening to the tutor and answering at the same time as others, and is used as context only unless the item sits in a labelled Quick set.
- **Pressure and anxiety.** A Sprint can make an anxious child worse and teach them that speed is what matters. Mitigations: sets are short, opt-out is a button, the parent can switch Fluency mode off for the child at registration or at any time (the consent in 8.3 has a separate tick), no time or score is shown, no group results are shown, and the tutor may skip a child on the day without a reason. Opt-out is recorded as "skipped", never as a low result. A child who opts out of the Sprint still gets a full report on the three outcomes.
- **Pace is not ability.** Fast does not mean gifted and slow does not mean weak. The report uses the phrase "on this skill, in these sets".
- **Tutor judgement stays final.** The tutor can set any pace statement aside before approval of a report.

### 3.7 What is never used
- Pace or accuracy as a rank, as a total ("minutes spent"), as points, as a streak, or as a leaderboard.
- Time on depth items as pace.
- Accuracy as a percentage shown to a parent or child; the report says what the child could do, in words.
- Comparing speed between children, groups, tutors or channels.

### 3.5 Quiet children
- **Rotation, not volunteers.** The tutor screen lists children least-recently observed first. Every child is observed at least 2 times per block (with 8 children, 3 per lesson, 10 lessons = 30 slots, about 3.75 each; the minimum rule is the guarantee). A lesson-start check shows who has fewer than 2.
- **A quiet child is not a low rung.** Speaking is not required. Rung evidence can come from the child's written one-line reason on paper or the runner's "selfcheck" box, a gesture ("show me, don't tell me", holiday_review 11.2), or a chat message. Cameras off and muted children (the owner's recording default) are still observed through these routes.
- **"Not observed" never counts against a child.** A report built from fewer than 3 observations for an outcome says "we have not seen enough yet to say; we will look closely next block", not a guess.
- **Parent can opt a child out of voice on recordings** (current privacy notice); this does not reduce what the record can say, because the record is written, not from recordings.
- The weekly check for the tutor: any child with no observation in 3 lessons is shown first.

## 4. Start and end mini-checks, and the Challenge Quest

### 4.1 Mini-checks at lesson 1 and lesson 10 of each block
Use the "Thinking Check" (holiday_review 11.1) for the holiday program and the start/end mini-check of term_review 11.1 for term blocks. This spec does not change their content; it only says how they are recorded.
- **Form A in lesson 1 and a parallel Form B in lesson 10,** about 8 minutes, the child's own paper. For a child who first attends later, form A in the first lesson attended, and the report says so.
- Four items, kinds: a find-every-case item, a work-backwards item, a pattern with a far place, a claim to test. The Level 1 term set has three (story solved with a picture, how many ways, claim to test). Forms must be scripted and verified before use (term_review says so).
- Recorded per child, per form: **Started** 0-2 (chose a way in without help), **Reason** 0-2 (said or wrote why), **Checked** 0-2 (did something to test), tool word used, and **answer right / not yet** recorded separately. This is the only place with a 0-2 scale; it is the owner-approved style of the Thinking Check. It is compared with the same child only. **[OWNER]** The Quest privacy checklist forbids "tally, not even in your own notes" and the term review marks any scale as an owner decision (D1). If the owner prefers, store the words "with help / with a prompt / on their own" only.
- The 0-2 values are never shown to parents as numbers. The report says "At the start, Mei needed a prompt to begin; at the end she chose her own tool."
- The free 30-minute placement check (`docs/levels_and_placement.md`) is not reused for this: it is a content check scored out of 10.

### 4.2 How the Challenge Quest contributes
The Quest (lessons 10, 20, 30, 40; "no scores or marks shown, no ranking, no visible timer, no word test") is the richest single observation of the spine. It contributes:
- The Quest v2 elements already proposed in term_review: two mixed gates with no lesson tag and a row of tool pictures to tick, a "Did I check?" tick, a choose-the-tool cave with a "because" line.
- Four tutor prompts in words (term_review 9 and 11.2): tool chosen without a prompt, how they checked, a reason in their own words, and what they did at the stuck moment.
- In this spec those become a **Quest observation**: the same tutor entry as 2.2 (tool, rung, checked, persisted, prompted, note) for **every** child, plus the child's own ticks (tool picture, "I checked") copied from the paper Quest Log. Because the Quest overlaps with lesson 10's mini-check form B, they are one session, not two: Form B sits in the first part and the gates in the second, and the tutor is not asked to rate twice.
- Quest items are not timed digitally and no time is recorded. The Quest remains a game for the child.
- A conflict to settle: the Quest decision says "the tutor keeps private notes only". A structured entry is more than notes. **[OWNER]** (D1).

## 5. Outputs

### 5.1 The parent report, once per block
Short (about 120-170 words), plain words, no numbers, no ranks, no exam language. Fixed structure:
1. **One named strength** (a specific thing seen, with a quote or example if one was captured).
2. **One next step** (a thing for the child to practise, plus a home prompt such as "Which tool did you pick first, and why?").
3. **Growth on the three outcomes in plain words, and a fluency line where a Quick set was done** using only these phrases: tools (starting to / sometimes / often chooses a tool without being asked), reasons (the rung in words, for example "gives a reason with objects"), checking and sticking with it (starting / sometimes / often).
3a. **Fluency line (only for Levels 4-6, only if the child did the Quest Sprint and did not opt out; never a number; none at Levels 1-3).** Examples: "Amira is getting quicker at fraction of a quantity and still checking her answers." / "Daniel answers multiplication facts smoothly; on word problems he is accurate but takes his time, which is fine while he checks." / "Ravi is accurate on the unit-conversion set; we are building speed gently, with no pressure." Levels 1-3 never get this line. If pace is slower than before because the child now checks, the line says so.
4. **A footer:** "This is what [Name] did in the lessons we watched. It is not a score, a ranking, or a prediction of exam results."

The tutor writes and approves each report; the system drafts from the structured entries (rules, not a third-party AI service; see 7.6) and the tutor edits and approves before it is released to the parent (status draft -> approved -> sent).

**Three worked examples (invented children and invented observations).**

*Example A: Level 2, quiet child, evidence mostly written.*
> **Block 1 report for Aisha (Level 2).** Strength: Aisha draws a picture first, and in lesson 6 her bar drawing showed us why the two amounts had to be equal. She does not say much aloud, but her written reasons are clear, for example: "I drew boxes so I could see the same size." Next step: try saying one sentence about why before she writes. At home you could ask: "Which tool did you pick first, and why?" Growth: Aisha now chooses Draw it on her own most of the time, and has started to try List every case when a picture is not enough. She gives reasons with a picture or objects. She checks when reminded and is starting to check on her own. In the lessons we watched, she stayed with hard problems. This is what Aisha did in the lessons we watched. It is not a score, a ranking, or a prediction of exam results.

*Example B: Level 4, fast and eager, not yet checking.*
> **Block 2 report for Daniel (Level 4).** Strength: Daniel works quickly and likes Make a table; in lesson 13 he spotted that a pattern doubled each time and tested it on three more numbers. Next step: pause before pressing Check and decide how he could check, for example by working backwards. At home you could ask: "How could you check that a different way?" Growth: Daniel sometimes chooses a tool without being asked and gives a reason that tests an example. He is starting to check; at the start of the block he did not check unless asked, and at the end he checked a few answers by working backwards. Staying with a hard problem is a growing area: he moved on quickly when the first idea did not work, and next block we will practise trying a second way. This is what Daniel did in the lessons we watched. It is not a score, a ranking, or a prediction of exam results.

*Example C: Level 1, enough evidence for only two outcomes.*
> **Block 1 report for Mei (Level 1).** Strength: Mei stuck with the "how many ways" puzzle in lesson 7 even after her first list missed one, and found the missing way by herself. Next step: say "because" out loud, for example "I know there are no more because...". At home you could ask: "How do you know?" Growth: Mei is starting to choose a tool on her own (she used List every case and Act it out). We saw her give a reason twice and have not seen enough to say more about her reasons yet; we will look closely next block. She checked her work after a prompt and, in the last lessons, sometimes without one. This is what Mei did in the lessons we watched. It is not a score, a ranking, or a prediction of exam results.

Consistency checks before a report can be approved: at least 3 observations per outcome (else the "not enough yet" phrase is forced), no adjectives about the child's character, no comparison words ("best", "ahead", "behind", "top"), no numbers or percentages (pace is words against the child's own earlier set).

### 5.2 The tutor view
After a lesson and before the next, per group (only the tutor's own groups):
- The seen-count per child ("Mei: 3 observations; Ravi: 1") with the least-observed first.
- The prompts from 3.2, by child, from the last lesson's digital items.
- Each child's recent entries as a timeline of words (tool, rung, checked, persisted, note), their start-of-block mini-check, and "suggested prompt for next lesson".
- No ranking of children, no per-group league table.

### 5.3 The owner view
- Fidelity: for each group and lesson, how many observations were taken and by whom, and the share of children seen at least twice per block (is the system being used?).
- Rubric reliability (section 8): the results of calibration sessions, and where two tutors differ.
- Aggregate direction: for each block, the number of children whose report phrases moved up on each outcome ("starting" to "sometimes"), shown only for cohorts of at least 5 children, without names, and never as a claim about the course causing growth.
- Reports awaiting tutor approval, deletion and export requests, retention-clock list (what is due for deletion).
- No child-level numbers except to open one child's full record to answer a parent's access request.

## 6. Online vs face-to-face

The product today is live online groups (Google Meet). Face-to-face is a possible future or pilot channel; the owner's answer to "online, face-to-face, or both?" is: **design channel-neutral, pilot online first, test the paper rubric face-to-face in a small separate pilot.**

### 6.1 What stays identical in both channels
The three outcomes, the toolbox and explain ladder, the tutor rubric and the same one-page sheet (paper or screen), the rotation rule, the mini-checks, the Quest observation, the parent report format, the retention and consent rules, and the principle that time and accuracy never become a score.

### 6.2 What can be captured in each

| | Online (Google Meet + runner) | Face-to-face |
|---|---|---|
| Tutor observation (tool, rung, checked, persisted, note) | Yes. Tutor sees faces if cameras on; relies on voice, chat, shared answer slides. Quiet or camera-off children are harder to see, so written and runner evidence matter more. | Yes, and easier to see working on paper, gestures, and who stalls. Small risk of tutor attention being pulled to the loudest child. |
| Accuracy | Automatic from runner (per item, attempts, hints); also marked photos. | Only from marked paper (tutor marks after the lesson), or if tablets/laptops are provided. |
| Time taken (pace) | Automatic (`active_ms`) in labelled Quick sets, with the caveats in section 3.6. | No reliable time without devices. A stopwatch or tutor estimate is possible for a paper Quick set (the tutor times the set as a whole, not a child) but is a weak measure; record "no pace" otherwise and do not infer it. |
| Hints used | Automatic. | Count of hint cards taken, if hint cards are used (cheap). |
| Tool chosen / checked tick | Runner asks; paper look-back copy via parent photo to the business WhatsApp (existing route). | The child's paper look-back is simply collected in class. |
| Mini-checks and Quest | Paper at home, photographed by parent via business WhatsApp; the tutor sees the child during. | Paper in the room, tutor sees the whole process; best case for the "persistence" evidence. |
| Recording | Meet recording (test on 4 Nov decides what it shows). | No recording by default; any CCTV, photos or video need a separate consent. |

### 6.3 What differs
- **Evidence of persistence:** face-to-face gives a better view of the stuck moment; online gives time data but at the cost of device noise.
- **Evidence of explaining:** online favours children who type or speak; face-to-face favours speakers but allows pointing and showing.
- **Privacy:** online adds a child login, stored answers and timings on Supabase; face-to-face with paper stores only tutor sheets and marked work. The privacy notice and consent differ (online needs the timing consent; face-to-face needs paper-handling and retention of marked work).
- **Cost:** online digital capture needs build (section 9); face-to-face paper needs only printing and training. A tablet/laptop plan would repeat the online build with extra hardware and supervision.

### 6.4 Recommended pilots
1. **Pilot 1, online (the November beta onward):** phase 0 paper/Google-Form tutor sheet, then phase 1 digital capture, phase 2 tutor screen and report. One or two groups per level.
2. **Pilot 2, small face-to-face, paper only:** one group of up to 8, one block, with the **same paper tutor sheet** and marked work, and **no time or digital capture at all**. Its question is whether the rubric and report work without the technology, and whether tutors rate the same way on paper.
3. **What to compare** (always as methods, never as children or groups ranked): (i) share of children with enough observations per outcome, (ii) tutor time per lesson spent on the sheet, (iii) inter-tutor agreement after calibration (section 8), (iv) share of reports that needed the "not enough seen" phrase, (v) parent comprehension and usefulness of the report (a two-question reply), (vi) what the digital data added beyond the tutor sheet, answered by the tutor ("did time or accuracy change what you asked a child?"), and (vii) a plain cost per child. Pace is not available face-to-face, so do not compare it across channels. Do not compare children's outcomes across the two channels: groups, tutors, and families differ and numbers are small.

### 6.5 What the owner must tell me about any face-to-face plan
Where and how often; group size; who the tutors are and whether they are the same as online; device policy (any child devices at all); who may take photos and whether marked work is kept or returned; the venue's own data rules (a school or community centre); the target levels; whether recording or CCTV exists; whether the fee, terms, and MOE/private education registration are affected (the legal review already flags MOE registration for 10 or more persons; confirm for face-to-face, which this spec does not assume). Until then this document does not cover face-to-face consent wording beyond the principles above.

## 7. Data model proposal (Supabase). SQL SKETCH, NOT APPLIED.

Principles: a child's learning rows hang off `children(id) on delete cascade`, so the existing `delete_my_data()` and `delete_child` remove them. Tutors need a new role: today there is only `admins`. Tutors never receive parent contact, payment or PIN data. All writes go through `SECURITY DEFINER` functions that check `auth.uid()`, like the rest of the portal. Run only after review; it needs a new migration file (for example `portal/supabase/learning_record.sql`) and testing on a Supabase branch. Verify names against the current schema before use.

### 7.1 People and sessions
```sql
-- New consent type (consents.consent_type is a CHECK list in schema.sql; must be altered)
-- alter table public.consents drop constraint consents_consent_type_check;
-- alter table public.consents add constraint consents_consent_type_check
--   check (consent_type in ('contact','terms','recording','childs_work','feedback_quotes','learning_record'));

create table public.tutors (
  user_id      uuid primary key,              -- auth.users id; insert by hand like admins
  display_name text not null,
  active       boolean not null default true,
  created_at   timestamptz not null default now()
);
create table public.tutor_groups (
  tutor_id uuid not null references public.tutors(user_id) on delete cascade,
  group_id text not null references public.groups(id),
  primary key (tutor_id, group_id)
);
create table public.lesson_sessions (            -- one row per group per lesson held
  id         uuid primary key default gen_random_uuid(),
  group_id   text not null references public.groups(id),
  lesson_no  smallint not null check (lesson_no between 1 and 40),
  block_no   smallint not null check (block_no between 1 and 4),
  held_on    date not null,
  tutor_id   uuid references public.tutors(user_id),
  unique (group_id, lesson_no)
);
```

### 7.2 Helper functions (RLS building blocks)
```sql
create or replace function public.is_tutor() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.tutors where user_id = auth.uid() and active);
$$;

-- The tutor may see a child only if the child has a non-cancelled enrolment in one of the tutor's groups,
-- and only while the group is active (so a tutor loses access when the group ends).
create or replace function public.tutor_can_see_child(p_child uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (
    select 1
      from public.tutor_groups tg
      join public.groups g      on g.id = tg.group_id and g.active
      join public.enrolments e  on e.group_id = tg.group_id and e.status <> 'cancelled'
     where tg.tutor_id = auth.uid() and e.child_id = p_child);
$$;

create or replace function public.parent_owns_child(p_child uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.children c where c.id = p_child and c.parent_id = auth.uid());
$$;
```

### 7.3 Digital item events (extends the unused `practice_attempts`)
```sql
create table public.item_events (
  id               uuid primary key default gen_random_uuid(),
  child_id         uuid not null references public.children(id) on delete cascade,
  session_id       uuid references public.lesson_sessions(id) on delete set null,
  lesson_key       text not null,                 -- same keys as the runner (e.g. 'l1-t1-l03')
  item_key         text not null,
  tier             text check (tier in ('core','stretch','challenge')),
  context          text not null check (context in ('live','home')),
  answer           text check (answer is null or char_length(answer) <= 200),
  correct          boolean,
  first_try_correct boolean,
  attempts         smallint not null default 1 check (attempts between 1 and 3),
  hints_used       smallint not null default 0 check (hints_used between 0 and 20),
  mode             text not null default 'depth' check (mode in ('depth','fluency')),
  skill            text,                           -- e.g. 'add-2digit'; used for the quadrant and pace
  item_type        text check (item_type in ('tap','typed','fields','written')),
  active_ms        int check (active_ms is null or active_ms between 0 and 1200000),
  wall_ms          int check (wall_ms is null or wall_ms between 0 and 1200000),
  tool_chosen      text,                           -- tool id, 'knew', 'unsure', or null (not asked/skipped)
  checked          boolean,                        -- null = not asked
  invalid          boolean not null default false, -- tutor can mark (device problem)
  created_at       timestamptz not null default now()
);
create index item_events_child_idx on public.item_events (child_id, created_at desc);
```

### 7.4 Tutor observations, mini-checks, Quest, reports
```sql
create table public.observations (
  id          uuid primary key default gen_random_uuid(),
  child_id    uuid not null references public.children(id) on delete cascade,
  session_id  uuid not null references public.lesson_sessions(id) on delete cascade,
  tutor_id    uuid not null references public.tutors(user_id),
  tool_id     text,                                     -- null = none visible
  tool_named  boolean,
  explain_rung smallint check (explain_rung between 1 and 5),   -- null = not observed
  checked     text check (checked in ('yes','no','not_observed')),
  persisted   text check (persisted in ('yes','no','not_observed')),
  prompted    text check (prompted in ('own','prompted')),
  note        text check (note is null or char_length(note) <= 200),
  is_quest    boolean not null default false,
  observed_at timestamptz not null default now(),
  unique (child_id, session_id, is_quest)
);

create table public.mini_checks (
  id         uuid primary key default gen_random_uuid(),
  child_id   uuid not null references public.children(id) on delete cascade,
  session_id uuid not null references public.lesson_sessions(id) on delete cascade,
  form       text not null check (form in ('A','B')),
  started    smallint check (started between 0 and 2),   -- OWNER decision D1: or replace by words
  reason     smallint check (reason between 0 and 2),
  checked    smallint check (checked between 0 and 2),
  tool_word  text,
  answer_status text check (answer_status in ('right','not_yet')),
  unique (child_id, session_id, form)
);

create table public.block_reports (
  id          uuid primary key default gen_random_uuid(),
  child_id    uuid not null references public.children(id) on delete cascade,
  group_id    text not null references public.groups(id),
  block_no    smallint not null,
  strength    text not null check (char_length(strength) <= 500),
  next_step   text not null check (char_length(next_step) <= 500),
  growth      jsonb not null,    -- {"tools":"sometimes","reasons":"rung 2","checking":"starting","fluency":{"skill":"add-2digit","pace":"quicker"},"evidence":{...}}; fluency optional
  status      text not null default 'draft' check (status in ('draft','approved','sent')),
  approved_by uuid references public.tutors(user_id),
  approved_at timestamptz,
  created_at  timestamptz not null default now(),
  unique (child_id, group_id, block_no)
);
```

### 7.5 Row level security: who sees what
```sql
alter table public.tutors, public.tutor_groups, public.lesson_sessions, public.item_events,
            public.observations, public.mini_checks, public.block_reports enable row level security;
-- as in policies.sql: revoke all from anon, authenticated first, then grant narrowly.

-- Parents: only their own child. Raw events are readable by the parent (access right under the PDPA).
create policy ev_parent  on public.item_events  for select to authenticated using (public.parent_owns_child(child_id));
create policy ev_tutor   on public.item_events  for select to authenticated using (public.is_tutor() and public.tutor_can_see_child(child_id));
create policy ev_admin   on public.item_events  for select to authenticated using (public.is_admin());

-- Observations and mini-checks: tutor notes may name other children and are TUTOR/OWNER only.
-- A parent does NOT read raw tutor notes; the parent sees the approved report. An access request is answered
-- by export_child_record() (7.7), which gives the parent that child's own entries only.
create policy obs_tutor  on public.observations for select to authenticated using (public.is_tutor() and public.tutor_can_see_child(child_id));
create policy obs_admin  on public.observations for select to authenticated using (public.is_admin());
create policy mc_tutor   on public.mini_checks   for select to authenticated using (public.is_tutor() and public.tutor_can_see_child(child_id));
create policy mc_admin   on public.mini_checks   for select to authenticated using (public.is_admin());

-- Reports: parents see only SENT reports for their own child; tutors see reports for their groups.
create policy rep_parent on public.block_reports for select to authenticated
  using (status = 'sent' and public.parent_owns_child(child_id));
create policy rep_tutor  on public.block_reports for select to authenticated
  using (public.is_tutor() and exists (select 1 from public.tutor_groups tg where tg.tutor_id = auth.uid() and tg.group_id = block_reports.group_id));
create policy rep_admin  on public.block_reports for select to authenticated using (public.is_admin());

-- Tutors get a roster view with first name and level only (no parent id, email, phone, payment).
create view public.tutor_roster with (security_invoker = false) as
  select e.group_id, c.id as child_id, c.display_name, c.level
    from public.enrolments e join public.children c on c.id = e.child_id
   where e.status <> 'cancelled' and public.is_tutor()
     and exists (select 1 from public.tutor_groups tg where tg.tutor_id = auth.uid() and tg.group_id = e.group_id);
-- No direct INSERT/UPDATE/DELETE grants on any of these tables. Writes only via the functions below.
```

### 7.6 Write functions (sketch)
```sql
-- Tutor: record or edit an observation. Checks the tutor-child link and the session's group.
create or replace function public.record_observation(
  p_child uuid, p_session uuid, p_tool text, p_named boolean, p_rung smallint,
  p_checked text, p_persisted text, p_prompted text, p_note text, p_quest boolean default false)
returns uuid language plpgsql security definer set search_path = public as $$
declare oid uuid;
begin
  if not public.is_tutor() or not public.tutor_can_see_child(p_child) then raise exception 'forbidden'; end if;
  if not exists (select 1 from public.lesson_sessions s join public.tutor_groups tg on tg.group_id = s.group_id
                  where s.id = p_session and tg.tutor_id = auth.uid()) then raise exception 'forbidden'; end if;
  insert into public.observations (child_id, session_id, tutor_id, tool_id, tool_named, explain_rung, checked, persisted, prompted, note, is_quest)
  values (p_child, p_session, auth.uid(), p_tool, p_named, p_rung, p_checked, p_persisted, p_prompted, left(p_note, 200), p_quest)
  on conflict (child_id, session_id, is_quest) do update
    set tool_id = excluded.tool_id, tool_named = excluded.tool_named, explain_rung = excluded.explain_rung,
        checked = excluded.checked, persisted = excluded.persisted, prompted = excluded.prompted, note = excluded.note
  returning id into oid;
  return oid;
end $$;

-- Child: log one item. The child has no Supabase auth user (family code + name + PIN), so this is called
-- by an Edge Function that has verified the PIN session; it is NOT granted to anon/authenticated.
-- create or replace function public.log_item_event(p_child uuid, p_payload jsonb) returns void ... ;
-- (service role only; validates ranges and the child's consent_type 'learning_record'; drops timing fields if no consent; fluency items also need the separate fluency consent.)

-- Parents' consent gate: timing and tool fields are written only if the latest 'learning_record' consent is granted.
```

Drafting reports (7.6a): the system fills the report template from structured entries by fixed rules. **No third-party AI service processes any child data** unless the owner decides otherwise and the privacy notice names it (otherwise this is a new disclosure). **[OWNER]** D6.

### 7.7 Retention, deletion, export (defaults, **[OWNER]** and **[LAWYER]** to confirm)
| Data | Proposed retention |
|---|---|
| Raw item events (answer, time, hints) | 90 days after the child's last lesson in the program, then deleted. (Matches the privacy notice's "answers to practice questions ... 90 days after the program ends".) |
| Tutor observations and notes, mini-check rows | 90 days after the child's last lesson, then deleted. A child still enrolled keeps the earlier blocks so baselines work. |
| Parent block report (the text the parent received) | 12 months after the child's last lesson (so the family can keep reading it), then deleted. The family can download it any time. |
| Aggregates for the owner (counts, no child id, no group id, cohorts of 5 or more) | Kept; contain no personal data. [LAWYER] to confirm they are truly anonymised. |
| Backups | Follow the Supabase backup window; note it in the notice. |

Mechanics: a nightly scheduled job (or a calendar reminder during the beta) deletes rows past retention; the `deletion_requests` pattern already exists. `delete_my_data()` deletes `children`, so all learning rows cascade. A "delete my child's learning record only" function should also exist (delete the learning rows but keep the enrolment). **Export:** `export_child_record(p_child)` (parent or admin) returns JSON of that child's events, that child's observation fields and notes (with other children's names removed), mini-check results, and reports; parents get it as a download within the PDPA 30-day window. Tutor free-text is therefore written knowing a parent could read it (guide section 8.4).

## 8. Privacy and legal (all drafts; **[LAWYER]** to confirm)

### 8.1 What the law and the existing notice require
- PDPA: parent or guardian gives consent for a child under 13; PDPC guidance (2024) treats under-18s as children and covers tech-aided learning. Purposes must be notified, consent obtained, data used only for those purposes, retained no longer than needed, and parents have access and correction rights (legal/review.md section 1.2). Do not collect directly from children; the child login stays a first name and a PIN.
- The current privacy page already covers "photos of your child's work, answers to practice questions and short progress notes ... to give your child feedback, show you how they are doing and improve the lessons", kept 90 days after the program ends, seen only by the family and the tutor. **It does not mention** time taken, hints, tutor ratings on a scale of 1-5, or per-child reports kept 12 months, so those need new wording and a decision on consent before capture starts.
- Providers: Supabase (the privacy notice says data may be outside Singapore; confirm the Singapore region) and Google (Meet, Drive). Nothing in this design shares data with any further third party.

### 8.2 Purpose limitation (to put in the notice)
The learning record is used only to (1) write the parent's report, (2) help the tutor choose prompts and group activities, (3) improve the lessons using anonymous totals. It is **not** used for placement or admission decisions, pricing, marketing, advertising, selling, ranking children, training any model, or any purpose outside the program. The business never shares it with schools, other families or third parties.

### 8.3 Draft consent wording
Registration form (a separate optional tick, recorded as `consent_type = 'learning_record'` with the terms and privacy versions, like the existing consents):
> "I agree that Math Inquirers may record how my child works in lessons, for my child's progress report: the tutor's short notes and ratings of the strategies my child uses, giving reasons and checking; and, on online practice, how long my child spends on a question, the answers, hints and tries. This is used only to write my child's report, help the tutor, and improve the lessons using totals that do not name anyone. It is never used to rank or compare children, is not shared with anyone else, and is deleted as described in the privacy notice. If I do not agree, my child is taught in the same way, and the report is written from my child's work and the tutor's notes only. I can change my mind at any time."

Privacy page: add rows to "What we collect, and why" (time taken, hints, tries and answers on online practice; tutor notes and ratings of strategies; mini-check forms; progress reports), the retention rows in 7.7, and "Who can see it": "Your child's tutor and our staff who prepare reports, and you. Not other families." Add the "never used to rank or compare children; never used for placement, pricing or marketing" sentence, and a line that you can ask for a copy of your child's learning record. Replace "answers to practice questions and short progress notes ... 90 days" with the new rows so the page is one consistent list. The practice page sentence in 2.1 must be added to the runner.

### 8.4 What must be said to parents
That time is noted in the background; that tutors rate strategies on a rubric live and a child is not observed every lesson; what the report is and is not; who sees it; how long it is kept; that they can see, correct, or delete it; the contact (DPO; the legal review notes the public contact is still a personal Gmail to be replaced); and that notes could be read by the parent when exported, so they are factual.

### 8.5 Google Meet recording test on 4 Nov
The test decides what a recording contains and so what the notice may say about it. It is separate from the learning record, and this spec adds three things to check in that test:
1. That the **tutor's observation screen is never in the recording or the shared screen** (use a second device or separate window, and confirm that only the presented tab is captured).
2. Whether **chat messages and typed answers** appear in the recording; if so, children should not type reasons into Meet chat. Use the runner or paper instead.
3. Whether a child's tile or voice appears. The standing wording (tutor, shared screen, anyone's unmuted voice) applies; cameras off and mute remain allowed.
Do **not** rate children from the recording afterwards as a routine: that would create a second use of recordings, whose purpose is catch-up and which are deleted 30 days after the last lesson, while the learning record has its own rules. The record is created live.

### 8.6 Security
Tutor accounts use individual logins (no shared password); tutor RLS is limited to current groups; export and admin access are logged; tutors agree in the tutor agreement not to screenshot or copy records and not to use personal phones. A "wrong parent sees another child's report" case is added to the breach plan (legal/review.md).

## 9. Tutor guide: rating consistently

### 9.1 Rubric (observe-describe-then-rate)
Rate what you saw in the last 2-3 minutes with that child. If you did not see it, mark "not observed". Do not rate personality.

**Tool used.** A tool counts when the child's working shows it (a drawing for Draw it; a systematic list for List every case; a table with headings for Make a table), even if they did not name it. "Named it" counts only when the child said or ticked the tool word.

**Explain ladder (pick the highest rung clearly shown, not the average).**

| Rung | Look for | Example, early band (Levels 1-2) | Example, middle band (Levels 3-4) | Example, upper band (Levels 5-6) |
|---|---|---|---|---|
| 1 Say what I did | Steps in order, no "why" | "I put 5 here and then 3 more." | "First I multiplied, then I took away." | "I found the area, then subtracted the hole." |
| 2 Say why it works, with objects or a picture | A because that points at the picture or objects | "I know because I counted the counters." | "The bar is split into 4 equal parts, so each part is 12." | "Folding the net shows two faces are the same." |
| 3 Test a claim | Tries an example to test, or finds a counterexample | "Add 1 to 3 gives 4, so it is not always odd." | "I tried 12 and 15; both fit, but 21 does not." | "I tested the rule with a small case and an extreme case." |
| 4 A reason that covers every case | "Always, because" in one sentence, not an example | "Odd numbers have one left over, so two odds make an even." | "Every multiple of 9 has digits adding to 9 because ..." | "The sum stays the same because each swap adds and removes the same amount." |
| 5 Pose and defend | Makes a problem with one answer and defends it | "I made a puzzle: I have 7 sweets and ... the answer is 4." | "My problem has one answer because the clues fix the number." | "I wrote a problem and showed why no other answer works." |

Level bands note typical Level and rung (term_review 2.4): Level 1 mostly rungs 1-3; Level 2 rungs 2-3; Levels 4-6 rung 4. A rung is judged against the child's own previous rung, not the level's typical rung; do not mark "low" because it is below typical.

**Checked** = yes only if the child did something to test (second method, add back, estimate with "about", an example, or checked someone else's working) and not just "looked again". **Persisted** = yes if they stayed past the first stuck moment by trying another way or asking a good question; asking for the answer straight away is "no"; waiting silently for the tutor is "no" with a prompt.

### 9.2 Rules
1. Rate the **highest rung clearly shown**, and prefer "not observed" to guessing.
2. A prompt lowers "own" status, not the rung: record the rung and mark **prompted**.
3. A quiet child can show rung evidence in writing; look at the page before rating.
4. Notes describe what was said or done, in 200 characters, e.g. "Drew 3 boxes then wrote 'same size so equal'". No labels ("lazy", "shy", "gifted", "weak").
5. Notes may be read by the parent through an access request: write what you would be happy to show them.
6. Never compare children in notes or aloud.
7. Never rate from time or accuracy alone; if a child got it right fast, that is not evidence of anything on the ladder.

### 9.3 Training and calibration
- Training time (proposal): 2 hours first time (45 min on the rubric, 45 min rating three recorded or scripted clips, 30 min on the screen and notes), then 45 minutes before each block (re-calibrate on three shared clips), then a 20-minute check after lesson 3.
- Calibration: two tutors (or tutor and owner) independently rate the same scripted clips; agree within one rung or the same yes/no on at least 80% of clips before live use. If lower, redraw the rubric examples. Scripted clips (not real children) avoid creating extra child data; real recordings need consent and are not recommended.
- Record the agreement as a number for the owner view, not per tutor ranking.
- Ongoing: once per block, the tutor reviews two of their own entries against the rubric with the owner.

## 10. Build plan, effort, risks, decisions

### 10.1 Phases (effort estimates are rough single-developer days; the owner has said many routine steps are done by the assistant, so these are planning numbers only)

| Phase | What | Effort | Needs |
|---|---|---|---|
| 0 (November beta) | Paper tutor sheet (A5, same layout as 2.3) or a Google Form with the same fields, one response per child per lesson; tutor-written paper report from a template; mini-check forms A and B on paper (to be scripted and verified); rubric and calibration clips. No digital timing. | 3-4 days (sheet, form, forms A/B scripting, rubric, tutor training material) plus 2 h tutor training | Owner approval of D1, D2; privacy page wording for tutor notes (the existing "short progress notes" row covers it, but the new rating wording should still be added) |
| 1 (after the beta, before first term) | Runner logs to portal: child login in the runner, `item_events` write via Edge Function, hints counter, active-time timer, optional "which tool" and "did you check" items, consent gating; privacy and runner wording; retention job. | 8-12 days (runner changes 3-4, Edge Function and schema 3-4, consent and notice 1-2, tests and RLS review 2) | Consent decision D3; privacy changes live before any capture; Supabase on the Singapore region |
| 2 | Tutor screen (mock-up 2.3), tutor roster view and RLS, rotation logic, tutor view, report drafting and approval, parent report page in the portal, owner view, export function. | 15-20 days (tutor screen 4-5, RLS and tests 3, rotation and prompts 2, report generator and approval 3-4, parent page 2, owner view 2-3) | Phases 0-1 results, a test group, lawyer review of the notice |

### 10.2 Risks
- **Speed becomes the message.** Pace is a real measure now, so tutors and parents may start to praise speed on its own. Mitigation: two modes, own-baseline reporting, young-child limits, no time on the live screen, rules 3.1/3.7, tutor guide.
- **Anxiety from timed sets** and noisy online timing: opt-out, no timed sets below Level 4, the Sprint labelled and short (3.4, 3.6).
- **Tutor rating noise and halo effects.** Calibration, "not observed", report wording limits; honest footer.
- **Quiet children under-observed.** Rotation, minimum count, written evidence route.
- **Over-claiming.** Report footer and website language: no exam, GEP, MOE or SASMO claims; never "measures ability".
- **Privacy drift.** New data (time, ratings) needs new consent text before capture; the notice must match what is stored (a Meet recording claim already needed correcting; the same applies here).
- **Workload.** 2-3 observations per lesson plus reports must fit in a 90-minute lesson with up to 8 children; test in phase 0 and drop fields if the sheet takes more than 20 seconds per child.
- **Small numbers.** No percentages, no cross-group claims; owner view limited to cohorts of 5 or more.
- **Quest conflict.** The Quest decision forbids tallies in notes; a structured entry may conflict.
- **Child devices at lesson time.** Reliable digital capture needs a second screen or a switch between Meet and the runner; weak devices make time data noisy.
- **Technical.** Runner is static with no child identity; adding it changes a "no account" feature. Keep the runner usable without login (no capture) so the free practice link still works.

### 10.3 Decisions the owner must make
| # | Decision | Recommended default |
|---|---|---|
| D1 | Structured tutor entries and the 0-2 mini-check lines vs "notes in words only" (the Quest checklist forbids tallies). | Allow the structured entry (categories, not tallies); use 0-2 only in the two mini-checks, words everywhere else. Record this as superseding the "private notes only" line for the Quest. |
| D2 | Phase 0 in the beta: yes or no, and paper or Google Form. | Yes, paper sheet; copy to a private Form after the lesson if the tutor wants. |
| D3 | Is background timing of online practice acceptable, and as optional or required consent? Pace in Fluency mode only? | Optional consent; no timing stored without it; pace used only from labelled Quick sets. |
| D4 | Retention periods in 7.7. | As proposed; lawyer to confirm. |
| D5 | Rotation target (every child seen at least twice per block). | Yes. |
| D6 | No third-party AI service for report drafting. | None, rules and tutor edit. |
| D7 | Whether the parent report is released automatically after tutor approval or held until the owner has read it (for the first two blocks). | Owner reads the first two blocks. |
| D8 | Parent may read raw tutor notes on request (access right), or only via export. | Export on request only. |
| D9 | Face-to-face pilot: go or not, and the details in section 6.5. | Not before the online pilot; paper only. |
| D10 | Public DPO contact (a business email or WhatsApp) before any of this goes live. | Required (legal review P1). |
| D12 | DECIDED (23 Oct 2026): optional Quest Sprint for Levels 4-6 only; none for Levels 1-3 for now. Still to confirm: Sprint length, the skill chosen per block, the visible-clock option. | As in 3.4. |
| D11 | Who develops the scripts for forms A/B per level and who owns calibration. | Assistant drafts, owner approves. |

## 11. Not in this document
No lesson, schema or Supabase change has been made. No claim here is tested; the thresholds in 3.3 (1.5x and 0.5x of a child's own median), the retention periods and the effort estimates are proposals to be tried in phases 0 and 1 and revised.
