"""Level 6 Unit 9: Data detectives (mean, median, mode, lists in code).  Follows holiday lesson 9."""
from lib import *

U = 'L6U09'
I = []
X = '×'
M = '−'

learn = {
    'intro': 'The mean is the total divided by how many values there are. It is the level you get when the towers are made equal. '
             'Total = mean × how many. One very large or very small value can pull the mean away from a typical value.',
    'example': {
        'problem': 'Five friends collect shells: Ali 8, Mei 3, Siti 12, Ben 5 and Kumar 7. Find the mean number of shells.',
        'figure': {'type': 'l6_bars', 'values': [8, 3, 12, 5, 7], 'labels': ['Ali', 'Mei', 'Siti', 'Ben', 'Kumar'], 'unit_mm': 3, 'ymax': 12, 'ytick': 4, 'show': True, 'mean': 7, 'bar_mm': 12},
        'steps': ['Add all the values: 8 + 3 + 12 + 5 + 7 = 35.',
                  'Divide by how many values there are: 35 ÷ 5 = 7.',
                  'Check by levelling. The towers above 7 have 1 + 5 = 6 extra shells. The towers below 7 are 4 + 2 = 6 short.'],
        'answer': 'The mean is 7 shells.'},
    'howto': {'title': 'How to work with a mean',
              'steps': ['Add all the values. A value of 0 still counts.',
                        'Divide the total by how many values there are.',
                        'Missing value: total = mean × how many, then take away the values you know.',
                        'Median is the middle value in order. Mode is the most common value.']},
    'try': IT(U, 'L', 1, 0, 'The mean of 4 numbers is 12. Three of them are 9, 15 and 10. The 4th number is {b}.',
              f'The total of 4 numbers is 4 {X} 12 = 48. The 3 known numbers add to 9 + 15 + 10 = 34. The 4th number is 48 {M} 34 = 14.',
              answer=A([14], '14')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'Find the mean of each list.',
            '(a) 14 + 9 + 11 + 6 = 40, and 40 ÷ 4 = 10. (b) 9 + 0 + 6 + 0 + 10 = 25, and 25 ÷ 5 = 5 (the 0s count as values). (c) 1.5 + 2.5 + 4 + 3 = 11, and 11 ÷ 4 = 2.75.',
            parts=[P('a', '14, 9, 11, 6:  mean = {b}', [10]),
                   P('b', '9, 0, 6, 0, 10:  mean = {b}', [5]),
                   P('c', '1.5, 2.5, 4, 3:  mean = {b}', [2.75])],
            space={'rows': ['Working:']}))
I.append(IT(U, 'S', 2, 1,
            'Move blocks from tall towers to short towers until all towers are equal.',
            'Total: 9 + 7 + 5 + 3 = 24 blocks, shared over 4 towers: 24 ÷ 4 = 6. Tower A gives away 3 blocks and tower B gives away 1: 4 blocks move. Towers C and D receive them (1 and 3).',
            fig={'type': 'l6_bars', 'values': [9, 7, 5, 3], 'labels': ['A', 'B', 'C', 'D'], 'unit_mm': 4.5, 'ymax': 9, 'ytick': 3, 'show': True, 'bar_mm': 12},
            parts=[P('a', 'The mean height is {b} blocks.', [6]),
                   P('b', '{b} blocks must move from the tall towers to the short towers.', [4])],
            figside=True))
I.append(IT(U, 'S', 3, 1,
            'The mean mass of 5 parcels is 6 kg.',
            f'Total mass = mean {X} how many = 6 {X} 5 = 30 kg. The 3 known parcels weigh 4 + 9 + 7 = 20 kg, so the other 2 weigh 30 {M} 20 = 10 kg together.',
            parts=[P('a', 'The 5 parcels weigh {b} kg in all.', [30]),
                   P('b', '3 of them weigh 4 kg, 9 kg and 7 kg. The other 2 weigh {b} kg together.', [10])]))
