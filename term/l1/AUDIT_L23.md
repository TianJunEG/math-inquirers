# Self-audit: Level 1 Term 3 Lesson 3 (Time Passes)

Table from the validator results of the final build (`python3 term/l1/tools/validate.py 23`, built files included); judgement lines written by the author after viewing every output. Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist.

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: all top-level keys present; passes `schema/lesson.schema.json` |
| Every answer verified independently (verify/lNN_checks.py) | PASS | verify: 200 answer checks by independent script passed (times recomputed in minutes since midnight, clock pictures and time lines read back from the lesson data) |
| Online practice variants verified (expression, oracle, runner JS) | PASS | practice: 91 template variants verified three ways (expression, brute-force oracle that steps the clock on minute by minute, runner JavaScript calc) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | 2+6+4+11+11+4+32+6+6+3+5 = 90; scripted need 68:54, slow-class 81:30; no part OVER in either model (tightest: mini 10:00 of 11:00, workbook 31:13 of 32:00 slow-class) |
| Slides and script linked (each slide once, in its part) | PASS | link: 30 slides each shown exactly once, all question ids resolve (S6 is shown big on its own slide `s-ws2b` and on the answer slide) |
| Tier counts and completeness (answer, hint, solution, mistakes) | PASS | Start here 6, Think harder 4, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording: no banned labels or claims in child and parent text |
| Recording cues short, with child action | PASS | rec: 11 cues, each at most 26 words, each with an action line |
| Spare-time menu present | PASS | spare: 3 activities, 11 optional minutes (not in the 90 sum) |
| No copied contest text | PASS | copy: no 7-word overlap with docs/sasmo or docs/books |
| Mascot used modestly | PASS | Mi on 4 slides (title, warm-up, look-back, end), short lines, no numbers |
| Beyond item named and not at Start here | PASS | `beyond`: Find the Start at G1 and G2 |
| Kit contract and hand-off | PASS | no new kit page; the clock (2 faces, 3 + 3 hands) is supplied by Term 3 Lesson 1 and the most this lesson uses is 2 faces and 2 + 2 hands; `parent.next_materials` names the 29 play-money pieces, the $1 tokens and the clock |
| Real PDF page count and fill | PASS | outputs: Workbook 5 pages, fill 97%, 92%, 92%, 90%, 99% (measured on the PDF); home sheet 1 page (99%), home answers 1 page, parent page 1 page (89%) |
| No template leak (other lesson titles, Lesson 1 text) | PASS | template leak: none |

Validator: 0 FAIL, 0 WARN (28 checks, built files included). Timing: script 68.9 min of 90, slow-class 81.5 min. Workbook fill measured on the PDF: 97%, 92%, 92%, 90%, 99% (no kit page).

## Judgement lines (author)

