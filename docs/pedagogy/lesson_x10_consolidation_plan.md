# Lesson x.10 consolidation plan: choose-the-tool lessons that host the Challenge Quest

Plan only, 23 Oct 2026 (night), branch `claude/great-fermi-1hv4vc`. Nothing in lesson JSON, books, tools or holiday material was edited; nothing is pushed. Source decision: `docs/terms/owner_decisions.md`, entry "23 Oct 2026 (night): TERM-ALL-RECOMMENDED" (decision 2: YES; scope Terms 2 to 4 first, Term 1 later; the Quest sits in lesson 10 of every term at every level). Evidence base: `docs/pedagogy/term_review.md` sections 0, 2.2, 3, 8, 9, 11; the built files `term/l1/lessons/l10.json`, `l13.json`, `l19.json`, `l20.json`, `l27.json`, `l30.json`, `l40.json`; `print/make_term_books.py`; `docs/printing/quote_request.md`; `term/l1/audit/BOOKS_5_8_BUILD_REPORT.md`; `term/l1/audit/DIAGRAM_FIXES.md`. Hours are agent-hours and are estimates (calibrated on the Level 1 pace of about 8 hours per lesson all-in, `docs/terms/l2_preflight.md` finding 8), not measurements. Nothing here has been tried with children.

---

## 0. Recommendation in one screen

1. **Make the change for Level 1 Terms 2 to 4 before the first release, inside the rebuild the release plan already requires.** The WAIT-DIAGRAMS entry says Books 1-8 are released together once, after the diagram fixes are re-checked and "lessons 20-40 and all eight books are rebuilt". Lessons 20 to 40 are being rebuilt anyway (and the strategy card and common look-back must still be carried into them), so the marginal cost of the restructure is mostly the new authoring and re-audit of six lessons, not a second rebuild. After release, every move would also move printed page counts, Quest Logs already sent to families and tutor scripts a second time.
2. **Smallest set of moves that satisfies the decision.** Only three lesson slots change identity per term at most, and no lesson from 14 to 18, 21 to 26, 28, 29, 31 to 38 changes number, title or content (hand-off lines aside):
   - Term 2: Picture Equations 19 to 13 (Doubles and Near Doubles is retired and its best items absorbed), Find One First 20 to 19, new lesson 20.
   - Term 3: Calendar Detective 30 to 27 (Fill the Grid is retired and one item absorbed), new lesson 30.
   - Term 4: nothing moves; lesson 40 keeps the Showcase and is reframed.
   - Term 1 (later): keep Story Steps in lesson 10 and reframe it (option B in section 5), unless the owner wants the swap with lesson 4 (option A).
3. **Effort.** About **72 agent-hours** for Level 1 Terms 2 to 4 (section 6), plus 4 for the optional lesson 39 rebalance and 9 (option B) or 18 (option A) for Term 1. At the Level 1 pace that is about 3 working days elapsed: one day of Quest engineering, one day for the six lessons in parallel, one for audits and the rebuild. Not counted: the strategy card and common look-back in the other term lessons (section 7, dependency), and the owner's review time.
4. **Do not ship Quest v2 without the tool naming it assumes.** A Quest tool row asks the child to tick a named tool. Term review finding 1: Lessons 1 to 37 hardly name tools. The strategy card ("tool of the day") and the common look-back must reach lessons 1 to 39 in the same rebuild, or the tool row shows names children never met.
5. **Five decisions for the owner** are in section 9 (retire two lessons, timing, Term 1 option, lesson 39, privacy wording for the three-word scale).

---

## 1. What a "choose-the-tool consolidation lesson" is (template for every level)

**Job.** Spiral the term's content in fresh numbers and make the child choose a tool, say why, and check. It teaches no new idea. It hosts the Quest. This matches the holiday lesson 10 ("Tool of the day: Choose one", all eight icons: `docs/pedagogy/spine_routine_spec.md`, strategy card, Lesson 10).