I.append(IT(U, 'S', 4, 2,
            '4 test scores have a mean of 82. Three of the scores are 78, 90 and 85.',
            f'Total of 4 scores = 4 {X} 82 = 328. The known scores add to 78 + 90 + 85 = 253. The 4th score is 328 {M} 253 = 75. A 5th score equal to the mean, 82, keeps the mean at 82.',
            parts=[P('a', 'The 4th score is {b}.', [75]),
                   P('b', 'A 5th score of {b} keeps the mean at 82.', [82])],
            space={'rows': ['Working:']}))
I.append(IT(U, 'S', 5, 2,
            'The mean of 10, 12 and 14 is 12. Predict, then find what happens when the list changes.',
            f'(a) A new value equal to the mean does not change it: the mean stays at 12. (b) 10 + 12 + 14 + 20 = 56, and 56 ÷ 4 = 14. (c) 10 + 12 = 22, and 22 ÷ 2 = 11.',
            parts=[P('a', 'Add the value 12. The mean   {circ:goes up|stays the same|goes down}', ['stays the same']),
                   P('b', 'Add the value 20. The new mean is {b}.', [14]),
                   P('c', 'Take away the value 14. The new mean is {b}.', [11])]))
I.append(IT(U, 'S', 6, 2,
            'The median is the middle value when the values are in order. The mode is the value that appears most often.',
            '12, 7, 9, 7, 5 in order: 5, 7, 7, 9, 12. The middle one is 7, the mode is 7 and the mean is 40 ÷ 5 = 8. '
            '2, 8, 4, 6 in order: 2, 4, 6, 8. The 2 middle values are 4 and 6, so the median is halfway between them: 5.',
            parts=[P('a', 'For 12, 7, 9, 7, 5 the median is {b}.', [7]),
                   P('b', 'The mode is {b}.', [7]),
                   P('c', 'The mean is {b}.', [8]),
                   P('d', 'For 2, 8, 4, 6 the median is {b}.', [5])],
            partsrow=True))
I.append(IT(U, 'S', 7, 2,
            'A cafe has 7 staff. Their pay in dollars a month is 1500, 1600, 1600, 1700, 1800, 1900 and 9500.',
            'Total: 1500 + 1600 + 1600 + 1700 + 1800 + 1900 + 9500 = 19600, and 19600 ÷ 7 = 2800. In order the middle (4th) value is 1700. '
            'Only the owner earns 9500. The mean is pulled up by that one value, so the median 1700 is more typical.',
            parts=[P('a', 'The mean pay is {b} dollars.', [2800]),
                   P('b', 'The median pay is {b} dollars.', [1700]),
                   P('c', 'Which describes what most staff earn better?   {circ:mean|median}', ['median'])]))
I.append(IT(U, 'S', 8, 3,
            'The bar chart shows the number of stickers 6 pupils have.',
            f'Total: 14 + 9 + 17 + 12 + 8 + 12 = 72. Mean = 72 ÷ 6 = 12. Above 12: 14 and 17 is 2 pupils. (Two pupils have exactly 12.)',
            fig={'type': 'l6_bars', 'values': [14, 9, 17, 12, 8, 12], 'labels': ['Ali', 'Mei', 'Siti', 'Ben', 'Kumar', 'Aisha'], 'unit_mm': 2.6, 'ymax': 20, 'ytick': 5, 'show': True, 'bar_mm': 11, 'gap_mm': 3},
            parts=[P('a', 'They have {b} stickers in all.', [72]),
                   P('b', 'The mean is {b} stickers.', [12]),
                   P('c', '{b} pupils have more than the mean.', [2])],
            figside=True))
