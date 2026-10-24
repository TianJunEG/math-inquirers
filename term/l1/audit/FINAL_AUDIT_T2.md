# Final audit: Level 1 Term 2 (Lessons 11-20), built state of 23 Oct 2026

Independent desk audit. Audit only: no lesson, tool or output file was edited. Nothing was pushed.

## 0. Method and limits
- Read: AUTHORING, WORDING_GUIDE, owner_decisions (all), plan sections 2 and 8, syllabus_by_level, privacy.html, FIXES*/FIXES3/FIXES4 files and the finding tables of the earlier WORKBOOK audits for L11-L20. I did not re-read every GUIDE_DECK and HOME audit in full; their High/Medium status is checked through the current lesson data and PDFs.
- Ran `validate.py NN` for 11-20 and the independent `verify/lNN_checks.py` (loaded through `common.load`, which expands the answer slides, as the validator does).
- Looked at: every workbook page of L14, L17 and L20 (all 6 pages each); workbook text of all ten; parent page of L11, L12, L14, L17 (images) and text of all; home sheet and answers (L14 image); kit pages (books 3 and 4); book covers and contents; L20 quest slides and all three Quest files (text); a contact sheet of the L17 deck and text dumps of every deck and guide. Other decks and guides were checked through data and text, not slide by slide.
- Maths: I solved every Start here, Think harder, Go further, Investigation, exit and home item of L11-L20 and all eight quest gates and the cave item by hand from the lesson data. No wrong final answer found.
- Instruments (same as Term 1, stated as estimates from a desk audit): A = gifted-style rubric, 12 criteria x 0-2 (max 24); tier compliance, strict (%); B = student journey, 6 dimensions x 1-5 (mean).

## 1. Validator and checks
| Lesson | validate.py | answer checks (independent script) |
|---|---|---|
| 11 | 25 pass, 4 warn, **1 FAIL** (copy: 7-word overlap with p1_non_routine_catalogue.md) | pass, 86 |
| 12 | 26 pass, 4 warn, 0 FAIL | pass, 74 |
| 13 | 26 pass, 1 warn, 0 FAIL | pass, 80 |
| 14 | 26 pass, 1 warn, 0 FAIL | pass, 76 |
| 15 | 27 pass, 1 warn, 0 FAIL | pass, 114 |
| 16 | 27 pass, 1 warn, 0 FAIL | pass, 110 |
| 17 | 26 pass, 2 warn, **1 FAIL** (copy: overlap with p2_non_routine_catalogue.md, "3 friends how many sweets does each friend") | pass, 141 |
| 18 | 27 pass, 0 warn, 0 FAIL | pass, 129 |
| 19 | 27 pass, 4 warn, 0 FAIL | pass, 127 |
| 20 | 28 pass, 4 warn, 0 FAIL | pass, 533 |

Warnings are mostly slow-class OVER flags (see section 4), plural slips in practice variants ("1 stickers" L17 t4, "1 sweets" L19 c6) and workbook page fill below 85% (L11 p6 53%, L13 p6 64%, L14 p6 51%, L15 p7 53%, L16 p6 74%, L19 p6/p7 72%; all are kit pages, which the template says may be short).

