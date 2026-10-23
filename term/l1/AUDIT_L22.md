# Self-audit: Level 1 Term 3 Lesson 2 (Five Minutes at a Time)

Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist. Numbers are from the final build (validator 0 FAIL).

## Automatic checklist

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | schema: passes term/l1/schema/lesson.schema.json |
| Every answer verified independently (verify/l22_checks.py) | PASS | clocks read back from hand angles; durations found by stepping the clock one minute at a time; am and pm from a 24-hour hour; the timetable answer by scanning the start times |
| Online practice variants verified (expression, oracle, runner JS) | PASS | all template variants verified three ways (c1, c2, c5, t1, t2, t3, g1, r2) |
| Timing: parts sum to 90, no part OVER, buffer, slow-class | PASS | script 68:02, slow-class 80:37 after the fix pass (the opening is exactly full in the slow-class model, 2:00 of 2:00; the standing buffer absorbs it), no LOOSE |
| Slides and script linked (each slide once, in its part) | PASS | reveal slides are written by hand so the script controls them |
| Tier counts and completeness | PASS | Start here 6, Think harder 4, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | wording check clean |
| Recording cues short, with child action | PASS | 11 cues, at most 26 words |
| Spare-time menu present | PASS | 3 activities |
| No copied contest text | PASS | no 7-word overlap |
| Mascot used modestly | PASS | Mi on 4 slides |
| Real PDF page count and fill | PASS with note | workbook 6 pages: 99%, 89%, 97%, 90%, 99% (final build); kit page 75% |
| Beyond item named, not at Start here | PASS | Chunk the Gap at G1 to G3 |
| Kit contract | PASS | 8 event cards supplied and used; the clock from the first lesson of Term 3 is reused |
| No template leak | PASS | |
| Hand-off from Lesson 21 | PASS | Lesson 21's `next_materials` asks for the event cards page cut out and the clock kept |

## Judgement lines (author)

- Tier principle: PASS. Start here (6 questions, about 19 modelled minutes) is Primary 1 work only: read three 5-minute clocks as digits, count in 5s to a minute number, draw the hands, a four-option choice with the school distractors (the long-hand number read as minutes, the next hour, digits swapped), am or pm for a morning and an evening event, and who leaves first in the same hour. No quarter word, no "ten past", no am or pm with full stops and no duration appears at Start here (the verify script asserts it). Think harder (4): am and pm with the tricky 12:30, 1 h 20 min, the short hand just before the next hour (3:50 is not 4:50) and a timetable of start times (which show is on, how long to wait). Go further (3): Chunk the Gap, beyond Primary 1 on purpose.
- Non-routine types (owner decision 23 Oct): chunk a gap (compare), a timetable (context) and the hour-hand trap, all at Think harder or Go further, named in `contest_moves`. G1 carries a drawn number line and two scaffold blanks; G2 and G3 do not.
- Age-appropriateness: PASS. One idea (each number is 5 minutes). Explore is 12 minutes with the child's own clock and the 8 event cards before any picture work; the movement break counts in 5s with arm circles; the tutor reads every question aloud.
- Joining cold: PASS. The warm-up claps the count in 5s, re-teaches the two hands with two clocks, and pairs that make 60 on a line. Marked NOT safe to miss (Lesson 23 and the Quest use 5-minute times).
- Safeguarding and privacy: PASS (same block as Lesson 21; loose paper hands, grown-up cuts the cards, small things stay on the table, no paper to the camera, still-stuck route through the look-back page and the business WhatsApp number on the parent page only).
- Pictures and pages: PASS with limits. Viewed all 34 slides, workbook pages 1 to 6, key (3 pages), home sheet, parent page and the kit page. Fixes made while viewing: first builds overflowed the workbook (clocks were sized down); G1's number line labels are small because the figure shrinks custom labels; the Think harder table was enlarged; slide overflows on the minute-reading and am and pm slides were fixed with columns.
- Wording against the P1 papers: digits with colon, am and pm without full stops and with a space, "The ___ show is on.", "Circle am or pm.", choice with bracket. See WORDING_REVIEW_L22.md.

## Instrument A (gifted-style, 0 to 2 each)

1 Low floor, high ceiling: 2. Setting the clock by counting in 5s at the floor; Chunk the Gap and comparing two readers at the ceiling.
2 Depth over speed: 2. Explore is 12 minutes of hands-on work.
3 Generalise: 1. Each number is 5 minutes; the Investigation asks why 12 steps make an hour.
4 Justify: 1. Talk time tests a claim; the Investigation asks why.
5 Multiple paths: 1. Counting in 5s, the clock itself, chunking to the next hour.
6 Challenge ladder: 2. Start here, Think harder, Go further, Investigation, optional slide, spare-time menu.
7 Student-led inquiry: 1. Children test the claim about the 2 and the short hand.
8 Complexity / context: 2. A timetable, a swim, two readers.
9 Problem posing: 1. Spare-time M2 and online g3 (make a Chunk the Gap puzzle).
10 Metacognition: 2. Look-back, tick your own work, check with the clock.
11 Pacing / compacting: 1. Choice page after Start here.
12 Extension, not acceleration: 2. Chunk the Gap deepens the same idea; nothing the next lesson needs is taught.

Total: 18 / 24.

## Known limits

- Never trialled with children; times and difficulty are modelled.
- Shared template items found: the event-card mat prints "a.m. (night" and "p.m. (aftern" because the label is cut at 12 characters (`figs3.event_cards`, `lab[:12]`), and prints a.m. and p.m. with full stops while the Primary 1 papers use am and pm; the deck builder ignores `size` on clocks inside `qs` rows.
- Online rewind: one static item from Lesson 12 and one templated item (Lesson 12 c4) are copied as r1 and r2; a rewind set is not built in the runner.
- The lesson is a new topic in the plan: a tutor should confirm the strand label (flagged in `moe.note`).
- Wording for durations (Chunk the Gap) has no Primary 1 paper behind it; half-hour and 1-hour durations are Primary 1, general durations are Primary 3, so the puzzle stays beyond-syllabus.

## Fix pass (23 Oct 2026, independent audits of 23 Oct)

`audit/FIXES_T3_L22.md` lists every finding and the action. Summary: the false "the short hand waits at the hour" is gone from the objective, titles, script, deck notes, parent summary and parent quote (the short hand creeps; the hour stays the same until the long hand has been all the way round); Explore round 2 has a tutor demonstration because loose paper hands do not creep; event cards now carry times and the sort has a clear answer; the hour-hand trap was moved out of Start here and the exit ticket (S1c 11:10, S6 Ben 6:20, E1 10:15); class, exit, home and online base numbers no longer repeat each other; G1 number line labels are all times; S4 clock changed to 8:25 so the hands are far apart; recording notice said before recording starts; one term-wide rule for "ten past" and "quarter" words. Validator 0 FAIL, 242 answer checks.

Still open, not mine (listed in `audit/FINAL_FIXES_T3.md`): the event-card mat and card gaps, time answer boxes, the half-page exit ticket, deck footers and small exit clocks, runner messages, the "papers to the camera" timing line in `b_guide.py`.
