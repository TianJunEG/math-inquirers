# Math Inquirers Level 1, term-time program: Term 1 (ages 6-8)

Term 1 of the Level 1 term-time program: 10 lessons of 90 minutes, all new content (the holiday course is a separate foundation course and is not copied). Plan: `docs/terms/level_1_year_plan.md`. Owner decisions: `docs/terms/owner_decisions.md`.

Status: **Term 1 (Lessons 1 to 10) is written, audited and fixed** (see `audit/FINAL_AUDIT_T1.md` and `audit/FINAL_FIXES_T1.md`). Later terms follow `AUTHORING.md`.

## Structure

```
term/l1/
  README.md            this file
  AUTHORING.md         steps, house style, quality rubric, the 9 remaining lessons (read this to write a lesson)
  AUDIT_L01.md         self-audit of Lesson 1 against the project's rubric
  build.sh             bash term/l1/build.sh 01   (validate, then build every output)
  schema/lesson.schema.json   JSON Schema for one lesson file
  lessons/l01.json     the single source of truth for Lesson 1 (one file per lesson)
  verify/l01_checks.py independent answer checks + brute-force oracles for the practice templates (one per lesson)
  tools/               validate.py (all checks), build.py and the builders, svg.py (pictures), common.py (timing model)
  out/l01/             generated files (do not edit by hand)
```

## One lesson file produces

| Output | File in `out/lNN/` | Style source |
|---|---|---|
| Tutor guide chapter (timings, time-stamped script, recording cues, answers, slide list) | `LNN_Tutor_Guide.pdf` and `.html` | project palette and fonts |
| Slide deck (1920x1080 `<section>` slides + `deck.json`, same format as `split/*/project`) | `deck/project/`, plus `LNN_Deck.pdf` and `.html` to view | `rebuild/slidekit.py` and `levels/restyle.py` look |
| Student workbook (Start here, Think harder, Go further, Investigation, exit ticket, look-back, kit cut-outs) | `LNN_Workbook.pdf` | `hp/wb_style.css` (A + D) |
| Answer key (separate PDF) | `LNN_Workbook_Answer_Key.pdf` | same |
| Home practice sheet (5 questions, one page) | `LNN_Home_Practice.pdf` | same |
| Home practice answers for grown-ups (separate sheet, so a double-sided print never shows answers on the back) | `LNN_Home_Answers.pdf` | same |
| Kit pages only, one side (Term 1 and 2 lessons with a kit) | `LNN_Kit_Pages.pdf` | same |
| Mi's Challenge Quest (last lesson of a term): Quest Log, tutor notes, grown-up note | `LNN_Quest_Log.pdf`, `LNN_Quest_Tutor_Notes.pdf`, `LNN_Quest_Parent_Note.pdf` | built by `tools/b_quest.py` from `build.sh` |
| One-page parent summary | `LNN_Parent_Summary.pdf` | `hp/parent_style.css` |
| Online practice (runner + data, brute-force verified variants) | `practice/` (serve it: `python3 -m http.server -d term/l1/out/l01/practice 8790`, open `/?lesson=t1l01`) | `practice/public` runner, unchanged |

## The lesson schema in one paragraph

A lesson file holds: `id, title, big_idea, child_idea, skill, moe` (strand label, tutor-only), `objectives`, `joining_cold` (the 6-minute Remember warm-up), `materials` (home-findable), `timing.parts` (11 parts summing to exactly 90 minutes with a 5-minute flex buffer and one optional slide), `sneak_peek`, `rec` (a short recording cue per part), `script.segments` (time-stamped lines of kinds SAY, READ, ASK, DO, SLIDE, WORK, HOLD, MOVE, REC, STUCK, NOTE; seconds are modelled, children's response time is in `resp` and `s`), `slides` (title, on-screen blocks, speaker note, part), `tiers` (start, think, go, investigation with hints, worked solutions and common mistakes), `talk`, `exit` (3), `look_back`, `home_practice` (5), `online_practice` (runner items with templates), `parent`, `safeguarding`, `tutor_prep`, `spare_time` (if-the-class-is-ahead menu: 2-3 optional whole-class activities, rules, never in the 90 sum). The JSON Schema is `schema/lesson.schema.json`; the validator enforces everything a schema cannot.

## Commands

```bash
python3 term/l1/tools/validate.py 01      # checks only (exit 1 on any FAIL)
bash term/l1/build.sh 01                  # validate then build all outputs
```

Needs Python 3 with Playwright 1.56.0 and Chromium (`/opt/pw-browsers`), `pypdf`, `jsonschema`, and Node (for the practice cross-check). Fonts come from `fonts/fonts.css` (`cd fonts && npm install && python3 make_fonts_css.py`). The builders use paths relative to the repo; if `fonts.css` points at `/home/claude/math-inquirers`, symlink that path to the repo.

## Where Lesson 1 follows the project rules

Tier principle (Start here = core, approachable, not yet taught at school; Think harder = a taught idea in a new setting, contest-style moves live here; Go further = mastery plus extension), neutral labels, no private chat, papers shown to the camera together, no claims such as MOE-aligned, GEP or SASMO preparation, a printed ruler only if the child has one at home (Lesson 1 needs none), materials found at home, short recording cues, 90 minutes with a standing buffer. Details and the checklist are in `AUTHORING.md`.
