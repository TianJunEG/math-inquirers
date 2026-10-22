"""Fix pass P3: rewrites p3/gifted.json check (sneak-peek puzzles: 1 access + 1 thinking), adds inv.easy and go (Go further what-if
for the explore stage), and the reflection data. Run: python3 -I docs/audit/mkfixpass_p3_gifted.py  (idempotent)."""
import json,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
fn=os.path.join(R,'p3','gifted.json'); g=json.load(open(fn,encoding='utf8'))
def pk(q,a,why,kind): return {'q':q,'a':a,'why':why,'kind':kind}
CH={
1:[pk('Take the digit cards 4, 0 and 9. Make the biggest 3-digit number you can. Move the cards around to try.','940','Biggest digit first, then the next biggest: 9, 4, 0.','access'),
   pk('Now use the cards 4, 0, 9 and 3, each once. What is the smallest ODD 4-digit number? Say how you know.','3049','Odd means the ones digit is 9 or 3. 0 cannot go first. Try 3049 and 4093: 3049 is smaller.','think')],
2:[pk('Find the missing digit A:  2A5 + 134 = 389. Try each digit for A, or add the ones, then the tens, then the hundreds.','A = 5','Tens: A + 3 must make 8, so A = 5. Check: 255 + 134 = 389.','access'),
   pk('Ali had some marbles. He won 1250 more and then had 4000. How many did he have at first? Draw a number line if it helps.','2750','Work backwards: take away what he won. 4000 − 1250 = 2750. Check: 2750 + 1250 = 4000.','think')],
3:[pk('Here is the 7 times table: 7, 14, 21, 28, 35, 42, 49, 56, 63, 70. Which of these numbers are in it: 49, 54, 63?','49 and 63','Look along the table: 49 and 63 are there; 54 is not.','access'),
   pk('You know 6 × 7 = 42. Use it to work out 6 × 14 and 6 × 6. Say how you did it.','84 and 36','14 is double 7, so double 42 = 84. 6 × 6 is one 6 less than 6 × 7: 42 − 6 = 36.','think')],
4:[pk('Ali has 70 stickers and Ben has 30. Draw two bars, or use counters. How many stickers must Ali give Ben so that they have the same number?','20','The difference is 40. Ali gives half of it: 20. Then both have 50.','access'),
   pk('A pen and a book cost $9 together. The book costs $5 more than the pen. How much is the pen?','$2','Take away the extra $5: 9 − 5 = 4. Two equal bars share 4, so the pen is $2 (the book is $7).','think')],
5:[pk('Mei puts 13 sweets in bags of 4. Use counters or draw it. How many full bags can she make? How many sweets are left over?','3 full bags, 1 left over','3 bags of 4 use 12 sweets. 1 sweet is left.','access'),
   pk('Ali says, "6 sweets are left over when I put the sweets in bags of 6." Draw 6 sweets in bags of 6. What is wrong?','6 sweets fill a bag, so 0 are left','A leftover must be fewer than 6, otherwise another bag of 6 can be filled.','think')],
6:[pk('Draw a rectangle. Cut it into 4 equal parts and shade 1 part. What fraction did you shade?','1/4','4 equal parts, 1 shaded: one quarter.','access'),
   pk('Mei says, "1/4 of a pizza is bigger than 1/3 of the same pizza, because 4 is bigger than 3." Is she right? Draw it.','No: 1/3 is bigger','More equal parts means each part is smaller. Quarters are smaller than thirds.','think')],
7:[pk('Draw a rectangle 3 cm long and 2 cm wide on squared paper (or use 6 tiles). What is its area? What is its perimeter?','Area 6 cm², perimeter 10 cm','6 squares cover it. Walk round the edge: 3 + 2 + 3 + 2 = 10.','access'),
   pk('Two different rectangles both have an area of 12 cm². Can they have different perimeters? Show two examples.','Yes, e.g. 26 cm and 16 cm','1 by 12 has perimeter 26 cm; 2 by 6 has 16 cm; 3 by 4 has 14 cm.','think')],
8:[pk('Look at the letters L, H and O. Which letters have a square corner? Which letter has two lines that never meet, however far they go?','L and H have square corners; H has two lines that never meet','L and H have square corners; O has none. The two upright lines of H stay the same distance apart.','access'),
   pk('Draw a rectangle. Draw a straight line from one corner to the opposite corner. You get two triangles. How many right angles does each triangle have? How do you know?','1 right angle each','Only the corner that was not cut is still a right angle. The corners that were cut are split into two smaller angles.','think')],
9:[pk('Which is longer: 1 m or 90 cm? Say how you know.','1 m','1 m is 100 cm, and 100 is more than 90.','access'),
   pk('A film starts at 3:45 p.m. and lasts 1 hour 30 minutes. When does it end? Say how you counted.','5:15 p.m.','3:45 + 1 h = 4:45. 15 minutes more makes 5:00, and 15 more makes 5:15.','think')],
10:[pk('Ali, Ben and Mei stand in a line. Use three name cards (or write A, B, M). How many different orders can you find?','6 orders','ABM, AMB, BAM, BMA, MAB, MBA. Listing by who is first helps to find them all.','access'),
    pk('Now Ben must stand somewhere in front of Mei (not always right in front). Which of your orders are still allowed?','3 orders: ABM, BAM, BMA','Cross out every order where Mei comes before Ben.','think')],
}
CH[8][0]['pic']='L   H   O'
EASY={
1:'Easy first step: with the cards 0, 1, 2, 3, write only the numbers that start with 1. Use the cards to help you.',
2:'Easy first step: try 842 − 248 = 594 for yourself. Then try 953 and 351 (reverse it, then subtract).',
3:'Easy first step: write the 9 times table up to 9 × 6 and add the digits of each answer.',
4:'Easy first step: fill in the first row. In 1 year Mei is 14 and her brother is 6. What is the difference?',
5:'Easy first step: circle the number in the 3 times table in 14, 15, 16. Then try 20, 21, 22.',
6:'Easy first step: make [[3/4]] with one half. How much is left to fill?',
7:'Easy first step: work out the area and perimeter of the 4 by 4 square and of the 5 by 3 rectangle.',
8:'Easy first step: draw the 1-step and 2-step staircases. Count the corners of the 2-step staircase.',
9:'Easy first step: pay 50 cents with ten 5-cent coins. Then swap some of them for 10-cent coins.',
10:'Easy first step: draw 3 dots and join every pair. Count the lines. Then try 4 dots.',
}
GO={
1:'Cards 2, 4, 5, 8 now: how many numbers between 4000 and 6000? Which is closest to 5000?',
2:'With the cards 1 to 9, what is the smallest answer you can make? The biggest?',
3:'Try the 5s and the 9s. How many dots does each table touch? Why?',
4:'Make 3 towers from 30 cubes, each 2 cubes taller than the last. How tall is each? (Then 3 taller.)',
5:'49 counters: which group sizes from 2 to 8 leave 1 over? Why?',
6:'Find 3 DIFFERENT pieces that make exactly [[1/2]]. Is there another way?',
7:'16 squares: make every rectangle. Which has the longest perimeter? The shortest?',
8:'Fold your corner in half again. Smaller or bigger than a right angle? Find two.',
9:'12 friends and $30: how many bottles of punch? Can you spend exactly $30?',
10:'A 120 cm ribbon is cut into 4 pieces, each 10 cm longer than the last. How long is each?',
}
GOANS={
1:'12 numbers: 6 start with 4 and 6 start with 5 (2, 4, 5, 8 each once). Closest to 5000: 4852 (148 away); the nearest above is 5248.',
2:'Smallest 459 (for example 173 + 286); biggest 981 (for example 235 + 746). Every answer has digits adding to 18.',
3:'The 5s touch only 2 dots (5 and 0). The 9s touch all 10 dots, going round the other way, like the 1s, because each 9 times answer is 1 less in the ones place than the one before.',
4:'30 cubes: 8, 10, 12 (3 towers, take away 2 + 4 = 6, share 24 into 3). With 3 taller each time: 7, 10, 13 (30 - 9 = 21, 21 / 3 = 7).',
5:'49 = 48 + 1. Sizes 2, 3, 4, 6 and 8 leave 1 over (48 is in all those tables). Size 5 leaves 4 and size 7 leaves 0 (49 = 7 x 7).',
6:'Only one way with three different pieces: 1/4 + 1/6 + 1/12 (3/12 + 2/12 + 1/12 = 6/12). Other ways repeat a piece, e.g. 1/4 + 1/8 + 1/8.',
7:'16 squares: 1 by 16 (perimeter 34 cm), 2 by 8 (20 cm), 4 by 4 (16 cm). Longest 1 by 16, shortest 4 by 4: the square, the most compact shape.',
8:'Smaller than a right angle: it is half of a right angle, so two of them make one right angle. It appears at the corner of a set square, or when a square is cut along its diagonal.',
9:'12 x 250 ml = 3000 ml = 3 l, so 2 bottles (2 l each) at least. Yes, there are many ways, e.g. 2 punch + 3 cupcakes + 3 balloons ($6 + $16.50 + $7.50), or 2 curry puffs + 2 punch + 2 cupcakes + 2 balloons.',
10:'15 cm, 25 cm, 35 cm and 45 cm (take away 10 + 20 + 30 = 60, 60 cm left, 60 / 4 = 15).',
}
COMMON={'warmcheck':(2,5),'warm1':(5,8),'warm2':(8,10),'explore1':(10,15),'explore2':(15,25),'break':(35,40),'ws1ans':(52,54),'ws2ans':(65,67),
        'stretch':(67,70),'challenge':(67,70),'chdiag':(67,70),'chwalk':(67,70),'talk':(70,80),'exit':(80,86),'reflect':(86,88)}
