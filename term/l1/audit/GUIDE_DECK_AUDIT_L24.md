# Guide and deck audit: Level 1 Term 3 Lesson 24 (Dollars and Change)

Auditor: independent desk review. Read all 20 pages of `L24_Tutor_Guide.pdf`, viewed all 28 slides of `L24_Deck.pdf` (45 dpi contact sheets, and word-box heights of every slide from `pdftotext -bbox`), read `lessons/l24.json` (script, slides, rec, timing, safeguarding, spare_time, tutor_prep, kit contract), the neighbouring hand-off fields (`l20` to `l23`, `l25`), `l30.json` (the Quest gates that lean on this lesson), `website/privacy.html`, `docs/terms/owner_decisions.md`, `l1_term3_term4_preflight.md` sections 1, 4, 5, 8, 13, `docs/books/p1_school_paper_patterns.md` (money), `TERM_WIDE_AUDIT.md`, `FIXES2_L*.md` and the Term 2 guide and deck audits. Maths re-checked: warm-up (5s to 100; 5, 10, 20, 50; 7 steps and 4 steps), sneak-peek (40¢; same amount: ten 10¢ is 100¢), Explore (60¢ ways; A 70¢, B 65¢; sweet 10¢ change; ruler $4), Mini-lesson (75¢; 100¢; $2; 15¢; 45¢ and $5), workbook S1 to G3, the Investigation, talk time (50¢ is not more than $1), exit ticket (90¢, $6, $15), optional slide (85¢ in 4 coins: 50, 20, 10, 5): all correct.

Instruments: AUTHORING 16-point rubric, delivery items 3, 7, 8, 9, 15: 3 PASS (parts sum to 90; script 67:53, slow class 80:23, no part OVER), 7 PASS (REC cues at most 23 words, each with a child action; chapter table present), 8 PASS, 9 PASS, 15 PASS; instrument A re-score for delivery 17 / 24; timing model of `timing_p1.md` as the guide's section 9. Verdict: **Ready after minor fixes**.

Findings: High 0, Medium 5, Low 7.

## What works

