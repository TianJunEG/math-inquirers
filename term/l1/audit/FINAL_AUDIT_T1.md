# Final independent audit: Level 1 Term 1 (Lessons 1 to 10), current built state

Audit only. No lesson, tool or output file was edited. Date 23 Oct 2026, branch `claude/great-fermi-1hv4vc`. Severity: High = wrong maths, unsafe, unusable, or a release gate broken; Medium = misleading, inconsistent, impractical; Low = polish.

## 0. Method, instruments, limits

Read: AUTHORING (key rules), WORDING_GUIDE, all owner decisions, TERM_WIDE_AUDIT, CUTOUT_AUDIT, FIXES*/FIXES4 notes, plan section 8, the P1 paper patterns, privacy.html and terms.html.

Run: `validate.py 01..10` and every `verify/l01..l10_checks.py` (via a runner that calls `run(d)`).

Looked at (re-rendered with pdftoppm): all pages of the L3, L9 and L10 workbooks; page 1 and one Think harder or Go further page of L1, L2, L4, L5, L6, L7, L8, plus the L2 kit page and the L6 kit page; contact sheets of the L3 and L10 decks; the L10 Quest Log, Quest Parent Note and Quest Tutor Notes text; L5 Parent Summary and L9 Home Practice text; the Book 2 cover, contents and a kit page, and a Mi crop from Book 1 (L3) and Book 2 (L10). Answer keys read as text for L3 and L9.

Not done (honest limits): I did not render every slide of every deck, every guide page or every key page; I did not run the online practice in a browser; no child was observed; ruler/real-size claims were judged from the book spec (`content_scale` 0.9429), not measured on paper.

Instruments (as before): Instrument A (12 criteria x 0-2, max 24, `reaudit_p1.md`) at term level, and the term-fit score D1 to D6 per lesson (D1 plan/strand fit, D2 prerequisites and cold joining, D3 materials and workload, D4 routines and safeguarding consistency, D5 hand-off and document/output consistency, D6 timing realism; each 0-2, max 12). D scores are judgement scores for comparing lessons, not the project instrument.

## 1. Summary

**Verdict: Term 1 is close, and much better than the second-round audit found it, but it is not releasable as built because of two High findings that are one root cause (a failing validator copy check blocks rebuilds of L3 and L10, so those two lessons, and the paid Book 1 and Book 2, still carry the old Mi with a calculator).** The mechanical fix is small. After it, Lessons 1 to 10 are all "Ready after minor fixes".

Counts: **2 High, 12 Medium, 9 Low** (section 4).

Instrument A, term level (12 x 0-2): low floor/high ceiling 2; depth over speed 1; generalise 2; justify 1; multiple paths 1; challenge ladder 2; student-led inquiry 1; complexity/context 1; problem posing 2; metacognition 2; pacing/compacting 1; extension not acceleration 2 (every lesson now names a beyond item at Think harder or Go further). **Total 19/24** (was 17/24).

Maths: I independently solved every workbook item of L3, L9, L10 and the L10 Quest, and the Start here, Think harder and Go further items of L5, L7, L8, and the Think harder and Go further items of L1, L2, L4, L6 (about 130 items, including all new beyond items: L3 G2c = 6, L10 T4 impossible story, L9 G1/G2, L2 G2 meet on 40, L4 G1/G2/G3, L6 G2 five jumps). **No wrong answer found.** All keys I read agree.

Script results:

| Lesson | validate.py | verify script |
|---|---|---|
| 1, 2, 4, 5, 6, 7, 8, 9 | 0 FAIL (5 to 8 slow-class timing WARN each) | PASS (155, 448, 789, 422, 357, 113, 2612, 178 checks) |
| 3 | **FAIL (exit 1)**: copy: 7-word overlap with `docs/books/p1_non_routine_catalogue.md` | PASS (304 checks) |
| 10 | **FAIL (exit 1)**: same check, 2 FAIL lines | **FAIL**: the script raises the same 7-word overlap error, so its answer checks do not complete |

## 2. Earlier High and Medium findings: current status (TERM_WIDE_AUDIT F1 to F20, plus CUTOUT_AUDIT)