PL={
1:dict(teach1=(25,27),we1=(27,29),we2=(29,30),try1=(30,31),teach2=(31,34),key=(34,35),teachpat=(40,42),ws1=(42,52),teachrename=(54,55),teachclues=(55,56),tryclues=(56,57),teachsum=(57,58),ws2=(58,65)),
2:dict(teach1=(25,27),try1=(27,28),teach2=(28,30),teach3=(30,33),try2=(33,34),key=(34,35),ws1=(40,52),teachmagic=(54,55),teachpyr=(55,56),teach999=(56,57),teachshape=(57,58),ws2=(58,65)),
3:dict(teach1=(25,27),we1=(27,28),try1=(28,29),teach2=(29,31),we2=(31,32),try2=(32,33),key=(33,35),ws1=(40,52),teachlist=(54,56),teachgrid=(56,57),teachboth=(57,58),ws2=(58,65)),
4:dict(we1=(25,27),try1=(27,28),we2=(28,31),try2=(31,33),key=(33,35),teachunits=(40,41),tryunits=(41,42),ws1=(42,52),teachtd=(54,56),teachgive=(56,57),teachsame=(57,58),ws2=(58,65)),
5:dict(teach1=(25,27),we1=(27,29),try1=(29,30),we2=(30,32),try2=(32,33),key=(33,35),teachback=(40,42),ws1=(42,52),teachlist=(54,56),teachbig=(56,57),teachtable=(57,58),ws2=(58,65)),
6:dict(teach1=(25,26),we1=(26,28),try1=(28,29),we2=(29,31),try2=(31,33),key=(33,35),ws1=(40,52),teachadd=(54,55),tryadd=(55,56),teachpairs=(56,57),teachbetween=(57,58),ws2=(58,65)),
7:dict(teach1=(25,27),try1=(27,28),teach2=(28,30),we2=(30,31),try2=(31,32),teach3=(32,34),key=(34,35),teachsq=(40,41),ws1=(41,52),teachadd=(54,56),ws2=(56,65)),
8:dict(teach1=(25,27),we1=(27,29),try1=(29,30),teach2=(30,31),we2=(31,32),try2=(32,33),teach3=(33,34),key=(34,35),ws1=(40,52),teachgrid=(54,57),ws2=(57,65)),
9:dict(teach1=(25,27),we1=(27,29),try1=(29,30),teach2=(30,32),we2=(32,33),try2=(33,34),key=(34,35),teachbudget=(40,42),ws1=(42,52),teach24=(54,56),teachlist=(56,57),ws2=(57,65)),
10:dict(teach1=(25,26),we1=(26,28),try1=(28,29),we2=(29,31),try2=(31,32),we3=(32,34),key=(34,35),ws1=(40,52),teachlist=(54,56),teachtable=(56,57),teachbetween=(57,58),ws2=(58,65)),
}
REFLECT_DO=['I kept trying','I asked a question','I checked my answer','I tried a new idea']
for k in g:
    n=int(k); g[k]['check']=CH[n]; g[k]['inv']['easy']=EASY[n]; g[k]['go']=GO[n]; g[k]['goans']=GOANS[n]
    g[k]['didwell']=REFLECT_DO
    pl={**COMMON,**PL[n]}
    g[k]['plan']={a:list(b) for a,b in pl.items()}
g['9']['inv']['table']['rows']=['']*14
json.dump(g,open(fn,'w',encoding='utf8'),ensure_ascii=False,indent=1)
print('gifted.json updated')