- Tier principle: PASS. Start here (6 questions, about 16.5 modelled minutes) is one hour or half an hour later from an o'clock or half past start (draw the hands, read a clock, a story with am, choose the clock, read how long from two clocks, a start-lasts-ends table). Every item is Primary 1 work and uses o'clock and half past only, with every time also written as digits. Think harder (4) is a taught idea in a new setting: the half-hour step that changes the hour (5:30 and half an hour), quarter-time starts (4:15 and 9:45, digits only), finding the start by counting back (one stage, a Primary 1 pattern) and a zoo timetable. Go further (3) is beyond Primary 1 on purpose: a trip in two stages found backwards (1 hour then half an hour, 90 minutes), a time that crosses noon from am to pm, and two starts that share one end. The named beyond item is "Find the Start" (G1, G2); `moe.note`, the guide, the parent page and tutor prep say so plainly and never call the lesson MOE-aligned.
- Age-appropriateness: PASS. One idea (later by an hour or half an hour). Objects first: Explore is 11 minutes on the kit clock before any written time. Start here questions are one command and one picture; the tutor reads every question aloud. Quarter words, "ten past", the 24-hour clock and the word clockwise are kept out of every child page.
- Joining cold: PASS. The warm-up (6 minutes) reads o'clock and half past on three clocks, counts in 5s round the clock and shows a tens jump on a line; none needs an earlier lesson. `safe_to_miss` is false: the Term 3 Quest has a gate on this idea, so a child who misses it does pages 1 and 2 before the Quest. The clock itself comes from the first lesson of Term 3; the lesson says a real clock or a paper plate clock works.
- Safeguarding and privacy: PASS. Main room only, no paper or boards to the camera, tick your own work, fingers and choral answers, still-stuck route via the look-back page and the business WhatsApp (the number is only on the parent page), recording statement as in the privacy notice, loose paper clock hands with no pins, a seated option in the arm-clock break. The wrong claim in Talk time is given to "one child" and "another child", never a cast name.
- Pictures and pages: PASS. Viewed all 5 workbook pages, the answer key, the home sheet and its answers, the parent page, the tutor guide cover and timing pages, and all 30 slides (contact sheets). Fixes made while viewing: page 1 spilled onto an extra page (S3 clock dropped, S1 and S2 clocks scaled), page 3 was squashed (T1 and T2 clocks dropped, times are digits), page 5 spilled its look-back (E1 clock dropped), the Go further time line was unreadable (width 640, shorter labels, "pm" left to the question), the warm-up line had two labels on top of each other, four slides overflowed or touched the footer (sizes; question 6 moved to its own slide), S5 choice words wrapped (shorter stem). Slide pictures never show the answer while the question is asked (answer boxes on the time lines; the filled table is a later slide).

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2. Set the clock one hour later at the floor; a trip in two stages found backwards and a film that crosses noon at the ceiling.
2 Depth over speed: 2. Explore is 11 minutes with the clock; the tutor asks "which hand moved, which stayed" before any rule is said; every answer is checked by moving the hands on.
3 Generalise: 1. One hour later keeps the long hand and the hour changes when the long hand passes 12, tested across several starts; the explicit "is it always true?" test is in the spare-time menu only.
4 Justify: 2. "I know because" in the sneak-peek, a two-children claim in Talk time, "who is right, how could we check", and why all four jobs do not fit in the Investigation; written reasons stay out of Start here.
5 Multiple paths: 2. Clock hands, a time line with jumps and counting 5-minute steps are modelled side by side, and G1 can be solved on the line or by counting back on the clock.
6 Challenge ladder: 2. Start here, Think harder, Go further, Investigation (plan the afternoon), optional slide, spare-time menu.
7 Student-led inquiry: 1. Children find what moves on the clock in Explore, and test the two children in Talk time; the Mini-lesson is guided.
8 Complexity / context: 1. Films, swims, a zoo timetable and a bus trip are simple contexts.
9 Problem posing: 1. Spare-time M2 and online g3 ask for a time puzzle for a grown-up.
10 Metacognition: 1. Check by adding the time on, tick your own work, look-back.
11 Pacing / compacting: 1. Choice page after Start here; Start here is about 16.5 of 32 workbook minutes.
12 Extension, not acceleration: 2. The spare-time menu and Go further deepen the same idea; nothing the next lesson needs is taught.

Total: 18 / 24

## Known limits

- Never trialled with children; times and difficulty are modelled. The slow-class model leaves the mini-lesson exactly at its 11 minutes (10:00), so the second pair on the How long? slide is the first thing to cut (the skip order says so).
- No new kit page: the lesson depends on the cut-out clock from the first lesson of Term 3 (or a real or paper plate clock). If a family has no clock, the arm-clock break and the printed clocks still work but the Explore hands-on rounds are weaker.
- The `table` figure is a thumbnail on a question row of a slide, so question 6 has its own slide; a template change (a wide slot for tables on `qs` rows) would remove the extra slide. Clock figures print at 175 px (46 mm); with three or four clocks on a page the builder tightens spacing, so page 2 is dense. A `size` of 75 to 80 percent was used on pages 1 and 2.
- The Term 3 Quest gate for this lesson (film at 2:30 for half an hour; 1 hour after 5:15) uses a quarter-time start, which the Primary 1 paper patterns place at Think harder or beyond; this lesson keeps 5:15 and the pair 2:30 + half an hour out of its own pages. Suggest 5:30 for the gate.
- The hand-off from Term 3 Lesson 2 (Five Minutes at a Time) is written by another author: it must say "keep your clock". The hand-off from Term 2 Lesson 10 to Term 3 Lesson 1 in `l20.json` still says "print it a week before" and "a toy or real clock (optional)"; it must now say the Term 3 book, the 6 clock hands cut out, and keep the $1 tokens (pre-flight section 5).
- Online practice: g1 (the bus trip) has no picture; every other time item shows its clock for each variant.

## Fix pass (Term 3, 23 Oct 2026)

After the three independent audits (`audit/WORKBOOK_AUDIT_L23.md`, `GUIDE_DECK_AUDIT_L23.md`, `HOME_PARENT_PRACTICE_AUDIT_L23.md`) every Medium finding that sits in lesson data was fixed and the Low ones that were cheap; see `audit/FIXES_T3_L23.md` (finding by finding). Changes that matter for the scores above: exit ticket E1 and E3 now use numbers that the Talk time slide does not touch (the old model answer for Talk time said "8:30 is a whole hour after 7:30", which was the answer to E1); the opening, the camera and microphone lines and the tutor_prep greeting follow the final Term 1 wording; the larger clocks on the How long? and question 4 and 5 slides (question 5 has its own slide); the optional slide no longer repeats G3's structure; slide wording no longer says "quarter" to children or "the hour changes at half past". Instrument A is unchanged by design (16 to 18): no new problem-posing or generalising item was added in a fix pass. Still open and not in lesson data: clock-hand drawing in the shared figure (see `FINAL_FIXES_T3.md`).