| Earlier finding | Status now |
|---|---|
| F1 High: L10 check did not fit 20 minutes | **Fixed.** Replaced by Mi's Challenge Quest (8 gates plus optional cave, all Start here level, about 16 minutes middle child, slot minutes 63 to 83, parts sum to 90). I solved all gates: correct. |
| F2 Medium: wrong "next lesson" materials, no pre-lesson list | **Fixed** for 8 of 9 hand-offs (`parent.next_materials` is truthful and matches the next lesson's kit). Gap left: L7 to L8 omits the L8 kit page (finding 14). |
| F3 Medium: "joining cold, counting to 20" overstated, no entry check | **Open.** Claim still in `joining_cold.assumes` of L7 to L10 while L7 S3 is 68 - 25 and L10 uses two-digit steps. L6 is now named as the helper for L7 (improved). No entry check in plan. |
| F4 Medium: no spiral review | **Open.** Home practice (checked L7, L9) and online practice are current-lesson only. The Quest revisits L1 to L9 ideas once, in the last lesson. |
| F5 Medium: check evidence too thin, "to say why" never assessed | **Resolved by design** (no bands, one descriptive line, private notes). Parent `term_line` ("notice patterns and to say why") is still pasted on L1 to L9 (finding 11). |
| F6 Medium: recording statements differ | **Partly fixed.** L6 to L10 share one wording; L1 to L5 differ (finding 4). |
| F7 Medium: paper held to camera | **Mostly fixed** in scripts and safeguarding. Two speaker notes and two "show bundles" lines remain (finding 3). |
| F8 Medium: still-stuck mechanism | **Fixed.** Tick on the look-back, parent photographs it to the business WhatsApp, same words in all ten lessons and on every Parent Summary. |
| F9 Medium: camera rules conflict | **Partly fixed**: L6 to L10 "on or off"; L1 to L5 "on if you can" and still need to see hands (finding 4). |
| F10 Medium: privacy notice and terms not for term programme | **Open** (finding 6). |
| F11 Medium: website pages disagree | **Open.** No Term 1 page; syllabus page text unchanged (finding 6). |
| F12 Medium: ruler hard dependency, no fallback | **Open, owner chose no printed ruler.** Hand-off now says "no ruler? tell your tutor" (finding 8). |
| F13 Medium: print and cut load | **Partly fixed.** Kit pages now say print one side, envelope, keep for later; bar cells and squares now the same size; 6 and 9 underlined on cards. Seven bars-and-squares pages still printed (L1, 3, 5, 6, 7, 8, 10), with reuse wording only in L6 and L8. |
| F14 Medium: workload and practice link undefined | **Open** (finding 7). |
| F15 Medium: timing realism | **Open by design.** Slow workbook still 3 to 4 minutes over in all ten lessons (finding 9). |
| F16 Medium: tutor console not wired | Not re-checked (out of scope for the built files). |
| F17 Medium: coverage choices | Plan open question unchanged; not re-audited. |
| F18 Medium: parent story is boilerplate | **Open** (finding 7). |
| F19 Medium: tier drift S/T | **Partly fixed.** L6 named as prerequisite of L7; scaffolds explicit in `moe.note` of L7, L8, L10. L8 S7 (35 + 12 = [] + 2) is still a Start here item. |
| F20 Medium: joiner never learns routines | **Fixed.** "New here?" one-minute note in L2 to L5 openings. |
| Cut-out F3 High (duplex kit page) | **Fixed.** Kit-page text says print on its own sheet; books put every kit on a front page with a blank back. |
| Cut-out F4 High: books shrink real-size pages to 94.3% | **Open** (finding 2). |
| Cut-out F8 to F11, F15 | Fixed (same-size cells, 6 mm channels not re-measured, 6 and 9 underlined, envelope wording). F8 reuse wording only partly. |
| Cut-out F12 ("page 6 not used") | **Fixed.** |
| Cut-out L10 to L11 hand-off High | **Fixed** (cards page, ten things, coin, FRONT paper, in script, slide and `next_materials`). |

## 3. Per-lesson table and verdicts

| L | Title | S/T/G | Start here modelled min (of 28) | Slow total / slow workbook | D1 D2 D3 D4 D5 D6 | Term-fit | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Bundles and Singles | 7/4/3 | 17.5 | 87:40 / 31:51 | 2 1 1 2 2 1 | 9/12 | Ready after minor fixes |
| 2 | Number Words and the Number Line | 8/4/3 | 19.0 | 88:27 / 31:37 | 2 1 1 2 2 1 | 9/12 | Ready after minor fixes |
| 3 | Digit Cards | 8/4/3 | 17.5 | 89:35 / 32:05 | 2 1 1 2 1 0 | 7/12 | Ready after minor fixes (High 1 and 2 are mechanical but block release) |
| 4 | The 100 Square Explorer | 6/4/3 | 17.5 | 87:46 / 31:59 | 2 2 2 2 2 1 | 11/12 | Ready after minor fixes |
| 5 | Make-a-Ten Adding | 7/4/3 | 18.0 | 86:17 / 31:26 | 2 1 1 2 2 2 | 10/12 | Ready after minor fixes |
| 6 | Tens Jump, Ones Hop | 7/4/3 | 19.0 | 89:46 / 31:21 | 2 1 1 2 2 1 | 9/12 | Ready after minor fixes |
| 7 | Take Away, Count Up | 7/4/3 | 19.0 | 88:11 / 31:05 | 2 1 1 2 1 1 | 8/12 | Ready after minor fixes |
| 8 | Balance and Swap | 7/4/3 | 19.0 | 87:50 / 30:45 | 1 1 1 2 2 1 | 8/12 | Ready after minor fixes |
| 9 | Draw and Measure | 6/3/3 | 17.0 | 89:52 / 31:44 | 2 1 1 1 2 1 | 8/12 | Ready after minor fixes |
| 10 | Story Steps + Mi's Challenge Quest | 6/3/3 | 15.5 (of 24) | 88:58 / 26:12 (of 24) | 2 2 1 1 2 1 | 9/12 | Ready after minor fixes (was Needs rework) |

No lesson is "Needs rework" now. Start here is reachable in every lesson (15.5 to 19 modelled minutes in 28; even at x1.2 it is under 23). Parts sum to exactly 90 in all ten.

## 4. Findings (ranked within severity)

### High

**1. High. L3 and L10 built outputs, and the paid Book 1 and Book 2, still show Mi holding a calculator.**
- Location: `term/l1/out/l03/*`, `term/l1/out/l10/*` (workbook, guide, deck, parent, home, Quest Log); `outputs/print/term/..._Book1_Lessons01-05_Workbook_PRINT.pdf` (L3, book pages 21 to 30) and `..._Book2_..._Workbook_PRINT.pdf` (L10, pages 33 to 46).
- Evidence: embedded Mi image hash in `L03_Tutor_Guide.html`, `L10_Tutor_Guide.html` and both `s-title.html` is `abe6b2` (old artwork); the other eight lessons use `5d7658` (no calculator). Crops of Book 1 p3 (L1) and p21 (L3) show the difference: L3 Mi holds a calculator. Cause: commit 12b6cb4 rebuilt only L1, 2, 4 to 9; L3 and L10 fail the validator (finding 2) so `build.sh` stopped; the books were then rebuilt from the stale L3 and L10 PDFs (3e5f906). Owner decision: Mi without calculator; "Mi never uses or mentions the calculator".
- Fix: resolve finding 2, run `build.sh 03` and `build.sh 10`, then re-run `print/make_term_books.py` and re-check the Mi on both books.

**2. High. The validator and the L10 verify script fail on L3 and L10 because of a false positive against our own catalogue.**
- Location: `tools/validate.py` copy check (line ~429); `verify/l10_checks.py` (same overlap rule, raises AssertionError); `lessons/l03.json` G3 and `l10.json` T2/Quest secret cave.
- Evidence: `validate.py 03` exit 1 (overlap "my tens digit what number am I", from catalogue EX-LOG-3); `validate.py 10` exit 1 ("how many children are in the line", from EX-DIAG-1). Both phrases are original text written for this project, not school text. The L10 verify script stops at the same assertion, so the rest of its answer checks do not complete (I re-solved L10 by hand: all correct).
- Fix: exclude `p1_non_routine_catalogue.md` (our own originals) from the shingle reference list, or reword the two stems; keep the check for school/contest text. Rebuild (finding 1).

### Medium

**3. Medium. Paper-to-camera wording survives in two speaker notes and in L1 and L3 lines.**
- Location: `l09.json` slide s-sneak note and `l10.json` slide s-sneak note ("Everyone holds the paper to the camera once, at the same moment, after puzzle 2"); `l01.json` explore and guide line 558 and 1847 ("a child who wants to may show their bundles to the camera"); `l03.json` ("may show a pair to the camera" next to "nobody holds anything up to the camera").
- Evidence: owner decision 9 says no paper hold-ups at all; the SAY lines of L9 and L10 say the opposite of their own notes. A tutor reading the note breaks the rule on a gallery view.
- Fix: replace with "children keep their own paper and check at Talk time" (as in L6 to L8). Optional kit items are lower risk but the L3 line contradicts itself.

**4. Medium. Recording, greeting and camera wording is still two different scripts (L1 to L5 versus L6 to L10).**
- Location: Opening SAY and DO in `l01` to `l05` versus `l06` to `l10`.
- Evidence: L1 to L5: "Cameras on if you can, so I can see your page and hands. Cameras off is fine too", greet "each child by first name before you start the recording", routine and no-paper line only as a NOTE ("New here?"). L6 to L10: "Cameras can be on or off", "Do not use children's first names on the recording", a SAY line "Microphone off until I ask you to speak ... Nobody holds paper up to the camera". The L6 note says to use the same words every lesson.
- Fix: copy the L6 to L10 three lines into L1 to L5; remove "so I can see your page and hands" (it contradicts "off is fine").

**5. Medium. L8 Think harder T1 repeats a class example and reveals its answer.**
- Location: `l08.json` mini-lesson slide "Same total? Do not add yet" (47 + 18 and 45 + 20, "47 goes down 2. 18 goes up 2") and workbook T1 ("Mei says 47 + 18 and 45 + 20 have the same total ... Who is right?").
- Evidence: identical numbers; the slide states the answer. T2 first item (29 + 14 and 30 + 13) is a near copy of the slide's "NOT THE SAME" pair. Other lessons pass this check (L5 T2 and G2 only match the optional spare menu; L10 G2 matches the same lesson's S3 numbers, which is acceptable).
- Fix: change the slide numbers (or the T1 numbers) so Think harder is not shown in class.

