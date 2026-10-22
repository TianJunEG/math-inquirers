# Authoring a Term 1 lesson (Lessons 2 to 10)

You write ONE lesson as ONE data file, `term/l1/lessons/lNN.json`, copy the shape of `l01.json` (the pilot), plus `term/l1/verify/lNN_checks.py`. Everything else (guide, deck, workbook, key, home sheet, parent page, online practice) is built from the data file. Do not edit generated files in `out/`. Do not edit shared tools unless a lesson needs a new picture type (add it to `tools/svg.py` and `tools/b_deck.py`, say so in your report).

## Steps

1. Read: `docs/terms/level_1_year_plan.md` (your lesson's row, Term 1 intro, tiers, section 3 reuse rules), `docs/terms/owner_decisions.md`, `docs/moe/syllabus_by_level.md` (strand), `docs/sasmo/g1_analysis.md` and `g1_original_problems_draft.md` (contest moves, ideas only), `docs/books/word_problems_g1_g2_*` (word-problem practice), `docs/audit/audit_p1.md`, `reaudit_p1.md`, `timing_p1.md` (the rubric), and `term/l1/lessons/l01.json` plus `out/l01/` (look at the guide, deck and workbook).
2. Copy `l01.json` to `lNN.json`; change `id, lesson, lesson_in_term, title, big_idea, child_idea, skill, moe, contest_moves, objectives, joining_cold`.
3. Write the Remember warm-up (6 minutes, see the joining-cold rule below).
4. Design the lesson on paper: one big idea; Explore (hands-on, objects first), Mini-lesson (about 5 slides, one new idea), tiers.
5. Fill `slides` (including an optional `s-menu` slide in the flex part), then `script` (every slide shown exactly once, in its part; the first lines of each part after Opening are a SLIDE then `{"k":"REC","text":"@rec"}`), `tiers`, `talk`, `exit`, `look_back`, `home_practice`, `online_practice`, `parent`, `safeguarding`, `tutor_prep`, `spare_time`.
6. Write `verify/lNN_checks.py`: recompute EVERY answer from first principles (enumerate, count, simulate; do not reuse the lesson's own formulas). Provide `ORACLES` (one brute-force function per templated practice item, keyed by item id) and `BASE_ENV`. `run(d)` returns the number of checks.
7. Run `python3 term/l1/tools/validate.py NN` until it prints 0 FAIL, then `bash term/l1/build.sh NN`.
8. Look at the rendered deck (`LNN_Deck.pdf`), guide, workbook and parent page at readable size; fix overflow, clipped text, unreadable pictures. The deck builder reports slides that overflow.
9. Audit your lesson against `AUDIT_L01.md` (copy its table; score honestly; fix failures). Write `term/l1/AUDIT_LNN.md`.
10. Commit only your own files: `lessons/lNN.json`, `verify/lNN_checks.py`, `AUDIT_LNN.md`, `out/lNN/`. Explicit `git add`; never push.

## Build command

`bash term/l1/build.sh NN` (validate first; stops on any FAIL). Outputs in `term/l1/out/lNN/`.

## House style and voice

- Singapore/British spelling; "program" for the brand; "colour", "centre". Money in $ and cents; names Mei, Ali, Ben, Siti, Ravi (mix, no stereotypes).
- Child text: short sentences (aim under 15 words), concrete, one idea per sentence, numbers as digits. A 6-year-old may read slowly: the tutor reads every question aloud (it is in the script).
- Tutor voice: warm, plain, "we"; SAY lines under about 60 words, read aloud at 120 words a minute.
- Labels everywhere: **Start here / Think harder / Go further / Investigation**. Never Core, Challenge, Stretch, Fast track, "early finishers", "strong thinkers", "gifted", "advanced". The validator rejects them.
- No unicode shape or emoji glyphs; pictures are SVG from `tools/svg.py`.
- Mascot: **Mi the dolphin** (owner-chosen; `term/l1/assets/mi_dolphin_transparent.png`, never edit the image). Use small and consistently: title and goodbye slides large (slide field `mascot: {size:"l", say:"..."}`), at most 2 small spot appearances (`size:"s"`, e.g. Remember and Look-back), tutor guide cover, parent header, workbook page 1 corner (24 mm, must not take writing space). Not on every page or slide (validator: at most 5 slides). Mi says only short friendly lines (title: "Hi, I'm Mi. Let's notice, test and explain why!"), never about answers or numbers. Do not show or rely on the calculator: the program teaches mental and written methods.
- Shared look: palette navy `#1B2A49`, teal `#1F7A6F`, yellow `#FFC93C`, cream `#FFF9EC`; Fredoka headings, Nunito Sans body; slides 1920x1080 modern2; workbook A + D grid paper.

## Shared assets to reuse (do not rebuild)

`tools/svg.py` (bundles of ten and singles, base-ten kit blocks, scatter, ten-frame, kit cut-out page), `tools/b_*.py` builders, `hp/wb_style.css`, `hp/parent_style.css`, `fonts/`, `practice/public/` runner (unchanged), `levels/reccues.js` conventions (the REC cue kinds), slide pattern of Lesson 1 (title, routine/rules only in Lesson 1, remember x3, sneak-peek, explore x3, mini x5 to 6, break, workbook slides with a check slide after each page, choice slide, talk, exit and answers, look-back, end, one optional slide).

## Rules every lesson must keep

**Tiers.** Start here = core, approachable, not yet taught at school (5 to 8 questions, workbook pages 1 and 2, under 20 minutes for a middle child). Think harder = a taught idea in a new setting (3 to 5 questions, page 3); every contest-style move (digit-card puzzles, changing sequences, queue counting, make-equal transfers, spend exactly an amount, fold and punch, day-of-week cycles, Latin squares, routes) is here and never Start here (owner decision 6). Go further = mastery plus extension (exactly 3, page 4). Investigation (page 5) has an "Easy first step". Every question has an answer, a hint, a worked solution, common mistakes and `mins`.

**Joining cold.** Lessons 2 to 10 open with a 6-minute Remember warm-up that (a) names exactly what the lesson needs (`joining_cold.remember`), (b) takes it from holiday topics or earlier Term 1 lessons, (c) re-teaches it with objects, fingers or a picture so a child who has only counted to 20 can join, (d) never assumes the previous lesson except through the warm-up, (e) uses no word that only an earlier lesson defined without defining it again. State in `joining_cold.note` whether the lesson is safe to miss (plan, Term 1 note: safest is Lesson 4; Lessons 1 and 5 to 7 are hardest to miss). Holiday topics the plan assigns to warm-ups: skip counting in 2s, 5s, 10s (L4); bonds to 10 and 20 (L5, L8); cube/ruler measuring (L9); "I think of a number" (L10).

**Safeguarding and privacy.** No private chat or private messages to children, ever (the validator rejects it). Sneak-peek and exit answers: each child holds their own paper to the camera at the same moment, once; no boards held up in front of the group; never read a name with a right or wrong answer. Check-ins for "I am still stuck" happen in the open session. Breakout rooms only when the task needs partner talk (they cost about 3 minutes round trip; Lesson 1 used none), and the tutor visits every room. Recording: tutor and screen only. Look-back is never collected or read out; a pass is always allowed. Talk time: volunteers first, no cold-calling, no tallies or rankings. The tutor never says who is on which page; invitations go to the whole group.

**If the class is ahead (spare-time menu).** (a) Whole class ahead: use the Spare-time menu in the Flex time and the optional Go further slide; pick one or two activities; depth not speed ("Is it always true?", "Make a puzzle for your grown-up", "Teach it back"). (b) A few children ahead: they may choose Go further or the Investigation, which are open to everyone; never a finisher label, never named. Never teach content the next lesson needs. The tutor slows down with "How do you know?" instead of rushing on. The menu minutes are optional and are never added to the 90 sum.

**Claims.** No "MOE-aligned", "syllabus-aligned", "GEP", "SASMO preparation", exam results, ranks or predictions on any child or parent page. The MOE strand is a tutor-only label. Contest moves are tutor-only labels too.

**Materials.** Findable at home; no purchases; never matches, toothpicks or sharp things; a printed ruler or a real ruler only if the child has one (`materials.ruler`), and then say so on the parent page; cut-outs are on a kit page that a grown-up cuts beforehand.

**Timing.** Eleven parts summing to exactly 90: Opening, Remember 6, Sneak-peek 4, Explore about 14, Mini-lesson about 10, Break 4, Workbook about 28, Talk 6, Exit 6, Look-back 3, Flex 5 (the buffer, nothing new). Lesson 1 has a 4-minute opening; later lessons may use 2 and give the 2 minutes to Explore. Script lines carry modelled seconds; each part must fit its minutes, the whole script must need at most 86 minutes, and the slow-class scenario (speech 10% slower, children and slide changes 20% slower) at most 90.

**Age-appropriateness (6 to 8).** One new idea; objects before symbols; no reading-heavy items in Start here; at most one writing line per Start here item; counting and numbers within 100; no speed pressure, no timers shown as races; a movement break; a worked example before each kind of task.

**No copied contest text.** Write original problems. You may adapt the ideas in `docs/sasmo/g1_original_problems_draft.md` and `docs/books/word_problems_g1_g2_original_draft.md`. The validator rejects any 7-word overlap with the SASMO analysis and solution notes and the books.

## Quality checklist (rubric)

Mark each PASS/FAIL in `AUDIT_LNN.md`; every FAIL is fixed or explained.

1. Schema and validator: 0 FAIL, warnings explained.
2. All answers verified by `verify/lNN_checks.py` (independent recomputation) and all practice variants verified by oracle and by the runner's JavaScript.
3. Timing: parts sum to 90; no part OVER; scripted need at most 86 minutes; slow-class at most 90; the part table in the guide matches the slide minute badges.
4. Slides: each shown once, in its part; no overflow (builder reports); on-screen text readable at 1920x1080 (at least 34 px body); every slide has a speaker note.
5. Tiers: counts and tier meaning as above; contest moves at Think harder; Start here approachable; neutral labels; Investigation has an easy first step; nothing named publicly.
6. Sneak-peek: Q1 access, Q2 thinking, unmarked, papers to the camera once, no private chat.
7. Recording: REC cue per part at most 26 words, with a child-watching-later action; questions and answers read aloud in the script; chapter markers in the guide.
8. Safeguarding block present and consistent with the script (see above).
9. Joining cold: Remember covers prerequisites; safe-to-miss stated; warm-up fits 6 minutes.
10. Materials home-findable; ruler only if the child has one; kit cut-outs fit one page.
11. No overclaims; no copied text (validator).
12. Printed pages: workbook pages not overflowing (check page count and view every page); answers only in the separate key; home sheet 5 questions with answers on page 2; parent page one page.
13. Gifted-style rubric (12 criteria, `docs/audit/reaudit_p1.md` instrument A) at least 18/24; tier compliance 100% (strict).
14. Real-PDF check (validator `outputs`, measured by rendering with pdftoppm): the workbook has exactly the designed number of pages (no orphan page from a spilled question), no page under 40% full (FAIL) and every page at least about 85% full; home sheet 2 pages; parent page 1 page. Workbook pages at least about 85% full (the validator warns below 80% and above 100%), with writing space sized for ages 6-8: answer lines about 31 px (8 mm) tall, drawing boxes about 105 px, 18.5 px question text, a generous gap between questions. If a page is under 85%, first enlarge writing space, then add a sensible question (keep tier meaning; update slides, script, timing, key, answers script and practice).
15. Spare-time menu present (`spare_time`: 2 or 3 whole-class activities of 3 to 5 minutes each with a tutor line, a recording cue of at most 26 words and an answer where one exists; an optional menu slide; shown in the guide; never added to the 90-minute sum) and the three rules below kept.
16. Reading load: no child-facing string over 40 words without a reason (validator warns).

## The 9 remaining lessons (plan rows; S = Start here, T = Think harder, G = Go further)

Strand names follow the plan. "New topic" lessons need a syllabus check by the owner or a tutor; say so in `moe.note`.

| # | Title | Big idea | Strand and contest moves | S / T / G | Skill |
|---|---|---|---|---|---|
| 2 | Number Words and the Number Line (new topic) | Every number has a place and a name | Whole Numbers (number words, counting to 100, before/between/after; nearest ten is flagged, check the syllabus). Keep spelling small | S: say, read, write numbers to 100 on a line; one before, one after. T: which ten is nearer; numbers between two marks. G: a line with the marks missing | Representing on a scale |
| 3 | Digit Cards | Order of digits changes the number | Whole Numbers (compare and order, compare sets). Contest: digit-card clue puzzles at T; 3-digit only at G | S: make and order 2-digit numbers; compare two sets. T: smallest and largest from three cards; every number fitting two clues. G: three-card clues, a number that fits all | Systematic cases |
| 4 | The 100 Square Explorer | Patterns live in rows and columns | Whole Numbers (patterns, counting to 100). Contest: changing-step sequences at T. Warm-up: skip counting 2s, 5s, 10s | S: colour 10s, 2s, 5s and say what you see. T: down one row adds 10; a sequence with a growing gap (+1, +2, +3). G: sum of the two numbers before; two rules interleaved | Pattern generalising |
| 5 | Make-a-Ten Adding | Make tens first | Addition and Subtraction (more than two 1-digit numbers; within 100; algorithm only after the mental method). Warm-up: bonds to 10 and 20 | S: 8 + 6, then 28 + 6 by making ten. T: add four numbers by finding tens. G: 18 + 7 + 12 + 23 + 3 + 17 | Strategy choice |
| 6 | Tens Jump, Ones Hop (new topic) | Add and take away tens without carrying | Addition and Subtraction (mental 2-digit plus or minus ones or tens without renaming). Number line jumps | S: 34 + 10, 34 + 20, 34 - 10. T: 34 + 25 by a tens jump then ones hops. G: how many jumps from 7 to 97, and the shortest way | Chunking |
| 7 | Take Away, Count Up | Difference is a gap | Addition and Subtraction (within 100, relation to addition) | S: take away 10s and 1s. T: count up to find the difference. G: which is quicker, and why? | Choosing a method |
| 8 | Balance and Swap | Adjust one side, adjust the other | Addition and Subtraction ("=" as balance). Beyond P1: compensation (38 + 25 = 36 + 27), at T. Boxes only, no letters. Warm-up: bonds | S: box numbers, 27 + 16 = box + 9. T: spot equal sums without adding; compensation. G: a chain of equal sums with two boxes | Reasoning about equality |
| 9 | Draw and Measure | Be exact to the nearest centimetre | Length (draw a line, measure to the nearest cm, compare). Needs a cm ruler: only if the child has one at home, else a printed ruler on the kit page. Warm-up: cube/ruler measuring | S: draw 7 cm; compare two drawn lines. T: lines on a bent path; a line that starts at 2 on the ruler. G: three pieces of a 30 cm ribbon | Precision |
| 10 | Story Steps: Read It Twice (added) | One operation per step | Addition and Subtraction in context (within 100). Gap: multi-step stories and reading traps. Bar strips come in Lesson 12. The 20-minute end-of-term check is taken in the last 20 minutes of this lesson or in the make-up slot (10 questions, one per lesson, privately returned; see plan section 5): build it as an extra data block. Warm-up: "I think of a number" | S: two-step story, one operation per step. T: reversed wording ("3 fewer than"); a story with a trap (who is in the group). G: three-step story, write it for a partner | Reading and planning |

Term 1 report line (plan, section 5): "Your child is learning to see numbers as tens and ones, to notice patterns and to say why." Each lesson file has its own `parent.report_line` too.

Safest to skip or make up: Lesson 4. Hardest to miss: Lessons 1 and 5 to 7.


## Template fields added for lessons 2 to 10 (all optional, backward compatible)

- `workbook.header` strand line printed on every page (default "<strand>: <big idea>"); `workbook.hint_p1`, `hint_p3`, `hint_p4` intro lines (generic defaults); `parent.quote` (default `big_idea`); `timing.skip_order` (list); `limits.max_child_words` (default 40) and `limits.max_parent_words` (default 90) for the reading-load warning. Nothing in the builders is specific to Lesson 1: titles, lesson numbers, minute marks and page lists come from the lesson file. The validator fails if a built file of lesson NN contains another lesson's title (except as a pointer after "Next lesson" or "Lesson N:") or stray "Lesson 1" text.
- **Kit pages.** `workbook.kits` is a list of cut-out pages (each is one printed page after page 5): `{"type":"base_ten"}` (tens bars and ones squares), `hundred_square`, `number_strip` (`start`,`end`), `cards` (`labels`, `cols`), `shapes` (`shapes:[{kind,color,n}]`), `number_line`. Use `"kits": []` for none. If the field is absent the old tens-bars page is printed (lessons written before this change keep working) and `materials.kit_pages` should say so.
- **Figure types** (in `slides[].blocks` of type `visual`, and in a question's `visual`): `bundles`, `scatter`, `ten_frame`, `ten_to_bundle`, `hundred_square` (`blank`), and **`number_line`**: `{"t":"visual","type":"number_line","start":0,"end":50,"step":10,"label_every":10,"marks":[34],"hide":[20],"jumps":[[30,40,"+10"],[40,44,"+4"]],"highlight":[30]}`. Big labels (34 px), tall ticks at labelled numbers, curved teal jump arrows with labels, yellow highlighted tiles, `hide` draws an empty answer box under a tick. In Python: `svg.number_line(start, end, step, label_every, marks, hide, jumps, highlight)`.
- **Answer boxes.** In question and part text, `___` prints a dashed answer line and `[]` prints a clear empty square box (36 px, rounded) for ages 6-8; use the box for single digits and the line for words or longer answers.
- **Dark slides** (`kind: "dark"`) no longer carry the cloud decoration (only the title slide does); the deck check fails if Mi, a speech bubble or a decoration overlaps text.

## More template fields (second pass)

- **100-square pictures** (figure type `hundred`, in slides and questions): `{"type":"hundred","shade":[..yellow cells],"shade2":[..mint cells],"hide":[..empty cells],"mark":[..counter cells],"outline":[..teal border],"arrows":[[from,to,"+10"]],"rows":[1,10],"cols":[1,10],"per":10,"cell":46,"qmarks":true,"tags":{"34":"a"},"wide":true,"label":"..."}`. A blank colourable square is `{"type":"hundred"}`; use `shade` for the answer key and for slides, nothing for the workbook. `rows`/`cols` choose a window. Number tiles with growing gaps: `{"type":"seq","items":[1,2,4,7,null],"gaps":["+1","+2","+3","+4"],"hl":[4]}` (`null` is an empty dashed tile). Kit page `{"type":"hundred","cell":64}` prints a full numbered square. A `cols` block may have `weights` (e.g. `[3,2]`) for unequal columns. In the workbook a question with a 100 square puts the picture beside the answer lines (`wide:true` for full width). On deck question rows a 100 square is left out (it does not fit).
- `workbook.choice_after` (default 3): the number in "After question N you may choose: carry on, or try Think harder." `workbook.home_hint` (default "Use real things or draw it.") is the home-sheet intro hint. `timing.skip_order` is an array of strings (a plain string also works).
- **Audit file is mandatory.** `build.py` writes `AUDIT_LNN.md` as a draft (automatic rubric table from the validator plus `TODO(author)` judgement lines) if it does not exist, and exits non-zero while any `TODO(author)` is left. Fill every judgement honestly, then rebuild; an audit without `TODO(author)` is never overwritten.

## Third pass (workbook audits)

- **Investigation writing space:** page 5 always reserves 4 to 6 ruled lines (the builder tightens spacing, never drops below 4). Keep the Investigation answer short enough for 4 lines.
- **Choice words to circle.** Write "Circle Yes or No.", "Circle Right or Wrong." or "Circle/Tick True or False." in the question or part text and the builder prints the words on the answer line to circle. For other choices set `"choices":["LEFT","RIGHT","SAME"]` on the question or part (or put "LEFT / RIGHT / SAME" in the part text). The validator fails if the text says Circle a word and no choices are printed.
- **Every question needs an answer slot:** `parts` with `___` or `[]`, `lines`, `draw`, `choices`, or empty boxes in the picture (`hide`). The validator fails if none.
- **Drawing size:** a question with `draw: true` that needs about 25 strokes or more draws a validator warning (a bundle of ten counts as 10 strokes; ask for a bar or ring, or lower the numbers). Set `draw_strokes` to override the estimate.
- **Ruler figure** (Lesson 9 and others): `{"type":"ruler","start":0,"end":12,"objects":[{"label":"pencil","from":0,"to":9,"color":"#FFC93C"},{"label":"crayon","from":2,"to":7.5}],"mark":9}`. In the workbook it prints at true 1:1 scale (measured on the PDF: a 12 cm ruler strip is 133.1 mm wide including margins; keep end minus start at most 15 so it fits the page). On slides it scales to the screen. It is never a cut-out: families use their own ruler (owner decision).
- **PDF checks:** the page-fill check also fails if a workbook page ends with a question tab whose body is on the next page.
