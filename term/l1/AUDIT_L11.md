# Self-audit: Level 1 Term 2 Lesson 1 (Who Is Where?, lesson 11)

Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist, Term 1 round-2 audit lessons (`audit/TERM_WIDE_AUDIT.md`, `FIXES2_L*.md`). Replaces the stub audit.

## Automatic checklist (validator, last build)

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | all top-level keys, schema 2020-12, identity term 2 / lesson 11 / lesson_in_term 1 / key t2l11 |
| Every answer verified independently | PASS | 86 checks in `verify/l11_checks.py` (lines modelled as lists; the seating puzzle and the race solved by trying every arrangement, exactly one fits) |
| Online practice variants verified | PASS | 62 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, buffer | PASS | 11 parts, sum 90; script 72:08 of 90:00; slow-class 85:10 (Explore 13 min, Mini 11 min) |
| Slides and script linked | PASS | 35 slides each shown once (4 reveal/check slides added: Explore round 2, from-the-back check, two previews), in its part; goodbye slide is last |
| Tier counts and completeness | PASS | Start here 7, Think harder 4, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | no banned labels; no MOE/GEP/SASMO claim |
| Recording cues | PASS | 11 cues of at most 26 words, each with an action |
| Spare-time menu | PASS | 3 activities, 11 optional minutes, rules present |
| No copied contest text | PASS | no 7-word overlap (one overlap, "the child in the middle of the", was reworded) |
| Mascot | PASS | Mi on 4 slides (title, Remember, Look-back, end) |
| Workbook page fill | PASS | measured on the PDF: 99, 99, 98, 93, 98 percent, kit page 49 percent; 6 pages as designed; home 2 pages, parent 1 page |
| Template leak | PASS | no other title, no stray "Lesson 1" text, footer says Term 2 |

Validator: 0 FAIL, 3 WARN (slow-class mini 12:02 of 11:00, workbook 28:17 of 28:00, talk 6:08 of 6:00; the buffer absorbs them). Earlier: 4 WARN (the model estimate for page 1 says 105 percent but the PDF measures 100 percent; slow-class mini 10:11 of 10:00, workbook 28:18 of 28:00, talk 6:03 of 6:00, all absorbed by the 5-minute buffer and stated in `timing.notes` and `skip_order`).

## Judgement lines

- Tier principle: PASS. Start here (S1 to S7) is P1 content: read a place from a picture, write 1st to 8th, count and name the last place (10th), one clue (right behind, between), the place from the back in a line of 6, and how many are in front. Contest-style moves are Think harder or Go further only: both ends (T1), between (T2), the line facing the other way (T3), mixed (T4), seating round a table (G1), the middle child of 13 (G2), race order from "beat" clues (G3).
- Start here approachable: PASS with caveat. Every item has a picture and one idea. S5 (place from the back) and S7 (how many in front) are taught in Explore round 3 and mini-lesson slides 2 and 3. No new word in Start here that the warm-up or Explore has not taught (front, back, behind, between, right behind). No "queue", "position" or "opposite" until Go further.
- Think harder reachable: PASS. Start here is modelled at 18 minutes of the 28; Think harder is reachable for a middle child, Go further and the Investigation are for home or next time and the page says so.
- Age fit: PASS with caveat. Pictures carry every question; the tutor reads each one aloud. Answers are short ordinals or one number. Caveat: the picture name labels are small on the printed page (the figure engine fixes the label size).
- Joining cold: PASS. The warm-up re-teaches counting, one before and after, and the four position words with a picture and with real things. A child who is new this term gets a one-minute routine card in the Opening. `safe_to_miss` is true and says why (nothing later in Term 2 needs ordinals; Lesson 14 is the plan's safest).
- Round-2 audit lessons applied: next_materials names exactly what Lesson 12 needs (the strips kit page cut into 11 strips with two cut after 6 cells, two colouring pencils, pencil and paper; counters dropped after the cut-out fix pass); no paper is held up to the camera (answers on three, fingers, thumbs, own ticks); the still-stuck route is the tick on the look-back page, photographed by the grown-up to the business WhatsApp (number only in the parent note, not on any slide, validator checks slides); the exit ticket is read aloud; recording statement in the privacy-notice words; safety line for small items; no first names on the recording; slow-class timing flagged; the goodbye slide is last; wrong working is attached to names that vary (Kumar, Mei, Siti), not always Siti.
- Beyond-P1 statements: PASS. Guide strand note, tutor prep and the parent summary say plainly that Think harder and Go further go past school Primary 1 on purpose, with no claim to match a syllabus.
- Viewed: PASS. All 6 workbook pages, the answer key (3 pages), home sheet (2), parent page, guide text, and every slide (31) were viewed after the final rebuild. The break slide first showed unreadable text in a white list card on a dark slide and was changed to plain lines; the Think harder preview slide was split in two because its pictures were too small.

## Instrument A (0 to 2 each)

1 Low floor, high ceiling: 2, touch-and-count to a 13-child line and round-table clues;
2 Depth over speed: 2, objects first, "how do you know" at every step;
3 Generalise: 2, the Investigation (front place + back place = children + 1);
4 Justify: 2, talk question (can Ali be 2nd and 6th), T1 error check;
5 Multiple paths: 1, count in front or use the place, one contrast;
6 Challenge ladder: 2, Start / Think / Go and Investigation;
7 Student-led inquiry: 1, hands-on Explore but tutor-led;
8 Complexity / context: 1, queue, table and race contexts only;
9 Problem posing: 2, menu M2, online g3 and H-sheet puzzle making;
10 Metacognition: 2, look-back, tick your own work, sneak-peek revisit;
11 Pacing / compacting: 1, choice after question 3 but a lockstep deck;
12 Extension, not acceleration: 2, optional slide and menu stay on places in a line.

Total: 20 / 24

## Remaining open items and template needs (shared files, not edited)

- Never trialled with children; times and difficulty are modelled.
- `line_up` has no `cell` or font-size option and `names` text is fixed at 22 units, so on A4 the names above children are about 7 pt; a size option, and a `FRONT`/`BACK` label option for a line counted from the other end, would help. `round_table` is limited to 175 px by the `.nar.rt` CSS rule so the seat labels in Go further question 1 are tiny.
- The look-back block on the printed page and on the slide (`common.STUCK_TEXT`, `b_print`, `b_deck.lookback`) still says "I am still stuck (I will ask in the class chat or show my tutor on camera)". Owner default 9 for Term 2 is the look-back tick photographed by the grown-up to the business WhatsApp. The wording should change in the shared tools.
- The deck question rows (`qs` blocks) draw only `visual`, not `visuals`, so workbook slides show no pictures for questions that use `visuals`. The printed page needs `visuals` (a `visual` line is too tall at 520 px).
- Workbook pages 1 and 2 are full: no room for a longer Start here.

## Fix pass (Term 2 round 2, 22 Oct 2026)
See `audit/FIXES_L11.md`. Applied: answers no longer on question slides (reveal slides), fingers instead of gallery look-around, one microphone routine, no public exit finger count, G1 "next to", S1/S2/T2/G2/G3/I1 layout fixes, number cards now used, hand-off and parent page wording, online steps rewritten. Template needs are listed in FIXES_L11.md.

## Update (final fix pass, 23 Oct 2026)

Fixes from `audit/FINAL_AUDIT_T2.md` are listed in `audit/FINAL_FIXES_T2.md`. Rebuilt; validator 0 FAIL. This lesson: recording notice said before the recording starts, with the identical Term 1 wording; identical recording sentence on the parent page; "Term 2 Lesson N" numbering; parent page kept to one sheet.