## 2. Earlier High and Medium findings: status
| Earlier finding | Status now |
|---|---|
| L14 High: T3(c) key says "Never odd" for a stem that asks "odd + odd is even" | Fixed: stem now says "is odd", answer Never. Seen on the page. |
| L11 M: G1 "between" on a round table; Investigation room; S2 boxes; unused number cards; round-table labels | Fixed in data (next to Ali and next to Mei; draw box; cards used in Explore). Not re-measured except by text. |
| L12 M: transfer arrow unreadable; kit cannot make 34/51; Investigation space; regroup in Start here | Data changed (kit 11 strips, draw box); arrow drawing and regroup scaffolding NOT re-checked visually. Open. |
| L13 M: Investigation space; T2 repeats class numbers; T1 solution garbled; talk answer wrong ("one less than double 8") | T2 renumbered (3+4, 8+7, 10+11, 2+3); talk answer now correct. Rest not re-checked visually. |
| L14 M: S3 chart cells tiny; T1/T3 repeat class numbers; T2 last-digit rule unexplained | T1/T3 renumbered (fixed). **S3 chart still tiny (about 6 mm cells, seen on page 1): open.** Page 3 is still crowded (frames touch the next tab). |
| L15 M: key gives one multiplication order; T1 repeats class; "Lesson 5" vs "Lesson 15" numbering | T1 now 2 x 8 array; key now prints "(5 x 4 = 20 is also right)". Numbering: still open (section 3, finding 6). |
| L16 M: 100 square has no zero; key order; T3 repeats class; Start here time | Zero explained on the kit page and in the hint; key order fixed; T3 renumbered (50, 27, 65). Time: still 1 minute over (finding 9). |
| L17 M: numbering; T1/T3 repeat class; key order; S5 number line too small | T1/T3 new numbers; key order fixed. Numbering open. Number line on page 2 now about 130 mm, readable (seen). |
| L18 M: T1/T2 repeat class; key order; page 3 small type; numbering; timing | Numbers fixed, key order fixed. Page 3 type and timing not re-checked visually. Numbering open. |
| L19 M: T2/T3 repeat class; shapes tiny; timing; numbering; page 5 small type | T2/T3 renumbered (6 and 9; 3 and 5). Shape size, page 5 type not re-checked visually. Numbering open. |
| L20 M: numbers repeat class; numbering; timing; page 5 small type | Page 5 viewed: exit and look-back are readable but look-back type is small (about 8 pt). Numbering open. |
| Term 1 patterns: hand-off truth, paper hold-ups, WhatsApp-only, recording statement | Hand-offs now match lesson to lesson (section 3). No hold-ups, WhatsApp-only route everywhere. Recording statement: see findings 4 and 5. |

## 3. Numbered findings

### High
**1. L11 and L17 built files are stale: Mi still carries the calculator.** Location: `out/l11/*`, `out/l17/*` (guide, deck, workbook, parent page) and the lesson pages inside Books 3 and 4. Evidence: embedded mascot hash in guide/deck HTML is `abe6b2` (old) for L11 and L17 and `5d7658` (nocalc) for every other lesson; the L17 workbook page 1 and the L11 and L17 parent pages show the calculator at 110 dpi. Files date 01:16 and 01:23, others 03:13-03:16. Owner decision 6: Mi never uses or mentions the calculator (and "Mi without calculator" was a requested change). Fix: clear finding 2, rebuild 11 and 17, rebuild the books.

**2. Two lessons fail the validator, which blocks `build.sh`.** Location: L11 (T-item "3rd from the back, how many children are in the line") and L17 ("3 friends ... how many sweets does each friend") against `docs/books/p1_` and `p2_non_routine_catalogue.md`. Evidence: validate output above; `build.py` exits "validation failed: nothing built". This is the cause of finding 1. Fix: reword the two sentences (or exempt the catalogue examples the lesson text legitimately mirrors); rerun; rebuild.

### Medium
**3. Quest tutor notes print wrong part answers for Gate 6.** Location: `L20_Quest_Tutor_Notes.pdf` section 4. Evidence: "Answer: 15; 11" but the part lines read "(a) ... = 20; (b) ... = 17"; cause is `challenge_quest.questions[C6].parts[].ans` ("20", "17") against `val [15, 11]`. Quest Log itself and the worked line are right. Fix: set the part answers to 15 and 11. Same class of slip: L20 S1 `parts[0].ans = "5"` against answer $4 (does not reach any printed file today; fix the data).

**4. The recording notice is spoken after the recording starts in six lessons.** Location: L13, L14, L17, L18, L19, L20 opening (DO "start the recording", then SAY "This lesson is recorded"; L13 NOTE says "after the recording has started"). L15 and L16 say it before. privacy.html: "We tell the group at the start of each lesson that it is being recorded". Fix: notice first, then start the recording, in every lesson.