I.append(IT(U, 'S', 9, 3,
            'The list scores holds 7, 9, 3 and 5. A loop adds up the items and the program says the mean.',
            f'i goes 1, 2, 3, 4 and the loop adds 7, 9, 3 and 5: total 24. The last line says 24 ÷ 4 = 6. If it divided by 3 it would say 24 ÷ 3 = 8.',
            fig=code([['var', 'set total to (0)'], ['var', 'set i to (1)'], ['ctl', 'repeat (4)', [['var', 'change total by (item i of scores)'], ['var', 'change i by (1)']]], ['look', 'say (total ÷ 4)']]),
            parts=[P('a', 'After the loop, total is {b}.', [24]),
                   P('b', 'The program says {b}.', [6]),
                   P('c', 'If the last line says total ÷ 3, it says {b}.', [8])],
            figside=True))
I.append(IT(U, 'S', 10, 3,
            'The mean of 4, 8 and 12 is 8. Change every number in the list in the same way.',
            f'Add 5 to each: 9, 13, 17. 39 ÷ 3 = 13, which is the old mean + 5. Double each: 8, 16, 24. 48 ÷ 3 = 16, which is the old mean × 2.',
            parts=[P('a', 'Add 5 to every number. The new mean is {b}.', [13]),
                   P('b', 'Double every number. The new mean is {b}.', [16])],
            space={'rows': ['Working:']}))
I.append(IT(U, 'S', 11, 3,
            'The mean mass of 5 children is 40 kg. A 6th child of mass 52 kg joins them.',
            f'Total of 5 children = 5 {X} 40 = 200 kg. With the 6th child: 200 + 52 = 252 kg. New mean = 252 ÷ 6 = 42 kg.',
            parts=[P('a', 'The 5 children weigh {b} kg in all.', [200]),
                   P('b', 'With the 6th child the total is {b} kg.', [252]),
                   P('c', 'The new mean is {b} kg.', [42])],
            space={'rows': ['Working:']}))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            'Five whole numbers have a mean of 7 and a median of 6. Their only mode is 4, and the largest number is 13.',
            f'The total is 5 {X} 7 = 35. In order the middle number is 6. 4 is the mode and the smallest, so the first two numbers are 4 and 4: 4, 4, 6, ?, 13. '
            f'4 + 4 + 6 + 13 = 27, so the 4th number is 35 {M} 27 = 8. The numbers are 4, 4, 6, 8, 13.',
            answer=A([4, 4, 6, 8, 13], '4, 4, 6, 8, 13', list=True),
            hint='The 2 smallest are 4 and 4. Use the total for the other.', space={'rows': ['The numbers are {ll}', 'Working:', '', '']}))
