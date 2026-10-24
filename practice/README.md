# Online practice (sample: Level 3 lesson 3)

Static practice page for children. Every question has an answer, a hint, a worked solution and, where useful, the common slips and a template that makes unlimited "similar" questions with a computed answer.

    python3 build_practice.py p3l3          # verifies every answer by brute force, writes dist/
    python3 -m http.server -d dist 8790     # then open http://localhost:8790/?lesson=p3l3

Rules built in: no timers, no scores, no streaks, no leaderboard. A wrong answer gets a hint, then a worked solution; "Try a similar one" makes a new variant; "Try an easier one first" links to a Start-here item. Progress dots are stored only in the child's browser.

Next steps: more lessons (items come from the question bank), solutions gated to subscribed families, and counts (not scores) for the tutor summary.
