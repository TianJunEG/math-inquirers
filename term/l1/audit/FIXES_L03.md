# Fixes after the independent audit: Lesson 3 (Digit Cards)

| # | Sev | Finding | What was done |
|---|---|---|---|
| 1 | Medium | S4 and E2 had no command and did not say "both cards" | Now "Make two numbers with both cards 6 and 2." with (a) "The greater number is ___" (b) "The smaller number is ___" (E2 likewise with 7 and 3). Solutions, key, slides and answer script updated. Answers unchanged (62, 26; 73, 37). |
| 2 | Medium | G1 and G3 used 3-digit numbers with hundreds not taught | Replaced, not taught: G1 is now cards 2, 5, 6, 9 (a) greatest number less than 60 = 59 (b) smallest number greater than 50 = 52; G3 is a two-digit clue puzzle with cards 1, 3, 4, 7 (between 35 and 45; ones digit greater than tens digit) = 37, every clue needed. verify/l03_checks.py, key, solutions, mistakes, online practice g1 and g3 changed to match (g1 template and its oracle removed). Tutor script notes and moe.note no longer mention 3-digit work. |
| 3 | Medium | S3 picture small, Mei only | Partly done: text now says "Count the bars and squares in Mei's picture." Picture size and a two-figure question are template limits (not edited): see below. |
| 4 | Medium | Investigation had no writing area | Already fixed by the template (4+ lines now print); viewed on page 5. |
| 5 | Low | One line for "write how you know" on T1, T2 | T1 and T2 now have 2 lines. |
| 6 | Low | G2b 16 numbers, no space | G2 asks how many (not to list); it keeps 3 lines. No change needed. |
| 7 | Low | greater vs greatest for two numbers | S4 and E2 now use greater/smaller (two numbers only). Three-card items keep greatest/smallest. |
| 8 | Low | "Circle Yes or No" had no words | Fixed by the template: Yes / No print on S6 and home 3. |
| 9 | Low | T1 "Use two cards" | Now "Use two different cards" (T1). |
| 10 | Low | G3 38 words | New G3 is 33 words in three short sentences. |
| 11 | Low | Mistaken child always Ravi/Siti | S6 now Kumar (Ravi stays the winner in S8). |
| 12 | Low | No make-your-own item | Not added to the workbook (Go further has exactly 3 items); it exists in the Spare-time menu and online g4. |

Owner decisions: moe.note and tutor_prep (tutor guide) and parent.summary now say Term 1 goes beyond the school Primary 1 syllabus on purpose; no MOE-aligned claim. S8 drawing: draw_strokes set to 14 (2+5 and 5+2 shapes; a bar is one long rectangle), warning gone.

Template/tool problems left for the owner: (a) the question picture width (270 px on page 1) makes the kit picture small and allows only one figure per question (S3 cannot show Mei and Ben); (b) home sheet page 2 is 43% full.

Result: validator 22 pass, 0 WARN, 0 FAIL, leak check clean; workbook 7 pages, PDF fills 91, 94, 85, 91, 96% (kit pages 89, 84%); home 2 pages; parent 1 page.
