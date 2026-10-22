# Mathematician stories: Level 4 integration

Source: docs/stories/final_p4.json (10 lessons, one person each). Nothing committed, pushed or published. No shared files (levels/*, hp/*, rebuild/slidekit.py) edited.

## What changed
- New `rebuild/p4_stories_build.py`: writes `p4/stories.json` (slide story, workbook blurb, try-it, answer, link) and verifies every try-it answer in Python (all assertions pass: 15 / 11 prime test, 97 420 and 20 479 by permutations, 6 x 48 = 288 by 300 - 12 and by division, 1/3 + 1/6 = 1/2 and 3/4 = 1/2 + 1/4, 2/17 = 1/12 + 1/51 + 1/68, 3.45 + 2.8 = 6.25, 360/10 = 36 and 360/7.2 = 50, 8 x 5 = 40 with a longer slanted side, squares 4 and rectangles 2 lines, biggest rise 5 degrees at 9 am to noon, 6 hens and 4 cows unique). Story word counts are 98 to 111 (checked 90 to 112).
- `rebuild/p4_fix.py`: new `story_slide(n)` and `story_tutor_line(n)`; `finish()` adds slide `p4lN-story` ("Story break: <name>", 32-34 MIN, OPTIONAL, 36px story, "Try it (optional)" box, answer, skip instruction, legend label and confidence in the speaker notes only); `order()` places it right after `p4lN-break`; break-slide notes explain the 2 + 2 minute split; title-slide time plan mentions it. All ten decks regenerated with `rebuild/gen_p4l1..10.py`, then `levels/restyle.py split/p4lK`. Slides are 29 to 31 per deck (+1 each). Preview: no overflow, min font 24, notes about 1000 chars.
- `p4/workbook_html.js`: "Story corner" box (name, country, years, 2-sentence blurb, Try it, no answer) at the foot of the Investigation + Looking back page. Lesson 8 only: that page is full, so its box sits at the foot of its Think harder page.
- `p4/guide.js`: tutor line "Story break (optional, 2 minutes): ..." plus skip instruction at each brain break; "Story corner try-it" with answer in each lesson answer key; new "Level 4 stories: the mathematicians" page (table lesson, person, country, years, link) before "How to use the scripts".
- Rebuilt with `bash levels/build_level.sh 4`. `python3 rebuild/p4_pagecheck.py`: all 10 lessons 2 core pages, OK. Workbook is 61 pages, 5 pages per lesson, so no spill.

## Content decisions (please review)
- Euclid try-it: dropped the "triangle on the same base" part (P4 rules forbid area of triangles); replaced with "which has the longer way round?" (slanted shape, answer: longer, bigger perimeter). Story sentence about the triangle half was also left out.
- Eratosthenes: the "about 250,000 stadia" figure was left out (P4 rule: no numbers above 100 000). Story keeps 7.2 degrees = one fiftieth of a turn and the uncertainty about his unit.
- Katherine Johnson keeps "accounts say" (Glenn story); no reference to the film. Mahavira is marked medium confidence in the source (little known); worded "we know almost nothing else".
- Stories trimmed from the source versions (some 120 to 144 words) to fit slides; nothing added.
- Terence Tao "youngest ever competitor/winner" and Euclid / Eratosthenes dates are as in the source; dates marked as estimates.

## Left for you
- Slides not re-published (no publish tools used); the published Claude Slides artifacts for P4 still lack the story slide.
- Word guide (.docx) and PDFs are regenerated; weekly PDFs zip and parent pack rebuilt by the build script. outputs/schemes P4 pdf was touched by scheme.py as part of the standard build.
- No illustration for the stories (icon_idea in the JSON unused).