**6. Medium. Privacy notice, terms and website do not describe the term programme (F10 and F11 still open).**
- Location: `website/privacy.html` (November beta draft, "children's names are not shown", "we message you on WhatsApp"; no mention that parents send photos of a child's page or Quest Log with the child's name to the business WhatsApp); `website/terms.html` (fee still a placeholder); `website/level_pages/ages-6-8.html` (no Term 1 text); `website/syllabus/index.html` (Level 1 "Start here ... school year", written for the holiday course).
- Evidence: lesson and Quest files promise 90-day retention and WhatsApp-only photos; the notice says 90 days for photos but does not name the flow, and names "children's cameras are not included" (fine) while lessons say voices that are unmuted are recorded (consistent). Lesson recording statement and privacy draft do agree on voices and mute; the gap is the photo flow and the term wording.
- Fix: add a term-time privacy paragraph (still-stuck and Quest photos, who receives them, 90 days) and a Term 1 page.

**7. Medium. Parent-facing story: no Term 1 overview, undefined home workload, no route for the online practice (F14 and F18).**
- Location: Parent Summaries L1 to L9 (`parent.term_line` is the same sentence in L1 to L9: "tens and ones, to notice patterns and to say why"; L9 is about length); "Online practice: your tutor will share the practice link" (L1 to L5).
- Evidence: a parent sees ten one-page summaries, a Quest note, and (only at L10) one descriptive line. Nothing says what is expected per week: 90 min live, Parent Summary "5 minutes", Home Practice "about 15 minutes", optional pages 3 to 5 (Think harder 14 to 18 modelled minutes, Go further 16 to 19, Investigation 8), and 13 to 14 online items.
- Fix: one half-page "Term 1 at a glance" (what your child can do by week 10, honest beyond-P1 sentence, what to do if Start here is hard) and one sentence on weekly expectation: "Home Practice (15 minutes) if you like; pages 3 to 5 and online practice are optional."