**5. Parent pages L13-L20 carry no recording statement.** Evidence: L11 and L12 "Next lesson" box says "The recording has the tutor, the shared screen and any voice that is not muted... private to the families in your child's group"; L13-L20 only say "Every lesson is recorded; your tutor will share a private link". The statement is the owner-decision 9 wording and privacy.html also promises a mute route for a parent ("tell us when you register"), which no parent page repeats. Fix: one shared sentence in the template for every lesson.

**6. Lesson numbering is mixed across what a family sees.** Evidence: pages and kit pages say "Term 2 • Lesson 1"; Book 3 and 4 covers/contents say "Lesson 11", "Lesson 12"; the L10 goodbye slide says "Term 2, Lesson 11: Who Is Where?" and the L19/L20 slides say "Term 2 Lesson 10". Fix: the book contents should print "Term 2 Lesson 1 (Lesson 11 of 40)" or one scheme throughout; correct the L10 slide.

**7. Book 4 contents row for Lesson 17 has no title or topic.** Location: `Math_Inquirers_L1_T2_Book4_..._Workbook_PRINT.pdf` page 2. Cause: the L17 workbook header ("MULTIPLICATION AND DIVISION: SHARING AND GROUPING") wraps to two lines, so `lesson_title` in `print/make_term_books.py` misreads it. Fix: shorten `workbook.header` or make the parser robust. Also page 2 of both books clips its last note ("...keep them in an e") at the right edge (Low).

**8. Families are told two different ways to get the workbook.** Evidence: L15 and L16 hand-offs say "Your tutor will send its workbook before class: please print it" (and L16 plan: print at 100%); L11-L14 and L18-L20 say "the printed Lesson N workbook"; owner decision: printed term books are issued on payment. Every kit page also says "Print this page on its own sheet, or on one side only", which is moot in the bound book. Fix: one sentence everywhere (the book is issued; a PDF is for a missing page), and a book-version of the kit note.

**9. Start here is modelled longer than the time the script allots (middle child).** Evidence (modelled / allotted for pages 1 and 2): L11 18.0 / 17.0, L12 18.5 / 16.5, L15 15.5 / 14.0, L16 16.5 / 15.5, L20 16.0 / 15.0; L13, L14, L17, L18, L19 within 0.5. A slower child (1.2 times) does not reach Think harder in L11, L12, L16. The notes say Think harder is "for home", so this is honest but weakens the tier labels. Fix: cut one Start here item in L11 and L12 (S2 box-heavy, S3) or lengthen work by taking from flex (buffer is 5 minutes).

**10. L14 workbook is the one earlier workbook Medium still open.** Page 1 S3 (1-20 chart cells about 6 mm, numerals 3 mm) is hard for a 6-year-old to colour; page 3 frames touch the next tab (T1/T2, T3/T4); T3(c) wraps "Circle Always, Sometimes or Never" across lines. Fix: 12 mm cells; page 3 spacing; short blank in G3(b) (the "because ___" line is about 20 mm).

**11. L15 parent page does not state the beyond-syllabus item.** Evidence: summary says "Equal groups and x are Primary 1 work"; Go further G2(c), 60 marbles, above the school range of 40, is named only in the tutor `moe.note`. L14 is beyond P1 in Start here itself (odd and even are P2), which conflicts with the 23 Oct rule that beyond items sit at Think harder or Go further (owner default 3 accepts this; say it plainly, which L14 does). Fix: add one parent sentence to L15; record the L14 exception.

**12. L19 shape cards are word cards.** Page 7 prints "circle", "square", "heart", "star" as words, 15 cards; the puzzles use drawn shapes. A 6-year-old must read the word to match a picture; the lesson says "children may draw the shape". Fix (already noted in FIXES3_L19): picture cards.

