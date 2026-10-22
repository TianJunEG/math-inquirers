# Level 3 (P3) mathematician stories - final set

Lessons 3, 4, 5 (Napier, Bhaskara II, Sun Zi) are copied unchanged from p3.json. Lessons 1, 2, 6-10 are new. Countries: UK x2 (Scotland, England), China x2, USA x2, India, Iraq/Egypt, Hungary, Morocco. Women: Peter, Clarke, Uhlenbeck.

| L | Topic | Person | Years | Country | Conf. |
|---|---|---|---|---|---|
| 1 | Numbers to 10 000 | Rozsa Peter | 1905 to 1977 | Hungary (Budapest) | high |
| 2 | Addition and subtraction | Joan Clarke | 1917 to 1996 | England (London, Cambridge, Bletchley Park) | high |
| 3 | Times tables 6-9 | John Napier | 1550 to 1617 | Scotland | high |
| 4 | Word problems, bar models | Bhaskara II | 1114 to 1185 | India | medium |
| 5 | Division | Sun Zi | lived more than 1,500 years ago (exact dates unknown) | China | medium |
| 6 | Fractions | Abu Bakr al-Hassar | 12th century (exact dates unknown) | Morocco / the Islamic West (sources differ between the Maghreb and Spain) | medium |
| 7 | Area and perimeter | Karen Uhlenbeck | born 1942 | USA (born in Cleveland, Ohio) | high |
| 8 | Angles, perpendicular and parallel | Ibn al-Haytham | about 965 to about 1040 | Born probably in Basra (now Iraq); worked mostly in Cairo, Egypt | medium |
| 9 | Length, mass, volume, money, time | Zu Chongzhi | 429 to about 500 (sources differ) | China (born in Jiankang, now Nanjing) | medium |
| 10 | Challenge Day: bar graphs, logic | Raymond Smullyan | 1919 to 2017 | USA (born in Far Rockaway, New York) | high |

## Lesson 1: Rozsa Peter (Numbers to 10 000)

Rózsa Péter was born in Budapest, in Hungary, in 1905. At university she began with chemistry, but she changed to mathematics. She became one of the people who started the study of recursion. In simple words, a recursive rule builds each new number from the number before it, so a pattern can keep going as far as you like. Later she taught at a university in Budapest. She also wrote a book for ordinary readers, called Playing with Infinity, and she said she loved maths mainly because it is beautiful. In 1973 she became the first woman elected to the Hungarian Academy of Sciences.

- Link: Today you continue number patterns, and a rule that makes each number from the one before is the idea of recursion that she studied.
- Try it: Start at 5. The rule is: double the number, then add 1. Write the next four numbers. Can you predict the one after that?
- Answer (checked in Python): 11, 23, 47, 95 (5 x 2 + 1 = 11, 11 x 2 + 1 = 23, 23 x 2 + 1 = 47, 47 x 2 + 1 = 95). The next one is 95 x 2 + 1 = 191.
- Legend / caution note: none
- Icon: A staircase of growing number tiles, each step made from the one below; not a portrait.
- Sources: https://mathshistory.st-andrews.ac.uk/Biographies/Peter.html; https://www.encyclopedia.com/computing/news-wires-white-papers-and-books/peter-rozsa; https://richardzach.org/?p=2783

## Lesson 2: Joan Clarke (Addition and subtraction)

Joan Clarke was born in London in 1917. She won a scholarship to Newnham College, Cambridge, to study mathematics, and she earned a double first, the top marks. At that time Cambridge did not give women full degrees, so hers was not officially awarded until 1948. In 1940 she joined the codebreakers at Bletchley Park. She worked in Hut 8, on secret messages sent by the German navy. She became skilled at a method that used careful counting and chance to cut down how many possibilities had to be tested. She was the only woman in the team that used it, and later became deputy head of Hut 8. After the war she studied old Scottish coins and won a medal for it.

- Link: Today you crack letter puzzles by trying possibilities and working out what must be true, and codebreakers also cut down possibilities to find the secret.
- Try it: Each letter is a different digit. A + A + A = BA, and B is not 0. Which digits are A and B? Check by adding.
- Answer (checked in Python): A = 5 and B = 1, because 5 + 5 + 5 = 15 and 15 reads B A (1 then 5). No other pair of different digits works.
- Legend / caution note: Sources differ slightly on the year she became deputy head and on her honours, so the story gives no years for those. Letter puzzles are our link; the sources do not say she did school-style puzzles.
- Icon: A hut-shaped door with a keyhole and a few coded letters; not a portrait.
- Sources: https://www.gchq.gov.uk/information/joan-clarke; https://www.english-heritage.org.uk/visit/blue-plaques/joan-clarke/; https://en.wikipedia.org/wiki/Joan_Clarke; https://mathshistory.st-andrews.ac.uk/Biographies/Clarke_Joan/

