"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 3: Picture Graphs ("Let's plan the fruit party!").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 3: Part A questions 1 to 7, Part B vote and questions 8 and 9;
hp/qbank.json lesson 3 stretch[0:4] for Think harder and challenge[-3:] for Go further, as the workbook builder slices them; hp/gaps.json lesson 3 for the Investigation).
The graph data (FRUIT) is the data of the printed picture graph (hp/figs_l1_3_l1.js fruitGraph); every answer is recomputed by an independent checker (counting and loops over the
numbers in the question) and the build stops if a checker and the printed answer (Tutor Guide answer key) differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=3, key='p1', title='Let’s plan the fruit party!', workbook_title='LET’S PLAN THE FRUIT PARTY!', topic='Picture Graphs',
            strand='Data: picture graphs',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['Our teacher wants to buy fruit for a class party. Every child voted for ONE fruit. The picture graph shows the votes.',
                   'The vote of your own group (Part B) is done on paper with your group. Use counters or draw pictures if you like.'])

S = 'Data: picture graphs'
FRUIT = dict(Apple=6, Banana=5, Orange=8, Grape=3, Watermelon=5)          # the printed graph: one picture for each child
NAMES = list(FRUIT)
GRAPH = picture_graph(list(FRUIT.items()), '1 child', lambda nm: ICONS[nm], 8, caption='Picture graph of fruit votes: one picture for each child')
STAR2 = dict(Red=3, Blue=5, Green=4)
STAR_GRAPH = picture_graph(list(STAR2.items()), '2 children', lambda nm: star, 6, half_key='1 child', caption='Picture graph: one star is 2 children, half a star is 1 child')
PIZZA_ROW = picture_graph([('Pizza', 0)], '2 children', lambda nm: star, 6, caption='An empty row for pizza. One star is 2 children')
APPLE_ROW = picture_graph([('Apple', 3.5)], '2 children', lambda nm: star, 5, caption='Apple row: 3 stars and half a star. One star is 2 children')
PETS = dict(Cats=4, Dogs=6, Fish=2)
VOTERS = 'one class'      # who voted in the printed graph (Tutor Guide answer key: "Only our class voted")


def votes(counts, name):
    """Count the pictures in a row one at a time."""
    n = 0
    for _ in range(counts[name]):
        n += 1
    return n


def pairs_with_same_votes(counts):
    names = list(counts)
    return [(a, b) for i, a in enumerate(names) for b in names[i + 1:] if counts[a] == counts[b]]


def graphs_with_banana_two_ahead(total):
    """Every (banana, second, third) with the three numbers adding to total, banana exactly 2 more than second place, no two the same, each fruit at least 1 vote."""
    out = []
    for b in range(1, total):
        for s in range(1, total):
            for t in range(1, total):
                if b + s + t == total and b - s == 2 and len({b, s, t}) == 3 and s > t:
                    out.append((b, s, t))
    return out


def pictures_for(children, per):
    """How many pictures are needed when 1 picture = per children (count picture by picture)."""
    n, got = 0, 0
    while got < children:
        n += 1; got += per
    return n if got == children else None


def D(**k):
    return dict(strand=S, **k)


EXAMPLE_TALLY = dict(Apple=2, Banana=1, Orange=3, Grape=1, Watermelon=2)


