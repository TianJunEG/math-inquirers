# Term-wide audit: Level 1 Term 1 (Lessons 1 to 10)

Role TERM_WIDE, second-round independent audit, 22 Oct 2026. Audit only: no lesson, tool, template or output file was edited. Severity scale (project scale): High = wrong maths, unsafe or unusable; Medium = misleading, ambiguous, impractical or inconsistent; Low = polish.

Method and limits (honest): I read the ten lesson JSON files in full (timing, scripts, tiers, exit, home, online practice, parent, safeguarding, spare time, materials), the ten Tutor Guide, Parent Summary and Home Practice PDFs (text of all of L1 to L3, L5 and L10; targeted text for the rest), the L10 check sheet notes and tutor key, the validator output for all ten lessons (`validate.py NN`, read-only), a contact sheet of the L5 deck, the L1 workbook and the L5 parent page by eye, plus `docs/terms/*`, `docs/moe/syllabus_by_level.md`, `docs/sasmo/g1_analysis.md`, `website/terms.html`, `website/privacy.html`, `website/level_pages/ages-6-8.html`, `website/syllabus/index.html`, `tutor/README.md` and `tutor/build_data.py`. I did NOT render every slide of every deck (that is the GUIDE_DECK role), did NOT run the online practice in a browser (HOME_PARENT_PRACTICE role) and observed no child. Maths: I recomputed about 60 answers by hand (L2 to L10 Think harder and Go further, home items, check items) and found none wrong; the first round and the verify scripts cover the rest. Sibling second-round files for GUIDE_DECK exist in this folder; I glanced only at their verdict lines after forming my own view on the L10 check.

---

## 1. One-page summary

**Verdict: Term 1 as a programme is NOT ready for a paid launch; it is ready for a supervised tutor trial once fixes 1 to 4 below are made. Lessons 1 to 9 are "Ready after minor fixes" as lessons. Lesson 10 is "Needs rework" (the 20-minute check does not fit). The family-facing wrapper (what to prepare, what is recorded, who to contact, what to do at home) is the weakest layer and is inconsistent with the lessons, the privacy notice and the website.**

Counts: 1 High, 19 Medium, 10 Low (section 5). Term-level score on the project's Instrument A (12 criteria x 0-2, applied to the term as a whole, section 9): **17/24** (the author-claimed lesson scores of 19 to 20 count tutor and online features; the first-round workbook audits scored the printed workbooks 14 to 17).

### Top 10 findings (ranked)