I.append(IT(U, 'T', 2, 4,
            'A class has 12 girls and 18 boys. The girls have a mean mass of 40 kg. The boys have a mean mass of 45 kg.',
            f'Girls: 12 {X} 40 = 480 kg. Boys: 18 {X} 45 = 810 kg. All 30: 480 + 810 = 1290 kg. 1290 ÷ 30 = 43. The mean of the whole class is 43 kg, not 42.5, because there are more boys.',
            parts=[P('a', 'The girls weigh {b} kg in all.', [480]),
                   P('b', 'The boys weigh {b} kg in all.', [810]),
                   P('c', 'The mean mass of all 30 is {b} kg.', [43]),
                   P('d', 'It is more than 42.5 because there are more   {circ:girls|boys}', ['boys'])],
            hint='Find each group total first. Then find the total for all 30.', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 3, 4,
            'The mean of 3 numbers is 6.4. Two of them are 5.5 and 7.2.',
            f'The total is 3 {X} 6.4 = 19.2. The known numbers add to 5.5 + 7.2 = 12.7. The third number is 19.2 {M} 12.7 = 6.5.',
            parts=[P('a', 'The 3 numbers add up to {b}.', [19.2]),
                   P('b', 'The third number is {b}.', [6.5])],
            hint='Total = mean × how many. Then take away what you know.', space={'rows': ['Working:', '', '']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'Beyond Level 6: Pairing up.\nThe numbers 7, 12, 17, 22, ..., 102 go up by 5 each time. There are 20 of them.',
            'The 1st and last add to 7 + 102 = 109. So do the 2nd and the 2nd last (12 + 97). 20 numbers make 10 pairs of 109, so the total is 1090. The mean is 1090 ÷ 20 = 54.5, which is halfway between 7 and 102.',
            parts=[P('a', 'The 1st and the last add up to {b}.', [109]),
                   P('b', 'The 20 numbers make {b} such pairs.', [10]),
                   P('c', 'The mean of the 20 numbers is {b}.', [54.5])],
            hint='Pair the 1st with the last, the 2nd with the 2nd last.', partsrow=True))
I.append(IT(U, 'G', 2, 5,
            'The list marks holds 4, 8, 6, 10 and 7. This program adds up the items and says the mean.',
            f'Total = 4 + 8 + 6 + 10 + 7 = 35, and 35 ÷ 5 = 7. With repeat 4 the loop adds only 4 + 8 + 6 + 10 = 28, and 28 ÷ 5 = 5.6. '
            f'A 6th item 13 gives a total of 48, and 48 ÷ 6 = 8 (the program must divide by 6, the length of the list).',
            fig=code([['var', 'set total to (0)'], ['var', 'set i to (1)'], ['ctl', 'repeat (length of marks)', [['var', 'change total by (item i of marks)'], ['var', 'change i by (1)']]], ['look', 'say (total ÷ length of marks)']]),
            parts=[P('a', 'It says {b}.', [7]),
                   P('b', 'With repeat 4 and ÷ 5 it says {b}.', [5.6]),
                   P('c', 'With 13 added to the list it says {b}.', [8])],
            hint='Add up the items the loop reaches. Then divide.', figside=True))
I.append(IT(U, 'G', 3, 5,
            'Beyond Level 6: A frequency table.\nIn 10 matches a team scored goals as shown.',
            f'Total goals = 0 {X} 2 + 1 {X} 4 + 2 {X} 3 + 3 {X} 1 = 0 + 4 + 6 + 3 = 13. Mean = 13 ÷ 10 = 1.3. In order the 10 values are 0, 0, 1, 1, 1, 1, 2, 2, 2, 3. '
            f'The 5th and 6th values are 1 and 1, so the median is 1.',
            fig=grid([['Goals', '0', '1', '2', '3'], ['Matches', '2', '4', '3', '1']], [30, 18, 18, 18, 18], rowhead=True, ch=9),
            parts=[P('a', 'The team scored {b} goals in all.', [13]),
                   P('b', 'The mean number of goals is {b}.', [1.3]),
                   P('c', 'The median number of goals is {b}.', [1])],
            hint='2 matches with 0 goals, 4 with 1 goal: count goals for each column.', partsrow=True))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            'The mean of 6, 10, 2 and 14 is {b}.',
            '6 + 10 + 2 + 14 = 32, and 32 ÷ 4 = 8.',
            answer=A([8], '8')))
I.append(IT(U, 'C', 2, 6,
            'For 4, 9, 4, 6, 11 the median is {b} and the mode is {b}.',
            'In order: 4, 4, 6, 9, 11. The middle value is 6, and 4 appears most often.',
            answer=A([6, 4], '6, 4')))
I.append(IT(U, 'C', 3, 6,
            'The mean of 3 numbers is 14. Two of them are 10 and 18. The third is {b}.',
            f'Total = 3 {X} 14 = 42. 42 {M} 10 {M} 18 = 14.',
            answer=A([14], '14')))
I.append(IT(U, 'C', 4, 6,
            'The mean of 4 tests is 70. A 5th test score is 80. The new mean is {b}.',
            f'The 4 tests total 4 {X} 70 = 280. With the 5th: 280 + 80 = 360, and 360 ÷ 5 = 72.',
            answer=A([72], '72')))

learn['tight'] = True
write_unit(9, 'Data detectives', 'Mean, median and mode',
           'I can find the mean, a missing value from the mean, and compare the mean with the median and mode.', learn, I)