**13. L17 Start here S1 hint contradicts the question; G1 stem miscounts parts.** S1 says "Share 8 dots" but the hint says "until you have drawn 12". G1 stem "Then answer (a) and (b)" but the question has (c). Fix both strings.

### Low
14. L16 plan promised "numbers in three tables" at Go further; delivered tables 4+5 and 3+5 only. 15. L14 G3 uses 4 + 6, the Explore example. L17 G1 table repeats 12 sweets from class (new structure). 16. Cover tagline "Think. Question. Prove." versus pages and Mi "Notice it. Test it. Explain why." 17. L13 tutor prep says the lesson "still needs a syllabus check", unresolved since the plan. 18. Tutor prep typo "Children video is excluded" (L19, L20). 19. L14 next_materials omits "the printed Lesson 5 workbook". 20. L17 G1(c) answer line (about 40 mm) is short for "1, 2, 3, 6, 9, 18". 21. Look-back type is about 8 pt on pages 5. 22. L12 and L11 mini parts slow-class over by 0.2-2 minutes (inside the buffer).

## 4. Timing
Parts sum to 90 in all ten. Scripted need 69:15-72:37; slow-class totals 82:05-85:38 (never over 90). Slow-class part flags (OVER, absorbed by flex): L11 mini 12:02/11, work 28:17/28, talk 6:08/6; L12 opening 3:17/3, explore 15:03/15, mini 10:56/10, work 28:10/28; L20 quest part 20:10/20. Other lessons all ok (L17, L19, L20 remember is LOOSE, not over). The exact flags for L20: the quest part is the tightest and the guide says never shorten it, so a slow class loses flex minutes, not the quest. Answers are held back by `reveal` slides (explore, mini, sneak, checks) in L11-L19; the L17 deck contact sheet shows answers only on the following slide. Think harder numbers no longer repeat class numbers except as in findings 15.

