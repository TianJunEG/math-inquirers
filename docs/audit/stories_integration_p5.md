# Level 5: mathematician stories integration

Source: `docs/stories/final_p5.json` (10 lessons, one person each). Branch `audit-fixes`, not committed or pushed. Verified with `python3 docs/audit/stories_verify_p5.py` (all 10 try-it answers recomputed; 10 story slides in the right place; 10 workbook boxes with no answer printed).

## Changes
| Where | What |
|---|---|
| `p5/content/stories.js` (new) | Reads the JSON; formats numbers in program style (2 450 000, 1250, x to the times sign, cm2/cm3, degrees); holds the short corner-box blurbs (2 to 3 sentences, only facts from the researched story) and short date/place labels. |
| `p5/data.js` | Attaches `content[n].story`, adds the script line `script.story` ("Story break (optional, 2 minutes): ..."), adds the Story break to the 33-37 row of the timeline (exports `stories`). |
| `rebuild/p5_gaps.py` (runs at the end of each `gen_p5lK.py`) | Adds slide `p5lK-story` after `p5lK-break` and before `p5lK-ws1`: title "Story break: <name>", story in 33px text, "Try it (optional)" box, a "Good to know" box when there is a legend or date note, speaker notes with skip instruction, link to the lesson, answer, sources pointer. Adds a "story follows" note to the break slide and a mention in the title-slide time plan. Label "33-37 MIN  •  OPTION": it sits inside the 4-minute brain break (after the stretch and drink), so the timeline, minutes 37-62 and the protected think time at 62-72 are unchanged. |
| `p5/guide.js` | New page "Level 5 mathematician stories" before the lesson scripts (table: lesson, person, country, years, link; honest-telling bullets with every legend note); a DO line at each brain break; the story try-it answer added to each lesson's "Answer key". |
| `p5/workbook_html.js` | Orange corner box "Meet a mathematician" under the reflection on every Investigation page: blurb, "Try it (optional)", one answer line. No answer on the child page. |
| Rebuilt | 10 decks (`rebuild/gen_p5l1..10.py`, then `levels/normfoot.py 5`, then `levels/restyle.py split/p5l1..10`), workbook PDF and body HTML, tutor guide docx/PDF/html, weekly zip (`hp/weekly_level.py`). Scheme and parent pack not rebuilt (their inputs did not change). |

## Checks
- Slides: no OVERFLOW from `rebuild/preview.py`; lowest content on any story slide is y 853 (limit 920); no font under 24px; 16 to 18 elements; notes 1264 to 1624 characters (limit 4000). Title and break slides re-previewed, no overflow.
- Workbook: still 57 pages; every lesson still starts on its own page (Lesson 1..10 at pages 3, 8, ..., 48); Investigation pages now end at 82 to 87 percent of the page height (they ended at 73 to 76 before), so no spill or clipping. Guide 89 to 93 pages; weekly tutor files 16 pages each.
- Safeguarding kept: whole-group invitation, volunteers only, pass always fine, no marking, no tally; story is skippable with a spoken skip line. Start here / Think harder / Go further names unchanged.

## Wording decisions (please review)
1. Lesson 6 (Mary Jackson): the program does not teach speed (SPEC.md), so the try-it now asks "how far in 1 hour?" (a rate) instead of "what is its speed", the link sentence says rates, and the story phrase "almost twice the speed of sound" became "almost twice as fast as sound travels". The facts are unchanged.
2. Lesson 7 (Adam Ries): the research note says the sources do not name percentages specifically. The slide shows only the birth-year uncertainty to children; the full note is in the speaker notes and the guide. The workbook blurb lists prices, wages, profit and loss, interest (what the sources say) and does not claim percentages.
3. Lesson 3 try-it is labelled as our own wording, and Lesson 5 keeps the "historians doubt the details" label on slide, in the blurb and in the guide.
4. Story texts were used as researched (99 to 125 words; Liu Hui 121 and Al-Karaji 125 are slightly over 120).
5. Corner box is on the Investigation page, not page 1: page 1 has only 2 to 21 percent spare height (Lessons 2, 5, 8 almost none), the Investigation page always has room. Children therefore meet the box after the break, at talk time or in open think time, not at minute 37.

## Left for later
- Final designer review of the box colours (orange, to match the Level 5 deck accent).
- Word workbook (`hp/workbook.js`) has no P5 version, so nothing to update there.
- `outputs/` copies of P5 files (scheme, taster, weekly email pack, question bank) do not use the stories and were not touched. The P5 workbook and guide are not copied into `outputs/`.
- Facts rest on the researched sources in the JSON (2 or more per person); Liu Hui, Alcuin, Eugenia Cheng, Adam Ries are marked medium confidence there.