## Lesson 3: John Napier (Times tables 6-9)

John Napier lived in Scotland, near Edinburgh. He looked after his family's farms, and maths was his hobby. He invented a set of rods with multiplication tables written on them. People call them Napier's bones. To multiply a big number, you place the rods side by side, read the rows, and add. His book about the rods came out in 1617. With the rods, you only need to add.

- Link: Napier's rods are made of times tables, so they turn multiplication into reading a table and adding, just like the tables of 6, 7, 8 and 9 we explore today.
- Try it: Make a rod for 9. Write 9 x 1 up to 9 x 9. What pattern do you see in the tens digits and in the ones digits?
- Answer (checked in Python): 09, 18, 27, 36, 45, 54, 63, 72, 81. The tens digits go up by 1 each time (0 to 8) and the ones digits go down by 1 (9 to 1). Each pair of digits adds to 9.
- Legend / caution note: none
- Icon: A set of tall thin rods, each with a small times-table grid and diagonal lines.
- Sources: https://mathshistory.st-andrews.ac.uk/Biographies/Napier/; https://mathshistory.st-andrews.ac.uk/Extras/Napier_rods/; https://library.si.edu/digital-library/book/rabdologiaseunu00napi

## Lesson 4: Bhaskara II (Word problems, bar models)

Bhaskara lived in India about 900 years ago. He wrote a maths book called the Lilavati. It has many word problems, with kings, elephants and pearl necklaces in them. A story often told says the book was named after his daughter. Historians have no proof that this story is true, so it is a legend. What we do know is that Bhaskara thought maths problems could be told as little tales, and that is a good way to learn.

- Link: Today we solve word problems by drawing a bar model, and Bhaskara's book is full of stories that ask us to find an unknown number.
- Try it: In the style of Bhaskara: a necklace has some pearls. Half of them fall on the floor, a quarter fall on the bed and 5 stay on the string. How many pearls were there? Draw a bar model.
- Answer (checked in Python): 20 pearls. Half and a quarter make three quarters, so the 5 left is one quarter. One quarter is 5, so the whole is 4 x 5 = 20. Check: 10 + 5 + 5 = 20.
- Legend / caution note: A story often told says the Lilavati was named after Bhaskara's daughter (historians have no proof; it is a legend). The necklace problem in try_it is our own, written in the style of the book, not a copy of his.
- Icon: A string of pearls with one pearl rolling away, and a small speech bubble.
- Sources: https://britannica.com/print/article/64067; https://en.wikipedia.org/wiki/L%C4%ABl%C4%81vat%C4%AB; https://old.maa.org/node/116870

## Lesson 5: Sun Zi (Division)

Almost nothing is known about the life of Sun Zi. We know the name of a Chinese maths book, the Sunzi Suanjing. Historians are not sure exactly when it was written, but it is more than 1,500 years old. It has a riddle about remainders: find a number that leaves 2 when we share it into groups of 3, leaves 3 in groups of 5, and leaves 2 in groups of 7. The answer is 23. The book also shows a method for riddles like this.

- Link: Today's "what number am I?" riddles use division with remainders, just like Sun Zi's riddle.
- Try it: Check the answer 23 for Sun Zi's riddle by dividing. Then find a number between 10 and 20 that leaves 1 when divided by 4 and leaves 2 when divided by 3.
- Answer (checked in Python): 23 / 3 = 7 r 2, 23 / 5 = 4 r 3, 23 / 7 = 3 r 2, so 23 works. The second riddle: 17 (17 / 4 = 4 r 1 and 17 / 3 = 5 r 2). Of 13 and 17, only 17 fits.
- Legend / caution note: Dates and author of the Sunzi Suanjing are uncertain; the story says so.
- Icon: A bundle of counting sticks tied in groups, with a few sticks left over.
- Sources: https://mathshistory.st-andrews.ac.uk/Biographies/Sun_Zi/; https://en.wikipedia.org/wiki/Chinese_remainder_theorem

## Lesson 6: Abu Bakr al-Hassar (Fractions)

Al-Hassar lived about 900 years ago, in the 12th century. Very little is known about his life, and his exact dates are not certain. Most sources say he came from Morocco. He wrote maths books about calculating. One is lost, and only part of another survives. In his chapter on fractions, he told readers to write the bottom number under a straight line and the top number above it. This is described as the first known use of the fraction bar. A little later, in 1202, Fibonacci used the same bar in his famous book.

