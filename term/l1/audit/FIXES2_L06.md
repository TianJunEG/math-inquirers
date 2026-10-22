# Second fix pass, Lesson 6 (Tens Jump, Ones Hop), 22 Oct 2026

Inputs: `audit/GUIDE_DECK_AUDIT_L06.md`, `audit/HOME_PARENT_PRACTICE_AUDIT_L06.md`, L6 rows of `audit/TERM_WIDE_AUDIT.md`, `FIXES_L06.md`, owner decisions (Term 2 defaults). Files changed: `lessons/l06.json`, `verify/l06_checks.py`, `out/l06/`, `AUDIT_L06.md`. Validator 0 FAIL (18 pass, 1 estimate warning); 357 answer checks; 1496 practice variants; leak check clean; workbook fill 93, 84, 87, 84, 96% (kit 91%), home 93%, parent 87%.

| Finding | Sev | Action |
|---|---|---|
| G1, F6, F9 recording, voices, names, cameras | Med | Opening now says "recorded: the tutor, the shared screen and any voice that is not muted; keep microphone and camera off if you like". Greeting is to the whole group, no first names; "Good morning" is now "Hello". Safeguarding, tutor prep (test the recording with several tiles) and parent page match. |
| G2, F7 hold-ups to camera | Med | All four hold-ups removed: sneak-peek (keep your paper), explore (thumbs up), exit (tick your own work, fingers for how many right). Slide text, notes and safeguarding rewritten. |
| G3, F8 still stuck | Med | Look-back tick, grown-up photographs the page and sends it to the business WhatsApp after class, whole-group catch-up question next lesson; "visit to the shared room" removed. Number only on the parent page (not on slides). |
| G4, F15 slow class, workbook | Med | Check slides read only when most have stopped writing; "if you are still working, carry on". Slow class needs 89:46 (workbook 31:21 of 28): guide says to take it from the flex buffer. |
| G5 ask waits | Med | Explore waits raised to at least 12 s, mini write time 90 s, round 2 build time added; slow total stays under 90. |
| G6 explore notes | Med | Round lengths 4 + 3 + 5 + 4 = 16, build step for 24 scripted. |
| G7 chorus | Med | Microphone routine in every opening; counting led by the tutor, children count quietly. |
| G8 paper number line | Med | Shared whiteboard or blank slide (script, notes, tutor prep). |
| G9 timer slide | Med | "Timer slide" removed from tutor materials; keep a clock. Console not wired: template/tool. |
| G10 journal, tracker | Med | Removed; exit now reads "show your ticket to a grown-up"; fingers, no per-child tracker. |
| G11 device set-up | Med | Greeting no longer asks for page and hands; no paper to the camera. |
| G12 timer chips | Med | "Timer: N minutes" now "About N minutes"; s-m5 2 minutes. |
| G13 to G15, G18, G19, G24 | Low | Lesson 5 pointer, sneak slide wording (Write Yes or No), flex REC line, "he" for Ben, one next-lesson wording, landing numbers hidden on the draw slide. |
| G20 | Low | T1 now 23 + 45, T2 79 - 35 (not the class examples); checks updated. |
| G21 | Low | "100 is ten tens"; "more than 3 minutes ahead" menu line. |
| Exit read aloud | | Script READs the three exit questions. |
| P2, P3, F2 | Med | `parent.next_materials` set for Lesson 7; "please do not teach the column method"; recording and private-link line added. |
| L06-1 | Med | Try at home: ones digit 1 to 6. |
| L06-2, L06-3 | Med, Low | H5: "on spare paper", second list removed. |
| L06-6, L06-8, L06-9, L06-10 | Low | Kit and coin materials; no "1 tens/1 ones" in variants; t1 slip text; shuffle is now in the runner. |
| F19 tier drift | Med | L6 stays Think harder; flagged for L7, L8, L10 passes. |
| F29 | Low | Beyond-Primary-1 reminder added to tutor prep. |

Not fixed (shared files, for the owner): look-back slide and workbook say "I am still stuck (my tutor will come and help)" (template); guide sneak-peek line "Papers are shown to the camera once, together" (b_guide.py); slide font sizes and chip colours (b_deck.py); no `hint_p2` field; home sheet cannot put parts on separate lines; look-back print size; key heading orphan; Mi calculator image; the validator estimate WARN "workbook page 5 overflows (107%)" while the built PDF is 96%; tutor console has no Term 1 data; the slow-class flag column in the guide never shows OVER.
