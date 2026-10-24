# Habits on the website: patch plan (staged, nothing applied)

Owner decision HABITS-WEB-YES. Source: `docs/pedagogy/inquiry_coverage.md` section 7 (rows 1-21). Nothing here is applied, built or published. `website/dist`, `website/mi_signup.html`, `website/level_pages/` and `website/hub/parent_questions.html` are generated copies: do not edit them, rebuild from the sources after the lawyer has seen the wording.

## Files in this folder
- `habits.html`: standalone preview of the new habits page (not linked anywhere).
- `patches/web.patch`: unified diff for `website/lp_build.py`, `website/level_pages.py`, `website/hub/qa.py`.
- `patches/docs.patch`: unified diff for the three parent-outcome / year-plan drafts.
- Both checked with `git apply --check` from the repo root (clean). Apply later with `git apply docs/website_habits_staged/patches/web.patch` (and `docs.patch`).

## Not covered by the patches (manual)
- Row 8, 14, 21: no change (kept on purpose). The slogan "Notice it. Test it. Explain why." stays (`lp_build.py:38`, `level_pages.py:260`, `build_site.py:61`, `shop_build.py:181`).
- Row 18 (`holiday_parent_outcomes_draft.md:15, 30, 45, 60, 75, 90`): keep the stem; reword individual "I can" items that name a habit as "I practise ..." when the owner picks the items. Not mechanical, so not in the patch.
- Row 4 is the interim wording (until Wonder and Look back are in every lesson, section 6). Revert to the fuller text only then.
- The patch adds a link `/habits/` in the home-page habits section. That route does not exist yet: when approved, copy `habits.html` into the site build (a `build_site.py` page entry) in a separate step, using the site's own CSS rather than this page's inline copy. Remove the link from patch if the page is not published.
- Line numbers below are from the files as they stand now; they differ slightly from section 7 (for example the "Hearing three different ways" source string is inside `lp_build.py:62`, and the build-time replace is `lp_build.py:178`).

## Edits (exact old -> new)

### `website/lp_build.py` line 44  (section 7 row 1)
Old:
```
<h2>Four habits of a young mathematician</h2><p class="muted">Every lesson follows the same four steps, so children learn how to think, not just what to write.</p>
```
New:
```
<h2>Habits of a young mathematician</h2><p class="muted">Every lesson practises six inquiry habits: noticing, wondering, trying, checking, explaining and looking back. Children practise how to think as well as what to write. <a href="/habits/">See the six habits</a>.</p>
```

### `website/lp_build.py` line 45  (section 7 row 2, 3)
Old:
```
<div class="rule"><b>1</b><h3>Notice the pattern</h3><p class="muted small">Look closely before rushing to an answer.</p></div>
<div class="rule"><b>2</b><h3>Test it with objects</h3><p class="muted small">Counters, coins and strips to check an idea.</p></div>
<div class="rule"><b>3</b><h3>Check your answer</h3><p class="muted small">Does it make sense? Try another way.</p></div>
<div class="rule"><b>4</b><h3>Explain why</h3><p class="muted small">Say or draw why it works. This is where learning sticks.</p></div></div></section>
```
New:
```
<div class="rule"><b>1</b><h3>Notice</h3><p class="muted small"><i>&ldquo;What do I see?&rdquo;</i> Look closely before rushing to an answer.</p></div>
<div class="rule"><b>2</b><h3>Wonder</h3><p class="muted small"><i>&ldquo;What could I ask?&rdquo;</i> Ask a question, or a "what if?", before looking for an answer.</p></div>
<div class="rule"><b>3</b><h3>Try</h3><p class="muted small"><i>&ldquo;Let me test it&rdquo;</i> Counters, coins and strips to test an idea.</p></div>
<div class="rule"><b>4</b><h3>Check</h3><p class="muted small"><i>&ldquo;Does it always work?&rdquo;</i> Try a second case. Does it still work?</p></div>
<div class="rule"><b>5</b><h3>Explain</h3><p class="muted small"><i>&ldquo;Here is why&rdquo;</i> Say or draw why it works. Children practise explaining in every lesson.</p></div>
<div class="rule"><b>6</b><h3>Look back</h3><p class="muted small"><i>&ldquo;What did I learn?&rdquo;</i> Say what was learnt, what was hard and what to change next time.</p></div></div></section>
```