## 5. Hand-off chain
L10 to L20 checked pairwise (`parent.next_materials`, spoken goodbye, `s-end` slide versus the next lesson's `materials`): all truthful and mutually consistent. L11 strips (11, two cut after 6) match L12; L12 ten-frames and 20 counters match L13; L13 cards 1-20 match L14; L16 groups-mat match L17; L17 ten strips, three cut after 6 match L18; L18 counters page and 15 shape cards match L19; L19 30 tokens and the Quest Log match L20; L20 to L21 clock kit matches. Only L14 to L15 omits the workbook line (finding 19) and L15/L16 use the "tutor sends it" wording (finding 8). Books: Book 3 has 44 pages, Book 4 has 48; every lesson starts on a front page; kit pages sit on fronts with blank backs (Book 3 p9, 17, 25, 33, 41, 43; Book 4 p9, 17, 25, 33, 35, 43); no front/back clash found; the tear margin reads fine; L19's two kit pages and L15's two mats are separate sheets. The Quest Log (3 pages) and key extras are in the books.

## 6. Wording, safeguarding, claims, Quest
- Wording: commands first, names varied, multiplication reads "groups of" with either order accepted and the key now says so; "x" and the minus glyph survive in the PDFs; money is whole dollars with the $ before the box (L20) and the 50 cent sign does not arise in Term 2. Reading load is acceptable; the validator has only one parent-string warning (L20).
- Safeguarding: no paper hold-ups, no breakout rooms, private paper, WhatsApp-only route with "+65 9880 5962" only on parent and tutor-note pages, never on slides (validator-enforced; quest slides say "business WhatsApp" only), retention statement "90 days after the program ends" matches privacy.html, recording wording matches the owner default apart from findings 4 and 5. No MOE, GEP or SASMO claims on any child or parent page; every lesson says "does not claim to match any school syllabus" in the guide. Mi speech lines contain no digits or answers and are short; Mi appears on 4 slides (5 in L20). The only "calculator" text is the tutor-only quest rule "Not allowed: a calculator".
- Quest (L20): 8 gates plus a cave item; solved: 5th and 3; 35 and 61; 18 and odd; 15 and 8; 4 and 5; 15 and 11; No and 9; $2 and $10; cave No and 15. Child and parent pages contain none of test, exam, score, mark, grade, out of, timer; the tutor notes use them only as prohibitions. Private notes sheet, one line per parent, make-up before the recording and no private call are all present; the recording pause is stated in the guide and slides. Only defect: finding 3.

## 7. Beyond-syllabus and non-routine (plan section 8)
Every lesson names its beyond item in `moe.note` (L15: doubling 6 groups of 5 to 60; L17: all ways to share 18; L16: 3 and 4 tables and common multiples; L13: double 35 and five near numbers; L14: whole lesson, P2). `beyond` field is null in all ten (required only from Term 3). Section 8 types are present at the stated tiers: L11 LOG/DIAG, L12 CMP/EQ/BACK (light), L13 EQ (G), L14 EXP, L15 WAYS (G) and EXP, L16 LIST/PAT, L17 CTX and WAYS, L18 DIAG/EQ/MULTI, L19 CTX/EXP, L20 MULTI and CMP (G3 compares two shops). None sits in Start here.

## 8. Parent story and workload
Across the term a parent sees: places and strips (11-12), doubles and odd/even (13-14), groups, tables, sharing, stories (15-18), picture equations (19), unit price and the Quest (20); every page repeats "never a rank or a mark". The footer term line is the same sentence every week and is not about odd/even or doubles (Low). Quest note and tutor line are clear. Workload per child per week: 90 minutes live, about 5 workbook pages (about 15-17 minutes of Start here in class, Think harder and Go further optional at home), one home sheet of 5 items (about 15 minutes), optional online practice, plus a weekly adult task (cut kit pages, find materials). Heavy adult weeks: L11 (20 cards cut), L12 and L18 (strips cut, some cut after 6 cells), L19 (35 pieces cut), L20 (30 tokens plus Quest Log in an envelope).

## 9. Scores (estimates) and verdicts
| Lesson | A rubric /24 | Tier compliance | B journey (mean) | Verdict |
|---|---|---|---|---|
| 11 | 18 | 94% | 3.9 | Ready after minor fixes (rebuild blocked: findings 1, 2) |
| 12 | 18 | 94% | 3.8 | Ready after minor fixes (9) |
| 13 | 17 | 94% | 3.9 | Ready after minor fixes |
| 14 | 17 | 94% | 3.7 | Ready after minor fixes (10) |
| 15 | 18 | 100% | 4.0 | Ready after minor fixes (11) |
| 16 | 18 | 100% | 4.0 | Ready after minor fixes |
| 17 | 18 | 100% | 4.0 | Ready after minor fixes (1, 2, 7, 13) |
| 18 | 18 | 100% | 3.9 | Ready after minor fixes |
| 19 | 18 | 94% | 3.7 | Ready after minor fixes (12) |
| 20 | 19 | 100% | 4.0 | Ready after minor fixes (3) |
No lesson needs rework. Term 2 is Ready after minor fixes as a whole.

## 10. Term-level summary: ranked top 10
1. L11 and L17 files still show Mi with the calculator (stale build).
2. Validator FAILs on L11 and L17 (catalogue overlap) block any rebuild.
3. Quest tutor notes Gate 6 print 20 and 17 as part answers (true answers 15 and 11).
4. Recording notice is said after recording starts in L13, L14, L17-L20.
5. Parent pages L13-L20 omit the recording statement that L11 and L12 carry.
6. Mixed lesson numbering (cover and contents "Lesson 11", pages "Lesson 1").
7. Book 4 contents has a blank row for Lesson 17; contents note clipped.
8. Workbook delivery wording conflicts (print it versus printed book; kit "print" note).
9. Start here modelled longer than allotted in L11, L12 (and by 1 minute in L15, L16, L20).
10. L14 S3 chart tiny and page 3 crowded; L19 shape cards are words; L17 S1 hint says 12.
