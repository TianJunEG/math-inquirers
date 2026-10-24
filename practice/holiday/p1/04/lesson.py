"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 4: Patterns ("Pattern inquiry": repeating and growing patterns).

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 4, Q1 to Q8; hp/qbank.json lesson 4 stretch[0:4] for Think harder and challenge[-3:] for Go further,
as the workbook builder slices them; hp/gaps.json lesson 4 for the Investigation).  The pictures are redrawn from the printed ones (hp/figs_l1_3_l1.js p1 to p6, t1, t3, stickSquares,
dotTriangles).  Every answer is recomputed by an independent checker: the pattern is built place by place by going round its set of shapes, and the stick counts come from counting
the distinct sticks of the drawn rows (no formula).  The build stops if a checker and the printed answer (Tutor Guide answer key) differ.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=4, key='p1', title='Pattern inquiry', workbook_title='PATTERN INQUIRY', topic='Patterns',
            strand='Patterns',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['Look for the set of shapes that repeats. Number the places to help you. Use counters or draw on paper if you like.'])

S = 'Patterns'


def D(**k):
    return dict(strand=S, **k)


def at(core, place):
    """The thing in a given place (1, 2, 3 ...) of a pattern that repeats `core`, found by building the pattern place by place."""
    return repeat(core, place)[place - 1]


def name(x):
    return x.title()


# ---- sticks: the distinct sticks of a row of triangles / squares, counted from the points they join
def triangle_sticks(n):
    pts = [(i, i % 2) for i in range(n + 2)]            # a zig-zag of n + 2 points: even places at the bottom, odd places at the top
    sticks = set()
    for k in range(n):
        a, b, c = pts[k], pts[k + 1], pts[k + 2]        # triangle k joins three neighbouring points
        sticks |= {frozenset((a, b)), frozenset((b, c)), frozenset((a, c))}
    return len(sticks)


def square_sticks(n):
    sticks = set()
    for k in range(n):                                   # square k has corners (k, 0), (k + 1, 0), (k + 1, 1), (k, 1)
        c = [(k, 0), (k + 1, 0), (k + 1, 1), (k, 1)]
        for i in range(4):
            sticks.add(frozenset((c[i], c[(i + 1) % 4])))
    return len(sticks)


def most_with(sticks_fn, have):
    """The biggest row that can be made with `have` sticks, and the sticks left over."""
    n = 0
    while sticks_fn(n + 1) <= have:
        n += 1
    return n, have - sticks_fn(n)


def triangular(k):
    """Dots in the k-th triangle of dots, counted row by row."""
    return sum(r for r in range(1, k + 1))


SHAPE3 = ['circle', 'triangle', 'square']
SHAPE3B = ['circle', 'square', 'triangle']
RRB = ['red', 'red', 'blue']
CSS = ['circle', 'star', 'square']
CDD = ['cat', 'dog', 'dog']
ABCD = ['L:A', 'L:B', 'L:C', 'L:D']
CTTS = ['circle', 'triangle', 'triangle', 'square']
RBB = ['red', 'blue', 'blue']
FIVE = ['red', 'red', 'blue', 'blue', 'green']
EXAMPLE5 = ['red', 'green', 'green', 'blue', 'red']      # the worked example for C3 (not the pattern of C1)


def row(core, shown, total):
    return pattern_row(repeat(core, shown) + ['?'] * (total - shown), caption=f'A pattern with {shown} places shown and places {shown + 1} to {total} empty' if total > shown else 'A pattern with numbered places')


def beads_example():
    items = repeat(EXAMPLE5, 10)
    r = pattern_row(items, caption='Example: red, green, green, blue, red, then again, places 1 to 10')
    return r


