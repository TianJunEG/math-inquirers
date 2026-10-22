# Second fix pass, Lesson 9 (Draw and Measure), 22 Oct 2026

Inputs: `audit/GUIDE_DECK_AUDIT_L09.md`, `audit/HOME_PARENT_PRACTICE_AUDIT_L09.md`, L9 rows of `audit/TERM_WIDE_AUDIT.md` (F12, F21), `FIXES_L09.md`, owner decisions. Files changed: `lessons/l09.json`, `out/l09/`, `AUDIT_L09.md` (checks file unchanged: 178 pass). Validator 0 FAIL (18 pass, 1 estimate warning), 230 practice variants, leak check clean; slow-class script 89:35 (workbook 31:44 of 28, covered by the flex buffer; very little margin, stated in the guide); workbook 5 pages, fill 84, 92, 95, 88, 91%; home 93%; parent 93%.

| Finding | Sev | Action |
|---|---|---|
| G1 no ruler pictures on slides | Med | Ruler figures added to "Measure: three steps", "Draw a line 7 cm long" and "Between two marks"; workbook and exit slides now show every part. |
| G2, L09-1, L09-2 rounding in Start here | Med | Start here needs no rounding: S3 asks for a short thing and a whole number next to the tip (either mark is fine); Explore says "about" and treats choosing the closer mark as Think harder; the mini-lesson slide is labelled a Think harder preview; online c5 moved to Think harder (easier link c1); home H3 answer, parent quote, summary, words, try-at-home and report line no longer lead with "nearest". |
| G3 pencil longer than a 15 cm ruler | Med | S3 asks for a crayon or a rubber. |
| G4, F7 ruler and paper to the camera | Med | Opening: a finger on the 0 mark and "zero" said quietly; Explore and exit use thumbs and fingers; no paper or ruler is held up. |
| G5 tutor-key text on the answer slide | Med | S3 and G3 answers are in child wording. |
| G6 webcam logistics | Med | Nothing is shown to the camera; drawing demonstrated on a shared whiteboard or the slide picture. |
| G7 slow class 89:35 | Med | Honest: skip order and the flex buffer stated; opening trimmed. Mi calculator image reported. |
| G8 brain break units | Low | "A big jump is ten, a small hop is one" (no cm). |
| G10 to G13 | Low | Cut becomes fold (slide, script, practice g3); Talk "show your grown-up"; goodbye last; journal and tracker removed. |
| F6, F8, F9 | Med | Recording statement, microphone routine, no first names, WhatsApp "still stuck" route, no shared room. |
| F2, L09-3 | Med | Next-lesson line and `parent.next_materials` for Lesson 10: 20 counters, ruler, printed workbook, 4-page check sheet at 100% (note to follow). |
| L09-4 | Med | Home sheet intro: "No ruler? Tell your tutor before the lesson"; materials line says the same. |
| L09-5, L09-6, L09-8, L09-10 | Low | H1 wording, try-at-home starts at the 1 mark, "OPEN ANSWER" removed from home answers, summary no longer says "up to 13 cm". |
| F29, P2 | Low, Med | Beyond-Primary-1 reminder; "do not hurry"; WhatsApp route and 90-day photo retention on the parent page. |

Not fixed: **F12 ruler fallback** (owner decision: no printed ruler; families use their own and tell the tutor); L09-7 (runner has no pictures); shared files: look-back "(my tutor will come and help)", guide sneak-peek line "Papers are shown to the camera once, together", ruler thumbnails on the s-ws2 slide stay small, Mi calculator image, no Term 1 console, the guide's slow-class flag never shows OVER, estimated "page 5 overflows (108%)" warning (built PDF 91%).