### `website/lp_build.py` line 54  (section 7 row 4)
Old:
```
<p class="muted small">Find every way, spot the pattern, make up your own puzzle, and ask "what if?".</p>
```
New:
```
<p class="muted small">Many lessons include finding every way, spotting a pattern, making up a puzzle or asking "what if?".</p>
```

### `website/lp_build.py` line 55  (section 7 row 4)
Old:
```
<p class="muted small">Children say why it works, try a second method, and note what was hard.</p>
```
New:
```
<p class="muted small">Each lesson ends with a look-back where children note what was hard and what helped.</p>
```

### `website/lp_build.py` line 57  (section 7 row 5)
Old:
```
mathematical habits of mind. We do not
```
New:
```
mathematical habits of mind. The six Math Inquirers habits are our own working set. We do not
```

### `website/lp_build.py` line 62  (section 7 row 15)
Old:
```
<li>Notes on where your child is ready to be stretched further</li>
```
New:
```
<li>A note after each lesson: the inquiry habits we practised and one thing your child said or did</li>
```

### `website/lp_build.py` line 64, 180  (section 7 row 6 (source string)) - 2 occurrences, replace all
Old:
```
Hearing three different ways is how thinking grows.
```
New:
```
Explaining is one of the habits we practise in every lesson.
```

### `website/lp_build.py` line 180  (section 7 row 6 (build-time replace, now redundant: drop whole line 178 once the source string is changed))
Old:
```
"Children then explain how they know, and hear other ways of seeing the same puzzle. That is where the thinking grows.")
```
New:
```
"Children explain how they know and hear other ways of seeing the same puzzle. Explaining is one of the habits we practise in every lesson.")
```

### `website/level_pages.py` line 264  (section 7 row 7)
Old:
```
<h2>What your child learns</h2><p class="muted">%(blurb)s Each lesson follows the same four steps: notice the pattern, test it, check the answer, explain why.</p>
```
New:
```
<h2>What your child works on</h2><p class="muted">%(blurb)s Each lesson practises the inquiry habits: noticing, wondering, trying, checking, explaining and looking back.</p>
```

### `website/level_pages.py` line 274  (section 7 row 6)
Old:
```
Children then explain how they know, and hear other ways of seeing the same puzzle. That is where the thinking grows.
```
New:
```
Children explain how they know and hear other ways of seeing the same puzzle. Explaining is one of the habits we practise in every lesson.
```

### `website/hub/qa.py` line 39  (section 7 row 10)
Old:
```
Children quickly learn that the reason matters.
```
New:
```
This gives your child regular practice at giving a reason.
```

### `website/hub/qa.py` line 48  (section 7 row 11)
Old:
```
struggling a little is how thinking grows.
```
New:
```
being stuck for a little while is a normal part of working on a puzzle.
```

### `website/hub/qa.py` line 59  (section 7 row 12)
Old:
```
the goal is curiosity and persistence. Watch for signs your child is ready: enjoys puzzles
```
New:
```
the aim is to give children practice at wondering and at keeping going. Signs your child may enjoy these: enjoys puzzles
```

### `website/hub/qa.py` line 52  (section 7 row 13)
Old:
```
This uses ideas from approaches common in gifted education (depth, reasoning and explaining why) and extends thinking beyond the school syllabus without racing ahead of it.
```
New:
```
This uses depth, reasoning and explaining why, which are common in enrichment approaches, and goes beyond the school syllabus without racing ahead of it.
```