- Link: Today you read and compare fractions, and the bar between the top and bottom numbers is the one al-Hassar described.
- Try it: Write two thirds and three quarters with a fraction bar. Use a fraction wall, or twelfths, to decide which one is bigger.
- Answer (checked in Python): 2/3 = 8/12 and 3/4 = 9/12, so 3/4 is bigger.
- Legend / caution note: His dates and place are uncertain, and the story says so. The claim that Fibonacci's use of the bar came after al-Hassar is stated by MAA and Muslim Heritage. The sources do not say whether Fibonacci learned the bar from al-Hassar.
- Icon: A palm-leaf style page with one neat fraction bar and a wall of equal bricks; not a portrait.
- Sources: https://www.maa.org/book/export/html/117587; https://muslimheritage.com/people/scholars/abu-bakr-al-hassar/; https://en.wikipedia.org/wiki/Abu_Bakr_al-Hassar

## Lesson 7: Karen Uhlenbeck (Area and perimeter)

Karen Uhlenbeck was born in Cleveland, in the USA, in 1942. As a child she read a great deal, especially about science. At university she began with physics but changed to mathematics. Think of a wire loop dipped in soapy water. The soap film pulls itself into the shape with the smallest area that fits the wire. Mathematicians call such shapes minimal surfaces. Uhlenbeck worked on them with another mathematician, Jonathan Sacks, and found new ways to study when and how they exist. In 2019 she became the first woman to win the Abel Prize, one of the top prizes in maths.

- Link: Today you find area and perimeter, and she studied shapes that use the smallest area for the edge that holds them.
- Try it: Two wire frames have the same perimeter, 20 cm: a rectangle 6 cm by 4 cm, and a square 5 cm by 5 cm. Which soap film has the larger area?
- Answer (checked in Python): Rectangle: 6 x 4 = 24 square cm. Square: 5 x 5 = 25 square cm. Both have perimeter 20 cm, and the square has the larger area, by 1 square cm.
- Legend / caution note: The story uses the soap film only as a picture of 'least area'; the sources say a soap film settles into a minimal surface.
- Icon: A wire loop holding a rainbow soap film; not a portrait.
- Sources: https://mathshistory.st-andrews.ac.uk/Biographies/Uhlenbeck_Karen.html; https://abelprize.no/sites/default/files/2021-04/I%27m%20Forever%20Blowing%20Bubbles.pdf; https://plus.maths.org/abel-prize-2019; https://en.wikipedia.org/wiki/Karen_Uhlenbeck

## Lesson 8: Ibn al-Haytham (Angles, perpendicular and parallel)

Ibn al-Haytham was born about 1,000 years ago, probably in Basra, in what is now Iraq. He spent much of his working life in Cairo, in Egypt. He wrote the Book of Optics, in seven volumes, about light and sight. He argued that we see when light from an object enters our eyes. He did not only argue, he also tested his ideas with experiments. He studied how light bounces off flat and curved mirrors, and used geometry to work out where the light goes. A story says he pretended to be mad to stay safe from a powerful ruler and was kept at home for years. Historians are not sure that is true.

- Link: Today you look for angles and perpendicular lines, and light bouncing off a mirror makes equal angles on either side of the perpendicular.
- Try it: A ray of light hits a flat mirror and makes an angle of 30 degrees with the mirror. The perpendicular to the mirror makes 90 degrees with it. What angle does the ray make with the perpendicular? The reflected ray leaves at the same angle on the other side of the perpendicular. How big is the angle between the two rays?
- Answer (checked in Python): 90 - 30 = 60 degrees with the perpendicular. The reflected ray also makes 60 degrees, so the angle between the two rays is 60 + 60 = 120 degrees.
- Legend / caution note: The house-arrest story is a legend (MacTutor says it 'appears' true; Wikipedia calls it a legend). Birth place and death place are uncertain, and sources give 1039 or 1040. The equal-angles rule is the modern law of reflection and is not claimed as his own words.
- Icon: A hand mirror with a beam of light bouncing off it and a small right-angle mark; not a portrait.
- Sources: https://mathshistory.st-andrews.ac.uk/Biographies/Al-Haytham/; https://en.wikipedia.org/wiki/Ibn_al-Haytham; https://www.encyclopedia.com/doc/1G2-2830905785.html; https://sciencenotes.org/law-of-reflection/

## Lesson 9: Zu Chongzhi (Length, mass, volume, money, time)

Zu Chongzhi lived in China about 1,500 years ago. His family were court astronomers who kept the calendar, and his father taught him mathematics and astronomy. Zu made a new calendar in the 460s. He measured the year as 365.24281 days. That is within about a minute of the length astronomers find today. He also showed that pi lies between 3.1415926 and 3.1415927, and he wrote a maths book with his son. Sadly that book is lost, so we do not know how he did his sums. Historians still are not sure of his exact dates.

