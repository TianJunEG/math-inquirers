# Wording review: Lesson 5

Format: old -> new, then a one-line reason. Strings are exact; (xN) = text appears in N places (slide, script, key).

- "Three of these sums make 30. Circle the sum that does not. 17 + 13   18 + 12   19 + 12   16 + 14" -> "Three of these sums make 30: 17 + 13, 18 + 12, 19 + 12, 16 + 14. Circle the sum that does not.". the four sums ran together on the printed page.
- "Is Siti correct? Circle:  Yes    No" -> "Is Siti correct? Circle Yes or No.". the Yes and No ran together.

## Later corrections in the same pass

- G2 and online g2: the sum is now written 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 (same total, 45), so no 7-word overlap with docs/books/school_paper_wording_patterns.md; the Think-harder pair hint "Pair 1 with 9" is unchanged.
- T3: sums are separated by commas (the four sums ran together when printed). S7 a): "Siti's answer: right or wrong? Circle Right or Wrong." (a plain "Is Siti correct? Circle Yes or No." was already quoted in the school-paper doc, so the overlap check refused it).
- Online c2 now reads "Fill in the missing numbers to make the next ten. 28 + ___ = 30" (changed together with S3).
- Maths and answers: unchanged. The only added answer is S7 c) = 4 (10 + 6 should be 10 + 4), which follows from the existing answer 14; the key and solution text are updated.

## Not fixed (template level, shared files)

- tools/b_print.py key page: the sneak-peek answer 1 prints as "12 stars." (a fixed word "stars." after the answer, copied from Lesson 1). Should be removed.
- tools/b_print.py page 5 fixed phrases: "Choose this any time you like. You do not have to finish it.", "Easy first step:", "Then:", "On your own, at the end of the lesson. No looking back."
- Blank style (rule 16/17): number sentences use "___" lines, not boxes, because totals such as 13, 34, 64 have two digits and the 36 px box is for single digits. Kept one style per question.
- Rule 25 (content range) mismatches: S4/S5 go to 28 + 6 = 34 and 35 + 7 = 42, G1 to 80 and G3 to 100 (P1 quizzes stay near 40; these stay in Start here only up to 64 in S6 d, 56 + 8). Listed, not changed: the plan fixes this lesson's range within 100.
- Kept on purpose: "tens bar", "ten-frame", "make a ten", "split" (taught in the lesson); "Make a ten first" stays on slides and in the tutor hints, not in the questions.