**8. Medium. L9 needs a ruler for all Start here items with no fallback (F7 and F12).**
- Location: `l09.json` materials, `l08.json` `next_materials`; workbook pages 1 and 2.
- Evidence: S1, S2, S3, S5 need a ruler; the only route is "tell your tutor before the lesson". The Quest (L10) repeats the need (Gate 7). Owner decision is no printed ruler, so this is a known trade-off, but a family without one cannot take part in 6 of 6 Start here items.
- Fix: say how the tutor will help (ruler by post, or a taped 15 cm strip made from squared paper) in the L8 hand-off; accept a grown-up's measurement of printed lines.

**9. Medium. Slow-class timing is only feasible by spending the whole buffer.**
- Location: `validate.py` timing tables for all ten lessons.
- Evidence: the workbook part is over by 3 to 4 minutes in every lesson (30:45 to 32:05 for 28; L10 26:12 for 24); slow totals are 86:17 to 89:52 of 90 (L9 89:52, L6 89:46, L3 89:35). Five to eight other parts are flagged OVER in each lesson. The optional slide and spare-time menu are unreachable in a slow class. Warm-ups are modelled at 12 seconds a question, the project rubric uses 30.
- Fix: measure in a trial; if confirmed, cut one warm-up question group per lesson or accept it explicitly in the guide.