1. **High, F1. The L10 end-of-term check does not fit its 20 minutes and squeezes the one word-problem lesson.** The check has 10 questions with 22 answer slots (including a ruler drawing and a number-line reading). The lessons' own per-question middle-child times for the matching Start here items (L1 S1 1.5, L2 2.5, L3 3, L4 3, L5 2.5, L6 3, L7 3, L8 3, L9 2.5, L10 3) sum to about 27 minutes, before about 3 minutes of reading aloud and a 1-minute stretch. The tutor key schedules 16 quiet minutes, the guide script 11:40, the plan and parent note say 20. It sits at minutes 63 to 83 of a 90-minute lesson for 6-year-olds, after an exit ticket that repeats check Q10, and it takes 24 of 90 minutes, leaving the story lesson 10 + 10 + 20 minutes.
2. **Medium, F2. The "Next lesson ... you need only a pencil and paper" line is wrong for 7 of 9 hand-offs** (both in the Parent Summary and in the tutor's spoken goodbye), and there is no pre-lesson family note: the only "Things to have ready" list is on the post-lesson Parent Summary. A family following the printed "next" lines arrives at L2 without number-card cut-outs, at L3 without digit cards, at L5 without kit and two kinds of counters, at L6 without the kit, at L8 without plates, at L10 without counters, ruler and the printed check sheet.
3. **Medium, F3. The "joining cold" rule is stated as "all you need is counting to 20" in every lesson, but it is not credible from L5 on, and nothing tests it.** A cold joiner at L7 meets 68 - 25 as a Start here item after a 6-minute warm-up. The plan's own entry story is the holiday graduate (or a child just starting Primary 1 in Term 1, whose school is still at numbers to 20; hub FAQ). There is no entry check for term joiners (plan open question 2 is unanswered) and the website placement check belongs to the holiday course.
4. **Medium, F6 and F7. Recording and camera statements disagree across scripts, privacy notice and terms; and "hold your paper to the camera ... so only you see it" is untrue on a group video call.** L5's script has no recording sentence (a NOTE only); the notice says voices may be heard and names are not shown, but every opening greets each child by first name aloud and children answer aloud; the L1 exit note says only the tutor sees the paper, while eight families see the same gallery.
5. **Medium, F4. There is no spiral review anywhere.** Warm-ups re-teach the prerequisite (tens and ones in 6 of 9 lessons), home practice and online practice are current-lesson only, so L2, L3 and L4 content is never revisited before check Q2 to Q4 test it six to eight weeks later.
6. **Medium, F5. The check's report is stronger than its evidence:** two of four reported "areas" rest on one question each and give a three-band word; the term line promises "to say why" but no check item asks for a reason; every check item is Start here, so the Think harder / Go further half of the term is never looked at; Q9 depends on a ruler and on print scale.
7. **Medium, F10 and F11. Privacy notice, terms and website are beta/holiday documents and do not yet describe the term programme:** no WhatsApp photo flow for the check, no term retention rule, no contact route on Parent Summaries L1 to L9, "no separate make-up lessons" (beta terms) versus a "make-up slot" for the check, a Level 1 web page that lists the holiday lessons and says the workbook is posted, and a syllabus page that labels Level 1 "Start here" as "At school level" although the owner decided Term 1 Start here goes beyond P1.
8. **Medium, F12 and F13. Materials: a cm ruler is a hard dependency of L9 (all six Start here items) and L10 Q9 with no fallback, although the plan and AUTHORING say a printed ruler is the fallback; the term prints about 96 A4 pages and a grown-up cuts about 80 pieces in L1 to L3, with the kit page reprinted in L5 to L8.** "Nothing needs to be bought" is true only if a ruler and a printer are already in the house.
9. **Medium, F14. Home workload is undefined:** three overlapping streams (Parent Summary "5 minutes", Home Practice "about 15 minutes", online practice of 13 or 14 items) plus the optional pages 3 to 5 (about 35 to 50 modelled minutes); the online link is "ask your tutor ... key t1l01" with no distribution route.
10. **Medium, F16. The tutor console is not wired to the term lessons** (`tutor/build_data.py` builds only the p1 to p6 holiday decks), and the lesson design leans on tutor load: eight cameras, papers read from gallery tiles, the deck, a recording, no breakout rooms, no co-host.

### Recommended order of fixes

1. F1 (re-time or restructure L10 and the check), because the term's only assessment and its report depend on it.
2. F2 + F12 + F13 (one "Term kit and print pack" sent before L1, a "Before lesson N" half page generated from `materials.child`, ruler fallback on the kit page, print-once kit).
3. F6, F7, F8, F9, F10 (one decision on recording voice/names/cameras/paper-to-camera/still-stuck, then one fixed opening statement; update privacy notice and terms for the term programme; one contact route on every parent page).
4. F3 + F20 (entry profile and a 5-minute readiness check; catch-up and routine onboarding for joiners; trial with cold joiners).
5. F4 + F5 (one review item in each home sheet and a 10-minute recap before L10; reduce the report to what the check supports).
6. F11 + F18 (a Term 1 page and parents' overview on the website; fix "At school level"; set the term price).
7. F14, F15, F16, F17 (home-work guidance, timing measurement in the trial, console, coverage choices).
8. Low items F21 to F30 (section 5b).

---

## 2. What a tutor trial must test (risks)

| # | Risk | What to measure in the trial |
|---|---|---|
| 1 | Warm-up and Explore timing with 8 live children. Scripts assume 12-second waits per question (`resp` 12) and 25-second slide changes; the project's own timing rubric (`docs/audit/timing_p1.md`) uses 30 s per question. At 30 s the Remember warm-up alone needs about 6.2 to 9.8 minutes against 6 allotted (my recomputation: L1 7.3, L2 8.2, L5 8.3, L7 8.4, L8 8.4, L10 9.8). | Actual minutes per part in L1, L5, L7, L10; whether finger/whisper answers really take 12 s. |
| 2 | The workbook part is 28 minutes but the validator's slow-class estimate is 29:56 to 32:01 in every lesson; the slack is taken from the 5-minute buffer (L3 total slow 89:06, L9 89:00). | Time of first finisher and last finisher on Start here; how often the buffer is used; whether the spare-time menu is ever reachable. |
| 3 | "Hold papers to the camera" with 8 tiles: can the tutor read 8 six-year-olds' handwriting in 1 to 2 seconds, and what do families see? | Legibility rate; time per HOLD; parents' reaction. |
| 4 | Cold joiners: two children who count to 20 and bring nothing else, joining at L5 and at L7; a child who has only just begun Primary 1. | Start here completion, warm-up success, need for scaffold, distress; time lost to missing materials. |
| 5 | Family readiness: kit cut, correct materials, ruler, printout scale (100%), colour/mono printing. | Share of families ready at minute 0; Opening time lost (the Opening is 2 minutes in L2, L3, L5 to L8, L10). |
| 6 | The L10 check end to end: timing per page, lockstep pacing, reading 4 questions at once on page 3, photo return by 8 parents, marking from phone photos, single-question strands. | Minutes to pencils down; share unfinished; photo quality; minutes to mark; whether the note wording can be justified from the evidence. |
| 7 | Recording as a watcher: do the REC cues and chapter timestamps work for an absent child working alone with a grown-up? | Two absentees, one lesson each; time to catch up; use of the "next lesson" materials line. |
| 8 | Tutor load without breakout rooms, console or co-host: deck + guide + eight cameras + recording + papers + still-stuck follow-up. | Missed cues; tutor self-rating; ask a second person to shadow. |
| 9 | Parent understanding of the beyond-P1 statement, the three home streams and the report words. | Short parent interview after L3, L7 and the report. |
| 10 | Child energy over 90 minutes (one 4-minute break; about 28 minutes seated writing; in L10 a silent 20-minute check starting at minute 63). | Off-task time by minute, especially minutes 63 to 83 in L10. |

---

## 3. Coverage, progression and balance

### 3.1 Coverage against the plan rows (Term 1, `level_1_year_plan.md` section 2)

All ten rows are built as planned (title, big idea, strand, S/T/G shape and skill). Differences from the plan that are deliberate and documented: L1 G now compares 6 tens 14 ones with 5 tens 29 ones (plan: versus 85 ones); L3 G uses four cards (plan: three; the plan says 3-digit numbers only at G, none used); L8 Start here contains small compensation shifts (F19). Counts: Start here 6 to 8 (plan 5 to 8), Think harder 3 to 4 (plan 3 to 5), Go further 3. Contest-style moves are labelled tutor-only and sit at Think harder or later, as owner decision 6 requires (one borderline case, F19).

### 3.2 Coverage against the MOE P1 strands (`docs/moe/syllabus_by_level.md`, pp. 31-32)

| P1 area | Term 1 | Comment |
|---|---|---|
| Whole numbers to 100: count, tens and ones, numerals | L1, L2, L3, L4 | Well covered; four of ten lessons. |
| Number words | L2 only (about 15 words) | Thin but by plan ("keep spelling small"). Check Q2b is the only later use. |
| Compare two sets of objects (1.4) | L3 warm-up and one item (S3) | Thin; the plan itself calls it "touched only lightly". |
| Compare and order numbers; patterns | L3, L4 | Good. |
| Ordinals 1st to 10th | none | Term 2 (L11) by plan. |
| Add and subtract: signs, inverse, more than two 1-digit numbers, within 100 | L5 to L8, L10 | Strong; this is 5 of 10 lessons. |
| Mental calculation within 20 | warm-ups only (bonds to 10 and 20 in L1, L5, L7, L8) | No practice sheet drills facts within 20; the programme says it does not drill, but this is the P1 outcome school will test most (F17). |
| Written algorithms | deliberately none | Plan open question 3 ("may lessons 5 to 7 show the vertical algorithm?") is still unanswered; school uses it from P1 Term 2. |
| Multiplication, division, money, time, shapes, picture graphs | none | Terms 2 to 4 by plan. Term 1 therefore covers 3 of the 8 P1 areas (whole numbers, add/subtract, length). |
| Length: measure, draw, compare, order, nearest cm | L9 | Good. "Order" lengths is only a home item (H3 L9). |

By plan, a child who joins in Term 2 or later never gets this block except through warm-ups; the website FAQ (`hub/parent_questions.html`) says school P1 starts Term 1 with numbers to 10 and 20, so Term 1 here runs well ahead of a school child's own Term 1 (see F3).

### 3.3 Coverage against the SASMO Grade 1 gap list (`docs/sasmo/g1_analysis.md` section 4)

| Gap | Where in Term 1 | Status after Term 1 |
|---|---|---|
| 1 Place value and digit puzzles (14/100) | L1, L3 (clue puzzles at Think harder) | Closed for number sense; no odd/even. |
| 2 Two-digit mental arithmetic and multi-term sums (13/100) | L5 to L8 (and L13) | Closed for add/subtract; "balance and compensate" at T. |
| 3 Changing-step sequences (10/100) | L4 T3, G1, G2 | Closed. |
| 4 Visual perception and 3-D (14/100) | none | Open until L34 and L35. |
| 5 Time and calendar (7/100) | none | Open until L21 to L23 and L30. |
| 6 Symbol equations and multiplication facts (about 11/100) | L8 box equations only | Open until L15, L16, L19. |

Three of six gaps are touched in Term 1 and none is marketed as SASMO preparation (no "SASMO", "MOE", "GEP" or "contest" appears in any Parent Summary, Home Practice or Workbook text; I searched all 30 PDFs and the deck HTML of L1, L5, L10). This is consistent with owner decision and with the analysis' own advice.

### 3.4 Progression and prerequisites (does lesson n use something only taught later?)

Nothing in Start here uses a later-taught idea. Specific observations:

- L1 to L4 are a clean sequence (tens and ones, number line, digit cards, 100 square). L2's "nearer ten" returns as "nearest cm" in L9 (good), though L9's warm-up does not mention it.
- L6 Think harder T1 (34 + 25) and T2 (68 - 24) become L7 and L8 Start here items (L7 S3 68 - 25, S4 46 - 12, S7 64 - 21; L8 S7 35 + 12 = [] + 2; L10 S5 23 + 33). A child who skipped L6 meets two-digit with two-digit work at Start here in L7, L8 and L10 with only a re-teaching of bars and squares in the warm-up. This is the owner-approved "keep the stronger arithmetic" decision, but it makes L6 a prerequisite of L7, L8 and L10, which the `safe_to_miss` flags do not say (F19, F3).
- L9 G1 (30 - 8 - 11) and L10 G1 (60 - 24 - 15) need subtraction across tens; both are Go further, fine.
- L8's note says Lesson 19 depends on it; the term itself does not.

### 3.5 Balance and over-weighting

| Lesson | S / T / G | Start here modelled minutes | Note |
|---|---|---|---|
| 1 | 7 / 4 / 3 | 17.5 | |
| 2 | 8 / 4 / 3 | 19.0 | |
| 3 | 8 / 4 / 3 | 17.5 | |
| 4 | 6 / 4 / 3 | 17.5 | |
| 5 | 7 / 4 / 3 | 18.0 | |
| 6 | 7 / 4 / 3 | 19.0 | |
| 7 | 7 / 4 / 3 | 19.0 | |
| 8 | 7 / 4 / 3 | 19.0 | |
| 9 | 6 / 3 / 3 | 17.0 | |
| 10 | 6 / 3 / 3 | 15.5 | |

Tier balance is even and sensible. Start here consumes 15.5 to 19 of the 28 workbook minutes (56 to 68 %), so for a middle child Think harder is reachable for one or two questions and Go further and the Investigation only at home or by a fast child; they are stated as optional. Over-weighted: tens-and-ones re-teaching (L2, L3, L5, L6, L7 and L10 warm-ups all re-teach it, taking most of six 6-minute warm-ups) and add/subtract (5 of 10 lessons). Under-weighted: fact fluency within 20, comparing sets, number words, reading/writing numbers as words, word-problem reading (one lesson, which is squeezed by the check, F1).

### 3.6 Spiral review

Every lesson's Remember warm-up re-teaches what that lesson needs (this is the joining-cold design), not earlier lessons. Home practice (5 items) and online practice (13 or 14 items each) are current-lesson only (checked item by item above, L1 to L10). Consequences: L4 content (counting in 5s and 10s) appears next in check Q4; L2 (number line, number words) appears next in check Q2; L3 (two cards, greater) in check Q3; L9 ruler drawing in check Q9 after one week. There is no recap item, recap practice set or review slide before the check (F4). The spare-time menu uses the same three titles every week and does not review.

---

## 4. Routines, mascot, materials, workload, check, privacy, parent story, website

### 4.1 Consistency of routines

Consistent: the 11-part skeleton and minutes (Opening 2 or 4, Remember 6, Sneak-peek 4, Explore 14 or 16, Mini 10, Break 4, Workbook 28, Talk 6, Exit 6, Look-back 3, Flex 5; L10 differs on purpose); the sneak-peek wording ("Two sneak-peek puzzles: ideas we have not learnt yet ..." in 9 lessons); exit wording; look-back wording; "After question 3 you may choose" (7 lessons); "Spare-time menu" line (10 lessons); the REC cue structure; the "volunteers first, never call a name, no tallies" talk note; the `S/D/H` tutor tracker. Opening and "Remember" count-in-tens are identical in L1, L3 and L6.

Inconsistent or repeated:
- Opening greeting is "Good morning, inquirers!" in all ten lessons while the term timetable is undecided (the beta runs 9:00 am Tue/Fri; school-term children are likely to attend after school or at weekends) (Low, F24).
- Camera instruction varies: "Cameras on" (L1, L2, L3, L4, L6, L9), "Cameras on if you like" (L5), "Your camera may be off" (L7), "you may switch your camera off" in the same sentence as "Cameras on" (L1) (F9).
- Recording statement varies in length and place (F6).
- Opening for L2 to L10 skips the routine, rules, page-choice and paper-to-camera routines. They are only explained in L1; a joiner at L5 is told only "do not re-teach" (F20).
- The spare-time menu is the same three activities by title every week ("Is it always true?", "Make a puzzle for your grown-up", "Teach it back"; L10 renames the second). "Make your own puzzle" also appears as a Go further item, a home item or an online "selfcheck" in L2, L3, L4, L5, L6, L7, L8, L9 and L10; the parent "make a mistake on purpose" idea appears in L1, L2, L5, L6, L8, L9. Good as routine; stale by week 6 (Low, F26).
- "I will stamp your inquiry journal" is said at the exit in 9 lessons (L1 to L9) and appears in the speaker notes; no inquiry journal is in any materials list, workbook, parent page or plan (F22).

### 4.2 Mascot (Mi the dolphin)

Consistent and within the rule (at most 5 slides): exactly 4 slides per lesson (title large, Remember small, Look-back small, end large), tutor guide cover, parent page header, workbook page 1 corner. Mi never talks about answers or numbers. Lines are identical every week ("Hi, I'm Mi. Let's notice, test and explain why!" x10; "Great thinking today!" x9; "Take your time. You can pass." x10); L10 changes the end line to "this term". Only observation: titles differ between data and deck (deck L4 "100 Square Explorer" versus "The 100 Square Explorer"; deck L10 "Story Steps" versus "Story Steps: Read It Twice") (Low, F25). No finding on Mi itself.

### 4.3 Materials load and what a family must prepare each week

| Lesson | Child materials (summary) | Cutting | Pages printed (A4) | Needs ruler | "Next" line told parents (and truth) |
|---|---|---|---|---|---|
| 1 | about 50 small things, 6 hair ties/cups/string, pencil | bars (9) and squares (20) = 29 pieces | 6 workbook + 2 home + 1 parent | no | to L2: "pencil and paper only" (false: L2 needs 22 number cards cut from two kit pages, a toy) |
| 2 | 11 + 11 number cards, toy or coin | about 22 cards | 7 + 2 + 1 | no | to L3: "pencil and paper only; keep the cards" (false: L3 needs 20 digit cards and bars/squares) |
| 3 | digit cards 0 to 9 x 2, bars and squares | 20 cards (plus kit re-use) | 7 + 2 + 1 | no | to L4: "pencil, paper, two or three colouring pencils" (incomplete: printed 100 square and about 12 counters) |
| 4 | printed 100 square, about 12 counters, colours | none | 6 + 2 + 1 | no | to L5: "pencil and paper only" (false: kit, about 20 small things of two kinds) |
| 5 | about 20 things of two kinds, ten-frame drawn by grown-up or tens bar | kit page again (L1 pieces re-usable) | 6 + 2 + 1 | no | to L6: "pencil and paper only" (false: the kit) |
| 6 | kit, about 30 small things (home) | kit page again | 6 + 2 + 1 | no | to L7: "the kit, a pencil and paper" (true) |
| 7 | kit, second colour pencil, envelope | kit page again | 6 + 2 + 1 | no | to L8: "pencil and paper only" (false: about 30 things, two plates marked LEFT and RIGHT) |
| 8 | about 30 things, two plates, kit (optional) | kit page again | 6 + 2 + 1 | no | to L9: ruler (true; also 10 paper clips and 3 to 4 objects) |
| 9 | cm ruler, clips, 3 to 4 objects | none | 5 + 2 + 1 | yes, all of Start here | to L10: "pencil and paper only" (false: ruler, about 20 counters, the 4-page check sheet printed at 100%) |
| 10 | about 20 counters, ruler, check sheet, a way to photograph 4 pages | kit page | 6 + 2 + 1 + 4 check + 1 note | yes (check Q9) | to L11: counters (true) |

Term totals for a family: about 61 workbook pages + 20 home + 10 parent + 5 check = about 96 A4 pages (about 48 sheets double-sided), colour used on headings, tens bars and highlights but legible in black and white; about 80 pieces cut by an adult in L1 to L3; no purchase except possibly a ruler and a printer (F12, F13).

### 4.4 Total workload per child per week

Live lesson 90 minutes. Take-home: Parent Summary "Try at home (5 minutes)" (3 activities), Home Practice "about 15 minutes, a few days after the lesson" (5 items, H5 usually needs 30 to 50 objects or a ruler), online practice (13 or 14 items, no timer), workbook pages 3 to 5 if unfinished (Think harder 12 to 18 modelled minutes, Go further 16 to 18, Investigation). A conscientious family can reach about 3 hours per week for a 6-year-old; nothing says what is expected, and the Terms say only "10 lessons of 90 minutes" (F14).

### 4.5 End-of-term check against lessons and the parent report line

Items map one to one to Start here ideas of L1 to L10 (checked item by item; the maths is right; "fresh numbers" are chosen so they do not repeat a lesson page). Issues are in F1 (time), F5 (evidence for the report), F12 (ruler), F10 (privacy flow). Additional observations:
- The term line "learning to see numbers as tens and ones, to notice patterns and to say why" is pasted as `term_line` on all ten Parent Summaries, including L9 (length) and L10 (stories), and no check question asks a child to say why.
- Strand "Numbers, tens and ones" is Q1 to Q4 (4 points), "Adding and taking away" Q5 to Q8, "Measuring length" Q9 alone, "Reading and solving stories" Q10 alone. For a one-question strand the key gives right = "Showing this often", partly = "Getting there", wrong = "Just beginning". The note text then names skills ("starting the next step from the last answer", "finding numbers on a number line") that no single item isolates.
- Question 10 and the L10 exit ticket test the same idea at the same level; the optional Think harder question ("who is in the line") is never scored, so the "Think harder" half of the term is not assessed at all.
- Reading load: the tutor reads page 3 (Questions 6 to 9, four questions with 7 parts) in one go before work time; a 6-year-old cannot hold that in mind and the sheet's text is for a reader.

### 4.6 PDPA and safeguarding consistency across documents

| Topic | Lessons / guides | Privacy notice (beta draft) | Terms (draft) | Issue |
|---|---|---|---|---|
| What is recorded | "me and the screen only" (L1 to L4, L6 to L10 in the SAY line; L5 NOTE only) | tutor and shared screen; "a child's voice may be heard if they speak"; "children's names are not shown"; parent can ask us to mute | "Lessons are recorded so a child who misses can catch up" | Scripts never say voices are captured; openings greet each child by first name in the recorded audio; ASK lines make children answer aloud (F6). |
| Telling the group | each opening (L5 only a NOTE) | "We tell the group at the start of each lesson" | refers to the notice | L5 does not script it (F6). |
| Cameras | on / if you like / may be off | "Children may keep their cameras off" | "A device with a camera" | Scripts need the tutor to see hands, pages and rulers; no fallback when a camera is off (F9). |
| Papers to the camera | "at the same moment ... so only you see it"; "no board held up in front of the group" | not covered | not covered | Untrue on a normal group call; and the L10 check uses the opposite rule (flat on table) (F7). |
| Private chat, private messages, 1:1 | none, validator enforces | tutor does not message children | same (section 10) | Consistent. The "tutor never sits alone with one child" rule appears only in the L10 key, for the make-up slot. |
| Still stuck | tick on look-back; check-in "in the open session next lesson, a quick visit to the shared room or a hand signal" | not covered | "check-ins go to the whole group or the parent" | The look-back is "never collected" so the tutor cannot know who ticked; "shared room" is undefined and there are no breakout rooms (F8). |
| Photos of work | L10: parent sends 4 pages with the child's name to the business WhatsApp +65 9880 5962; tutor marks there; photos deleted after the note; record sheet deleted | "photos of your child's work ... 90 days after the program ends"; names WhatsApp only for messaging | "we also keep photos" | The term-time flow is not described; WhatsApp business is a processor not named for photos; retention in key (delete after note) differs from notice (F10). |
| Recording access and retention | "your tutor will share a private link with enrolled families" | same group only; 30 days after the group's last lesson | other classes may be attended | A term group continues for four terms; "30 days after the last lesson" is undefined for a rolling term programme; a make-up slot after the term may be after deletion (F10). |
| Contact route | Parent Summaries L1 to L9 have none; L10 business WhatsApp | data protection contact "Jasmine Hon, [pypteltd@gmail.com, to be changed later]" | WhatsApp +65 9880 5962 | Three routes in three documents (F10). |
| Make-ups | L10 "make-up slot, small group, parent beside the child" | not covered | beta: "There are no separate make-up lessons"; term: same lesson in another class or holiday class if a seat is free | The make-up slot is not in the terms (F10). |
| Tutor trackers | S/D/H per child (exit ticket) in 9 lessons; record sheet in L10 | "short progress notes" | | Retention of the S/D/H tracker is not stated (Low). |

### 4.7 The term's story for a parent (what will my child be able to do after 10 weeks?)

There is no Term 1 overview for parents; the story has to be assembled from ten one-page summaries and the L10 note. A fair reading of the objectives: a child who attends all ten lessons and does Start here can say a two-digit number as tens and ones, find it on a number line, compare and order two-digit numbers, count in 2s, 5s and 10s and use the 100 square, add within about 50 by making a ten, add and subtract tens and small numbers mentally, take away and count up to find a gap, use "=" as "the same amount", measure and draw to the nearest centimetre and write one number sentence per step of a two-step story. Claims that are not supported by the material: "to say why" (practised in Talk time and the Investigation, never assessed); "notice patterns" (one lesson); "tens and ones" as the lens for all ten weeks (L9 and L10 do not use it); and the unsaid implication that Start here is within reach of any child who can count to 20 (F3). The beyond-P1 sentence is on every Parent Summary (as the owner decided) and is honest, but it is word-for-word boilerplate that tells parents what is true and not what to do if their child finds Start here hard (F18).

### 4.8 Fit with `website/terms.html`, the website and owner decisions

- Terms section 7 (term programme): 10 lessons, places open every term, pro-rated fee, 5 % for paying in full, instalments after lessons 3 and 6, holiday graduates follow the calendar. The lesson set matches (10 lessons, one a week implied by "a few days after the lesson"). The fee is still "[S$ per term]".
- Terms section 3 and 9: "workbook is a PDF you print yourself. Printing costs are yours" and "the materials listed before the first lesson". The level page (holiday) says "We post the printed workbook and kit to your home", the lessons assume self-print at 100% (ruler figures, 10 cm check bar), and no "list before the first lesson" exists (F2, F11, F13).
- Owner decision 3 (make-up days) and Terms section 5/7 (watch the recording, other class or holiday class) versus L10 "make-up slot" (F10).
- Owner decision "keep the stronger arithmetic, say plainly it goes beyond P1, no MOE-aligned": the tutor guide `moe.note` and the Parent Summary say it in all ten lessons. The tutor-prep checklist tells the tutor to say it to families plainly in only L1, L2, L3, L5 and L10 (F29). The website syllabus page still says Level 1 Start here is "At the Primary 1 level ... Almost all use Primary 1 skills" (written for the holiday course), which contradicts the Term 1 decision if read as covering the term (F11).
- Owner decision 5 and Terms: group size up to 8; Terms say a group runs with at least 4. The lesson design (no breakout rooms, whole-group talk) works for 4 to 8.
- Owner decision 6 (contest items at Think harder): kept.
- The end-of-term check: 20 minutes and business WhatsApp return per the owner; timing and privacy detail in F1, F10.

---

## 5. Findings

IDs are used in the summary. Severity per the project scale.

### 5a. High and Medium

**F1. High. The end-of-term check cannot be done in 20 minutes, and its slot squeezes Lesson 10.**
- Location: `lessons/l10.json` timing (Exit ticket and check 24 min, minutes 59 to 83), `end_of_term_check`; `L10_Tutor_Guide.pdf` part table and script from s-check1; `L10_Check_Tutor_Key.pdf` section 2 (quiet work 3 + 4 + 5 + 4); `L10_Check_Parent_Note.pdf` ("about 20 minutes").
- Evidence: 10 questions, 22 answer slots, one ruler drawing and one number-line reading. Using the lessons' own middle-child `mins` for the same Start here items (1.5, 2.5, 3, 3, 2.5, 3, 3, 3, 2.5, 3) the writing alone is about 27 minutes. The key schedules 16 minutes of quiet work; the guide script models 11:40 of child time. Reading aloud is lockstep by page (page 3 reads Questions 6 to 9, seven parts, in one go). A slow child is cut off ("Turn to page 2"), against "not a race". The exit ticket (3 items) duplicates check Q10 (two-step story) and costs about 4 minutes. The check takes 24 of 90 minutes, leaving the one word-problem lesson Explore 10, Mini 10, Workbook 20 (of which Start here is the whole workbook) and a 4-minute Talk, so "reading traps" and "reversed wording" are taught in about 25 minutes. The slow-class validator figure for the exit part is 24:57 against 24:00.
- Fix: choose one of: give the check 25 to 28 minutes and move the exit ticket out (drop it, or fold it into check Q10); let children work at their own pace after the tutor has read each page, with a visible finish clock; cut to 8 questions, moving Q9 and Q10 to the make-up slot; or take the check in a separate 30-minute session as the plan's "make-up slot" allows. Reconcile the key (16 min), guide (11:40) and note (20) into one table. Restore Explore and Mini time for the story lesson.

**F2. Medium. "Next lesson" materials lines are wrong in 7 of 9 hand-offs, and no pre-lesson family note exists.**
- Location: `parent.next` in l01 to l09 and the Flex SAY ("Next lesson is ... You need only a pencil and paper") in l01, l02, l04, l05, l07, l09; table in section 4.3. Parent Summary "Things to have ready" is on a post-lesson page ("What we did"). Tutor_prep says "Tell parents a week before" in every lesson but there is no template for it (only L10 has `L10_Check_Parent_Note.pdf`).
- Evidence: L1 to L2 says pencil and paper only, L2 needs 22 cut-out number cards and a toy; L2 to L3 same, L3 needs digit cards and bars/squares; L4 to L5, L5 to L6, L7 to L8, L9 to L10 likewise; L3 to L4 omits the printed 100 square and counters. The tutor's spoken goodbye repeats the same understatement to the children and any adult listening. Terms section 9 promises "the materials listed before the first lesson".
- Fix: generate `parent.next` and the goodbye SAY from the next lesson's `materials.child` (and `kit_pages`); add a one-page "Before Lesson N" note (print, cut, find, ruler, scale) sent a week before; add a "Term 1 kit and print pack" before L1 (see F13).

**F3. Medium. "Joining cold: all you need is counting to 20" is overstated, untested, and there is no entry check.**
- Location: `joining_cold.assumes` and the Remember NOTE in l02 to l10; plan section 2 Term 1 note; plan open question 2; website placement check; `hub/parent_questions.html` (school P1 term 1: numbers to 10 and 20).
- Evidence: the warm-up is 6 minutes with 12 to 13 quick questions (e.g. L7: bars and squares, bonds to 10, count on in tens, how far to the next ten), after which Start here asks 68 - 25 (S3), 46 - 12, 64 - 21 and a bus-seats story; L5 Start here has 47 + 6 and 35 + 7; L8 S7 is a two-digit sum; L10 S5 adds 23 + 33. A child who has never met tens and ones, number words in tens (forty, fifty), or bars and squares meets them in the warm-up and is expected to use them within 10 minutes. Equally the warm-ups of six lessons repeat the same re-teaching, so a child who attended gains nothing from it. No document states a minimum entry skill (for example "counts to 100 by tens, bonds to 10, reads two-digit numbers") and none offers an entry check; the placement diagnostic on the website belongs to the holiday course and is "scored out of 10".
- Fix: state a realistic entry profile and test it (5-minute check at sign-up); keep the warm-up claim but add a lesson-specific "if you joined late" catch-up page (recording chapter, two pages, three practice items); trial two cold joiners at L5 and L7; reduce Start here steps for L7 and L10 first-time items or mark them honestly.

**F4. Medium. No spiral review.**
- Location: all `home_practice` and `online_practice` items (current lesson only); Remember warm-ups; L10 mini-lesson; `spare_time`.
- Evidence: see section 3.6. Check Q2, Q3, Q4 content was last practised in weeks 2, 3 and 4; Q9 in week 9.
- Fix: add one review item to each Home Practice from lesson n - 2 or n - 3; one "from earlier" minute in the Remember warm-up from L5; an online "Term 1 recap" set (the runner already supports sets) released before L10; keep it neutral (no score).

**F5. Medium. The check and the progress note claim more than the evidence supports.**
- Location: `L10_Check_Tutor_Key.pdf` sections 4 to 6; `parent.term_line` in all ten lessons.
- Evidence: see section 4.5. Two of four areas are one question each; the band cut-offs for a one-question strand are right / partly / wrong; the note text asserts specific skills; "to say why" is never assessed; all items are Start here; Q9 depends on the child's ruler and printed scale, and a photo of a pencil line is judged against a 10 cm printed bar (57 to 63 %).
- Fix: report only the two larger areas as bands, give length and stories as one sentence each from tutor notes; add one "explain why" item to the check or drop "to say why" from the term line; keep Q9 but accept the grown-up's measurement; do not describe a single item as a skill band.

**F6. Medium. Recording statements are inconsistent across scripts, notice and terms.**
- Location: Opening SAY/NOTE in l01 to l10; `website/privacy.html` "How lessons are recorded".
- Evidence: L5's Opening SAY has no recording sentence ("Cameras on if you like ...") and a NOTE says "Remind the group once ... that the lesson is recorded"; L3 says "We record me and the screen only" but not "recorded"; L2, L4, L6, L7 and L9 differ again. The notice says voices may be heard, names are not shown, a parent may ask for a child to be muted and "we tell the group at the start of each lesson that it is being recorded". Scripts say "me and the screen only" (no mention of voices), tell the tutor to greet "each child by first name" (L1 to L8) in the recorded opening, and the Remember and Talk parts have children answer aloud (the tutor repeating answers "in their own words" is not in any script).
- Fix: one fixed 3-sentence recording statement in every Opening SAY (recorded, tutor and screen, children's voices may be heard, tell us if you would like your child muted); greet by first name only before recording starts or use no names; add "repeat the child's answer in your words" to the ASK routine; align the notice wording ("names are not shown" is not true of audio).

**F7. Medium. "Hold your paper to the camera ... so only you see it" is not true on a group call and contradicts "no board held up in front of the group".**
- Location: HOLD lines in every lesson (sneak-peek, exit), L1 exit READ/slide note ("so only the tutor sees it"), safeguarding bullet 3 in all ten lessons; L10 check uses "paper flat on the table, never held up".
- Evidence: on a gallery-view call every family sees the same tiles; handwriting is visible next to the child's name label; the tutor has to read 8 papers at the same moment (1 to 2 seconds each). The rule "never read out a child's name with a right or wrong answer" is in practice undone for any wrong answer visible with a name tile.
- Fix: replace with a mechanism that is private by design: tutor asks children to hold up fingers or a coloured card for choices; or the child tells a grown-up who whispers "yes" to the tutor through the "thumbs" signal; or take papers by photo to the business number (as L10 already does) for the exit ticket; if kept, say truthfully that the group can see and keep names off.

**F8. Medium. The "I am still stuck" mechanism contradicts the privacy rule it sits beside.**
- Location: look-back block (all lessons), safeguarding bullet 5, guide "IF STUCK" lines.
- Evidence: the look-back "is never collected or read out in front of the group", yet "a child who ticks still stuck gets a check-in in the open session next lesson (a quick visit to the shared room or a hand signal)". The tutor cannot know who ticked, and there are no breakout rooms ("main room only"), so "visit to the shared room" is undefined. For L10 the check-in is "at the start of Term 2".
- Fix: say what actually happens (for example: the child shows the tick to a grown-up, who may message the business WhatsApp; tutor greets the whole group with a catch-up minute); delete "quick visit to the shared room".

**F9. Medium. Camera rules conflict.**
- Location: Opening SAY in L1 to L10; privacy notice ("children may keep their cameras off").
- Evidence: "Cameras on, pencil ready ... You may switch your camera off whenever you like" in one breath (L1, L2, L4, L6, L8, L9); L5 "Cameras on if you like"; L7 "Your camera may be off". Several routines depend on the tutor seeing hands, a page, a ruler or a paper; the L10 check requires "cameras show the child and the table".
- Fix: decide: cameras on for the lesson except by arrangement, with a one-line fallback (parent types or tells the tutor at the end); say the same sentence in every opening.

**F10. Medium. Privacy notice, terms and parent pages do not yet cover the term programme.**
- Location: `website/privacy.html` ("November beta"), `website/terms.html` sections 5 and 7; Parent Summaries L1 to L9; L10 check note and key.
- Evidence: section 4.6 table: WhatsApp photo return of check pages with names is a new data flow; retention is "30 days after your group's last lesson" (undefined for a continuing term group; recordings may be gone before a make-up check); the check key deletes photos once the note is sent, the notice says 90 days; no contact route on nine Parent Summaries and three different routes in three documents; "no separate make-up lessons" (beta) versus a make-up slot for the check; the L10 key's "tutor never sits alone with one child" appears nowhere else.
- Fix: a term-time privacy section and terms update (check photos, retention per term, contact, make-up); the same two-line contact box on every Parent Summary.

**F11. Medium. Website pages disagree with the term programme.**
- Location: `website/level_pages/ages-6-8.html`, `website/syllabus/index.html`, `website/terms.html` section 3 and 7.
- Evidence: the Level 1 page describes the ten holiday lessons (frog, bonds, fruit party ...), "We post the printed workbook and kit to your home", lists "a mini whiteboard and marker" and scissors (Term 1 uses paper and tells children not to use scissors), and prices S$25 a lesson; the syllabus page says Level 1 Start here is "At the Primary 1 level ... Almost all use Primary 1 skills"; the term fee is "[S$ per term]"; the only mention of Term 1 is Terms section 7.
- Fix: a Term 1 page (ten lesson titles, what the child can do, what you print, what you need, beyond-P1 sentence); limit the syllabus claims to what was checked for each programme; set the fee.

**F12. Medium. A centimetre ruler is a hard dependency with no fallback.**
- Location: `materials.ruler` in l09 and l10; AUTHORING ("else a printed ruler on the kit page"), plan row 9, `README.md` ("printed ruler only if the child has none"), AUTHORING later section ("never a cut-out: families use their own ruler (owner decision)").
- Evidence: L9 Start here S1, S2, S3, S4, S5, S6 and warm-up all need the ruler; L10 check Q9 needs it; the guides' fallback is "a grown-up can look for any straight-edged ruler or strip marked in centimetres, or tell the tutor". The check sheet already prints a 10 cm scale bar, so a printed paper ruler is feasible. AUTHORING contradicts itself on the printed ruler.
- Fix: add a paper cm ruler to the L9 kit page with a scale check (reusing the check's 10 cm bar), or put "a ruler (about S$1)" in the pre-term pack; correct AUTHORING.

**F13. Medium. Print and cutting load is undeclared and inconsistent.**
- Location: `materials.kit_pages` and `child` in L5 to L8; parent "Things to have ready"; Terms section 3.
- Evidence: about 96 A4 pages a term; L1 29 pieces, L2 22, L3 20 cut by an adult; page 6 (the same bars and squares) is reprinted in L1, L3, L5, L6, L7, L8 and L10, with "cut out before the lesson" (L5, L7, L8) against "the same cut-outs as Lesson 1, keep them in an envelope" (L6, L7). Terms say printing costs are the family's; nothing states colour needs or paper count.
- Fix: one printed kit set for the term (bars, squares, number cards, digit cards, 100 square, ten-frame, ruler) on 3 pages sent before L1; tell families which pages to print each week (usually 1 to 5).

**F14. Medium. Home workload and online practice access are undefined.**
- Location: Parent Summary "Try at home (5 minutes)", Home Practice header ("About 15 minutes, a few days after the lesson"), Home Practice page 2 ("ask your tutor for the practice link, key t1l01"), `online_practice` (13 or 14 items).
- Evidence: section 4.4; the internal key is shown to parents; no document says who sends the link or when.
- Fix: one sentence: "Our ask each week: the 5-minute games and Home Practice if you like; pages 3 to 5 and online practice are optional". Replace the key with a link or QR code once hosting is decided.

**F15. Medium. Timing is feasible only on optimistic child-response assumptions and a consumed buffer.**
- Location: `script` `resp` values; validator "slow" tables; `common.py` model; `docs/audit/timing_p1.md`.
- Evidence: every ASK in warm-ups waits 12 s (25 s in L1's opening); the project's own rubric uses 30 s. Recomputed with 30 s per question and 25 s per slide change, Remember needs 6.2 to 9.8 minutes in all ten lessons against 6 (L10 9.8). The validator's slow scenario gives Workbook 29:56 to 32:01 against 28 in every lesson, and totals of 84:59 to 89:06 (L3 89:06, L9 89:00) with the Flex part counting only 0:36 to 0:43 of its 5 minutes as spoken; so the "buffer" is also the contingency for the slow workbook, and the spare-time menu (3 to 5 minutes) is not available in a slow class.
- Fix: measure in the trial (risk 1 and 2); if confirmed, cut one warm-up question group per lesson or lengthen Remember to 7 minutes taken from the Opening of L2 to L10.

**F16. Medium. The tutor console is not wired to Term 1 and the live-tutor load is high.**
- Location: `tutor/README.md`, `tutor/build_data.py` (builds `split/*/project` holiday decks and `budget.json`), `tutor/data` (p1l1 ... p6l10, no t1l01).
- Evidence: the console serves the 60 holiday lessons; the term decks are at `term/l1/out/lNN/deck/project` but not ingested; there is no `t1l` index. The lesson design has the tutor read eight tiles for papers, run the deck, watch eight cameras (no breakout rooms), run the recording, keep the clock and read about 25 ASK/READ lines per part.
- Fix: add the term decks to `build_data.py` (IDs t1l01 to t1l10) before the trial or say how the trial will run without it; plan a second adult (co-host) for the first three live lessons.

**F17. Medium. Coverage choices that need an owner decision.**
- Location: section 3.2.
- Evidence: no practice of addition and subtraction facts within 20 (a P1 outcome and a SASMO Section A staple); number words only in L2; comparing sets only one item; vertical algorithm question open (plan open question 3) while school starts the algorithm in Term 2; five of ten lessons in add/subtract.
- Fix: decide (a) a 2-minute fluency routine in the warm-up of L5 to L10 or accept the gap and tell parents; (b) answer open question 3; (c) one more word-reading item in L3 or L4.

**F18. Medium. The parent story is assembled from boilerplate, and one line is pasted onto all ten lessons.**
- Location: `parent.term_line` (all ten), `parent.summary` (beyond-P1 sentence in all ten), no Term 1 overview.
- Evidence: section 4.7.
- Fix: a Term 1 "what your child can do" half page (supported claims only); replace the pasted term line by a lesson-specific line; add one sentence to the beyond-P1 statement on what to do if Start here is hard ("it is fine to use the kit, or to leave pages 3 to 5").

**F19. Medium. Tier and prerequisite drift in the arithmetic block.**
- Location: `l08.json` S5 and S7; `l07.json` S3, S4, S7; `l10.json` S5; plan row 8.
- Evidence: plan row 8 puts compensation at Think harder; L8 S5 has "34 + 5 = 35 + []" and "61 + 8 = 60 + []" (a one-for-one shift) and S7 "35 + 12 = [] + 2" at Start here. L6 T1 and T2 (34 + 25, 68 - 24) are Think harder in L6 but the same skill is Start here in L7, L8 and L10. `safe_to_miss` is true for L2, L3, L4, L9 and false for L1, L5 to L8, L10, but L6 is not named as a prerequisite of L7, L8 and L10 (L8's note is about L19).
- Fix: move L8 S5's last two parts to Think harder or add the scaffold plates (the lesson already provides plates); state L6 as a prerequisite in L7, L8 and L10 `joining_cold.note`.

**F20. Medium. A joiner never learns the routines.**
- Location: Opening NOTE in L2 to L10 ("Lessons after the first skip the routine and rules slides"; L5: "do not re-teach them"); L1 routine and rules slides.
- Evidence: the four inquirer rules, the page-choice rule ("you may choose Think harder"), paper-to-camera, look-back ticks and the "still stuck" tick are explained only in L1 (and L2 says the three rule words once). A child who starts at L5 (or Term 2) never hears them; the guide says only "if someone has joined who missed it ... say it in one sentence".
- Fix: a 60-second "new here?" routine card in every Opening NOTE, and a recorded 3-minute "how our lessons work" clip (the L1 opening) linked in the pre-lesson note.

### 5b. Low

**F21. Low. L9 validator WARN left unresolved.** `validate.py 09` says "workbook page 5 overflows (102%) and will spill onto an extra page" while the built PDF is 5 pages at 91 % (the WARN is an estimate); the fix commit and the guide do not mention it.

**F22. Low. "I will stamp your inquiry journal" (exit, nine lessons; guide and notes).** No journal exists in any materials list, workbook, parent page or plan; leftover from the holiday course. Remove or create the journal.

**F23. Low. L1 rubber bands.** Guide tutor materials: "a tray of 30 lolly sticks or straws with three rubber bands"; child materials list rubber bands; safeguarding bullet: "Use hair ties, cups or paper rings, not stretched rubber bands that can flick".

**F24. Low. "Good morning, inquirers!" in all openings.** The term timetable is undecided (the beta runs 9:00 am; school-term children will probably attend after school or at weekends). Use "Hello".

**F25. Low. Title drift.** Deck title slides "100 Square Explorer" (L4) and "Story Steps" (L10) differ from the lesson titles.

**F26. Low. Stale routine content.** The same three spare-time titles every week, identical Mi lines, "make your own puzzle" and "mistake on purpose" repeated across at least six lessons, three identical count-in-tens openings (L1, L3, L6). Vary by lesson.

**F27. Low. Documents out of date or contradictory.** `term/l1/README.md` says only Lesson 1 is complete and L2 to L10 are "to be written"; AUTHORING contradicts itself on the printed ruler (F12); `FIXES_L10.md` exists but the first-round list in the brief names L01 to L09 only.

**F28. Low. Missing apostrophes in the safeguarding text.** L4: "the child own paper", "Never read out a child name", "children video excluded", "child page"; L4, L6 and L7: "I am still stuck gets a check-in" (quotes dropped). Visible in the guide PDFs.

**F29. Low. Tutor-prep omits the beyond-P1 reminder in L4, L6, L7, L8 and L9** (present in L1, L2, L3, L5, L10), although each `moe.note` and Parent Summary carries it.

**F30. Low. `safe_to_miss` notes cite warm-up re-teaching that is not there.** L3 says comparing two-digit numbers "comes back in Lessons 5 to 7, and each of those warm-ups teaches it again" (no warm-up in L5, L6 or L7 teaches comparison); L2 says L6's warm-up re-teaches the number line (it counts in tens on tiles; the number line is taught in the L6 Explore).

(Counts: High 1 (F1); Medium 19 (F2 to F20); Low 10 (F21 to F30).)

---

## 6. What is good and should not be changed

- The 11-part skeleton, the sneak-peek / talk / exit loop, and the REC cues are consistent and short.
- Tier discipline: contest moves are tutor-only labels and none sits at Start here; Investigation has an easy first step.
- No claims of MOE alignment, GEP, SASMO or ranks on any child or parent page; the beyond-P1 sentence is present on all ten Parent Summaries.
- Mascot use is restrained and consistent.
- Safeguarding core is consistent: no private chat or message, no breakout rooms, no read-out of names with answers, look-back never read out, the L10 key's private-return procedure is careful and specific.
- Maths in every item I recomputed is correct.

---

## 7. Instrument scores (term as a whole)

Instrument A (12 criteria x 0-2, as in `docs/audit/reaudit_p1.md`), term-level: 1 low floor / high ceiling 2; 2 depth over speed 1; 3 generalise 2; 4 justify 1; 5 multiple paths 1; 6 challenge ladder 2; 7 student-led inquiry 1; 8 complexity / context 1; 9 problem posing 2 (puzzle-making in home, menu and G items); 10 metacognition 2 (look-back every lesson); 11 pacing / compacting 1; 12 extension not acceleration 1 (the arithmetic block accelerates). **Total 17/24.**

Term-fit score per lesson (my own 6 dimensions, each 0-2, max 12): D1 plan/strand fit, D2 prerequisites and cold joining, D3 materials and workload, D4 routines and safeguarding consistency, D5 hand-off and document consistency, D6 timing realism. These are judgement scores for comparing lessons, not the project instrument.

---

## 8. Lesson-by-lesson matrix

| L | Title | S/T/G | Script / slow total | Slow workbook | Materials burden | "Next" line accurate | D1 D2 D3 D4 D5 D6 | Term-fit | Key term-level issues | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Bundles and Singles | 7/4/3 | 74:20 / 88:18 | 31:47 | about 50 things, hair ties, 29 cut pieces | no (says pencil only; L2 needs cards and toy) | 2 2 1 1 0 1 | 7/12 | F2, F6, F7, F9, F23; routine and rules only here (F20) | Ready after minor fixes |
| 2 | Number Words and the Number Line | 8/4/3 | 74:34 / 88:27 | 31:34 | 22 cards to cut, toy | no (L3 needs digit cards and bars) | 2 2 1 1 0 1 | 7/12 | F2, F6; new-topic syllabus check still open; F30 | Ready after minor fixes |
| 3 | Digit Cards | 8/4/3 | 75:06 / 89:06 | 32:01 | 20 cards, bars and squares | partly (omits 100 square, counters) | 2 1 1 1 0 0 | 5/12 | tightest slow total (0:54 slack); F30; F2; F19 | Ready after minor fixes |
| 4 | The 100 Square Explorer | 6/4/3 | 73:11 / 86:51 | 31:20 | 1 printed page, 12 counters, colours | no (L5 needs kit, things) | 2 2 2 1 0 2 | 9/12 | F2, F28 (apostrophes), F25; safest lesson to miss as planned | Ready after minor fixes |
| 5 | Make-a-Ten Adding | 7/4/3 | 71:36 / 84:59 | 30:46 | 20 things of two kinds, ten-frame | no (L6 needs kit) | 2 1 1 0 0 2 | 6/12 | F6 (no recording sentence), F2, F13 | Ready after minor fixes |
| 6 | Tens Jump, Ones Hop | 7/4/3 | 74:38 / 88:33 | 31:34 | kit, about 30 things | yes | 2 1 1 1 2 1 | 8/12 | F19 (T becomes S in L7 to L10), F28 | Ready after minor fixes |
| 7 | Take Away, Count Up | 7/4/3 | 73:03 / 86:43 | 31:20 | kit, colour pencil, envelope | no (L8 needs plates, things) | 2 1 1 1 0 2 | 7/12 | S3 68 - 25 after warm-up (F3), F19, F28 | Ready after minor fixes |
| 8 | Balance and Swap | 7/4/3 | 72:24 / 85:45 | 29:56 | 30 things, two plates, kit | yes (ruler) | 1 1 1 1 2 2 | 8/12 | F19 (S5 shifts, S7 needs L6 T) | Ready after minor fixes |
| 9 | Draw and Measure | 6/3/3 | 75:05 / 89:00 | 31:41 | ruler (no fallback), clips | no (L10 needs ruler, counters, check sheet) | 2 1 0 1 0 1 | 5/12 | F12, F21, F2 | Ready after minor fixes |
| 10 | Story Steps: Read It Twice (and the check) | 6/3/3 | 74:49 / 88:25 | 20:07 (of 20) | check sheet 4 pages at 100%, ruler, 20 counters, photo return | n/a (to L11, accurate) | 1 2 0 1 1 0 | 5/12 | F1 (High), F5, F10, F12 | Needs rework |

Term verdict: Lessons 1 to 9 Ready after minor fixes; Lesson 10 Needs rework; family-facing layer needs rework before launch (F2, F6 to F14, F18).

---

## 9. Not audited here

- Slide-by-slide deck legibility, speaker notes and guide wording (GUIDE_DECK role).
- The online practice runner in Playwright, typed-answer handling and accessibility (HOME_PARENT_PRACTICE role).
- Whether the lesson times fit a school-term timetable and which day the term runs.
- Any child's reaction; every score and estimate above is desk judgement.
