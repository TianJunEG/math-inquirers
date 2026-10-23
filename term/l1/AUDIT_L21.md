# Self-audit: Level 1 Term 3 Lesson 1 (What Time Is It?)

Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist. Numbers below are from the final build (validator 0 FAIL).

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: passes term/l1/schema/lesson.schema.json |
| Every answer verified independently (verify/l21_checks.py) | PASS | 154 checks; every clock is turned into hand angles and read back, mirrors are reflected angles, orderings use minutes since 12 |
| Online practice variants verified (expression, oracle, runner JS) | PASS | 140 template variants verified three ways |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | script 66:27, slow-class 78:40, no part OVER, no LOOSE warning |
| Slides and script linked (each slide once, in its part) | PASS | every slide shown exactly once; reveal slides are written by hand so the script controls them |
| Tier counts and completeness | PASS | Start here 6, Think harder 3, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording check clean |
| Recording cues short, with child action | PASS | 11 cues, at most 26 words |
| Spare-time menu present | PASS | 3 activities, 11 optional minutes |
| No copied contest text | PASS | no 7-word overlap (two phrases were reworded after hits: "write the time shown on the clock", "the long hand points to the 6") |
| Mascot used modestly | PASS | Mi on 4 slides, no numbers in Mi's lines |
| Real PDF page count and fill | PASS with note | workbook 6 pages, fill 100%, 90%, 99%, 96%, 99%; kit page 64% (a kit page may be short) |
| Beyond item named, not at Start here | PASS | Mirror Clock at G1 to G3 |
| Kit contract | PASS | 2 faces and 6 hands supplied; at most 2 faces and 2 pairs used |
| No template leak | PASS | no other lesson title, no stray "Lesson 1" |
| Hand-off from Lesson 20 | WARN (not mine to fix) | Lesson 20's `next_materials` and goodbye do not mention cutting out the clock page (see Known limits) |

## Judgement lines (author)

- Tier principle: PASS. Start here (6 questions, about 18 modelled minutes) is Primary 1 school work only: read four clocks (o'clock and half past, digits), draw the hands for 4 o'clock, choose the right clock for half past 7, a four-option choice question with the school distractors (same hour other form, the long-hand number read as the hour), order three clocks (earliest and latest) and name the short and long hand. No quarter word and no minute other than 0 and 30 appears (checked by the verify script). Think harder (3) reads quarter past and quarter to by counting in 5s, tests the hour-hand trap at half past (a claim to check) and a true/false table. Go further (3) is the beyond-syllabus Mirror Clock.
- Non-routine types (owner decision 23 Oct): context (the clock in a mirror, the hour-hand trap) and logic (which times look the same in a mirror), all at Think harder or Go further, named in `contest_moves`.
- Age-appropriateness: PASS. One idea (two hands, two jobs). Explore is 13 minutes with the child's own hands on the cut-out clock before any picture work; a movement break uses arms as clock hands; the tutor reads every question aloud.
- Joining cold: PASS. The warm-up claps the count in 5s, goes round the ring of 1 to 12 and shares 6 counters between two plates. A child who has never read a clock can follow. The lesson is marked NOT safe to miss (Lessons 22, 23 and the Quest build on it).
- Safeguarding and privacy: PASS. Main room only; no paper to the camera; tick your own work; still-stuck route through the look-back page and the business WhatsApp (the number is only on the parent page); the recording statement as in the privacy notice; safety line for small items, loose paper hands (no pins) and mirrors; seated option in the movement break. No error-spotter has a cast name ("A child says").
- Pictures and pages: PASS with limits. Viewed all slides (contact sheet and the changed ones at full size), workbook pages 1 to 6, the kit page, key (3 pages), home sheet, home answers, parent page and the first guide pages. Fixes made while viewing: the first workbook build was 10 pages (clocks drawn at full width); clocks were sized, Start here page 1 holds S1 to S3 and page 2 S4 to S6; Think harder dropped a fourth question (a quarter-words choice) because the page overflowed, so quarter words are taught in the mini-lesson and tested in the true/false table; slide overflows were fixed by putting lists and clocks in columns and splitting the page 1 slide in two.
- Wording against the P1 papers (docs/books/p1_school_paper_patterns.md): o'clock and half past with digits; "The time is ___"; draw-the-hand items say "Use a ruler"; choice of clocks, four-option choice with bracket, order three clocks. See WORDING_REVIEW_L21.md.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2. Setting a clock with your hands at the floor; a clock in a mirror at the ceiling.
2 Depth over speed: 2. Explore is 13 minutes of hands-on work; the tutor asks how do you know.
3 Generalise: 1. The long hand on the 12 or the 6 tells o'clock or half past for every hour; the Investigation asks why the short hand sits half way.
4 Justify: 1. Talk time tests a claim with the clock; the Investigation asks why. Written reasons are kept out of Start here.
5 Multiple paths: 1. Counting in 5s, the clock itself, the angle picture in the mirror items.
6 Challenge ladder: 2. Start here, Think harder, Go further, Investigation, optional slide, spare-time menu.
7 Student-led inquiry: 1. Children test the 12 claim and the short hand; Explore is guided.
8 Complexity / context: 1. Bus, waking up and a bathroom mirror.
9 Problem posing: 1. Spare-time M2 and online g3.
10 Metacognition: 2. Look-back, tick your own work, check with the clock.
11 Pacing / compacting: 1. Choice page after Start here; Start here about 18 of 28 minutes.
12 Extension, not acceleration: 2. Mirror Clock and the menu deepen the same idea; nothing the next lesson needs is taught.

Total: 17 / 24 (the rubric asks 18 or more; item 3 and 8 are low by nature of a reading-a-scale lesson. Not forced upward.)

## Known limits

- Never trialled with children; times and difficulty are modelled.
- Lesson 20 hand-off is wrong for this lesson: its `parent.next_materials` says to print the workbook a week before and that a clock is optional; this lesson needs the clock page cut out (2 faces and 6 hands). Reported; `tutor_prep` here tells the tutor what to say.
- Shared template items found: the clock kit page prints "Lay a hour hand" (grammar) and the event-card mat in the next lesson prints "a.m." and "p.m." while the Primary 1 papers use am and pm without full stops; the deck builder ignores `size` on clocks inside `qs` rows; the clock figure at small `size` in the workbook is the only way to fit five or more clocks on a page.
- The mirror pictures show the clock without numerals (a real mirror reverses digits; hiding them keeps the puzzle about left and right).
- Wording for quarter past and quarter to is unverified against school papers (the papers use o'clock and half past only), so those words sit at Think harder and are said as 15 and 45 minutes.
