# Fix pass, Term 3 Lesson 2 (lesson 22, Five Minutes at a Time)

Changed: `lessons/l22.json`, `verify/l22_checks.py` (242 checks), `AUDIT_L22.md`, `out/l22/`. Validator 0 FAIL, leak check clean; workbook fill 99/89/97/90/99%, kit page 75%; parts 2/6/4/12/12/4/30/6/6/3/5 = 90; script 68:02, slow class 80:37. One WARN left: the opening is exactly full in the slow-class model (2:00 of 2:00; the standing buffer absorbs it). Not touched: shared tools, other lessons.

Source audits: `WORKBOOK_AUDIT_L22.md` (W), `GUIDE_DECK_AUDIT_L22.md` (G), `HOME_PARENT_PRACTICE_AUDIT_L22.md` (H).

| Finding | Action |
|---|---|
| G1 / H1 "the short hand waits at the hour" is false | Removed everywhere it appeared: objective 3, timing notes, title-slide note, `s-explore2` and `s-m3` titles ("Explore: the long hand moves on", "Read this clock"), the Explore answer SAY ("The short hand has crept nearly to the ten ... the hour is still nine until the long hand is back on the twelve"), the Talk reveal note, the parent summary and the parent quote ("The hour stays the same until the long hand has been all the way round"). The `s-m3-ans` card now says "nearly at the 9, but not there yet" and gives the rule. `tutor_prep` tells the tutor the short hand never waits |
| G2 Explore discovery cannot happen with loose hands; script contradicts slide | Tutor demonstrates on their own clock (new DO line), children slide the short hand nearly to the 10 but not onto it; slide list, notes, SAY and WORK changed |
| G3 slide titles give the answer | Neutral titles on `s-explore2`, `s-explore2-ans`, `s-m3`, `s-m3-ans` |
| G4 paper-hold-up wording in the warm-up | Now "point to the short hand, then the long hand, on your own clock, and give a thumb" |
| G5 / W6 event-card sort: ambiguous cards, mat is boxes, "hardest to place" | Every card has a time (wake up 6:10, breakfast 6:50, school 7:20, break 10:40, come home 1:15, play ball 4:45, night bath 7:05, go to bed 8:05; labels shortened to fit the card); "pocket" became "box"; the "hardest card" question became "The night bath card says seven oh five. Is that am or pm? How do you know?"; notes say a morning bath child is answered with "this card is the bath before bed"; `verify` checks each card time against its 24-hour time and four am then four pm. The mat itself (too small for four cards, headings clipped, "a.m." with full stops, card gaps 3.4 mm) is a shared tool: listed |
| G6 / W6 notice after recording starts | Opening reordered as in Lesson 20 and Term 1: greet by first name, hello, notice, "Start the recording now. Do not use children's first names", REC, microphone routine and "Nobody holds paper up to the camera"; the NOTE and `tutor_prep` agree. The "Look at a clock near you" ask was dropped to make room (the opening is 2 minutes) |
| G7 / W7 Start here minutes | Page 1 9:30, page 2 8:30, choice time 3:40; "about 17 minutes" became 18; the work part is 29:39 of 30:00 in the slow class |
| G8 / W2 / W4 footers, small clocks, 11 mm answer boxes, exit page | Template/deck builder: listed. Exit E1 clock 54 (was 48), E3 face 48 (was 40), checked that page 5 still holds the look-back |
| G9 whole-class duration example | The s-m5 class example is now "A swim lasts 1 h 40 min" (no start and end times), so Go further is not pre-empted and T2's "film 1 h 20" is not repeated |
| G10 optional slide mislabelled | Retitled "Optional: the next hour" |
| G11 "papers to the camera 30 s" | `tools/b_guide.py`: listed |
| G12 / W10 / H3 "ten past" and "quarter" contradiction | One rule for the term: digits first. The parent "when stuck" now says "We write and say times as digits, like four ten, so please do not worry about words such as 'ten past'". Lesson 21 no longer teaches the quarter words to the whole class (its page 3 has one gloss), so the two parent pages agree |
| G13 Mi calculator | Rebuild |
| W1 hour-hand trap at Start here and in the exit ticket | S1 third clock is now 11:10, S6 Ben 6:20, exit E1 10:15; :45, :50 and :55 stay at T3 and the mini-lesson. `verify` asserts no Start here minute above 35 |
| W3 pictures cannot show "not yet reached" | The mini-lesson note and the answer card state the rule (past 30 minutes the short hand is nearly at the next number; the hour stays until the long hand is back on the 12); nobody is told to read it from the picture |
| W5 class answers repeat in workbook, exit, home | Class am/pm examples are now 6:45 breakfast, 7:15 bedtime at night, 12:45 lunch; the s-explore3 rule line is "6:45 am and 7:15 pm"; E2 is "The bus home leaves at 1:20 in the afternoon"; home H2 8:35, H3 3:05, H4 12:10; online c4 tea at 6:20, g1 base 3:40 to 4:15, t3 base 3:15 to 3:50 (`verify` BASE_ENV and the class-time list updated) |
| W7 Go further number line | Every tick label is a time (3:00 to 4:00, 3:00 at the left), the 4:05 tick is unlabelled so 4:00 and 4:05 do not touch, 70 dropped, and the stem says "Each step on the line is 5 minutes" |
| W8 "at night" missing | Added to S5(b) and T1(d) |
| W9 Investigation first answer missing from key | Key now starts "First: 3 steps (5, 10, 15). Next: 12 steps ..." |
| W11 h and min | One-line gloss on the page 3 instruction line |
| W12 S4 option 5:52, hands overlap at 5:25 | S4 clock is 8:25 (hands far apart), options 8:05, 8:25, 9:25, 8:30; script, key, notes and `verify` updated |
| W13 page 5 header wraps | Header is now "Reading a scale: the clock minutes" |
| H2 online c5 base unanswerable; H5 "just past" false for half the variants | Base card and template read "The short hand has passed the {h}. The long hand is on the {n}." (true for every minute value) |
| H4 c1/t1 "has just passed the hour" | c1 step: "The hour is the number the short hand has passed." |
| H6 / H7 repeated numbers, plural | See W5; c2 step "Count {n} steps of 5. You reach {ans}." |
| H8, H12 runner messages and the range hint | Runner/tool: listed or optional |
| H10 g3 example | Added 3:40 to 4:10 example to the steps |
| H9, H11 | Not changed (fine by design / optional) |

Numbering: "Term 3 . Lesson 2" on every page; next lesson "Term 3 Lesson 3: Time Passes". Hand-off from Lesson 21 (event cards page cut, clock kept) matches `l21.json` `parent.next_materials`; hand-off to Lesson 23 unchanged. No money in this lesson.
