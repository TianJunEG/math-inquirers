// P5 open investigations (one per lesson). Model answers were checked by brute force in Python (docs/audit/close_gaps_p5.md).
// `first` is a low-floor first step printed above part (a) on the Investigation page that every child gets.
module.exports = {
 "1": {
  "title": "What if we change the target?",
  "first": "Easy first step: use the cards 0, 1, 2, 4, 5, 7, 8 for just ONE target, 4 000 000. Write one number from just below it and one from just above it. Which is closer? Then do part (a).",
  "parts": [
   "Use the digit cards 0, 1, 2, 4, 5, 7, 8, each once, to make the 7-digit number closest to a TARGET. Find the closest number for the targets 3 000 000, 4 000 000, 5 000 000 and 6 000 000.",
   "For each target, does the winner come from just BELOW the target or just ABOVE it? What do you notice? Try 7 000 000 and 8 000 000 to test your idea.",
   "What stays the same in every case? Write a rule that tells someone which side wins."
  ],
  "a": "Closest: 3 000 000 gives 2 875 410 (below, 124 590 away); 4 000 000 gives 4 012 578 (above, 12 578); 5 000 000 gives 5 012 478 (above, 12 478); 6 000 000 gives 5 874 210 (below, 125 790); 7 000 000 gives 7 012 458 (above); 8 000 000 gives 8 012 457 (above). Rule: when the leading digit of the target (4, 5, 7, 8) is one of the cards, start with it and make the rest as small as possible, so the winner is just above. When the card is missing (3 and 6) the winner has to come from below, and the number just below starts with the next smaller card and is as big as possible. Look for: both sides tested every time, gaps compared by subtracting, a rule in words."
 },
 "2": {
  "title": "Is it always true? Test and explain",
  "first": "Easy first step: cut a bar into 6 equal parts. 1/2 is ___ parts and 1/3 is ___ parts, so 1/2 − 1/3 = ___/6. Now try part (a).",
  "parts": [
   "Take two unit fractions that are next to each other, such as 1/3 and 1/4. Take the smaller away from the bigger: 1/3 − 1/4 = ______. Try at least four more pairs (1/4 and 1/5, 1/5 and 1/6, 1/9 and 1/10, 1/20 and 1/21).",
   "What do you notice about the answer each time? Write your idea in words. Is it always true? Explain with a drawing (hint: cut a bar into 3 × 4 = 12 equal parts).",
   "Use your idea to write 1/6 + 1/12 + 1/20 as one fraction without finding a common denominator."
  ],
  "a": "Each answer is a unit fraction whose bottom number is the two bottom numbers multiplied: 1/3 − 1/4 = 1/12 (3 × 4), 1/4 − 1/5 = 1/20, 1/5 − 1/6 = 1/30, 1/9 − 1/10 = 1/90, 1/20 − 1/21 = 1/420. It is always true for neighbouring unit fractions (checked for every pair from 1/1 and 1/2 up to 1/1999 and 1/2000): cut a bar into n × (n + 1) parts; 1/n is (n + 1) parts and 1/(n + 1) is n parts, so the difference is 1 part. Part 3: 1/6 = 1/2 − 1/3, 1/12 = 1/3 − 1/4, 1/20 = 1/4 − 1/5, so the sum is 1/2 − 1/5 = 3/10 (check: 10/60 + 5/60 + 3/60 = 18/60 = 3/10). Accept any clear picture or well-chosen examples; watch for \"it works for my five pairs so always\" and ask for the reason."
 },
 "3": {
  "title": "What if we change the total?",
  "first": "Easy first step: the total is 48 + 12 = 60. Draw one bar for 60 and cut it into 3 equal parts. How many stickers is one part? Then do part (a).",
  "parts": [
   "Ali has 48 stickers and Mei has 12. Ali gives Mei some stickers. Afterwards Ali has exactly twice as many as Mei. How many does Ali give? Draw the After bars.",
   "What if the total is different? Try the totals 45, 50, 30 and 60 in any way you like (Ali has more than Mei to start). For which totals can Ali end up with exactly TWICE as many as Mei, with whole stickers? For which can it NOT be done?",
   "What stays the same? Write a rule that tells you which totals work, and explain with a bar."
  ],
  "a": "Part 1: total 60, After is 3 units (Ali 2 units, Mei 1 unit), 1 unit = 20, so Ali ends with 40 and Mei 20: Ali gives 8. Part 2: totals 45 (Ali 30, Mei 15), 30 (Ali 20, Mei 10) and 60 work; 50 does not (50 ÷ 3 is not a whole number). Rule: the total never changes when one child gives to the other, and the After has 3 equal units, so the total must be a multiple of 3 (checked for every total from 1 to 100). The amount given then depends on the start: it is (Ali's start) − 2/3 of the total. Look for: the total drawn as one bar split in 3, the \"multiple of 3\" idea, and children testing a total like 50 and explaining why it fails."
 },
 "4": {
  "title": "Find all the ways",
  "first": "Easy first step: draw a right-angled triangle on squared paper with short sides 3 cm and 4 cm. What is its area? Then look for others with area 6 cm².",
  "parts": [
   "On square grid paper (1 square = 1 cm), draw right-angled triangles whose two short sides are along the grid lines and are whole numbers of cm, and whose area is exactly 6 cm². Find ALL of them (a triangle turned round is the same triangle). How do you know you have them all?",
   "Now keep the base 4 cm along the bottom. Mark where the top corner can go so that the area is still 6 cm². What do you notice about all the possible top corners?",
   "What if the area is 10 cm²? 12 cm²? How many right-angled triangles can you find each time? Which area gave the most?"
  ],
  "a": "Part 1: three triangles, with short sides 1 and 12, 2 and 6, 3 and 4 (the two short sides multiply to 12, which is double the area; checked by listing every pair). Part 2: base 4 means height 3 cm, so the top corner can be anywhere on a straight line 3 cm above and parallel to the base (same base, same height, same area), not just above the end of the base. Part 3: 10 cm² gives 3 (1 and 20, 2 and 10, 4 and 5); 12 cm² gives 4 (1 and 24, 2 and 12, 3 and 8, 4 and 6); 12 gave the most because 24 has the most factor pairs. Look for: a systematic list, the doubling idea, and the parallel-line observation."
 },
 "5": {
  "title": "Find all the ways",
  "first": "Easy first step: list every box that holds exactly 12 cubes (for example 1 × 1 × 12). Then do part (a).",
  "parts": [
   "A shop wants a box that holds exactly 48 small cubes of sugar, packed with no gaps. The box is a cuboid with whole-number edges in cubes. Find ALL the different boxes (a 2 by 4 by 6 box is the same as a 6 by 4 by 2 box). Make a list in order.",
   "Which box would you choose to sell, and why? Which is most like a cube?",
   "What if the shop packs 64 cubes? How many different boxes now? Is there a number of cubes that gives only ONE box shape?"
  ],
  "a": "Part 1: nine boxes: 1×1×48, 1×2×24, 1×3×16, 1×4×12, 1×6×8, 2×2×12, 2×3×8, 2×4×6, 3×4×4 (brute-forced over every possible edge). Part 2: open; 3×4×4 is closest to a cube. Part 3: 64 cubes gives seven boxes (1×1×64, 1×2×32, 1×4×16, 1×8×8, 2×2×16, 2×4×8, 4×4×4); 64 has a cube-shaped box (4×4×4) but several others too. A prime number of cubes (2, 3, 5, 7, 11 …) gives exactly ONE box, 1×1×n, and so does 1 cube. Look for: ordered list by smallest edge, factor pairs, and the reason a prime gives one box."
 },
 "6": {
  "title": "Find all the ways",
  "first": "Easy first step: tap A runs for 6 minutes. How many litres go in? How many litres are still needed, and how many minutes of tap B give that? Then do part (a).",
  "parts": [
   "Tap A puts 2 litres a minute into an empty tank. Tap B puts 3 litres a minute. The taps are used ONE AT A TIME, each for a whole number of minutes (0 is allowed). Find ALL the ways to put exactly 24 litres into the tank. Make a table.",
   "Which way takes the shortest total time? Why does the faster tap win?",
   "What if the tank needs 25 litres? How many ways now? What changes and what stays the same?"
  ],
  "a": "Part 1: five ways (minutes on tap A, minutes on tap B): (12, 0), (9, 2), (6, 4), (3, 6), (0, 8). Each time B is on 2 minutes more, A must be on 3 minutes fewer (6 litres swapped). Part 2: B only, 8 minutes (total times are 12, 11, 10, 9, 8): B puts in 3 litres a minute, more than A, so less time. Part 3: 25 litres gives four ways: (11, 1), (8, 3), (5, 5), (2, 7); shortest is 9 minutes (2 and 7). The swap rule (3 minutes of A for 2 minutes of B, always 6 litres) stays the same. The number of ways changes because 25 is odd, so tap B must be on an odd number of minutes (1, 3, 5 or 7); this was checked by listing all pairs. Look for: an ordered table and noticing the pattern in the table."
 },
 "7": {
  "title": "Is it always true? Test and explain",
  "first": "Easy first step: on a $100 bag take 20% off (that is $20) and write the new price. Then take 10% off that new price. Then do part (a) the other way round.",
  "parts": [
   "A $100 bag is on sale. Shop 1 takes 20% off and then a further 10% off the new price. Shop 2 takes 10% off first and then a further 20% off the new price. Work out both prices. Is one cheaper?",
   "Test two more pairs of discounts of your own (for example 50% and 10%, or 30% and 20%). Does the ORDER of two discounts ever change the final price? Is it always true?",
   "Is 20% off then 10% off the same as 30% off? Test and explain. (Hint: after 20% off, you pay 4/5. After 10% off, you pay 9/10.)"
  ],
  "a": "Part 1: both $72 (100 → 80 → 72 and 100 → 90 → 72). Part 2: the order never matters; checked by computer for every pair of whole-number percentages from 1% to 99%. Reason: after 20% off you pay 4/5 of the price and after 10% off you pay 9/10, and 4/5 of 9/10 is the same as 9/10 of 4/5, so the order makes no difference. Part 3: not the same: 20% then 10% is $72, but 30% off is $70. The second discount is taken from a smaller price, so it takes off less than 10% of $100. Look for: at least two extra tests, the fraction reason (or \"the same two parts of the price are kept\"), and the \"percentage of WHAT\" idea."
 },
 "8": {
  "title": "Find all the ways",
  "first": "Easy first step: start with a base angle of 10°. The other base angle is also 10°. What is the top angle? Write it as three angles. Then try 20°.",
  "parts": [
   "An isosceles triangle has all three angles equal to a whole number of TENS of degrees (10°, 20°, 30° and so on). Find ALL the possible triangles. Write each as three angles.",
   "How many of your triangles have an angle bigger than 90°? Which one is equilateral?",
   "What if the angles are multiples of 15° instead? How many triangles now? What stays the same in your method?"
  ],
  "a": "Part 1: eight triangles, written (top, base, base): 160, 10, 10; 140, 20, 20; 120, 30, 30; 100, 40, 40; 80, 50, 50; 60, 60, 60; 40, 70, 70; 20, 80, 80 (every base angle from 10° to 80°; 90° base angles leave 0° at the top, so no triangle). Part 2: four have an angle over 90° (160, 140, 120 and 100); the equilateral one is 60, 60, 60. Part 3: multiples of 15° give five: 150, 15, 15; 120, 30, 30; 90, 45, 45; 60, 60, 60; 30, 75, 75. Method that stays the same: choose a base angle, then top = 180° − 2 × base. Checked by computer for both sets. Look for: a systematic list by base angle and the reason it must stop at 80° (or 75°)."
 },
 "9": {
  "title": "Is it always true? Test and explain",
  "first": "Easy first step: fill in the first three totals: 1 = 1, 1 + 3 = 4, 1 + 3 + 5 = ___. Then carry on.",
  "parts": [
   "Add the first odd numbers: 1, then 1 + 3, then 1 + 3 + 5, then 1 + 3 + 5 + 7. Make a table of the first 6 totals. What do you notice?",
   "Is it always true? Use a picture of square dots (add an L-shaped border each time) to explain why.",
   "What if you add the first EVEN numbers instead (2, then 2 + 4, then 2 + 4 + 6 …)? Find a rule in words. Use it to predict the total of the first 20 even numbers, then check it another way."
  ],
  "a": "Part 1: totals 1, 4, 9, 16, 25, 36: the square numbers (1 × 1, 2 × 2, 3 × 3 …). Part 2: always true (checked for the first 3000 odd numbers): each new odd number is an L-shaped border of dots around the square (3 dots round a 1 by 1, 5 dots round 2 by 2, 7 round 3 by 3), which turns an n by n square into an (n + 1) by (n + 1) square. Part 3: first even numbers add to 2, 6, 12, 20, 30, 42: each is the figure number times the next number (n × (n + 1)). First 20: 20 × 21 = 420. Check: twice the sum of 1 to 20 (210), or \"two columns of the 20 by 21 rectangle\". Look for: a table, the L-shape picture, and a rule in words, not just examples."
 },
 "10": {
  "title": "Find the pattern",
  "first": "Easy first step: with 1 step there is 1 way. With 2 steps there are 2 ways (1 + 1, or 2). Draw the ways for 3 steps first.",
  "parts": [
   "Ali climbs a staircase and takes either 1 step or 2 steps at a time. How many different ways can he climb a staircase with 1 step? 2 steps? 3 steps? 4 steps? List every way for 4 steps (for example 1+1+2 and 2+1+1 are different).",
   "Make a table up to 6 steps. What pattern do you see? Explain why it works (hint: think about the LAST jump Ali makes).",
   "Use your pattern to predict the number of ways for 8 steps. What if Ali could also take 3 steps? Try 3 and 4 steps again."
  ],
  "a": "Part 1: 1 step: 1 way; 2 steps: 2 ways (1+1, 2); 3 steps: 3 ways (1+1+1, 1+2, 2+1); 4 steps: 5 ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2). Part 2: 1, 2, 3, 5, 8, 13: each is the sum of the two before it. Reason: the last jump is 1 step (so Ali had climbed n − 1 steps before) or 2 steps (n − 2 steps before), so the ways for n steps = ways for n − 1 + ways for n − 2. Part 3: 8 steps gives 34 ways (1, 2, 3, 5, 8, 13, 21, 34; checked by brute force). With 3-steps allowed: 3 steps has 4 ways and 4 steps has 7 (each is the sum of the three before). Look for: a complete, ordered list, the table, and the last-jump reasoning."
 }
};