**10. Medium. L9 workbook and books claim real-size rulers but the books print at 94.3% (cut-out F4 still open).**
- Location: `l09.json` notes and `workbook` text ("the ruler pictures are real size, so a child can lay their own ruler beside them"); `outputs/print/term/term_books_spec.json` (`content_scale` 0.9429); Book 2 pages 27 to 32.
- Evidence: the book shrinks every page including S4, S6, T2, T3, G2 ruler pictures; a laid ruler will drift (8 cm looks like 7.5 cm). Not measured on paper.
- Fix: do not scale L9 pages (shift instead), or delete the lay-your-ruler claim for the book and the "print at 100%" line from the books.

**11. Medium. "Nobody sees your answers" in the Quest Log is not true.**
- Location: `L10_Quest_Log.pdf` page 1 ("It is not a race and nobody sees your answers"), deck slide "Mi's Challenge Quest" ("Nothing is shown to the group").
- Evidence: the parent photographs all four pages and sends them to the business WhatsApp; the tutor reads them and writes the one line. The parent note is honest; the child text is not.
- Fix: "Only your grown-up and your tutor see your answers. Nobody in the group does."

**12. Medium. Term-wide timeline and joiner support remain thin (F3, F4 open).**
- Location: `joining_cold.assumes` L7 to L10; `home_practice`, `online_practice` L1 to L10.
- Evidence: "only counting to 20" is still the stated entry level for lessons whose Start here has 68 - 25 (L7 S3) and two-digit steps (L10); no review item from an earlier lesson in any Home Practice I read (L7, L9). The Quest is the only review.
- Fix: one review item from lesson n - 2 in Home Practice from L5; state an honest entry profile (counts to 100 by tens, bonds to 10) and offer the 5-minute entry check from plan open question 2.

**13. Medium. Hand-off gap L7 to L8 and kit duplication (F8 partly open).**
- Location: `l07.json` `parent.next_materials` (plates, 30 things, printed workbook; no kit), `l08.json` materials ("kit page already cut out by a grown-up"); seven identical bars-and-squares pages in L1, 3, 5, 6, 7, 8, 10.
- Evidence: L8's kit page is optional, but the text says "already cut out"; reuse wording ("keep from Lesson 1") appears only in L6 and L8. A literal family cuts 7 x 29 pieces.
- Fix: say "your bars and squares from Lesson 1, keep them all term" in L3 to L10 and in `next_materials`.

**14. Medium. L10 timing of the Quest versus guide wording of a "check".**
- Location: `L10_Tutor_Guide.pdf` lines about "check sheet is on screen" and "End-of-term check"-style words; build-note text ("owner decision 22 Oct 2026: a game, not a test ... block challenge_quest by assets/quest_build.py") printed in the guide.
- Evidence: the word "test" appears in the L10 guide only in the brand phrase and "not a test"; no child or parent page uses test, exam, score, mark, rank. Quest compliance is good (see section 6). The guide still prints internal build notes.
- Fix: remove build-process wording from the tutor-facing page. (Counted as Medium only because it is on the tutor guide cover page; it could be Low.)

