# Self-audit: Level 1 Term 2 Lesson 2 (Bar Strips: More and Fewer, lesson 12)

Rubric: `docs/audit/reaudit_p1.md` instruments A and tier compliance, `AUTHORING.md` checklist, Term 1 round-2 audit lessons (`audit/TERM_WIDE_AUDIT.md`, `FIXES2_L*.md`).

## Automatic checklist (validator, last build)

| Criterion | Result | Evidence |
|---|---|---|
| Schema valid (JSON Schema + key checks) | PASS | all top-level keys, schema 2020-12, identity term 2 / lesson 12 / lesson_in_term 2 / key t2l12 |
| Every answer verified independently | PASS | 74 checks in `verify/l12_checks.py` (strips modelled as lists of cells; sum-and-difference, transfer, the shelf puzzle and the chain of three solved by trying every whole-number split) |
| Online practice variants verified | PASS | 180 template variants verified three ways (expression, brute-force oracle, runner JavaScript calc) |
| Timing: parts sum to 90, buffer | PASS | 11 parts, sum 90; script 72:37 of 90:00; slow-class 85:38 |
| Slides and script linked | PASS | 31 slides each shown once, in its part; goodbye slide is last |
| Tier counts and completeness | PASS | Start here 7, Think harder 3, Go further 3, exit 3, home 5 |
| Neutral labels, no overclaims, no private chat | PASS | no banned labels; no MOE/GEP/SASMO claim |
| Recording cues | PASS | 11 cues of at most 26 words, each with an action |
| Spare-time menu | PASS | 3 activities, 11 optional minutes, rules present |
| No copied contest text | PASS | no 7-word overlap with the reference texts |
| Mascot | PASS | Mi on 4 slides (title, Remember, Look-back, end) |
| Workbook page fill | PASS | measured on the PDF: 96, 100, 98, 88, 99 percent, kit page 95 percent (eleven strips); 6 pages as designed; home 2 pages, parent 1 page |
| Template leak | PASS | no other title, no stray "Lesson 1" text, footer says Term 2 |

Validator (after the fix pass): 0 FAIL, 4 WARN (slow-class opening 3:17 of 3:00, Explore 15:03 of 15:00, mini-lesson 10:56 of 10:00 and workbook 28:10 of 28:00; all absorbed by the 5-minute buffer and stated in `timing.notes`).

## Judgement lines

- Tier principle: PASS. Start here (S1 to S7) is school-level addition and subtraction stories with a picture: the gap (how many more), "more than" by adding the extra part, a total by joining strips, a drawn pair of strips (S4), and choosing the number sentence (S7). Reversed wording ("fewer than" with the unknown person first, T3), total and difference (T1), make equal by a transfer (T2) are Think harder; the shelf transfer with a total (G1), the chain of three (G2) and how the gap changes when marbles move (G3) are Go further. No contest-style item is at Start here.
- Think harder count: three questions (the minimum). A fourth, "group totals then compare", was written and then dropped because it pushed Think harder onto a second page; its idea (join the parts, then compare) is in Start here S3, S5 and the mini-lesson.
- Start here approachable: PASS. Every item has a strip picture or a drawing box and one idea; S3 and S5 add tens and ones without regrouping (31 + 15, 21 + 6) with the extra part shown on the strip. The explore rounds give the same stories with real strips before the page. No word is used that the warm-up or Explore has not taught (strip, gap, more than, altogether).
- Think harder reachable: PASS. Start here is modelled at 18.5 minutes of the 28; Go further and the Investigation are for home or next time and the page says so.
- Age fit: PASS with caveat. Pictures carry the stories and the tutor reads each question aloud. Caveat: bar labels and numbers on the printed pictures are small (the figure is limited to 430 px width).
- Joining cold: PASS. The warm-up re-teaches undoing a step, counting up for a gap, and reading a strip of cells, each with a picture and real strips. `safe_to_miss` is false and says why (Lessons 18 and 20 draw strips).
- Round-2 audit lessons applied: next_materials matches Lesson 13's own materials (kit page of ten-frames and counters, or about 20 things of two kinds); nothing is held to the camera; the still-stuck route is the look-back tick photographed to the business WhatsApp (number only in the parent note); exit ticket read aloud; recording statement; safety line for small items and for cutting (a grown-up cuts); no children's first names on the recording; the error-check name is Aisha in the talk question (Kumar in Lesson 11); slow-class timing flagged.
- Beyond-P1 statements: PASS. Guide strand note, tutor prep and the parent summary say plainly that strips ("bar models" at school), total and difference, and make-equal go past school Primary 1 on purpose.
- Viewed: PASS. All 6 workbook pages, key (3), home (2), parent page and all 31 slides were viewed after the final rebuild. Fixed during viewing: the title slide title ran into the decoration (shortened to "Bar Strips" with a subtitle), the Think harder page and page 2 spilled onto extra pages (T4 dropped, S7 made picture-free).

## Instrument A (0 to 2 each)

1 Low floor, high ceiling: 2, laying two strips to a chain of three with a total;
2 Depth over speed: 2, four Explore rounds with objects and "how do you know";
3 Generalise: 2, the Investigation (same total, the gap goes up by 2 as the bigger number goes up by 1);
4 Justify: 2, talk question (is Aisha's picture good), "is it the gap or the whole line";
5 Multiple paths: 1, count up or take away, add or count on;
6 Challenge ladder: 2, Start / Think / Go and Investigation;
7 Student-led inquiry: 1, hands-on Explore but tutor-led;
8 Complexity / context: 1, stickers, marbles, shelves, cards only;
9 Problem posing: 2, menu M2, online g3, H-sheet;
10 Metacognition: 2, look-back, tick your own work, sneak-peek revisit;
11 Pacing / compacting: 1, choice after question 3 but a lockstep deck;
12 Extension, not acceleration: 2, optional slide and menu stay on strips.

Total: 20 / 24

## Remaining open items and template needs (shared files, not edited)

- Never trialled with children; times and difficulty are modelled.
- Printed `bar_model` pictures cap at 430 px (`.vis.wide.bm`) and have fixed bar height; names and numbers are about 8 pt on A4 and the `brace over` option draws its label across the next bar, so it is not used. A bar height or scale option would help.
- The deck question rows (`qs` blocks) draw only `visual`, not `visuals`, so the pictures are not on the workbook-page slides; the printed page needs `visuals` (a single `visual` bar picture is too tall).
- The look-back text printed on the page and slide still says "(I will ask in the class chat or show my tutor on camera)" (shared `common.STUCK_TEXT`, `b_print`, `b_deck.lookback`); owner default 9 is the look-back tick photographed by the grown-up.
- Strips on the kit page are in two colours but not numbered, so an "equal cell" check depends on printing at 100 percent.

## Fix pass (23 Oct 2026)

See `audit/FIXES_L12.md`. Kit is now eleven strips (two cut after 6 cells by a grown-up; nobody cuts in the lesson); Explore uses 10, 6 and 4; Start here has no regrouping and one "fewer than" item (S4); answers are revealed after the question on four slides (explore round 3, mini-lesson 2, 5 and 6) and the Remember strip no longer prints 36; the exit-ticket finger count and the "next lesson catch-up" promise are removed; counters are dropped from the lists; Dev is now Jamie.
