# Wording review, Lesson 2 (Number Words and the Number Line)

Changes in `lessons/l02.json` (maths and answers unchanged). Old -> new, reason.

| # | Where | Old | New | Reason |
|---|---|---|---|---|
| 1 | S1, sneak puzzle 1 | "Write the missing numbers on the number line." | "Fill in the missing numbers in the boxes." / "...on this line:" | Fixed command phrase |
| 2 | S2 | "Write the missing numbers." | "Fill in the missing numbers." | Same command for same job |
| 3 | S3 | "Write the number one before and the number one after." | "Fill in the number just before and the number just after." | Plainer |
| 4 | S4, E1, home 2 | "Read the number word. Write the number." | "Write the number(s) in digits." | One job |
| 5 | S5 | "Copy the number word." (but the child writes it from digits) | "Write each number in words. Word bank: ..." | Picture/text mismatch: nothing to copy |
| 6 | S6 | "This number line counts in tens. Write the missing numbers." | "Fill in the missing numbers. The numbers go up by 10 each time." | Command first |
| 7 | S7, E2 | "Which two tens is each number between?" | "Fill in the missing numbers." (frame "23 is between [] and []") | Question became a frame |
| 8 | S8 | "Siti wrote 57, ... Say what she mixed up." | "Siti counts: 57, 58, 59, 510, 511." (a) "Is Siti's counting correct? Circle Yes or No." (b) "After 59 comes []" | Hidden second question; no space to explain |
| 9 | T1 | "Count the hops on the number line to check." | removed | Method in the stem |
| 10 | T2 | "Do not count 28 or 35." in the stem; "How many numbers are between" | "How many numbers are there between 28 and 35? (Do not count 28 and 35.)"; frame "There are [] numbers between them." | Instruction after the question; unit in the frame |
| 11 | T3 and online item 9 | "Mystery number. Clue 1... Clue 3: One before me is halfway..." | "My number is between 50 and 60. It is nearer to 60 than to 50. The number before it is halfway between 50 and 60. What number is it?" | Riddle as one paragraph |
| 12 | T4 | "It hops on one number at a time... Write each number it lands on, and how many hops." | stem "Mei's frog is on 96. It hops 1 number at a time to 100." (a) "It lands on [], [], [], []." (b) "It makes [] hops." | Two questions in one sentence |
| 13 | G1 | "The boxes on each line are equal jumps. ... write how big each jump is." | "Complete each line. The jumps are equal." + "Each jump is []" in each line | Plainer; blank has a sentence |
| 14 | G2 and online item 11 | "They hop towards each other, one number at a time, at the same speed." | "...1 number at a time, at the same time." | "Speed" is too abstract |
| 15 | G3, home 5, online item 13 | "Make your own... Fill in two boxes that are not next to each other, so that only one number fits each empty box." | "Make a puzzle. Draw 5 boxes in a row. The jumps are equal. Write numbers in 2 boxes that are not next to each other. Leave 3 boxes empty. Give it to a grown-up." | Equal jumps were never stated (puzzle was ambiguous); one job per sentence |
| 16 | Online item 13 step | "...are not next to each other, and still make one jump." | "...are not next to each other." | Muddled |
| 17 | E3 | "Write where it lands." | "Where does it land?" | Natural question |
| 18 | Talk, sneak puzzle 2 | "Ravi says fourteen and forty are the same... Do you agree?" / "Write 30 or 40, and say why." | "Are fourteen and forty the same number? Circle Yes or No. I know because ___." / "Circle 30 or 40. I know because ___." | Do not state a wrong idea in the stem; sentence frame |
| 19 | Home 1-4 | "Write the missing numbers"; "Which two tens...?"; "Count the hops to show how you know." | "Fill in the missing numbers"; "Fill in the blanks: 83 is between ___ and ___."; "Is 56 nearer to 50 or to 60? Circle your answer. Show how you know." | Fixed commands, no method |
| 20 | Everywhere | bigger / biggest | greater / greatest ("the greater ten", "Which is greater, thirteen or thirty?") | Rule 13 |
| 21 | Script | "the round-cornered ones" (ones cards) and "the round ones" (tens cards) | "the square ones" | The kit page has square ones cards and round tens cards; the two words were confusable |
| 22 | Script, choice slide | "Question 5: copy the number word", "Siti made a mistake. Find it." | matching new wording; "Always, sometimes or never?" -> "A pattern to find" | Tutor lines match the page |
| 23 | Workbook | page lines | G1 and E boxes; page fills 88, 95, 92, 86, 89% | Page count unchanged (5 + 2 kit pages) |

## Not fixed / for the owner
- Rule 25 mismatches (left as they are, not changed): "nearer ten" (S-level sneak-peek, T1, home 4, online items 7, 8, 10) is rounding, which is above P1 and not tested in school papers; "halfway" (T3, Investigation); numbers up to 100 in start questions; "between two tens" (S7, E2) is not school-paper wording but is a lesson idea.
- Validator copy check blocks wording quoted in docs/books/school_paper_wording_patterns.md, so some frames differ slightly from the doc's suggestions.
- Home sheet template prints `[]` literally, so the home items use `___` for blanks; the workbook prints boxes. Template-level: tools/b_print.py home renderer.