### Low

15. **Low. Child-facing wording against the guide.** "Bigger puzzles" (choice slide L2, L3, L6, L9 "bigger clips"), "work out" (L6 spare menu, L9 s-m6 "WORK OUT" card, hints in L1, L6, L7, L8). Guide rule 14: say "Find the value" or give the command; rule 13: avoid "bigger" for numbers.
16. **Low. L10 workbook S4(d) layout.** "12 [ ] 6 =" wraps and the printed result "18" sits alone on the next line; looks like a stray answer.
17. **Low. Book 2 contents page.** Lesson 6 line has no title or strand; the "Kit pages (cut-outs)" paragraph runs off the right edge.
18. **Low. Two page numbers on book pages.** Lessons say "page 6" and "pages 1 to 5"; book pages say "-9-" as well as "Page 6" (cut-out F23).
19. **Low. L9 Home Practice header.** "No ruler? Tell your tutor before the lesson" on a sheet used "a few days after the lesson".
20. **Low. Stale wording.** `term/l1/README.md` still says "Lesson 1 is complete ... Lessons 2 to 10 are to be written"; L6 `moe.note` says "The owner or a tutor should check the placement ... before the first live class"; L1 guide timing line says "papers to the camera 30 s"; L4 `tutor_prep` lacks the beyond-P1 reminder (F29).
21. **Low. L7 T1 number line.** The highlighted 38 and 62 labels overlap 40 and 60.
22. **Low. Parent summary on the post-lesson page.** "Have ready for next lesson" is correct, but the Parent Summary carries no pointer to the recorded-lesson privacy sentence in L1 to L5 (L6 to L10 do).
23. **Low. Spare-time menu titles repeat every week** (Is it always true? / Make a puzzle / Teach it back).

(Counts: High 2, Medium 12 (findings 3 to 14), Low 9 (findings 15 to 23).)

## 5. Checks requested, by number