- Link: Today you work with units of time, and Zu measured the year in days, hours and parts of a day.
- Try it: Zu's year was about 365 and a quarter days. How many hours is a quarter of a day? How many days are there in 4 years of that length?
- Answer (checked in Python): A quarter of a day is 24 / 4 = 6 hours. In 4 years: 4 x 365 = 1460 days, plus 4 quarters = 1 day, so 1461 days.
- Legend / caution note: Wikipedia and MacTutor disagree on his dates and on the polygon he used, so the story gives neither polygon nor an exact death year. The 'within about a minute' comparison is our own check: 365.24281481 - 365.24219878 days is about 53 seconds, and MacTutor says about 50 seconds. Only MacTutor says the calendar was never put into use, so the story leaves it out.
- Icon: A round sun-and-moon calendar wheel with a small ruler; not a portrait.
- Sources: https://mathshistory.st-andrews.ac.uk/Biographies/Zu_Chongzhi/; https://en.wikipedia.org/wiki/Zu_Chongzhi

## Lesson 10: Raymond Smullyan (Challenge Day: bar graphs, logic)

Raymond Smullyan was born in New York in 1919. He was a mathematician, a logician, a magician and a pianist. He studied mathematics and logic on his own, and in 1959 he earned a doctorate at Princeton. He loved puzzles, and wrote many puzzle books, such as What Is the Name of This Book?, in 1978. In his famous puzzles, a knight always tells the truth and a knave always lies. You must use the clues to work out who is who. He also used puzzles to introduce big ideas in logic to readers of all ages.

- Link: Today you solve logic puzzles with ticks and crosses, just like working out who is a knight and who is a knave.
- Try it: Ana says: 'Ben is a knave.' Ben says: 'We are both knights.' A knight always tells the truth and a knave always lies. Who is the knight and who is the knave?
- Answer (checked in Python): Ana is a knight and Ben is a knave. If Ben were a knight, both would be knights, but then Ana's words 'Ben is a knave' would be a lie, which a knight never tells. So Ben is a knave, his words are false, and Ana's words are true, so she is a knight.
- Legend / caution note: none
- Icon: Two doors, one with a tick and one with a cross, and a small top hat; not a portrait.
- Sources: https://en.wikipedia.org/wiki/Raymond_Smullyan; https://mathshistory.st-andrews.ac.uk/Obituaries/Smullyan_NYTimes/; https://blog.computationalcomplexity.org/2017/02/raymond-smullyan-was-born-on-may-25.html

## Claims I could not confirm (left out or hedged)

- Rozsa Peter: MacTutor says she turned to poetry after finding her number theory results already proved; only one source, so left out. First publication year of Playing with Infinity differs by source (written 1943, published 1945 per one source), so no year is given. Her death date differs by a day between sources (16 vs 17 February 1977); only years are given.
- Joan Clarke: deputy head date (September 1944, or early 1944) and honours year (MBE 1946 vs 1947; medal 1986 vs 1987) differ between sources, so no years are given. The engagement to Alan Turing was left out as unsuitable detail.
- al-Hassar: no exact dates; place is Morocco in Wikipedia and Muslim Heritage but MAA says Maghreb or Andalus. Whether Fibonacci took the bar from him is not stated. Only MAA calls it the first known use of the fraction bar; Muslim Heritage says he developed the notation; Wikipedia (as fetched) does not mention the bar.
- Karen Uhlenbeck: Wikipedia and MacTutor do not mention soap films; the soap-film picture comes from the Abel Prize explainer and Plus Magazine. Her exact contribution is described only in simple terms.
- Ibn al-Haytham: birth in Basra and death in Cairo are 'possibly' in MacTutor; death year 1039 or 1040. Wikipedia credits him with the first complete statement of the law of reflection, but the sources do not give the 'equal angles' wording as his; the try-it uses the modern law (sciencenotes.org). Claims that he founded modern physics are debated, so not used. House arrest is told as a legend.
- Zu Chongzhi: Wikipedia gives lifespan 491-780 in its infobox (clearly wrong) and MacTutor 429-501, so the story says 429 to about 500. Polygon used for pi differs (12,288 or 24,576 sides) so is left out. Only MacTutor says his calendar was never introduced. The link to this lesson is about measuring time; length units (chang) were left out.
- Raymond Smullyan: the NYT obituary (via MacTutor) does not mention knights and knaves; those come from Wikipedia and the computational complexity blog.

## Rejected choices

- Maria Montessori (fractions): could not confirm from opened pages that she designed the fraction insets, so rejected; reservation released.
- Georges Cuisenaire (fractions): a teacher, not a mathematician, and sources give conflicting dates for the rods (1931 or 1945); not used.
- Hypatia (place value): could not confirm any place-value link, and her story ends darkly; not used.
- Gerbert of Aurillac (numbers/abacus): good link, but sources disagree on his numeral knowledge and the story involves a pope with legends; replaced by Peter so the level has a third woman. Reservation released.
- Henry Dudeney (cryptarithms): good link, but would make a third UK person; Clarke chosen for a woman.