### `website/hub/qa.py` line 67  (section 7 row 9)
Old:
```
follows the four Inquirer steps: notice the pattern, test it with objects, check the answer, explain why.
```
New:
```
practises six inquiry habits: noticing, wondering, trying, checking, explaining and looking back.
```

### `docs/pedagogy/holiday_parent_outcomes_draft.md` line 43  (section 7 row 16)
Old:
```
and learn to test an idea before they trust it.
```
New:
```
and practise testing an idea before they trust it.
```

### `docs/pedagogy/holiday_parent_outcomes_draft.md` line 111  (section 7 row 17)
Old:
```
Your child will also learn eight simple tools
```
New:
```
Your child will also practise using eight simple tools
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 31  (section 7 row 19)
Old:
```
Children learn to test an idea, not just to give an answer.
```
New:
```
Children practise testing an idea, not just giving an answer.
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 82  (section 7 row 19)
Old:
```
Children learn how to check an idea.
```
New:
```
Children practise checking an idea.
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 257  (section 7 row 19)
Old:
```
They learn to prove that something cannot happen, to break a long question into short ones, and to write a problem
```
New:
```
They practise showing that something cannot happen, breaking a long question into short ones, and writing a problem
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 299  (section 7 row 19)
Old:
```
Children learn to write a rule with letters so that it covers every case.
```
New:
```
Children practise writing a rule with letters that covers every case.
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 13  (section 7 row 20 (adds the line))
Old:
```
a look-back where children say what was hard and what helped.
```
New:
```
a look-back where children say what was hard and what helped. Every term practises all six inquiry habits.
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 19, 70  (section 7 row 20 (appears in two level blocks; patch uses replace-all)) - 2 occurrences, replace all
Old:
```
### Lessons 1-10: Notice it
```
New:
```
### Lessons 1-10: emphasis on noticing
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 30, 81  (section 7 row 20 (appears in two level blocks; patch uses replace-all)) - 2 occurrences, replace all
Old:
```
### Lessons 11-20: Test it
```
New:
```
### Lessons 11-20: emphasis on testing
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 41, 92  (section 7 row 20 (appears in two level blocks; patch uses replace-all)) - 2 occurrences, replace all
Old:
```
### Lessons 21-30: Explain why
```
New:
```
### Lessons 21-30: emphasis on explaining
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 52  (section 7 row 20 (appears in two level blocks; patch uses replace-all))
Old:
```
### Lessons 31-40: Choose and create
```
New:
```
### Lessons 31-40: emphasis on choosing and creating
```

### `docs/pedagogy/term_parent_outcomes_draft.md` line 103  (section 7 row 20 (appears in two level blocks; patch uses replace-all))
Old:
```
### Lessons 31-40: Create and connect
```
New:
```
### Lessons 31-40: emphasis on creating and connecting
```

### `docs/terms/level_1_year_plan.md` line 33  (section 7 row 20)
Old:
```
The year arcs Notice it, Test it, Explain why, then Choose and create.
```
New:
```
Each term has an emphasis (noticing, testing, explaining, then choosing and creating) and every term practises all six inquiry habits.
```

### `docs/terms/level_1_year_plan.md` line 46  (section 7 row 20)
Old:
```
### Term 1: Notice it (
```
New:
```
### Term 1: emphasis on noticing (
```

### `docs/terms/level_1_year_plan.md` line 63  (section 7 row 20)
Old:
```
### Term 2: Test it (
```
New:
```
### Term 2: emphasis on testing (
```

### `docs/terms/level_1_year_plan.md` line 80  (section 7 row 20)
Old:
```
### Term 3: Explain why (
```
New:
```
### Term 3: emphasis on explaining (
```

## After applying
1. Rebuild with the normal site build (this writes `website/dist`, `mi_signup.html`, `level_pages/`, `hub/parent_questions.html`).
2. Search the output for "four steps", "four habits", "how thinking grows", "learn how to think": expect none.
3. Lawyer sees final wording first (`docs/owner_kit/lawyer_email_draft.md` question 14).
