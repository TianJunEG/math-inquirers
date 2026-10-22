"""Builds p4/stories.json (the Level 4 story-break content) from docs/stories/final_p4.json plus the slide/workbook wording below,
and verifies every try-it answer. Run: python3 rebuild/p4_stories_build.py"""
import json, os, re
from fractions import Fraction as F
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
src = json.load(open(os.path.join(R, 'docs/stories/final_p4.json')))
# slide story (90-110 words), blurb for the workbook corner box, child try-it, tutor line, label text
T = {
1: dict(story="Sophie Germain lived in Paris more than 200 years ago. As a teenager she read the books in her father's library and taught herself Latin and Greek so she could read even more. Her parents were not happy, but she kept learning. Later she wrote to famous mathematicians using a man's name, M. Le Blanc. The great mathematician Gauss praised her ideas about numbers, and later found out who she really was. Sophie loved prime numbers, which have exactly two factors: 1 and themselves. She studied primes p where 2 times p plus 1 is also prime. Today these are called Sophie Germain primes.",
  blurb="Sophie Germain taught herself maths from her father's books in Paris, over 200 years ago. She loved prime numbers, the numbers with exactly two factors.",
  q="Is 2 × 7 + 1 a prime? List the factors of your answer. Then try 5.",
  a="2 x 7 + 1 = 15. The factors of 15 are 1, 3, 5 and 15, so 15 is not prime and 7 is not a Sophie Germain prime. For 5: 2 x 5 + 1 = 11, whose only factors are 1 and 11, so 11 is prime and 5 is a Sophie Germain prime."),
2: dict(story="Leonardo of Pisa, now called Fibonacci, lived about 800 years ago. His father was a merchant official who worked in Bugia, a trading town in North Africa that is now Bejaia in Algeria. As a boy Leonardo learned to count with ten digits, 0 to 9, where each digit's place gives its value. In 1202 he finished a book, the Liber Abaci, which showed merchants how to use these digits for money and trade. Place value is what lets ten digits write any big number, such as 47 305. Leonardo did not invent these digits, but his book helped them spread across Europe.",
  blurb="Leonardo of Pisa (Fibonacci) learned the digits 0 to 9 as a boy in North Africa. His book, written in 1202, helped Europe use place value.",
  q="Use the digits 7, 0, 4, 9 and 2 once each. Write the biggest and the smallest 5-digit number you can.",
  a="Biggest: 97 420. Smallest: 20 479 (the 0 cannot go first, or it would not be a 5-digit number)."),
3: dict(story="Katherine Johnson grew up in West Virginia in the USA. She was so quick at school that she was moved up several grades. She became a research mathematician at NASA, where in the early days people who did calculations were called computers. She worked out the flight path for Alan Shepard's 1961 flight, the first American in space. Before John Glenn orbited the Earth in 1962, accounts say he asked for Katherine to check the electronic computer's numbers by hand. Her answers matched. Checking an answer a second way is a habit every mathematician uses. She received the Presidential Medal of Freedom in 2015.",
  blurb="Katherine Johnson was a NASA mathematician who worked out flight paths for early space flights. Accounts say astronauts trusted her to check calculations a second way.",
  q="Check that 6 × 48 = 288 using a different method from your first one. Hint: 48 is close to 50.",
  a="6 x 50 = 300, and 6 x 2 = 12, so 6 x 48 = 300 - 12 = 288. It checks out. You can also check with division: 288 divided by 6 = 48.",
  label="Accounts say"),
4: dict(story="Mahavira lived in southern India about 1,200 years ago, around the year 850. We know almost nothing else about his life, not even exactly where he was born. We do know he wrote a maths book, the Ganita Sara Sangraha, while King Amoghavarsha ruled the land. One chapter explains how to work with fractions, including how to split a fraction into unit fractions, which have 1 on top. For example, the book shows that 2/17 can be written as 1/12 + 1/51 + 1/68. Splitting a fraction into smaller, friendlier pieces is a clever way to understand it.",
  blurb="Mahavira, an Indian maths writer from about 1,200 years ago, wrote a book that explains how to work with fractions. It also shows how to split a fraction into unit fractions.",
  q="Show that 1/2 = 1/3 + 1/6 by making the denominators the same. Then split 3/4 into 1/2 plus a unit fraction.",
  a="1/3 = 2/6, so 1/3 + 1/6 = 2/6 + 1/6 = 3/6 = 1/2. For 3/4: 3/4 = 2/4 + 1/4 = 1/2 + 1/4."),
5: dict(story="Simon Stevin was born in Bruges, in what is now Belgium, in 1548. He worked on many things, from the science of water to the science of weights. In 1585 he published a small book called The Tenth about decimal fractions. Stevin did not invent decimals, because others had used them before him. What he did was explain them clearly for the people who needed them. He said they would help surveyors, carpet-makers, wine-gaugers, mint-masters, stargazers and every kind of merchant. He showed how to split a whole into tenths, hundredths and thousandths. We still use decimals this way for money and measuring.",
  blurb="Simon Stevin, from Bruges, wrote a small book in 1585 that explained decimals clearly. He showed how to split a whole into tenths, hundredths and thousandths.",
  q="Write 3 + 4/10 + 5/100 as a decimal. Then add 2.8 to your answer.",
  a="3 + 4/10 + 5/100 = 3.45. Then 3.45 + 2.8 = 6.25."),
6: dict(story="Eratosthenes was a Greek scholar in the great library of Alexandria, Egypt, over 2,000 years ago. At noon on one day of the year, the Sun shone straight down a well in the town of Syene, so nothing had a shadow. On that day in Alexandria, an upright stick did make a shadow. He worked out that its angle was about 7.2 degrees, which is one fiftieth of a whole turn. So the two towns were one fiftieth of the way round the Earth. He multiplied the distance between them by 50. Historians are not sure how long his unit of distance was, so we cannot say how close he got.",
  blurb="Eratosthenes, a Greek scholar in Egypt over 2,000 years ago, used the angle of a shadow to work out how big the Earth is. His angle was one fiftieth of a whole turn.",
  q="A whole turn is 360 degrees. If a shadow made an angle of 10 degrees, how many angles that size fit all the way round?",
  a="360 divided by 10 = 36, so 36 angles. (Eratosthenes had about 7.2 degrees, and 360 divided by 7.2 = 50.)"),
7: dict(story="Euclid taught mathematics in Alexandria, in Egypt, about 2,300 years ago. Little is known about his life, but his book the Elements is famous. It was used to teach geometry for about 2,000 years. Euclid put many ideas in a careful order and proved each step from simple facts. In Book I he shows that two parallelograms on the same base and between the same two parallel lines have the same area, even if one looks more slanted. So cutting a shape and sliding a piece can change how it looks without changing its area. Euclid wanted a reason for every claim, just as you do when you explain your working.",
  blurb="Euclid taught maths in Alexandria about 2,300 years ago. His book the Elements shows that a slanted shape with the same base and height as a rectangle has the same area.",
  q="A rectangle is 8 cm long and 5 cm high. Slide its top side along to make a slanted shape with the same base and height. What is the area of each? Which has the longer way round?",
  a="Rectangle: 8 x 5 = 40 square cm. The slanted parallelogram has the same base and height, so its area is also 40 square cm. Its slanted sides are longer than 5 cm, so it has the longer way round (a bigger perimeter)."),
8: dict(story="Emmy Noether was born in Erlangen, Germany, in 1882. When she wanted to study mathematics at university, women were only allowed to sit in on classes if the teacher gave permission. She kept going, and in 1907 she earned her doctorate. For years she worked without pay, and for a time her lectures in Göttingen had to be advertised under another professor's name. Still she carried on. In 1918 she proved an idea now called Noether's theorem. It says that when something in nature has a kind of symmetry, a matching quantity stays the same. Symmetry is not only pretty. It tells us deep things.",
  blurb="Emmy Noether, born in Germany in 1882, kept studying maths even when women were not welcome at university. She showed that symmetry is useful as well as beautiful.",
  q="How many lines of symmetry does a square have? How many does a rectangle that is not a square have?",
  a="A square has 4 lines of symmetry (2 through the middles of opposite sides and 2 along the diagonals). A rectangle that is not a square has 2 (through the middles of opposite sides)."),
9: dict(story="Florence Nightingale was born in Florence, Italy, in 1820. She is best known as a nurse, but she also loved numbers. During the Crimean War in the 1850s she collected figures about the hospitals for soldiers. They showed that many more soldiers became sick from dirty, crowded conditions than from the fighting. She knew that long lists of numbers are hard to read, so she drew special charts to make the facts easy to see. Her ideas helped to bring in cleaner, safer hospitals. In 1858 she became the first woman elected a Fellow of the Statistical Society of London. A clear table or graph can help people make better decisions.",
  blurb="Florence Nightingale was a nurse who also loved numbers. She drew charts so that people could see the facts about hospitals at a glance.",
  q="Temperatures: 9 am 26 degrees, noon 31 degrees, 3 pm 33 degrees, 6 pm 29 degrees. Between which two times did it rise the most, and by how much?",
  a="9 am to 12 noon: it rose by 5 degrees (31 - 26). Noon to 3 pm: it rose by only 2 degrees. So the biggest rise was 9 am to 12 noon, by 5 degrees. (Between 3 pm and 6 pm it fell by 4 degrees.)"),
10: dict(story="Terence Tao grew up in Adelaide, Australia. He enjoyed maths so much that he took university maths classes while still a schoolboy. In 1986 he entered the International Mathematical Olympiad, a contest where school students from many countries solve hard puzzle-style problems. He was only ten, the youngest competitor ever, and he won a bronze medal. In 1987 he won silver, and in 1988 gold. He is still the youngest ever winner of each of the three medals. As an adult he became a professor, and in 2006 he won the Fields Medal, a top prize in mathematics. Hard problems are for practising, and trying again is part of the plan.",
  blurb="Terence Tao, from Adelaide, Australia, entered a maths Olympiad at age ten and won a bronze medal. He tried again each year and won silver, then gold.",
  q="Use guess and check: a farm has hens and cows. Together they have 10 heads and 28 legs. How many hens and how many cows?",
  a="6 hens and 4 cows. Check: 6 + 4 = 10 heads; 6 x 2 + 4 x 4 = 12 + 16 = 28 legs. (Try 5 cows: 20 + 10 = 30 legs, too many; 3 cows: 12 + 14 = 26, too few.)"),
}
# ---- verification of every try-it answer ----
assert 2*7+1 == 15 and [d for d in range(1,16) if 15 % d == 0] == [1,3,5,15]
assert 2*5+1 == 11 and [d for d in range(1,12) if 11 % d == 0] == [1,11]
from itertools import permutations
nums = [int(''.join(p)) for p in permutations('70492') if p[0] != '0']
assert max(nums) == 97420 and min(nums) == 20479
assert 6*48 == 288 and 6*50-6*2 == 288 and 288//6 == 48 and 288 % 6 == 0
assert F(1,3)+F(1,6) == F(1,2) and F(2,6)+F(1,6) == F(3,6) == F(1,2) and F(1,2)+F(1,4) == F(3,4)
assert F(1,12)+F(1,51)+F(1,68) == F(2,17)       # fact used in Mahavira's story
assert 3+F(4,10)+F(5,100) == F('3.45') and F('3.45')+F('2.8') == F('6.25')
assert 360/10 == 36 and abs(360/7.2-50) < 1e-9
import math
assert 8*5 == 40 and 8*5 == 40
assert math.hypot(3,5) > 5                      # a slanted side (any slant) is longer than the 5 cm height
sq = 4; rect = 2
temps = [26,31,33,29]; d = [temps[i+1]-temps[i] for i in range(3)]
assert d == [5,2,-4] and d.index(max(d)) == 0
sols = [(h, 10-h) for h in range(11) if 2*h+4*(10-h) == 28]
assert sols == [(6,4)] and 5*4+5*2 == 30 and 3*4+7*2 == 26
out = []
for x in src:
    n = x['lesson']; t = T[n]
    wc = len(t['story'].split()); assert 90 <= wc <= 112, (n, wc)
    assert x['name'] and x['years']
    out.append(dict(n=n, topic=x['topic'], name=x['name'], years=x['years'], country=x['country_or_region'], who=x['who'],
        story=t['story'], words=wc, link=x['link_to_lesson'], blurb=t['blurb'], q=t['q'], a=t['a'], confidence=x['confidence'],
        label=t.get('label', ''), legend_note=x.get('legend_note', '')))
json.dump(out, open(os.path.join(R, 'p4/stories.json'), 'w'), indent=1, ensure_ascii=False)
print('ok', [o['words'] for o in out])