def cats_graph(per):
    return picture_graph([(nm, (c // per) + (0 if c % per == 0 else 0.5)) for nm, c in PETS.items()], f'{per} child' + ('ren' if per > 1 else ''), lambda nm: ICONS[nm], 6,
                         caption=f'Picture graph of cats, dogs and fish: one picture is {per} child' + ('ren' if per > 1 else ''))


def two_graphs(trios):
    """The graphs for C3 in one picture (1 picture = 1 child)."""
    body, y = '', 0
    inner_h = 0
    import re as _re
    for k, (b, s, t) in enumerate(trios):
        g = picture_graph([('Banana', b), ('Apple', s), ('Grape', t)], '1 child', lambda nm: ICONS[nm], 8)
        m = _re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', g)
        w, h = float(m.group(1)), float(m.group(2))
        inner = _re.sub(r'^<svg[^>]*>', '', g)[:-6]
        body += T(6, y + 18, f'Graph {k + 1}: banana {b}, apple {s}, grape {t}', 15, 'start', 800) + f'<g transform="translate(0 {y + 26})">{inner}</g>'
        y += h + 40; inner_h = max(inner_h, w)
    return svg(inner_h, y, body, 'Two picture graphs for 15 children where banana wins by exactly 2 votes')


ITEMS = [
    # ================= Start here: Part A, read the graph
    D(id='1', tier='core', no='1', type='choice', skill='reading a picture graph', options=NAMES, answer='Orange',
      q='Which fruit got the most votes?', svg=GRAPH, check=lambda: max(FRUIT, key=lambda f: votes(FRUIT, f)),
      hint='One picture is one child. Look for the longest row.',
      steps=['Count the pictures in each row: apple 6, banana 5, orange 8, grape 3, watermelon 5.', 'Orange has the most pictures, so orange got the most votes.'],
      src=['Which fruit got the most votes?']),
    D(id='2', tier='core', no='2', type='choice', skill='reading a picture graph', options=NAMES, answer='Grape',
      q='Which fruit got the fewest votes?', svg=GRAPH, check=lambda: min(FRUIT, key=lambda f: votes(FRUIT, f)),
      hint='Look for the shortest row.',
      steps=['Count the pictures in each row: apple 6, banana 5, orange 8, grape 3, watermelon 5.', 'Grape has the fewest pictures, so grape got the fewest votes.'],
      src=['Which fruit got the fewest votes?']),
    D(id='3', tier='core', no='3', type='number', skill='comparing two rows', answer=5,
      q='How many more children chose orange than grape?', svg=GRAPH, check=lambda: votes(FRUIT, 'Orange') - votes(FRUIT, 'Grape'),
      hint='Count the pictures in the orange row and in the grape row. Line the two rows up. How many pictures does orange have left over?',
      steps=['Orange has 8 pictures and grape has 3.', 'Match each grape with an orange. 3 oranges are matched and 5 oranges are left over.', '8 - 3 = 5, so 5 more children chose orange.'],
      src=['How many more children chose orange than grape?']),
    D(id='4', tier='core', no='4', type='choice', skill='reading a picture graph', answer='Banana and Watermelon',
      options=['Apple and Banana', 'Apple and Orange', 'Banana and Watermelon', 'Grape and Banana', 'Grape and Watermelon'],
      q='Two fruits got the same number of votes. Which two fruits are they?', svg=GRAPH,
      check=lambda: (lambda p: f'{p[0][0]} and {p[0][1]}' if len(p) == 1 else None)(pairs_with_same_votes(FRUIT)),
      hint='Compare the rows. Which two rows are exactly the same length?',
      steps=['Count: apple 6, banana 5, orange 8, grape 3, watermelon 5.', 'Banana and watermelon both have 5 pictures.', 'Banana and watermelon got the same number of votes.'],
      src=['Two fruits got the same number of votes. Which two fruits are they?']),
    D(id='5', tier='core', no='5', type='number', skill='totalling a picture graph', answer=27,
      q='How many children voted altogether? (Hint: each child had only 1 vote.)', svg=GRAPH, check=lambda: sum(votes(FRUIT, f) for f in FRUIT),
      hint='One picture is one child, and every child voted once. Count every picture in every row. Counting in 5s can help.',
      steps=['Add the pictures in all the rows: 6 + 5 + 8 + 3 + 5.', '6 + 5 = 11, 11 + 8 = 19, 19 + 3 = 22, 22 + 5 = 27.', '27 children voted.'],
      src=['How many children voted altogether? (Hint: each child had only 1 vote.)']),
    D(id='6a', tier='core', no='6(a)', type='choice', skill='what a graph tells us', options=['Yes', 'No'], answer='No',
      q='Mei says, "Orange is the best fruit for the whole school!" Is Mei right?', svg=GRAPH,
      check=lambda: 'Yes' if VOTERS == 'whole school' else 'No',
      hint='Think about who voted. Read the sentence above the graph again.',
      steps=['The graph shows the votes of one class, not the whole school.', 'Other classes may like different fruits, so Mei cannot say orange is the best for the whole school.'],
      src=['Mei says, “Orange is the best fruit for the whole school!”', 'Is Mei right?']),
    D(id='6b', tier='core', no='6(b)', type='selfcheck', open=False, skill='what a graph tells us',
      q='Mei says, "Orange is the best fruit for the whole school!" Say why you think she is right, or why she is not right.',
      facts=27, check=lambda: sum(votes(FRUIT, f) for f in FRUIT),
      hint='Who voted? How many children is that? How many children are in the whole school?',
      steps=['Only our class voted: 27 children.', 'Other classes may like different fruits. The graph tells us about our class only.', 'Any reason that talks about who voted is good.'],
      src=['Why do you think so?']),
    D(id='7', tier='core', no='7', type='selfcheck', open=True, skill='what a graph tells us',
      q='What else should the teacher think about before buying fruit for the party?',
      hint='Think about the party. What could go wrong if she only counts the votes?',
      steps=['Here are some good ideas: the cost, how much fruit we need, whether it is easy to share, whether it keeps fresh, whether it is messy to eat, and any child who cannot eat it.', 'Any sensible idea is good.'],
      src=['What else should the teacher think about before buying fruit for the party?']),

    # ---- Part B: your own group's vote (on paper)
    D(id='vote', tier='core', no='Vote', type='selfcheck', paper=True, skill='making a tally', q='Now it’s your turn! Ask your own group to vote. Each child votes for ONE fruit. Make a tally mark for each vote.',
      svg=tally_table(NAMES), check=lambda: sum(EXAMPLE_TALLY.values()),
      sol_fig=lambda f: tally_table(NAMES, EXAMPLE_TALLY),
      hint='Make one mark for each child. Fill in the Total column when everyone has voted.',
      steps=['Here is an example for a group of 9 children. Your group’s marks will be different.', 'Draw one mark for each vote. Cross four marks with a fifth to make a group of 5.', 'Write the total for each fruit. The totals should add up to the number of children who voted.'],
      src=['Ask your own group to vote. Each child votes for ONE fruit. Make a tally mark for each vote.']),
    D(id='8', tier='core', no='8', type='selfcheck', open=True, skill='what a graph tells us',
      q='Which fruit did YOUR group like best? Is it the same as the fruit with the most pictures on the graph?',
      hint='Look at your tally table. Which fruit has the most marks?',
      steps=['The fruit with the most tally marks is the one your group liked best.', 'Now look at the graph in this lesson. If your fruit is the one with the longest row, the answer is yes. If not, the answer is no.', 'Both answers can be right: your group is not the same as the class on the graph.'],
      src=['Which fruit did YOUR group like best?', 'Is it the same as the graph above?']),
    D(id='9', tier='core', no='9', type='selfcheck', open=True, skill='what a graph tells us',
      q='Why might two groups choose different fruits?',
      hint='Do all children like the same things?',
      steps=['Different children like different things.', 'A small group may not match a big group. Two groups can have different results and both can be right.', 'Any sensible reason is good.'],
      src=['Why might two groups choose different fruits?']),

    # ================= Investigation
    D(id='I1', tier='invest', no='Investigation 1', type='selfcheck', paper=True, skill='choosing the key',
      q='Investigation: What if we change the key? Draw a picture graph with 1 picture = 1 child: Cats 4, Dogs 6, Fish 2.',
      facts=PETS, check=lambda: {nm: votes(PETS, nm) for nm in PETS}, sol_fig=lambda f: cats_graph(1),
      hint='Draw a row for each pet. Draw one picture for each child. Write the key.',
      steps=['Cats get 4 pictures, dogs get 6 and fish get 2.', 'Write the key: 1 picture = 1 child.', 'That is 4 + 6 + 2 = 12 pictures.'],
      src=['Draw a picture graph with 1 picture = 1 child: Cats 4, Dogs 6, Fish 2.']),
    D(id='I2', tier='invest', no='Investigation 2', type='selfcheck', paper=True, skill='choosing the key',
      q='Now draw it again with 1 picture = 2 children. The children are the same: Cats 4, Dogs 6, Fish 2.',
      facts=dict(Cats=2, Dogs=3, Fish=1), check=lambda: {nm: PETS[nm] // 2 for nm in PETS if PETS[nm] % 2 == 0}, sol_fig=lambda f: cats_graph(2),
      hint='Count in 2s. How many pictures do you need for 4 children?',
      steps=['Cats: 4 children is 2 pictures. Dogs: 6 children is 3 pictures. Fish: 2 children is 1 picture.', 'Write the new key: 1 picture = 2 children.'],
      src=['Now draw it again with 1 picture = 2 children.']),
    D(id='I3', tier='invest', no='Investigation 3', type='selfcheck', open=False, skill='choosing the key',
      q='Compare your two graphs. What stays the same? What changes?',
      facts=dict(children=(12, 12), pictures=(12, 6), most=('Dogs', 'Dogs'), fewest=('Fish', 'Fish')),
      check=lambda: dict(children=(sum(PETS.values()), sum(2 * (PETS[nm] // 2) for nm in PETS)), pictures=(sum(PETS.values()), sum(PETS[nm] // 2 for nm in PETS)),
                         most=(max(PETS, key=PETS.get), max(PETS, key=lambda nm: PETS[nm] // 2)), fewest=(min(PETS, key=PETS.get), min(PETS, key=lambda nm: PETS[nm] // 2))),
      hint='Count the children each graph shows. Count the pictures. Which row is longest in each?',
      steps=['Stays the same: 12 children in all, dogs still have the longest row and fish still have the shortest row.', 'Changes: the number of pictures. There are 12 pictures with the first key and 6 with the second.', 'Any answer that says the number of pictures changes but the number of children stays the same is good.'],
      src=['What stays the same? What changes?']),
    D(id='I4', tier='invest', no='Investigation 4', type='choice', skill='choosing the key', options=['Yes', 'No'], answer='No',
      q='Cats 4, Dogs 6, Fish 2. Could you use 1 picture = 3 children? Use only whole pictures.',
      check=lambda: 'Yes' if all(pictures_for(c, 3) is not None for c in PETS.values()) else 'No',
      hint='Try drawing each row with whole pictures of 3 children. Does every row work?',
      steps=['Dogs 6 is 2 pictures of 3. But cats 4 and fish 2 do not fit: 3 is too few and 6 is too many.', 'We would need part of a picture, so a key of 3 does not work here.'],
      src=['Could you use 1 picture = 3 children?']),
    D(id='I5', tier='invest', no='Investigation 5', type='selfcheck', open=False, skill='choosing the key',
      q='Cats 4, Dogs 6, Fish 2. Why can you or can you not use 1 picture = 3 children?', facts=[4, 2], check=lambda: [c for c in PETS.values() if pictures_for(c, 3) is None],
      hint='Count in 3s for each row: 3, 6, 9 ... Which counts do you land on?',
      steps=['Counting in 3s goes 3, 6, 9 ... It lands on 6 for the dogs, but it does not land on 4 or on 2.', 'A key only works when every count is in its counting pattern. Here the keys 1 and 2 work, but 3 does not.', 'Any reason that talks about counting in 2s or 3s is good.'],
      src=['Why or why not?']),

    # ================= Think harder
    D(id='T1', tier='stretch', no='T1', type='number', skill='reading a key', answer=10,
      q='1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children chose blue?', svg=STAR_GRAPH,
      check=lambda: sum(2 for _ in range(STAR2['Blue'])),
      hint='Each picture is 2 children. Count in 2s as you point to each blue picture.',
      steps=['Blue has 5 pictures and each picture is 2 children.', 'Count in 2s: 2, 4, 6, 8, 10.', '10 children chose blue.'],
      src=['1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children chose blue?']),
    D(id='T2', tier='stretch', no='T2', type='number', skill='reading a key', answer=24,
      q='1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children voted altogether?',
      check=lambda: sum(2 for p in (3, 5, 4) for _ in range(p)),
      hint='First find how many pictures there are in all. Then think about what each picture is worth.',
      steps=['The pictures in all: 3 + 5 + 4 = 12 pictures.', 'Each picture is 2 children. Count in 2s twelve times: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24.', '24 children voted.'],
      src=['1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children voted altogether?']),
    D(id='T3', tier='stretch', no='T3', type='number', skill='reading a key', answer=3,
      q='1 picture = 2 children. Six children chose pizza. How many pictures should we draw?', svg=PIZZA_ROW,
      check=lambda: pictures_for(6, 2),
      hint='Count in 2s until you get to 6. How many 2s did you count?',
      steps=['Count in 2s: 2, 4, 6. That is 3 counts.', 'Each count is one picture, so draw 3 pictures.'],
      src=['1 picture = 2 children. Six children chose pizza. How many pictures should we draw?']),
    D(id='T4', tier='stretch', no='T4', type='number', skill='half a picture', answer=7,
      q='1 picture = 2 children. A half picture means 1 child. Apple has 3 pictures and a half. How many children chose apple?', svg=APPLE_ROW,
      check=lambda: sum(2 for _ in range(3)) + 1,
      hint='Count the whole pictures first, in 2s. Then think about the half picture.',
      steps=['3 whole pictures: 2, 4, 6 children.', 'The half picture is 1 more child: 6 + 1 = 7.', '7 children chose apple.'],
      src=['1 picture = 2 children. A half picture means 1 child. Apple has 3 pictures and a half. How many children chose apple?']),

    # ================= Go further
    D(id='C1', tier='challenge', no='C1', type='fields', skill='two numbers with a total and a difference', answer=[6, 12],
      q='24 children voted. Apple got 6 votes. Orange got 6 more votes than banana. How many votes did banana and orange get?', frame='Banana {f1}      Orange {f2}',
      check=lambda: next([b, o] for b in range(25) for o in range(25) if 6 + b + o == 24 and o - b == 6),
      hint='Apple got some of the votes. How many votes are left for banana and orange together?',
      steps=['24 - 6 = 18 votes are left for banana and orange.', 'Orange has 6 more than banana. Take away the extra 6: 18 - 6 = 12. Share 12 equally: 6 and 6.', 'Banana gets 6 and orange gets 6 + 6 = 12.', 'Check: 6 + 6 + 12 = 24 and 12 is 6 more than 6.'],
      src=['24 children voted. Apple got 6 votes. Orange got 6 more votes than banana. How many votes did banana and orange get?']),
    D(id='C2', tier='challenge', no='C2', type='number', skill='reading a key', answer=4,
      q='1 picture = 2 children. 20 children voted for three fruits. A has 3 pictures. B has 2 more pictures than A. How many children chose C?',
      check=lambda: next(2 * c for c in range(11) if 3 + (3 + 2) + c == pictures_for(20, 2)),
      hint='Work with pictures first. How many pictures are there in all? How many do A and B have?',
      steps=['20 children is 10 pictures in all (count in 2s to 20).', 'A has 3 pictures. B has 2 more, so B has 5 pictures.', 'A and B have 3 + 5 = 8 pictures, so C has 10 - 8 = 2 pictures.', '2 pictures is 2 + 2 = 4 children.'],
      src=['1 picture = 2 children. 20 children voted for three fruits. A has 3 pictures. B has 2 more pictures than A. How many children chose C?']),
    D(id='C3', tier='challenge', no='C3', type='selfcheck', paper=True, skill='making a graph from clues',
      q='Make up your own: 15 children vote for three fruits. Draw a picture graph where banana wins by exactly 2 votes (banana has 2 more than the fruit in second place) and no two fruits are tied. Then try to find a second graph that works.',
      facts=[(7, 5, 3), (8, 6, 1)], check=lambda: graphs_with_banana_two_ahead(15), sol_fig=lambda f: two_graphs(f),
      hint='Try a number for second place. Add 2 to get banana. Is there something left for the third fruit?',
      steps=['Try banana 7, second place 5. That leaves 15 - 7 - 5 = 3 for the third fruit. 7, 5 and 3 are all different.', 'Another way: banana 8, second place 6. That leaves 1 for the third fruit.', 'These are the only two graphs. Any graph that adds to 15, has banana exactly 2 ahead of second place, and has no ties is good.'],
      src=['Make up your own: 15 children vote for three fruits. Draw a picture graph where banana wins by exactly 2 votes (banana has 2 more than the fruit in second place) and no two fruits are tied. Then try to find a second graph that works.']),
]


VARIANTS = {
    'T2': dict(
        base=dict(k=2, r=3, b=5, g=4),
        tpl=dict(vars=dict(k=[2, 3, 5, 10], r=[2, 3, 4], b=[3, 4, 5, 6], g=[1, 2, 3, 4]),
                 q='1 picture = {k} children. Red has {r} pictures, blue has {b} and green has {g}. How many children voted altogether?',
                 answer='k*(r+b+g)', derive=dict(p='r+b+g'),
                 hint='First find how many pictures there are in all. Then count in {k}s.',
                 steps=['The pictures in all: {r} + {b} + {g} = {p} pictures.', 'Each picture is {k} children. Count in {k}s, {p} times.', 'The answer is {ans} children.']),
        oracle=lambda e: sum(e['k'] for p in (e['r'], e['b'], e['g']) for _ in range(p))),
    'T3': dict(
        base=dict(k=2, p=3),
        tpl=dict(vars=dict(k=[2, 3, 4, 5, 10], p=[2, 3, 4, 5, 6]),
                 q='1 picture = {k} children. {c} children chose pizza. How many pictures should we draw?',
                 answer='p', derive=dict(c='k*p'),
                 hint='Count in {k}s until you get to {c}. How many {k}s did you count?',
                 steps=['Count in {k}s until you reach {c}.', 'You count {p} times, so draw {p} pictures.']),
        oracle=lambda e: pictures_for(e['k'] * e['p'], e['k'])),
    'C2': dict(
        base=dict(k=2, a=3, d=2, c=2),
        tpl=dict(vars=dict(k=[2, 3, 5], a=[2, 3, 4], d=[1, 2, 3], c=[1, 2, 3]),
                 q='1 picture = {k} children. {n} children voted for three fruits. A has {a} pictures. B has {d} more pictures than A. How many children chose C?',
                 answer='k*c', derive=dict(n='k*(2*a+d+c)', pa='2*a+d', pt='2*a+d+c'),
                 hint='Work with pictures first. How many pictures are there in all? How many do A and B have?',
                 steps=['{n} children is {pt} pictures in all (count in {k}s).', 'A and B have {pa} pictures together, so C has {c} pictures.', '{c} pictures of {k} children is {ans} children.']),
        oracle=lambda e: next(e['k'] * c for c in range(20) if e['a'] + (e['a'] + e['d']) + c == pictures_for(e['k'] * (2 * e['a'] + e['d'] + e['c']), e['k']))),
}
