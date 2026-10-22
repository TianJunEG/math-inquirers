# Levels named by age, and placement by diagnostic
Each level is a three-year age band that overlaps the next (6-8, 7-9, 8-10, 9-11, 10-12, 11-13), so children who are ahead or behind their school year can join the level that suits how they learn now. Typical school year in Singapore:
| Program level | Name on pages (3-year band) | Typical school year |
|---|---|---|
| P1 | Ages 6-8 | Primary 1 |
| P2 | Ages 7-9 | Primary 2 |
| P3 | Ages 8-10 | Primary 3 |
| P4 | Ages 9-11 | Primary 4 |
| P5 | Ages 10-12 | Primary 5 |
| P6 | Ages 11-13 (maths + coding bridge, after PSLE) | Primary 6, after PSLE |
Pages show the age name first and the school level in brackets, e.g. "Ages 8-10 (builds on Primary 3 maths)".
## Placement
This is the one placement rule (tutor guides should quote it, not restate it differently). The Placement Check PDFs (`diag/build_diag.py`), the extras (`levels/mkextras.py`) and the website (home page `website/lp_build.py`, level pages `website/level_pages.py`, parent hub `website/hub/qa.py`) all follow it.
1. Parent takes the free 30-minute diagnostic (the Math Inquirers Placement Check) for the level that matches their child's school year. There is no wider "year either side" rule: a child who finds it too easy tries the next level's check (step 3).
2. The score is the warm-up plus the 6 main questions, out of 10, which is the percentage. The Brain stretchers are a bonus and are not counted. Questions ticked "not learnt yet" score 0 and show what to teach first.
   - 70% or more (7 to 10): enrol at that level.
   - 40-69% (4 to 6): enrol at that level with a note to the tutor that support may help, or choose one level down.
   - Under 40% (0 to 3): recommend one level down.
3. If the check was too easy (90% or more, so 9 or 10 out of 10), the child may also try the diagnostic one level up. There is no separate warm-up or Brain stretcher rule.
4. Parent has the final say; the level can be changed before lesson 1 at no cost. Same price at every level.
5. Ages 6-8 is the lowest level, so "one level down" does not exist there: for a score under 40% (and, in the middle band, instead of "one level down") weaker learners start with the free taster and a tutor chat. Ages 11-13 has no level above, so the 90% line only points to Go further questions and open investigations.
