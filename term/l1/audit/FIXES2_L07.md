# Second fix pass, Lesson 7 (Take Away, Count Up), 22 Oct 2026

Inputs: `audit/GUIDE_DECK_AUDIT_L07.md`, `audit/HOME_PARENT_PRACTICE_AUDIT_L07.md`, L7 rows of `audit/TERM_WIDE_AUDIT.md`, `FIXES_L07.md`, owner decisions. Files changed: `lessons/l07.json`, `out/l07/`, `AUDIT_L07.md` (checks file needed no change: 113 checks pass). Validator 0 FAIL, leak check clean; slow-class script 88:11 (workbook 31:05 of 28, covered by the flex buffer, stated in the guide); workbook fill 90, 94, 96, 95, 97% (kit 89%), home 98%, parent 97%.

| Finding | Sev | Action |
|---|---|---|
| G1 slides and reads omit the sums | Med | Workbook and exit slides now show every part (`short: false`); the script reads the numbers of every question and all of E1 to E3. |
| G2 stars only on screen | Med | Puzzle 1 says "15 stars on the screen. Take away 4. You may draw stars on your paper." (slide, script, key text). |
| G3 hop and jump undefined | Med | Mini-lesson says once "a small step of ones is a hop, a big step of tens is a jump"; joining note names Lesson 6 as the helpful prerequisite. |
| G4, L07-1, F2 next-lesson materials | Med | Goodbye, end slide, parent "next" and `parent.next_materials` list Lesson 8's things (30 small things, two plates marked LEFT and RIGHT, workbook, pencil). |
| G5 gap wording, swap ten squares | Med | "What is the gap?" with "two, twenty, two"; scripted "ten squares: swap them for one bar"; STUCK line for counting the start number. |
| G6 answer shown while asking | Med | Slide s-m3 shows "+?" steps; both count-up checks use new numbers (46 to 53 is 7; 29 to 54 is 25). |
| G7, G11, G14 to G16 recording, voices, names, cameras, paper hold-ups, still-stuck | Med | Same wording as Lesson 6: recording statement, microphone routine, no first names, no hold-ups (sneak-peek, exit), fingers for how many right, WhatsApp route for "I am still stuck", no shared room. |
| G10, G11 timing | Med | Check slides read only when most have stopped writing; waits and write time realistic; opening trimmed to fit; flex absorbs the slow-class workbook overrun (guide). |
| G12 chorus counting | Med | Tutor leads the count, children count quietly. |
| G13 kit on camera | Med | Shared whiteboard or blank slide, in tutor prep. |
| G14 timer slide, G15 journal, tracker | Med | Removed (clock on own device); "show your ticket to a grown-up". |
| G17 E3 | Low | Child circles "the way you used": nothing in it is marked. |
| G18 movement bullet | Low | Added. |
| G19 timer chips | Low | "About N minutes". |
| G20 to G22, G25, G26 | Low | Camera sentence unified, ten-frame wording, STUCK line, flex REC cue, printing fallback in tutor prep. |
| L07-2 | Med | Try at home: choose numbers where the ones fit (68 - 25, not 62 - 28). |
| L07-3, L07-4 | Low | H5 page numbers 20 to 99, Circle Yes or No, short answer; H2 "Check: ___ + 43 = 76". |
| L07-6 | Low | Variants no longer produce "1 tens" or "1 ones" (checked by enumeration). L07-7 shuffle is in the runner. |
| F19, F29 | Med, Low | Lesson 6 stated as prerequisite; beyond-Primary-1 reminder in tutor prep. |
| P2, P3 | Med | "Do not teach the column method yet"; WhatsApp route and photo retention (90 days after the program ends) in the parent page. |

Not fixed (shared files): "I am still stuck (my tutor will come and help)" on the look-back slide and workbook; guide sneak-peek line "Papers are shown to the camera once, together" (b_guide.py); slide font sizes; home-sheet parts cannot sit on separate lines; look-back print size; key heading orphan; Mi calculator image; the estimated "page 5 overflows (105%)" warning (built PDF 97%); no Term 1 console; the guide's slow-class flag never shows OVER.