**Skeleton (unchanged from today's Quest lessons, so the validator, timing model and guide builder need no change):** Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Brain break 4, **Quest 20 (minutes 35 to 55, straight after the break)**, Workbook 25, Talk 4, Look-back 2, Flex 4 = 90. The exit ticket stays optional (as in `l20.json`).

| Part | What it holds in a consolidation lesson |
|---|---|
| Remember (6) | The toolbox page for the tools met so far, one small picture each, with a 1-minute use of three of them on tiny problems. A child who joins cold gets the tools from the page, not from earlier lessons (joining-cold rule). |
| Sneak-peek (4) | Two unlabelled puzzles that want different tools; no tool is named in the question. |
| Explore (10) | "Tool market": six problem cards, nobody solves. For each, point to the tool you would start with and say "I will ... because ...". Two cards have two good tools. |
| Mini-lesson (9) | One problem solved with two tools (which was quicker?), then checked a third way; one card where the first tool gets stuck and the child tries another ("Wait. Try a tool. Try a smaller case. Ask."). |
| Quest (20) | Quest v2, below. |
| Workbook (25) | Start here: 6 mixed items in fresh numbers from the term's lessons, never tagged with a lesson, each with a "tool I used" tick and an "I checked" tick. Think harder (3 to 4): the same problem with a second tool, and which was quicker. Go further (3): no tool named. Investigation: write a problem that needs a stated tool. Tool names appear at Start here and Think harder only (term review 2.2, "fade the hint"). |
| Talk (4) | "Which tool did you pick first, and why?" (the fourth home prompt of term review 11.3). |
| Look-back (2) | The common look-back of the spine routine (tools used, "I checked", "I asked"). |

**Tool row per term (only the tools met so far; schedule from term review 2.2):** Term 1: Draw it, Act it out, Spot the pattern, List every way (4). Term 2: add Make a table, Work backwards (6). Term 3: add Guess and check (7). Term 4: add Try something simpler (8, the holiday lesson 10 row). Guess and check and Try something simpler are introduced by items that the spine task must add (term review 6.1: "never taught" or "dropped in Block 4"); this plan does not write them.

**Quest v2 (from term review section 9, within the owner's rules: no scores, no tests, no rankings, no timer, recording paused, private paper):**
- Keep 8 gates and the optional cave, 20 minutes after the break.
- Six gates stay tagged to lessons (pairing lessons so all content lessons are still visited); **two gates become unlabelled mixed gates** (no lesson tag).
- The Quest Log gets a row of the tool pictures met so far (icons exist in `levels/spine_icons/*.svg`); the child ticks the one they used. A "Did I check?" tick, the same tick as the lesson look-back.
- The cave becomes a choose-the-tool problem with a "because" line.
- Tutor notes (private, words not counts): tool chosen without a prompt, how they checked, a reason in their own words, what they did at the stuck moment; plus the optional three-word scale (with help, with a prompt, on their own) as a word per habit per child per block (owner decision 3). The parent line is written in tool words ("Mei chose to list every way and checked that none was missing"), and the note still says it shows what the child did that day.
- **Privacy wording must change when this is built.** Every built Quest says "No score, no x out of 8, no ranking, no tally, no comparison between children, not even in your own notes" (`challenge_quest.privacy_checklist` in l10, l20, l30, l40) and `b_quest.py` bans "record sheet" in tutor notes. The scale is a word per habit written in the tutor's own note, never a count or a table across children; reword the checklist line to say that, so the rule and the practice agree.
- Target the same Quest Log page counts (4, 3, 4, 4) so the book page counts do not move. If a log needs one more page it costs a sheet (two pages) in Book 2, 4, 6 or 8.

---

## 2. Level 1 slot map (Terms 2 to 4 first)

Working titles are for the owner to change. "Lesson in term" follows the lesson number (13 = Term 2 lesson 3).

| Slot | Today | After | Why this slot | What changes in the file |
|---|---|---|---|---|
| 13 | Doubles and Near Doubles | **Picture Equations** (from 19) | Review section 8: doubles within 20 are inside Primary 1 and the best idea (double, then adjust by 1) is a mental-arithmetic move; Picture Equations needs only balance (8) and strips (12) and its warm-up re-teaches the rest | Renumber l19 to l13 (`id l1-t2-03`, lesson_in_term 3, outputs `out/l13`, `verify/l13_checks.py`); absorb the Doubles talk (Mei: 1 more than double 7) as a Remember item and two Start here items |
| 19 | Picture Equations | **Find One First** (from 20), restored to an ordinary lesson | Directly after Equal Groups (15), Sharing and Grouping (17) and Times Stories (18); its warm-up already re-teaches plates and strips | Renumber l20 to l19; drop the Quest block; re-time to the ordinary skeleton (Explore 12, Mini 12, Workbook 30, Talk 6, Exit 6 live, Look-back 3, Flex 5); the exit ticket E1 to E3 already exists in the file and becomes live |
| 20 | Find One First + Quest | **Choose Your Tool ("Tool Market")**, new, hosts Quest v2 | Skeleton and Quest gates reused | New content per section 1 (6 tools); gates re-tagged (below) |
| 27 | Fill the Grid | **Calendar Detective** (from 30) | The cheapest slot: the review flags Fill the Grid as repeated at Level 2 lesson 18, Level 3 lesson 29, Level 5 lesson 34, Level 6 lesson 36 and in the holiday Logic Lab, and plan open question 10 already questions it. Cost: the time strand is split by the money lessons 24 to 26. If strand continuity matters more, put Calendar Detective at 24 and shift 24 to 26 down one (adds about 12 hours and changes Book 5 as well) | Renumber l30 to l27; drop the Quest block; re-time as for 19; the `calendar_cards` kit page moves from Book 6 lesson 10 to Book 6 lesson 7 |
| 30 | Calendar Detective + Quest | **Choose Your Tool ("Tool Detectives")**, new, 7 tools | Builds on Spot the Mistake (29) | The elimination idea of Fill the Grid survives as one Think harder item solved by making a table; Latin squares stay in the holiday Logic Lab and Levels 2, 3, 5, 6 |
| 39 | The Problem-Solving Toolbox | Optional: same lesson, wording rebalanced to the eight card names | It becomes the lesson that teaches how to choose (signal words), no longer where seven tools are first named | `skill`, big idea and slides only; no new items |
| 40 | Inquirers' Showcase + Quest | Same title and lesson, reframed | Already a consolidation lesson (Quest 20, Workbook 15, Showcase 14); nothing moves out | Quest v2 (all eight tools); Remember uses the full toolbox; the Showcase frame becomes "my tool, why I picked it, a check" next to "a good puzzle has one answer"; Start here items re-aimed as mixed choose-the-tool; gate 8 (check a friend's puzzle) stays |

**Lessons that keep number, title and content:** 11, 12, 14 to 18, 21 to 26, 28, 29, 31 to 38. Only these hand-off lines change: l12 (NEXT LESSON card and closing SAY line: Doubles becomes Picture Equations), l18 (card says Picture Equations; becomes Find One First), l19 (card says "Find One First, and Mi's Challenge Quest"; becomes Choose Your Tool and the Quest), l26 (card says Fill the Grid; becomes Calendar Detective), l29 (four mentions of Calendar Detective; becomes Choose Your Tool and the Quest). Also check "Term 2 Lesson 9/10" and "Term 3 Lesson 10" phrases in tutor_prep and `joining_cold` of l12, l18, l19, l20, l21 to l25, l30, l31, l39, l40 (the grep list is in section 8).

**Quest gate re-tagging (gates are tagged by lesson in `challenge_quest.questions[].lesson` and `quest_map`).**

| Quest in | Today | After |
|---|---|---|
| Lesson 20 | C1 to C8 tag lessons 11, 12, 13, 15, 17, 18, 19, 20 | C3 (13) becomes a Picture Equations gate (the old C7 idea); C7 (19) becomes the Find One First gate (the old C8 idea); old C8 and one more gate become the two mixed gates. All 9 content lessons 11 to 19 still visited through pairing |
| Lesson 30 | Gates tag 21 to 26, 27, 28, 29, 30 | C5 (27) becomes the calendar gate; the old lesson 30 gate (C8) and one more become mixed; 7 (29) stays the claim-checking gate |
| Lesson 40 | Gates tag 31 to 40 | Two of the paired gates become mixed; gate 8 (check a puzzle, tagged 40) stays because lesson 40 keeps its content |

---

## 3. What happens to the new ideas in lessons 10, 20, 30

| Idea | Where it goes | Which lesson loses what |
|---|---|---|
| Find One First (unit method, each, a dozen, such, compare two shops) | Slot 19 (Term 2), whole lesson kept | Lesson 13 (Doubles) is retired; Picture Equations moves up two places before it |
| Calendar Detective (cycle of 7, count on from tomorrow, a week later, Hundred Days Later) | Slot 27 (Term 3), whole lesson kept | Fill the Grid is retired; one grid item survives in lesson 30 |
| Story Steps (read twice, one operation per step, reversed wording, a story trap) | Term 1, later (section 5): stays in lesson 10 under option B, or takes the slot of lesson 4 under option A | Option A: The 100 Square Explorer is demoted (its skip-count work already returns in lesson 16; its pattern sequences in 28 and 30) |
| Doubles and near doubles | A Remember item and two Start here items inside the new lesson 13 | No Term 1 file is touched (Books 1 and 2 stay as they are) |
| Fill the Grid (elimination) | One Think harder "make a table" item in the new lesson 30 | Not taught as a lesson at Level 1 |

---

## 4. Numbering, titles, cross-references, Books, kit, Quest Log, answer key, home pack

- **Numbering.** Lesson numbers 1 to 40 do not change. Only which content sits in 13, 19, 20, 27, 30 changes. Term books say "Term 2, Lessons 1 to 5" and do not show the global number; headers, covers and contents regenerate from the lesson data. Plans: add a dated note per level (done in the six year plans) but do not renumber.
- **Titles and fields to change in the three renumbered lessons:** `id`, `lesson`, `lesson_in_term`, the `workbook.header` is unchanged, the `online_practice.key` (`t2l20` becomes `t2l19`) and its item ids, `verify/lNN_checks.py` file name and any `ORACLES` keys that embed the lesson number, `out/lNN/` folders, the `AUDIT_LNN.md`, `WORKBOOK_AUDIT_LNN.md`, `HOME_PARENT_PRACTICE_AUDIT_LNN.md` and `WORDING_REVIEW_LNN.md` file names (rename and re-run, do not trust the old pass).
- **Cross-references.** Searches of the 40 lesson files found: "Find One First" in l19 (3), l20 (16), l39 (38 mentions); "Calendar Detective" in l29 (4), l30; "Picture Equations" in l08, l17, l18 (4), l19 (7), l20; "Fill the Grid" in l26 (3), l27 (4); "Doubles and Near Doubles" in l12 (3), l13. The l39 mentions are the Toolbox lesson's own content and stay. The website and parent pages do not list Level 1 term lesson titles (searched the repository outside `term/l1/out`).
- **Books.** Book k holds lessons 5k-4 to 5k. Affected: Book 3 (l13), Book 4 (l19, l20, Quest Log), Book 6 (l27, l30, Quest Log; l26 and l29 hand-offs), Book 8 (l40, Quest Log; l39 if rebalanced). Books 5 and 7 have no content change. Kit pages: Book 3 gains or keeps Picture Equations' ten-frame and shape kits and loses Doubles'; Book 4 loses the shape kit and keeps Find One First's `cards`; Book 6 swaps `grid_tiles` for `calendar_cards`. Read the real page counts from `term_books_spec.json` after the build; do not assume them.
- **Quest Log.** New tool row and check tick (section 1); target 3, 4, 4 pages for Quests 20, 30, 40. Loose copy files `L20_Quest_Log.pdf`, `L30_Quest_Log.pdf`, `L40_Quest_Log.pdf` sent to families a week before are regenerated.
- **Answer key (tutor only).** `Quest_Tutor_Notes` per Quest: new gate tags (mixed), four process prompts, scale line, reworded privacy checklist; the answer keys of l13, l19, l27 move with their lessons. Answer-sheet gate tags such as "Lesson 29" stay for unchanged gates.
- **Home pack.** Home sheets for l13, l19, l27 move with their lessons (they are ordered by lesson number inside Books 3, 4, 6); `Quest_Parent_Note` is regenerated with the tool-words report pattern. Books 3 and 4 home packs regenerate; Book 5 and 7 do not need to.
- **Parent summaries.** The "NEXT LESSON" cards named above, and the parent line patterns. The boilerplate `term_line` fields are a separate known fix (term review 11.3).
- **Quest page text bans.** The new text must pass `BAN_FAMILY` and `BAN_TUTOR` in `b_quest.py`; "tool row" and "tick" are fine, "score" and "mark" are not.
- **Print quote.** `docs/printing/quote_request.md` and `outputs/print/term/term_books_spec.json` page and sheet counts for Books 3, 4, 6, 8 must be re-run before a quote is sent (the same note already stands at line 64).

---

## 5. Term 1 lesson 10 (later)

Story Steps has the weakest case for moving: it is the first Quest of the year and children hold only four tools; its core idea ("choose add or take away from the words, check each step") is itself choose-and-check. Two options:

- **B (recommended): keep Story Steps in lesson 10 and reframe.** The Quest becomes v2 with a four-tool row and "Did I check?"; the Talk, look-back and tutor notes carry the tool words; no content moves; Books 1 and 2 are touched only in Book 2 (lesson 10 and its Quest Log). Cost 6 author + 3 audit = **9 hours**.
- **A: move it.** Story Steps takes lesson 4's slot (it needs only counting and small add/take away, which its warm-up re-teaches); The 100 Square Explorer is demoted (patterns return in 16, 28, 30; skip counting is a holiday topic); lesson 10 becomes a new four-tool lesson. Touches Book 1 (lesson 4) and Book 2, re-tags Quest gates, re-handoff lessons 3 and 4 and 9. Cost about **18 hours**.

Timing matters here: Term 1 starts 4 Jan 2027 (`docs/schedule/term_2027_t1_availability.md`, secondary-source dates) and Book 2 is the first book printed. If Term 1 is changed after the first print order the printed Book 2 and the lesson no longer match. Either include option B in the same wave (recommended, +9 hours) or accept that the 2027 Term 1 stays as built and Term 1 is changed for the next intake.

---

## 6. Effort, in agent-hours (Level 1, Terms 2 to 4)

"Author" is writing or transplanting, verifying every answer from first principles (`verify/lNN_checks.py`), validating and building. "Audit and fix" is the independent audit, workbook and home/parent audits, wording review and fix pass that every Level 1 lesson received.

| Slot | Work | Author | Audit and fix | Total |
|---|---|---|---|---|
| 13 | Picture Equations in, Doubles retired and absorbed, renumber, hand-offs | 3 | 2 | 5 |
| 19 | Find One First in, re-time to ordinary skeleton, live exit ticket, renumber | 4 | 3 | 7 |
| 20 | New Choose Your Tool lesson, Quest v2 gates (retag, 2 mixed, cave) | 7 | 3 | 10 |
| 27 | Calendar Detective in, re-time, kit page moves, renumber | 4 | 3 | 7 |
| 30 | New Choose Your Tool lesson, 7 tools, Quest v2, absorbed grid item | 7 | 3 | 10 |
| 40 | Reframe (Quest v2, Remember, Showcase frame, Start here re-aim) | 5 | 3 | 8 |
| 12, 18, 26, 29 | Hand-off cards and lines, re-validate and rebuild | 2 | 1 | 3 |
| Shared engineering | `b_quest.py` v2 (tool row from `spine_icons`, mixed gate, check tick, tutor prompts, scale line), validator rules for mixed gates and the tool row, Quest page count check | 10 | 2 | 12 |
| Docs | Year plan sections 2, 4, 5, 8 matrix, Level 1 pre-flights, parent outcomes, quote request | 4 | 0 | 4 |
| Rebuild | Lessons 20 to 40 (already required) re-built colour and B&W, `check_bw.py`, even page counts for all eight books, `term_books_spec.json` | 4 | 2 | 6 |
| **Terms 2 to 4 total** | | **50** | **22** | **72** |
| Optional lesson 39 rebalance | Wording to the eight card names; no new items | 3 | 1.5 | 4.5 |
| Term 1, option B | Reframe lesson 10, Quest v2 | 6 | 3 | 9 |
| Term 1, option A instead | Swap with lesson 4 plus new lesson 10 | 12 | 6 | 18 |

Comparison: writing six fresh lessons at the Level 1 all-in pace would be about 50 hours; the plan costs more than that only because of the Quest engineering and the re-audits of moved material. The moved lessons are cheap because their content is already verified (Find One First and Calendar Detective carry their own checks).

Not counted: owner review of Quest v2 wording and one tutor trial run of a consolidation lesson (2 to 3 hours of the owner or a tutor); the strategy card and common look-back in the other 36 term lessons (section 7).

---

## 7. Dependencies, risks, what not to do

- **Dependency, tool naming.** Term review findings 1 and 8: the Level 1 term lessons barely name tools and the toolbox page was dropped; the owner adopted the spine routine (strategy card in every lesson, one common look-back) for the holiday program on 23 Oct and it "follows" in the term lessons (`level_1_year_plan.md` section 1 update). The tool row and "tool I used" ticks depend on it. Rough extra cost, a guess: 1 to 1.5 agent-hours per lesson for the card and look-back in lessons 1 to 39 (the holiday rollout audit `docs/audit_final/spine_rollout.md` is the better source). Do it in the same rebuild so each lesson is built once.
- **Diagram work in progress.** `term/l1/audit/DIAGRAM_FIXES.md` is changing lessons keyed by number. Tell the diagram agents: skip the Doubles dominoes in l13 (the lesson is retired; the audit item "L13 S1 dominoes" is wasted); do the renumbering at a quiet moment, since concurrent edits to l13, l19, l20, l27, l30 and l40 will collide; the two new lessons need their own figure review.
- **Risk, load.** Six tools in a 6 to 8-year-old's head is a lot; hence the tool row shows only tools met and the Explore never asks the child to solve. If the trial shows overload, the fallback is a row of four in Terms 1 to 3 (draw it, list every way, table, work backwards).
- **Risk, untried.** No child has taken any term lesson. Run one consolidation lesson with a real group before Term 2 starts (about 22 March 2027 on secondary-source MOE dates) and adjust the other two from it.
- **Do not:** add a fifth gate or lengthen the Quest; add timers; put tool names inside Quest gate questions; make the tick a mark; let the scale become a table across children; merge Cubes and Views with Spot It or add a guess-and-check lesson in the same wave (those are separate review verdicts competing for the same limited slots; the freed slots here are only 13 and 27).

---

## 8. Sequencing against WAIT-DIAGRAMS, and the recommendation

Current release plan (`owner_decisions.md`, "WAIT-DIAGRAMS"): Books 1-8 released together once (a) the Level 1 diagram fixes are done and independently re-checked, (b) lessons 20 to 40 and all eight books are rebuilt (colour and B&W, `check_bw.py` ok, even page counts), (c) the owner says RELEASE.

**Proposed order (adds one step, does not change the gates):**
1. Owner approves this plan (section 9).
2. Finish the current diagram batch on the lessons that stay; hold l13 (Doubles), l19, l20, l27, l30, l40 for step 4.
3. Shared engineering: Quest v2 in `b_quest.py` and validator (1 day).
4. Renumber the three moved lessons (13, 19, 27), fix hand-offs, then write the new 20 and 30, reframe 40 (1 day, in parallel); diagram fixes for these six lessons are done in the same pass.
5. Independent audits and fixes; the diagram re-check covers them.
6. The already-required rebuild of lessons 20 to 40 and Books 3-8 (and Books 1-2 for the spine routine if it is included), B&W check, `term_books_spec.json`, `quote_request.md`.
7. Owner says RELEASE.

**Before the first release or a v2 after?** Before, for Terms 2 to 4. Reasons: (i) the rebuild and the diagram re-check are already on the critical path, so the restructure adds about 3 working days, not a second cycle; (ii) after release the books, the Quest Logs sent a week ahead, the printer quote page counts and the tutor scripts all exist in the old shape, and a v2 must reprint and re-send each; (iii) no family or tutor has used a term lesson yet, so a pre-release change costs no goodwill; (iv) the lesson 20 restructure is also the one that makes the tool row meaningful for the whole Term 2 to 4 sequence. A v2 after release is acceptable only for Term 1 option A (it touches Book 1 and the first-printed books) and, if the owner prefers, for the optional lesson 39 rebalance. The cost of waiting for Terms 3 and 4 alone is small (their books print later) but it leaves an inconsistent release: tool lessons in Term 2 and not in Terms 3 and 4.

---

## 9. Decisions for the owner

1. Retire **Doubles and Near Doubles** (lesson 13) and **Fill the Grid** (lesson 27) as lessons, absorbing their best items as in section 2. Yes or no.
2. Timing: Terms 2 to 4 before the first release (recommended), or as a v2 after.
3. Term 1 lesson 10: include option B in the same wave (recommended), option A, or leave Term 1 as built for 2027.
4. Rebalance lesson 39 to the eight card names (optional, 4.5 hours).
5. Reword the Quest privacy checklist so a word per habit in the tutor's own notes is allowed while counts and tallies stay banned (needed for the three-word scale; decision 3 of TERM-ALL-RECOMMENDED).

---

## 10. Levels 2 to 6 at plan level

Same rule for all levels: the Quest sits in lesson 10 of every term (10, 20, 30, 40). The x.10 lessons below are named as in each year plan (T1.10 is lesson 10, and so on). No renumbering anywhere; a lesson file is changed only when it is built (none of Levels 2 to 6 is built). Each build uses the section 1 template. Hours for a built level are covered by that level's pre-flight estimate; the additional cost of this plan per level is about one hour per x.10 lesson (the content is chosen as the lesson is written, not rewritten).

| Level | Lesson x.10 today | What changes | New idea that moves (to) | Quest Sprint note (Levels 4 to 6 only) |
|---|---|---|---|---|
| 2 | T1.10 Posts, Gaps and Queues | Becomes a Term 1 choose-the-tool lesson | Gaps versus posts becomes a Think harder strand of lesson T2.7 Find All the Ways (term review section 8) | None: no timed sets below Level 4 (owner decision, Quest Sprint) |
| 2 | T2.10 Puzzle Lab 2 | Already a spiral with no new idea; add the tool row (6) and two mixed gates | None | None |
| 2 | T3.10 Robot Recipes | Replaced by a consolidation lesson; sequences, loops and debugging are beyond MOE and nothing later needs them (review section 8) | Dropped, or one Investigation | None |
| 2 | T4.10 Year Challenge Day | Already a consolidation; Quest with all eight tools | None | None |
| 3 | 10 Price per Piece (added) | Becomes a choose-the-tool lesson | Unit price merges into lesson 8 Dollars and Cents (price of one from a pack, then many); the "exactly a total from two prices" item moves to lesson 10 as a choose-the-tool item (the plan's Level 3 pre-flight finding 4 says lesson 10 introduces an idea in about 19 minutes) | None |
| 3 | 20 The Class Shop, 30 The Playground Plan | Already integrative projects; keep them as the Quest-lesson problem, but the brief gives no tool hint; add the tool row | None | None |
| 3 | 40 Mathematicians' Fair | Keep; Quest with all eight tools | None | None |
| 4 | 1.10, 2.10, 3.10, 4.10 Challenge Day 1 to 4 | Already consolidation ("Choose a way in", "Choose a model", "Choose a move"); change the wording "Term N check" to the Quest, add the tool row and a tool menu in the Start here set | None | Optional Sprint, clearly labelled, beside the Quest (not inside the 20 minutes, which stay untimed): a 4-minute fluency set of 10 to 12 items at the lesson's Start here demand, in the flex minutes; pace shown against the child's own baseline; an anxious child may opt out; none in lesson 4.10 (year end) |
| 5 | 10, 20, 30 Review and Challenge | Already consolidation; keep, add the tool row and the "Choose a heuristic" Start here menu | None | Optional Sprint as for Level 4 (fractions, percent and measure facts); not at lesson 40 |
| 5 | 40 Year Showcase | Keep; Quest with all eight tools | None | None |
| 6 | 10 Term 1 Studio, 30 Term 3 Studio, 40 Capstone 2 | Already project or mixed lessons; keep; add the tool row; the Studio problem is a choose-the-tool problem (hand trace, then code) | None | Optional Sprint (code-trace and fluency facts); a Primary 6 child may opt out; no extra homework; not at lesson 40 |
| 6 | 20 Scale Models and Same-Height Triangles | Becomes the Term 2 Studio (choose-the-tool, Quest) | Scale Models moves to slot 19, taking the place of the stand-alone added lesson Mixtures, Fair Shares and Best Buys; mixtures (concentration) becomes a Think harder strand of lesson 13 percent change. The plan's "safest to skip in an exam period" note then moves from lesson 19 to lesson 14 (labelled enrichment) | As above |

Level 6 Term 3 is a **bridge block** (owner decision 5): lessons 21 to 29 connect primary reasoning to secondary-style algebra, graphs and code, are pitched at depth (why the rule works, checked by hand and by code) and not as acceleration of next year's drills, keep their "Beyond MOE" labels, and are not promised as PSLE preparation. The intake question (P6 children in Terms 3 and 4 around the PSLE, plan open question 1) is not decided here.

---

## Sources read

`docs/terms/owner_decisions.md`; `docs/pedagogy/term_review.md` (sections 0 to 3, 6, 8, 9, 11, 12); `docs/pedagogy/spine_routine_spec.md`; `docs/pedagogy/toolbox_card_notes.md`; `docs/audit_final/spine_rollout.md` (headings); `docs/terms/level_1_year_plan.md` to `level_6_year_plan.md` (lesson tables for lesson 10 of each term and the Quest paragraphs); `docs/terms/l3_preflight.md` (finding 4); `docs/printing/quote_request.md`; `docs/schedule/term_2027_t1_availability.md` (grep); `term/l1/lessons/l10.json`, `l13.json`, `l19.json`, `l20.json`, `l27.json`, `l30.json`, `l40.json` (timing, Quest, kits, cross-references); `term/l1/tools/b_quest.py` (bans, structure); `print/make_term_books.py` (header); `term/l1/AUTHORING.md`; `term/l1/audit/BOOKS_5_8_BUILD_REPORT.md`; `term/l1/audit/DIAGRAM_FIXES.md` and `DIAGRAM_AUDIT.md` (grep). Not done: reading the whole of any Level 2 to 6 pre-flight, a trial with children, or any build or validation run (this task was documents only).