1. **Regressions and earlier findings.** Section 2. No regression in maths. One regression in the build chain: L3 and L10 outputs stale (finding 1).
2. **Maths.** All correct (section 1). Beyond items verified: L3 G2c 3-digit numbers from three cards = 6; L1 T1/T4/G1; L2 T3 = 56 and G2 = 40; L4 T3 (21, 27) and G1 (8 and 36); L6 G2 = 5 jumps; L9 G1 = 11, G2 = 8 and 14; L10 T4 "No" (12 - 7 = 5, then 8 impossible), Quest gates 1 to 8 and cave (9). Pictures: L9 S4 ruler tips read 13 and 9 and S6 reads 7 cm, matching the key; L10 Quest Gate 2 arrow reads 67.
3. **Hand-off chain.** `next_materials` L1 to L10 are truthful against the next lesson's materials and kit text (L7 to L8 omission, finding 13). L9 has no kit, L10 kit is only the squares. No front/back clash in the books (every kit page on a front with a blank back). `kit_contract` is null in all ten Term 1 lessons: kit pieces versus tasks were therefore compared by hand: bars and squares (9 and 20) are enough for every task (max 9 bars in L6, 19 squares in L7); L2 11 + 11 cards; L3 20 digit cards. Book pagination: 46 pages each, contents correct except finding 17.
4. **Timing.** Sums to 90 in all lessons. Slow-class OVER flags in finding 9. Start here reachable. Think harder does not repeat class numbers except L8 T1 (finding 5). No slide shows an answer while a child is asked (the deck check slides are separate "Check" slides; L10 "Who is in the group?" shows the worked trap answer in the mini-lesson as teaching, not as a question).
5. **Wording.** Term 1 has no money, times or picture graphs, so the 50¢, time-word and picture-graph conventions do not apply. Command words and fixed question words are used. Reading load is acceptable (stems 1 to 3 sentences; L10 stories are 3 sentences). Finding 15.
6. **Safeguarding and consistency.** No private chat, no breakout rooms, WhatsApp-only photo route consistent in all ten lessons and in the Quest note. Paper-to-camera: findings 3 and 4. Recording statement consistent with the privacy draft for voices and muting; photo flow not in the privacy draft (finding 6). No "MOE-aligned", GEP or SASMO claim on any child or parent page (only the tutor-only "not MOE-aligned" note). Mi: no numbers or answers in any speech bubble (all slides checked); no calculator in any lesson text; calculator artwork present in L3 and L10 outputs (finding 1). The only "calculator" word is the Quest rule "Not allowed: a calculator" in the tutor notes (acceptable).
7. **Beyond-syllabus item and non-routine assignment.** Every lesson's `moe.note` names a beyond item (L1 opening a bundle, L2 nearer ten, 3s and between, L3 four cards and three-digit listing, L4 growing-gap sequences, L5 crossing a ten and sums to 100, L6 jump and hop split, L7 two-digit subtraction and counting up, L8 give-and-take, L9 nearest cm, bent paths and snail, L10 impossible story at T4). L5 to L8 notes describe the beyond content in general terms. Plan section 8 types are present in all ten lessons (L1 LOG/CTX, L2 LOG/DIAG, L3 LIST/LOG, L4 PAT/LIST, L5 LIST, L6 GC/BACK, L7 CMP/EXP, L8 EQ/EXP, L9 DIAG/CMP, L10 MULTI/CMP/CTX). Thin spots flagged in the plan (work backwards beyond L6 T4, three-number equations) are unchanged.
8. **Parent-facing story.** Finding 7. What a parent sees: a Parent Summary after each lesson with a 5-minute home idea, a Home Practice sheet (5 items) and separate answers, an optional online practice (no route), the Quest note in week 9 or 10, and one descriptive line after the Quest. Good: the beyond-P1 sentence is on every page and is honest; the "still stuck" route is clear. Missing: term overview, weekly expectation, practice link.
9. **Workload per child per week.** 90 min live; about 5 min of family games; Home Practice about 15 min; optional pages 3 to 5 about 35 to 45 modelled minutes; online practice 13 to 14 items (about 10 to 15 min). A middle child at the stated minimum is about 110 minutes; with every optional part about 3 hours. The files do not say which is expected (finding 7).
10. **Challenge Quest compliance.** Compliant: no "test", "exam", "score" or "mark" in the Quest Log, Parent Note, Parent Summary or Home sheet (only "never a mark" statements); tutor notes say no scores, tallies, bands or points even in private notes; no visible timer (the deck has no timer slide, tutor watch out of sight); private paper; paper flat, never held up; partner may not give answers; skipping allowed; make-up route stated ("not on the recording, plays at the make-up slot"); photos to the business WhatsApp only, kept 90 days after the program ends. Issues: finding 11 ("nobody sees your answers"); finding 14 (build-note wording in the guide).

## 6. What is good and should not be changed

- The Quest: well-designed, honest to parents, private, shortened to fit, with verified gates.
- The "still stuck" route (tick, parent photographs, business WhatsApp) and its identical wording everywhere.
- Hand-off lines that name exactly what to cut, find or print next, including the L10 to L11 carry across the term break.
- Kit pages: same-size cells, underlined 6 and 9, single-sided print instruction, blank-back kit pages in the books.
- Tier discipline: contest-style moves only at Think harder or later; beyond items named in every lesson.
- Mi use: restrained, no numbers or answers in speech (once the artwork is rebuilt).

## 7. Ranked top 10

1. **High: stale calculator Mi in L3 and L10 and in the paid Book 1 and Book 2** (finding 1).
2. **High: validator and L10 verify script fail on a false positive, blocking rebuilds** (finding 2).
3. **Medium: speaker notes in L9 and L10 still tell everyone to hold paper to the camera** (finding 3).
4. **Medium: recording, greeting and camera script differs between L1 to L5 and L6 to L10** (finding 4).
5. **Medium: Think harder T1 in L8 is shown, with its answer, in class** (finding 5).
6. **Medium: privacy notice, terms and website are not updated for the term programme, and the photo flow is unnamed** (finding 6).
7. **Medium: parent story: no Term 1 overview, workload undefined, no online-practice route, pasted term line** (finding 7).
8. **Medium: books shrink real-size ruler pages to 94.3% while L9 says they are real size** (finding 10).
9. **Medium: L9 ruler is a hard dependency without a working fallback** (finding 8).
10. **Medium: slow-class timing is only feasible by spending the full buffer, and the "counting to 20" entry claim and no spiral review remain** (findings 9 and 12).