One idea at a time and a clean order: value is the number on the piece; count the biggest first; a dollar is 100¢; change by counting up. The warm-up counts in 5s and 10s again, orders four coins and counts up on a line, so a child who joins cold can follow (the guide says so, and says the lesson is not easy to miss because Mi's Quest has a gate on it; `l30.json` gate C3 does ask coins and change). Explore is kit-led (make 60¢ two ways; count two pictures; change twice) and the IF STUCK lines are concrete ("what number is on the coin?", "put the price coins away first, then count up"). The Mini-lesson answers are held off the screen for the Your turn (`s-m5` then `s-m5a`). Check slides follow each workbook page; the exit ticket is read aloud with its four options. Safeguarding block is consistent with the script (small pieces, nothing in mouth or ears, away from younger children, real coins only if a grown-up is present, no cutting during the lesson, no paper to the camera, no private chat, WhatsApp-only route, no names with answers). Recording and greeting wording is word for word that of L20, L22 and L23. The beyond-P1 statement is in the strand note, the "Plain statement" NOTE and tutor_prep, and is honest: counting and change are P1; listing every way, fewest notes and coins and the number of amounts are beyond on purpose. No MOE-aligned claim. The hand-off lines (price tags page, play money in its envelope) are true against `l25.json`.

## Timing and tutor load

Script 67:53 of 90, slow class 80:23, the last 5 minutes untouched. The workbook allotment (page 1 8:00, page 2 9:00, choice 4:00) fits the guide's estimates (8.0 and 8.5 minutes for a middle child). One tutor can run it. Two practical points: Explore starts with "Take your coins. Make 60¢" but nothing in the opening or the warm-up says "lay your coins out by value"; with 29 loose pieces and a handful of tokens in an envelope, a six-year-old needs about 30 seconds to find a 10¢ coin, which the script (1:00 for the first make) does not budget (Low, finding 9). The tutor cannot see small pieces on a video call: the guide's remedy ("children say what they have made and may tilt the camera to the table") is the right one.

## Slide audit (28 slides)

Clean: 3 to 10, 12 to 15, 17, 19, 20 to 22, 24, 28 (warm-up, sneak-peek, explore, change, your turn, check, break, check slides, choice, talk, exit check, look-back, menu); slides 1, 2, 25, 26 are clean except for the calculator Mi. Mi appears on the title, two small bubbles (slides 2 and 25) and the end slide (26); the bubbles carry no numbers. Every slide has a speaker note. Concerns:

- Slide 11 (`s-m3`, "A dollar is 100¢") draws ten 10¢ coins and two 50¢ coins with the caption "Two 50¢ coins make $1. Ten 10¢ coins make $1." on screen while the tutor asks "How many ten-cent coins make one dollar?" (28:03) and "Check it on your table" at 27:25. The guide's prep line says only `s-m4` and `s-m5` keep answers off the screen, so the author counted this slide as a worked example, but the question is asked of the children on the same slide (finding 2).
- Slides 16, 18 and 23 (workbook pages 1 and 2 and the exit ticket as slides): the coin and note pictures are 1 to 1.5 cm tall at 1080p and the coin labels are 5.0 to 5.5 pt on a 1440-pt page, about 7 px at 1920 wide (finding 3). The word-box test shows the rest of the deck at 28 to 45 pt, so the money rows are the only unreadable text.
- Slide 27 (`s-opt`, "Make 85¢ with coins: fewest number of coins?") shows exactly a 5¢, a 10¢, a 20¢ and a 50¢ coin: they total 85¢, so the picture gives the answer (4 coins) before anyone has tried (finding 4).
- Slides 1, 2, 25, 26: Mi holds the calculator (finding 1).
- Slide 9 (`s-m1`) draws coins and notes in ascending size (5¢ smallest, $50 largest) under the sentence "The number tells the value, not the size": the picture agrees with the misconception the sentence warns about (Low; real coins and notes also grow with value, so this is fair, but workbook T4 and S5 test it).

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Deck slides 1, 2, 25, 26 (Mi); guide cover; parent page | Built 02:18; the no-calculator image `term/l1/assets/mi_dolphin_nocalc.png` appeared at 03:08 and `common.py` uses it automatically; Mi still holds the calculator in all four poses (owner default 6) | Rebuild all Term 3 decks; fail the build if the calculator image is used |
| 2 | Medium | Slide 11 `s-m3`; script 27:25 to 28:22; kit | Answer chips ("Ten 10¢ coins make $1") and ten drawn 10¢ coins are on the slide while the tutor asks the question; the script says "Check it on your table" for ten ten-cent coins but the kit has six | Make the answer caption a `reveal` block (answer slide `s-m3-ans`); show two 50¢ coins and a $1 only, and say "count in tens to 100" for the ten coins; or supply ten 10¢ coins |
| 3 | Medium | Slides 16, 18, 23 (workbook and exit slides) | Coin labels 5.0 to 5.5 pt (about 7 px at 1080p), pictures 1 to 1.5 cm; the guide tells the tutor to "read every question with its amounts aloud: the figures are small" | One question per slide for money rows at 25% of slide width; labels at least 24 px; keep the check slides as they are |
| 4 | Medium | Slide 27 `s-opt` | The four coins drawn (5¢, 10¢, 20¢, 50¢) total exactly 85¢, so the question "fewest coins to make 85¢" shows the 4-coin answer; the guide expects many children to try 20 + 20 + 20 + 20 + 5 | Draw a tray with several of each coin, or reword as "Make 85¢ with as few coins as you can" with no picture |
| 5 | Medium | Guide strand note, `moe.note`, tutor_prep and slide 1 speaker note | The tutor-facing text carries "decision D1; the rules on reproducing notes and coins have not been checked". Twenty-nine pieces in a paid book rely on an unchecked rule | Owner to confirm the position before the first book is printed; keep the sentence out of the guide once settled |
| 6 | Low | Guide section 9, assumptions | "papers to the camera 30 s" remains in the timing assumptions although paper hold-ups were removed (Term 2 default 9) | Delete the clause (same line in L23) |
| 7 | Low | Guide opening, 0:26 to 0:56 | The recording starts after the greeting; the notice is said about 30 seconds into the recording. Same wording as L20 to L23 and `privacy.html` says the group is told at the start. Carried over from Term 2 | Owner to confirm the order for all of Term 3 |
| 8 | Low | `s-m1` | Pieces drawn in ascending size under "not the size" | Draw one coin and one note per row at a common size, or add one pair where the smaller piece is worth more (a $2 note smaller than the 50¢ row) |
| 9 | Low | Opening/Remember | No "lay your coins out by value" 30-second step before Explore | Add a SAY line in the warm-up: "Put your coins in rows: all the 10¢ together" |
| 10 | Low | Hand-off for the $1 tokens | The tokens come from Lesson 20; L21 and L22 parent pages say nothing about them (only L23 does), and the L20 hand-off is unfixed (see the L23 audit). A family that threw the tokens away is warned only a week before; the "5 counters or buttons" fallback is good | Add "keep the $1 tokens" to the L21 and L22 hand-offs |
| 11 | Low | Slide 21 (talk) | The Talk time claim ("a fifty-cent coin is worth more than a one-dollar coin") is introduced as "A child says" - fine - but Sneak-peek 2 already used the same $1 = ten 10¢ idea, so the two pieces of the lesson overlap | Fine; note for the term-wide pass |
| 12 | Low | `s-m2` | The chips 50¢, 60¢, 70¢, 75¢ are on the slide while the tutor says them; a worked example, acceptable; but the next try (20, 20, 10) is not shown on a slide | None required |

## Joining cold, misconceptions, inclusion

Joining cold is handled: counting in 5s and 10s, ordering four coins by the number printed on each and counting up on a line are re-taught with pictures. Misconceptions anticipated and answered: counting each piece as 1, 50 is bigger than 1, giving the price as the change. Names and cast are inclusive; "A child says" for the false claim. No child is named with a wrong answer.

## Scores

AUTHORING delivery items: 5 of 5 PASS. Instrument A (delivery): 17 / 24. Slide audit: 28 slides; 19 clean; 3 with unreadable money rows (16, 18, 23); 1 with an answer shown while asking (11); 1 optional slide that gives the answer (27); 4 with only the calculator Mi (1, 2, 25, 26).