def example_beads_fig(colour):
    """The worked example of C3: beads of a pattern of 5 and where place 33 falls."""
    body = ''
    x0, y0, pitch = 12, 6, 36
    for i, c in enumerate(repeat(EXAMPLE5, 10)):
        body += draw_item(c, x0 + (i % 5) * pitch + pitch / 2, y0 + 14 + (i // 5) * 52, 28) + T(x0 + (i % 5) * pitch + pitch / 2, y0 + 44 + (i // 5) * 52, i + 1, 14, 'middle', 700, '#44506F')
    body += T(12, y0 + 128, 'Each set has 5 beads.', 14, 'start', 600) + T(12, y0 + 148, 'Places 5, 10, 15 ... 30 end a set.', 14, 'start', 600) + T(12, y0 + 168, 'So place 33 is bead 3 of a set:', 14, 'start', 600)
    body += draw_item(colour, 28, y0 + 196, 28) + T(52, y0 + 202, colour, 15, 'start', 800)
    return svg(270, y0 + 222, body, f'An example pattern of 5 beads. Place 33 is {colour}.')


def cores_of_three(symbols='abc'):
    return list(itertools.product(symbols, repeat=3))


ITEMS = [
    # ================= Start here
    D(id='1a', tier='core', no='1(a)', type='choice', skill='repeating patterns', options=['Circle', 'Triangle', 'Square'], answer='Triangle',
      q='Look at the shape pattern. Which shape goes in place 8?', svg=row(SHAPE3, 7, 9), check=lambda: name(at(SHAPE3, 8)),
      hint='Find the set of shapes that repeats. Keep it going until you reach place 8.',
      steps=['The set that repeats is circle, triangle, square.', 'Places 1 to 3 are circle, triangle, square, places 4 to 6 are the same again, and place 7 is a circle.', 'Place 8 is the next one in the set: a triangle.'],
      src=['Look at the shape pattern. Draw the missing shapes in places 8 and 9.']),
    D(id='1b', tier='core', no='1(b)', type='choice', skill='repeating patterns', options=['Circle', 'Triangle', 'Square'], answer='Square',
      q='Look at the shape pattern. Which shape goes in place 9?', svg=row(SHAPE3, 7, 9), check=lambda: name(at(SHAPE3, 9)),
      hint='Find the set of shapes that repeats. Keep it going until you reach place 9.',
      steps=['The set that repeats is circle, triangle, square.', 'Place 7 is a circle and place 8 is a triangle.', 'Place 9 is the next one in the set: a square.'],
      src=['Look at the shape pattern. Draw the missing shapes in places 8 and 9.']),
    D(id='2', tier='core', no='2', type='choice', skill='repeating patterns', options=['Circle', 'Square', 'Triangle'], answer='Circle',
      q='The pattern is circle, square, triangle, circle, square, triangle, circle ... What is the 10th one? Keep going until you reach it.', svg=row(SHAPE3B, 7, 10),
      check=lambda: name(at(SHAPE3B, 10)),
      hint='Keep the pattern going. Say the shapes for places 8, 9 and 10.',
      steps=['The set is circle, square, triangle.', 'Place 7 is a circle, place 8 a square, place 9 a triangle.', 'Place 10 starts the set again: a circle.'],
      src=['The pattern is circle, square, triangle, circle, square, triangle, circle … What is the 10th one? (Keep writing the pattern until you get there.)']),
    D(id='3', tier='core', no='3', type='choice', skill='repeating patterns', options=['Red', 'Blue'], answer='Red',
      q='The pattern is red, red, blue, red, red, blue, red ... What is the 8th one?', svg=row(RRB, 7, 8), check=lambda: name(at(RRB, 8)),
      hint='Find the set that repeats. What comes after the 7th one?',
      steps=['The set is red, red, blue.', 'Place 7 is the first of the set (red), so place 8 is the second of the set.', 'Place 8 is red.'],
      src=['The pattern is red, red, blue, red, red, blue, red … What is the 8th one?']),

    D(id='4a', tier='core', no='4(a)', type='choice', skill='repeating patterns', options=['Circle', 'Star', 'Square'], answer='Circle',
      q='Look at this pattern. It keeps going in the same way. What shape will be in place 10?', svg=row(CSS, 8, 12), check=lambda: name(at(CSS, 10)),
      hint='Find the set of shapes that repeats. Keep it going to place 10. You may draw in the empty boxes on paper.',
      steps=['The set is circle, star, square.', 'Place 9 is a square, so place 10 starts the set again.', 'Place 10 is a circle.'],
      src=['Look at this pattern. It keeps going in the same way. You may draw in the empty boxes.', 'What shape will be in place 10?']),
    D(id='4b', tier='core', no='4(b)', type='choice', skill='repeating patterns', options=['Circle', 'Star', 'Square'], answer='Square',
      q='Look at this pattern. It keeps going in the same way. What shape will be in place 12?', svg=row(CSS, 8, 12), check=lambda: name(at(CSS, 12)),
      hint='Find the set of shapes that repeats. Keep it going to place 12.',
      steps=['The set is circle, star, square.', 'Place 10 is a circle, place 11 is a star.', 'Place 12 is a square.'],
      src=['What shape will be in place 12?']),
    D(id='4c', tier='core', no='4(c)', type='choice', skill='repeating patterns', options=['Circle', 'Star', 'Square'], answer='Square',
      q='Look at this pattern. It keeps going in the same way. What shape will be in place 30? Keep drawing, or look for a shortcut.', svg=row(CSS, 8, 12), check=lambda: name(at(CSS, 30)),
      hint='Which places finish a whole set? Is there a quicker way than drawing every shape?',
      steps=['Each set has 3 shapes, so the places that finish a set are 3, 6, 9, 12 ... (count in 3s).', '30 is one of the numbers we say when we count in 3s: 3, 6, 9, ... 27, 30.', 'So place 30 finishes a set, like place 3. It is a square.'],
      src=['What shape will be in place 30? (Keep drawing, or look for a shortcut.)']),
    D(id='4d', tier='core', no='4(d)', type='selfcheck', open=False, skill='repeating patterns',
      q='How do you know the shape in place 30?', svg=row(CSS, 8, 12),
      facts=True, check=lambda: at(CSS, 30) == at(CSS, 3) and all(at(CSS, p) == at(CSS, 3) for p in range(3, 31, 3)),
      hint='Think about the places that finish a set. How do you count to them?',
      steps=['Each set has 3 shapes. The places that finish a set are 3, 6, 9, ... and we say 30 when we count in 3s.', 'So place 30 is the same shape as place 3: a square.', 'Any answer that counts in 3s, or draws the pattern all the way to 30, is good.'],
      src=['How do you know?']),

    D(id='5', tier='core', no='5', type='choice', skill='repeating patterns', options=['Cat', 'Dog'], answer='Dog',
      q='The pattern is cat, dog, dog, cat, dog, dog, cat ... What is the 12th one?', svg=row(CDD, 7, 12), check=lambda: name(at(CDD, 12)),
      hint='Find the set that repeats. Keep going to place 12, or find which places finish a set.',
      steps=['The set is cat, dog, dog.', 'Places 3, 6, 9 and 12 finish a set, and a set finishes with a dog.', 'Place 12 is a dog.'],
      src=['The pattern is cat, dog, dog, cat, dog, dog, cat … What is the 12th one?']),
    D(id='6', tier='core', no='6', type='choice', skill='repeating patterns', options=['A', 'B', 'C', 'D'], answer='C',
      q='The pattern is A, B, C, D, A, B, C ... What is the 11th one? Keep the pattern going and number the places.', svg=row(ABCD, 7, 11), check=lambda: at(ABCD, 11)[2:],
      hint='Keep the letters going. Where does each set of letters end?',
      steps=['The set is A, B, C, D.', 'Places 4 and 8 finish a set. Place 9 is A and place 10 is B.', 'Place 11 is C.'],
      src=['The pattern is A, B, C, D, A, B, C … What is the 11th one? (Write the letters in a row and number them.)']),

    D(id='7a', tier='core', no='7(a)', type='fields', skill='growing patterns', answer=[9, 11, 13],
      q='Ben makes a row of triangles with sticks. 1 triangle needs 3 sticks, 2 triangles need 5 and 3 triangles need 7. Keep going. How many sticks do 4, 5 and 6 triangles need?',
      frame='4\u00a0triangles: {f1}   5\u00a0triangles: {f2}   6\u00a0triangles: {f3}',
      svg=triangle_rows(), check=lambda: [triangle_sticks(n) for n in range(4, 7)],
      hint='Look at 3, 5, 7. What comes next? You can check by drawing the 4 triangles on paper and counting the sticks.',
      steps=['1 triangle: 3 sticks. 2 triangles: 5. 3 triangles: 7.', 'The numbers go up by the same amount each time: 3, 5, 7, 9, 11, 13.', 'The boxes are 9, 11 and 13.'],
      src=['Ben makes a row of triangles with sticks.', 'Count the sticks. Fill in the table. Keep going until you reach 10 triangles.']),
    D(id='7b', tier='core', no='7(b)', type='number', skill='growing patterns', answer=2,
      q='Ben makes a row of triangles with sticks. Each time Ben adds 1 more triangle, how many more sticks does he need?', svg=triangle_rows(),
      check=lambda: (lambda d: d.pop() if len(d) == 1 else None)({triangle_sticks(n + 1) - triangle_sticks(n) for n in range(1, 10)}),
      hint='Count the sticks for 1, 2 and 3 triangles. How many more is each row than the one before?',
      steps=['3 sticks, then 5, then 7.', '5 - 3 = 2 and 7 - 5 = 2.', 'Ben needs 2 more sticks each time.'],
      src=['Each time Ben adds 1 more triangle, how many more sticks does he need?']),
    D(id='7c', tier='core', no='7(c)', type='selfcheck', open=False, skill='growing patterns',
      q='Each time Ben adds 1 more triangle, he needs only a few more sticks. Why? Look at the picture.', svg=triangle_rows(),
      facts=dict(whole=3, needed=2, shared=1), check=lambda: dict(whole=triangle_sticks(1), needed=triangle_sticks(2) - triangle_sticks(1), shared=triangle_sticks(1) - (triangle_sticks(2) - triangle_sticks(1))),
      hint='Look at where a new triangle joins the one before it. Is every side of the new triangle a new stick?',
      steps=['A triangle has 3 sticks, but a new triangle shares 1 stick with the triangle before it.', 'So Ben needs only 3 - 1 = 2 new sticks.', 'Any answer that says the triangles share a stick is good.'],
      src=['Why does he need only that many more sticks? (Look at the picture.)']),
    D(id='7d', tier='core', no='7(d)', type='number', skill='growing patterns', answer=21,
      q='Ben makes a row of triangles with sticks. How many sticks are needed for 10 triangles?', svg=triangle_rows(), check=lambda: triangle_sticks(10),
      hint='Use the numbers you have found, and keep adding on until you reach 10 triangles.',
      steps=['The sticks are 3, 5, 7, 9, 11, 13, 15, 17, 19, 21.', '10 triangles need 21 sticks.'],
      src=['How many sticks are needed for 10 triangles?']),
    D(id='8a', tier='core', no='8(a)', type='number', skill='growing patterns', answer=7,
      q='If you have time: Ben makes a row of triangles with sticks. Ben has 15 sticks. How many triangles in a row can he make?', svg=triangle_rows(),
      check=lambda: most_with(triangle_sticks, 15)[0],
      hint='Keep counting the sticks: 3, 5, 7 ... Stop before you go over 15.',
      steps=['The sticks for each row are 3, 5, 7, 9, 11, 13, 15.', 'The row of 7 triangles needs exactly 15 sticks.', 'Ben can make 7 triangles.'],
      src=['If you have time: Ben has 15 sticks. How many triangles in a row can he make?']),
    D(id='8b', tier='core', no='8(b)', type='selfcheck', open=False, skill='growing patterns',
      q='Show how you worked out how many triangles Ben can make with 15 sticks.', facts=[3, 5, 7, 9, 11, 13, 15], check=lambda: [triangle_sticks(n) for n in range(1, most_with(triangle_sticks, 15)[0] + 1)],
      hint='Write the number of sticks for 1 triangle, 2 triangles, 3 triangles ... and stop at 15.',
      steps=['Write the sticks: 3, 5, 7, 9, 11, 13, 15.', 'Count how many numbers you wrote: 7. The last one is exactly 15, so no sticks are left over.', 'Any working that reaches 7 triangles is good.'],
      src=['Show how you worked it out:']),

    # ================= Investigation
    D(id='I1', tier='invest', no='Investigation 1', type='selfcheck', paper=True, skill='repeating patterns',
      q='Is it always true? Draw your own pattern of 3 shapes that repeats (for example circle, square, triangle, circle, square, triangle ...) up to place 9.',
      facts=['square', 'star', 'circle'], check=lambda: (lambda c: c if all(at(c, p) == at(c, 3) for p in (6, 9)) else None)(['square', 'star', 'circle']),
      sol_fig=lambda f: pattern_row(repeat(['triangle', 'star', 'circle'], 9), caption='An example pattern of 3 shapes, places 1 to 9'),
      hint='Pick three different shapes. Draw them in order, then draw them again and again until place 9. Number the places.',
      steps=['Here is one example: triangle, star, circle, then the same three again, and again.', 'Look at places 3, 6 and 9. They are all the same shape (a circle in this example).', 'Any pattern with a set of 3 shapes that repeats to place 9 is good.'],
      src=['Draw your own pattern of 3 shapes that repeats (for example circle, square, triangle, circle, square, triangle ...) up to place 9.']),
    D(id='I2', tier='invest', no='Investigation 2', type='choice', skill='repeating patterns', options=['Yes', 'No'], answer='Yes',
      q='Mei says: "In a pattern that repeats every 3 shapes, place 30 is the same shape as place 3." Test Mei on places 6 and 9, then on place 30. Is she always right?',
      check=lambda: 'Yes' if all(at(c, 3) == at(c, p) for c in cores_of_three() for p in (6, 9, 30)) else 'No',
      hint='Try it on your own pattern, then on a different one. Does it work every time?',
      steps=['In a pattern with a set of 3 shapes, places 3, 6, 9, 12 ... all finish a set. We say them when we count in 3s, and 30 is one of them.', 'So place 30 is the same shape as place 3 for any set of 3 shapes.', 'Yes, Mei is always right.'],
      src=['Mei says: "In a pattern that repeats every 3 shapes, place 30 is the same shape as place 3." Test Mei on places 6 and 9, then on place 30. Is she always right?']),
    D(id='I3', tier='invest', no='Investigation 3', type='set', ordered=False, skill='repeating patterns', answer=[4, 8, 12, 16, 20],
      q='Now think about a pattern that repeats every 4 shapes. Which places up to 20 are the same shape as place 4? Type them with a comma between.',
      check=lambda: sorted(set.intersection(*[{p for p in range(1, 21) if at(list(c), p) == at(list(c), 4)} for c in itertools.permutations('abcd')])),
      hint='Draw a pattern with a set of 4 different shapes. Which places finish a set?',
      steps=['Each set has 4 shapes, so the places that finish a set are 4, 8, 12, 16 and 20 (count in 4s).', 'Those places are all the same shape as place 4.'],
      src=['What about a pattern that repeats every 4 shapes: which places match place 4?']),

    # ================= Think harder
    D(id='T1', tier='stretch', no='T1', type='choice', skill='repeating patterns', options=['Circle', 'Triangle', 'Square'], answer='Triangle',
      q='Pattern: circle, triangle, triangle, square, circle, triangle, triangle, square ... What is the 14th shape?', svg=row(CTTS, 8, 14), check=lambda: name(at(CTTS, 14)),
      hint='Find the set that repeats. Keep it going to place 14.',
      steps=['The set is circle, triangle, triangle, square (4 shapes).', 'Place 12 finishes the third set. Place 13 is a circle.', 'Place 14 is a triangle.'],
      src=['Pattern: circle, triangle, triangle, square, circle, triangle, triangle, square … What is the 14th shape?']),
    D(id='T2', tier='stretch', no='T2', type='number', skill='counting in a repeating pattern', answer=10,
      q='Pattern: circle, triangle, triangle, square, circle, triangle, triangle, square ... How many triangles are in the first 20 shapes?',
      check=lambda: sum(1 for x in repeat(CTTS, 20) if x == 'triangle'),
      hint='How many triangles are in one set? How many sets fit into 20 shapes?',
      steps=['One set is circle, triangle, triangle, square, so it has 2 triangles.', 'Count the sets in 4s: 4, 8, 12, 16, 20. That is 5 sets.', 'Count the triangles in 2s: 2, 4, 6, 8, 10. There are 10 triangles.'],
      src=['Same pattern: how many triangles are in the first 20 shapes?']),
    D(id='T3', tier='stretch', no='T3', type='choice', skill='repeating patterns', options=['Red', 'Blue'], answer='Blue',
      q='Red, blue, blue, red, blue, blue ... What colour is the 20th bead?', svg=pattern_row(repeat(RBB, 6), caption='Beads red, blue, blue, red, blue, blue, places 1 to 6'),
      check=lambda: name(at(RBB, 20)),
      hint='Find the set that repeats. Which places finish a set?',
      steps=['The set is red, blue, blue (3 beads).', 'Places 3, 6, 9, 12, 15 and 18 finish a set. Place 19 is red.', 'Place 20 is the next bead in the set: blue.'],
      src=['Red, blue, blue, red, blue, blue … What colour is the 20th bead?']),
    D(id='T4', tier='stretch', no='T4', type='fields', skill='growing patterns', answer=[6, 1],
      q='Squares in a row need 4, 7, 10, ... sticks. With 20 sticks, how many squares can you make? How many sticks are left over?', frame='Squares: {f1}      Sticks\u00a0left\u00a0over: {f2}',
      svg=square_rows(), check=lambda: list(most_with(square_sticks, 20)),
      hint='Write the stick numbers: 4, 7, 10 ... Keep going and stop before you pass 20.',
      steps=['The sticks needed are 4, 7, 10, 13, 16, 19, 22 ...', '6 squares need 19 sticks. 7 squares need 22, which is too many.', '20 - 19 = 1, so 1 stick is left over.'],
      src=['Squares in a row need 4, 7, 10, … sticks. With 20 sticks, how many squares can you make? How many sticks are left over?']),

    # ================= Go further
    D(id='C1', tier='challenge', no='C1', type='number', skill='counting in a repeating pattern', answer=9,
      q='Beads repeat in a pattern of 5: red, red, blue, blue, green. How many green beads are in the first 47 beads?',
      check=lambda: sum(1 for x in repeat(FIVE, 47) if x == 'green'),
      hint='Which bead in each set of 5 is green? Which places do the green beads have?',
      steps=['Green is the 5th bead of each set, so the green beads are at places 5, 10, 15, ... 45 (count in 5s).', '5, 10, 15, 20, 25, 30, 35, 40, 45 is 9 numbers.', 'Beads 46 and 47 are red, so there are 9 green beads.'],
      src=['Beads repeat in a pattern of 5: red, red, blue, blue, green. How many green beads are in the first 47 beads?']),
    D(id='C2', tier='challenge', no='C2', type='fields', skill='growing patterns', answer=[21, 28, 55],
      q='Dots: 1, 3, 6, 10, 15 ... What are the next two numbers? What is the 10th number?', frame='Next\u00a0two\u00a0numbers: {f1}, {f2}.   The\u00a010th\u00a0number: {f3}',
      svg=dot_triangles(), check=lambda: [triangular(6), triangular(7), triangular(10)],
      hint='Look at how much each number grows: 1 to 3, 3 to 6, 6 to 10. What do you notice about the growing?',
      steps=['The numbers grow by 2, then 3, then 4, then 5. So they grow by 6, then 7.', '15 + 6 = 21 and 21 + 7 = 28.', 'Keep going: 28 + 8 = 36, 36 + 9 = 45, 45 + 10 = 55. The 10th number is 55.'],
      src=['Dots: 1, 3, 6, 10, 15 … What are the next two numbers? What is the 10th number?']),
    D(id='C3', tier='challenge', no='C3', type='selfcheck', paper=True, skill='repeating patterns',
      q='Make up your own repeating pattern with a set of 5 beads (use up to 3 colours). Ask a friend or a grown-up: what colour is the 33rd bead? Write the answer and how you know.',
      facts='green', check=lambda: at(EXAMPLE5, 33), sol_fig=lambda f: example_beads_fig(f),
      hint='Which places finish a set of 5? How far past one of those places is 33?',
      steps=['Here is one example: red, green, green, blue, red, then the same five again and again.', 'Count in 5s: 5, 10, 15, 20, 25, 30. Place 30 finishes a set.', 'Place 33 is 3 beads after place 30, so it is bead 3 of the set: green in this example. Your own pattern gives its own answer.'],
      src=['Make up your own repeating pattern with a core of 5 beads (use up to 3 colours). Ask a partner: what colour is the 33rd bead? Write the answer and how you know.']),
]


def _oracle_triangles(e):
    return sum(1 for x in repeat(CTTS, e['n']) if x == 'triangle')


def _oracle_greens(e):
    return sum(1 for x in repeat(FIVE, e['n']) if x == 'green')


VARIANTS = {
    'T2': dict(
        base=dict(n=20),
        tpl=dict(vars=dict(n=[8, 12, 16, 20, 24, 28, 32]),
                 q='Pattern: circle, triangle, triangle, square, circle, triangle, triangle, square ... How many triangles are in the first {n} shapes?',
                 answer='n/2', derive=dict(s='n/4'),
                 hint='How many triangles are in one set? How many sets fit into {n} shapes?',
                 steps=['One set is circle, triangle, triangle, square, so it has 2 triangles.', '{n} shapes is {s} sets, because 4 shapes make a set.', '{s} sets of 2 triangles is {ans} triangles.']),
        oracle=_oracle_triangles),
    'C1': dict(
        base=dict(n=47),
        tpl=dict(vars=dict(n=[23, 31, 36, 42, 47, 53, 58, 64]),
                 q='Beads repeat in a pattern of 5: red, red, blue, blue, green. How many green beads are in the first {n} beads?',
                 answer='n//5',
                 hint='Which bead in each set of 5 is green? Which places do the green beads have?',
                 steps=['Green is the 5th bead of each set, so the green beads are at places 5, 10, 15 ... (count in 5s).', 'Count in 5s as far as you can without going over {n}.', 'There are {ans} green beads.']),
        oracle=_oracle_greens),
    'T4': dict(
        base=dict(s=20),
        tpl=dict(vars=dict(s=[13, 16, 20, 23, 25, 28, 31, 34, 38]),
                 q='Squares in a row need 4, 7, 10, ... sticks. With {s} sticks, how many squares can you make? How many sticks are left over?', frame='Squares: {f1}      Sticks\u00a0left\u00a0over: {f2}',
                 answers=dict(f1='(s-1)//3', f2='(s-1)%3'),
                 hint='Write the stick numbers: 4, 7, 10 ... Keep going and stop before you pass {s}.',
                 steps=['The sticks needed are 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40 ...', 'Stop at the last number that is not more than {s}.', 'The answers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), most_with(square_sticks, e['s'])))),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and not _d.get('open'):
        _d['marking_mode'] = 'self'

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Wonder',
    'A pattern goes circle, square, circle, square, ... Write a question of your own that starts with "What if ...?" about this pattern. You do not need to answer it.',
    ['Many questions are good. A good "What if" changes one thing about the pattern.', 'For example: What if I put a triangle after every square? What if the pattern had three shapes that repeat? What would the 10th shape be?'],
    'Change one thing: the shapes, the order, or how long the pattern is. Then ask what happens.'))
