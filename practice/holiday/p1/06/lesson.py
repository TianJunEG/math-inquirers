"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 6: Money ("Coin combos").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 6, Q1 to Q6; hp/qbank.json lesson 6 stretch[0:4] for Think harder and challenge[-3:] for Go
further, as the workbook builder slices them; hp/gaps.json lesson 6 for the Investigation and for the extra Think harder T5, Dollars).  Every answer is recomputed by an
independent checker that tries every combination of coins (loops over how many of each coin), never a formula.  The build stops if a checker and the printed answer (Tutor
Guide answer key) differ.  No coin or note pictures: coins are written as words and numbers (5¢, 10¢, 20¢, 50¢).
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=6, key='p1', title='Coin combos', workbook_title='COIN COMBOS', topic='Money',
            strand='Money',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['We have 5¢, 10¢, 20¢ and 50¢ coins. You can use the same kind of coin more than once.',
                   'The same coins in a different order are the same way. Use play coins, or draw the coins on paper, if you like.'])

S = 'Money'
COINS3 = (20, 10, 5)
COINS4 = (50, 20, 10, 5)


def D(**k):
    return dict(strand=S, **k)


# ---- independent checkers: try every number of each coin
def ways(amount, coins):
    """Every way to pay `amount` with `coins`: the tuple says how many of each coin (same order as coins). The biggest coin's count is listed from most to fewest."""
    out = []
    for counts in itertools.product(*[range(amount // c + 1) for c in coins]):
        if sum(n * c for n, c in zip(counts, coins)) == amount:
            out.append(counts)
    return sorted(out, reverse=True)


def pieces(w):
    return sum(w)


def fewest(amount, coins):
    """The ways that use the fewest coins."""
    ws = ways(amount, coins)
    m = min(pieces(w) for w in ws)
    return [w for w in ws if pieces(w) == m]


def most(amount, coins):
    ws = ways(amount, coins)
    m = max(pieces(w) for w in ws)
    return [w for w in ws if pieces(w) == m]


def values(w, coins):
    """The coins of a way written out one by one, biggest first: (1, 0, 2) with (20, 10, 5) -> [20, 5, 5]."""
    out = []
    for n, c in zip(w, coins):
        out += [c] * n
    return out


def words(w, coins):
    return ' + '.join(f'{c}¢' for c in values(w, coins))


def makeable(amount, coins):
    return bool(ways(amount, coins))


def subset_amounts(coins):
    """Every different non-zero amount made by using any of the coins once each."""
    seen = set()
    for pick in itertools.product((0, 1), repeat=len(coins)):
        if any(pick):
            seen.add(sum(p * c for p, c in zip(pick, coins)))
    return seen


def two_coin_totals(coins):
    return sorted({a + b for a in coins for b in coins})


def fmt_ways(ws, coins):
    return ';  '.join(words(w, coins) for w in ws)


ITEMS = [
    # ================= Start here
    D(id='1', tier='core', no='1', label='1', type='selfcheck', open=False, marking_mode='self', skill='listing the ways',
      q='Show the different ways to make exactly 20¢ using only 20¢, 10¢ and 5¢ coins. Write each way, with how many of each coin.',
      check=lambda: ways(20, COINS3), sol_fig=lambda f: ways_table(f, COINS3, 'The ways to make 20 cents with 20, 10 and 5 cent coins'),
      hint='Start with the biggest coin that fits. Then change one coin at a time. Do not list the same coins twice in a different order.',
      steps=['Start with the biggest coin and work down, so no way is missed or repeated.', 'The ways are: ' + fmt_ways(ways(20, COINS3), COINS3) + '.', 'There are ' + str(len(ways(20, COINS3))) + ' ways. Yours may be in a different order.'],
      src=['Show different ways to make exactly 20¢ using only 20¢, 10¢ and 5¢ coins. Write how many of each coin in the table.']),
    D(id='1a', tier='core', no='1(a)', type='set', ordered=False, skill='fewest coins', answer=[20],
      q='Of all the ways to make 20¢ with 20¢, 10¢ and 5¢ coins, which way uses the FEWEST coins? Type the coins it uses, like 10 + 5 for 15¢.',
      check=lambda: values(fewest(20, COINS3)[0], COINS3) if len(fewest(20, COINS3)) == 1 else None,
      hint='Think of the ways to make 20¢. Count the coins in each way. Which way has the fewest?',
      steps=['Try the ways: one 20¢ coin is 1 coin. The other ways use 2, 3 or 4 coins.', 'The fewest is 1 coin.', 'The way is one 20¢ coin.'],
      src=['Which way uses the FEWEST coins?']),
    D(id='1b', tier='core', no='1(b)', type='set', ordered=False, skill='most coins', answer=[5, 5, 5, 5],
      q='Of all the ways to make 20¢ with 20¢, 10¢ and 5¢ coins, which way uses the MOST coins? Type every coin it uses, like 10 + 5 for 15¢.',
      check=lambda: values(most(20, COINS3)[0], COINS3) if len(most(20, COINS3)) == 1 else None,
      hint='Think of the ways to make 20¢. Count the coins in each way. Which way has the most?',
      steps=['Count the coins in each way: 1, 2, 3 and 4 coins.', 'The most is 4 coins.', 'The way is 5¢ + 5¢ + 5¢ + 5¢.'],
      src=['Which way uses the MOST coins?']),
    D(id='1c', tier='core', no='1(c)', type='selfcheck', open=False, marking_mode='self', skill='knowing you have all the ways',
      q='How do you know you have found ALL the ways to make 20¢?', check=lambda: len(ways(20, COINS3)),
      hint='How did you decide which way to write first? Did you change one coin each time?',
      steps=['Start with the biggest coin that fits. Find every way that uses it.', 'Then take that coin away and do the same with the next coin. Use a table so you do not repeat a way.', 'When there are no coins left to try, there are no more ways. Any answer like this is good.'],
      src=['How do you know you have found ALL the ways?']),

    D(id='2', tier='core', no='2', label='2', type='selfcheck', open=False, marking_mode='self', skill='listing the ways',
      q='Find ALL the ways to make 25¢ using 20¢, 10¢ and 5¢ coins. Start with the biggest coin. Write each way with + signs, like 10¢ + 5¢. (Hint: there are 4 ways.)',
      check=lambda: ways(25, COINS3), sol_fig=lambda f: ways_table(f, COINS3, 'The ways to make 25 cents with 20, 10 and 5 cent coins'),
      hint='Make a table with a column for each coin. Begin with the biggest coin, then work down.',
      steps=['With a 20¢ coin: the 5¢ left needs one 5¢ coin.', 'With no 20¢ coin but 10¢ coins, then with only 5¢ coins: keep going down.', 'The ways are: ' + fmt_ways(ways(25, COINS3), COINS3) + '. That is ' + str(len(ways(25, COINS3))) + ' ways.'],
      src=['Find ALL the ways to make 25¢ using 20¢, 10¢ and 5¢ coins. Start with the biggest coin.', '(Hint: there are 4 ways.)']),

    D(id='3a', tier='core', no='3(a) coins', label='3(a) coins', type='number', skill='fewest coins', answer=4,
      q='Mei wants to pay exactly 85¢ using 5¢, 10¢, 20¢ and 50¢ coins. What is the smallest number of coins she can use?', check=lambda: pieces(fewest(85, COINS4)[0]),
      hint='Use the big coins first. Which big coins fit into 85¢ without going over?',
      steps=['Try the 50¢ coin first, then the 20¢, then the 10¢, then the 5¢.', '50¢ + 20¢ = 70¢, then 10¢ makes 80¢, and 5¢ makes 85¢.', 'That is 4 coins. No way with fewer coins makes 85¢.'],
      src=['Mei wants to pay exactly 85¢ using 5¢, 10¢, 20¢ and 50¢ coins.', 'What is the smallest number of coins she can use? Which coins are they?']),
    D(id='3b', tier='core', no='3(a) which', label='3(a) which', type='set', ordered=False, skill='fewest coins', answer=[50, 20, 10, 5],
      q='Mei pays exactly 85¢ with 5¢, 10¢, 20¢ and 50¢ coins, using the smallest number of coins. Which coins does she use? Type their values with commas.',
      check=lambda: values(fewest(85, COINS4)[0], COINS4) if len(fewest(85, COINS4)) == 1 else None,
      hint='Use the biggest coin that fits first. Then the next biggest, and so on, until you reach 85¢.',
      steps=['Take the 50¢ coin: 85¢ - 50¢ = 35¢ left.', 'Take the 20¢ coin: 35¢ - 20¢ = 15¢ left. Take the 10¢ coin: 5¢ left. Take the 5¢ coin.', 'The coins are 50¢, 20¢, 10¢ and 5¢. They are the only coins that give the smallest number.'],
      src=['What is the smallest number of coins she can use? Which coins are they?']),
    D(id='3c', tier='core', no='3(b)', label='3(b)', type='selfcheck', open=False, marking_mode='self', skill='different ways to pay',
      q='If you have time: Mei pays exactly 85¢ a different way, using exactly 6 coins. Which coins could she use? Use 5¢, 10¢, 20¢ and 50¢.',
      check=lambda: [w for w in ways(85, COINS4) if pieces(w) == 6],
      hint='Try using some smaller coins. Add the coins up to check you reach exactly 85¢. Then count them.',
      steps=['Many answers are right. Here is one: 50¢ + 10¢ + 10¢ + 5¢ + 5¢ + 5¢ = 85¢ and it is 6 coins.', 'Another one: 20¢ + 20¢ + 20¢ + 10¢ + 10¢ + 5¢ = 85¢ and it is 6 coins.', 'To check yours: the coins must add to 85¢ and there must be exactly 6 of them.'],
      src=['If you have time: find a different way that uses exactly 6 coins.']),

    D(id='4a', tier='core', no='4(a)', type='choice', skill='reasoning about two coins', options=['Yes', 'No'], answer='No',
      q='Can Ben make 35¢ using only 2 coins? He has 5¢, 10¢, 20¢ and 50¢ coins.', check=lambda: 'Yes' if 35 in two_coin_totals(COINS4) else 'No',
      hint='Try the pairs of coins. Add each pair. Does any pair make 35¢?',
      steps=['The pairs of coins make: ' + ', '.join(f'{t}¢' for t in two_coin_totals(COINS4)) + '.', '35¢ is not in the list.', 'No, Ben cannot make 35¢ with only 2 coins.'],
      src=['Can Ben make 35¢ using only 2 coins?']),
    D(id='4b', tier='core', no='4(b)', type='selfcheck', open=False, marking_mode='self', skill='explaining',
      q='Ben has 5¢, 10¢, 20¢ and 50¢ coins. Explain how you know whether he can make 35¢ with only 2 coins.', check=lambda: two_coin_totals(COINS4),
      hint='List the pairs of coins and add each pair. Look at your list.',
      steps=['Add every pair: 5¢ + 5¢ = 10¢, 5¢ + 10¢ = 15¢, 5¢ + 20¢ = 25¢, 5¢ + 50¢ = 55¢, 10¢ + 10¢ = 20¢, 10¢ + 20¢ = 30¢, 10¢ + 50¢ = 60¢, 20¢ + 20¢ = 40¢, 20¢ + 50¢ = 70¢, 50¢ + 50¢ = 100¢.',
             'None of the pairs makes 35¢. For 35¢ you would need 5¢ + 30¢, 10¢ + 25¢ or 20¢ + 15¢, and there is no 30¢, 25¢ or 15¢ coin.', 'Any answer that tries the pairs and finds that none makes 35¢ is good.'],
      src=['Explain your answer.']),
    D(id='5', tier='core', no='5', label='5', type='text', accept=['35', '35¢', '35 ¢', '35 cents', '35 cent', '35c', '35 c'], shown='35¢', skill='adding coins',
      q='Ali has a 20¢ coin, a 10¢ coin and a 5¢ coin. How much money does he have?', check=lambda: str(20 + 10 + 5),
      hint='Add the three coins. Add the two bigger coins first if it helps.',
      steps=['Ali has 20¢, 10¢ and 5¢.', '20¢ + 10¢ = 30¢, then 30¢ + 5¢ = 35¢.', 'Ali has 35¢.'],
      src=['Ali has a 20¢ coin, a 10¢ coin and a 5¢ coin. How much money does he have?']),
    D(id='6', tier='core', no='6', label='6', type='text', accept=['45', '45¢', '45 ¢', '45 cents', '45 cent', '45c', '45 c'], shown='45¢', skill='adding coins',
      q='Mei has two 20¢ coins and one 5¢ coin. How much money does she have?', check=lambda: str(20 + 20 + 5),
      hint='Add the two 20¢ coins first. Then add the 5¢ coin.',
      steps=['Mei has 20¢ and 20¢ and 5¢.', '20¢ + 20¢ = 40¢, then 40¢ + 5¢ = 45¢.', 'Mei has 45¢.'],
      src=['Mei has two 20¢ coins and one 5¢ coin. How much money does she have?']),

    # ================= Investigation
    D(id='I1', tier='invest', no='Investigation 1', type='set', ordered=False, skill='what if a coin is missing', answer=[10, 20],
      q='Put the 5¢ coin away. Now you have only 10¢, 20¢ and 50¢ coins. Which of 10¢, 20¢ and 15¢ can you make? Type the ones you can make.',
      check=lambda: [a for a in (10, 20, 15) if makeable(a, (50, 20, 10))],
      hint='Try to make each amount with the coins you still have. Write down which ones work.',
      steps=['10¢ is one 10¢ coin, and 20¢ is one 20¢ coin (or two 10¢ coins).', '15¢ needs a coin that ends in 5, and there is none now. Every coin you have is worth a number of tens.', 'You can make 10¢ and 20¢, but not 15¢.'],
      src=['Put the 5¢ coin away.', 'Use your coins to make 10¢, then 20¢, then 15¢.']),
    D(id='I2', tier='invest', no='Investigation 2', type='set', ordered=False, skill='what if a coin is missing', answer=[5, 15, 25, 35, 45],
      q='Use only the 10¢, 20¢ and 50¢ coins. Which amounts from 5¢ to 50¢ (5¢, 10¢, 15¢ ... 50¢) can you NOT make? Type them with commas.',
      check=lambda: [a for a in range(5, 51, 5) if not makeable(a, (50, 20, 10))],
      hint='Write the amounts 5¢, 10¢, 15¢ ... 50¢. Try to make each one. Which ones do not work?',
      steps=['You can make 10¢, 20¢, 30¢, 40¢ and 50¢ with these coins.', 'You cannot make 5¢, 15¢, 25¢, 35¢ or 45¢.', 'The amounts you cannot make are 5, 15, 25, 35 and 45.'],
      src=['Which amounts from 5¢ to 50¢ (5¢, 10¢, 15¢ ... 50¢) can you NOT make with the 10¢, 20¢ and 50¢ coins?']),
    D(id='I3', tier='invest', no='Investigation 3', type='selfcheck', open=False, marking_mode='self', skill='explaining a pattern',
      q='Look at the amounts you cannot make with the 10¢, 20¢ and 50¢ coins. What do they have in common? Why?',
      check=lambda: (sorted({a % 10 for a in range(5, 51, 5) if not makeable(a, (50, 20, 10))}), sorted({c % 10 for c in (50, 20, 10)})),
      hint='Look at the last digit of each amount you cannot make. Then look at the last digit of each coin you have.',
      steps=['The amounts you cannot make are 5, 15, 25, 35 and 45. They all end in 5.', 'The coins 10¢, 20¢ and 50¢ all end in 0, so any total of them ends in 0.', 'So an amount that ends in 5 can never be made. Any answer about the last digit is good.'],
      src=['What do those amounts have in common? Why?']),

    # ================= Think harder
    D(id='T1a', tier='stretch', no='T1', label='T1 list', type='selfcheck', open=False, marking_mode='self', skill='listing the ways',
      q='Make 70¢ using exactly 4 coins from 5¢, 10¢, 20¢ and 50¢. Find every set of 4 coins that works. Write each set.',
      check=lambda: [w for w in ways(70, COINS4) if pieces(w) == 4], sol_fig=lambda f: ways_table(f, COINS4, 'The sets of 4 coins that make 70 cents'),
      hint='The coins must add up to 70¢. Start with the 50¢ coin. Then try with no 50¢ coin.',
      steps=['Try a 50¢ coin: 20¢ is left for 3 coins. Only 10¢ + 5¢ + 5¢ works.', 'Try no 50¢ coin: 3 coins of 20¢ make 60¢, and a 10¢ coin makes 70¢.', 'The sets are: ' + fmt_ways([w for w in ways(70, COINS4) if pieces(w) == 4], COINS4) + '.'],
      src=['Make 70¢ using exactly 4 coins from 5¢, 10¢, 20¢ and 50¢. Find every set.']),
    D(id='T1b', tier='stretch', no='T1 how many', label='T1 how many', type='number', skill='listing the ways', answer=2,
      q='How many different sets of exactly 4 coins make 70¢? Use 5¢, 10¢, 20¢ and 50¢ coins.', check=lambda: len([w for w in ways(70, COINS4) if pieces(w) == 4]),
      hint='Find every set of 4 coins that adds up to 70¢. Then count them.',
      steps=['Check each way to make 70¢ and keep the ones with exactly 4 coins.', 'The sets are ' + fmt_ways([w for w in ways(70, COINS4) if pieces(w) == 4], COINS4) + '.', 'There are 2 sets.'],
      src=['Find every set.']),
    D(id='T2', tier='stretch', no='T2', type='fields', skill='two kinds of coin', answer=[3, 3],
      q='Sam has only 10¢ and 20¢ coins. He pays exactly 90¢ using 6 coins. How many of each coin does he use?', frame='Number of 10¢ coins: {f1}      Number of 20¢ coins: {f2}',
      check=lambda: [list(p) for p in itertools.product(range(7), repeat=2) if sum(p) == 6 and p[0] * 10 + p[1] * 20 == 90][0],
      hint='Try some numbers of each coin that make 6 coins. Add up the money. Is it 90¢?',
      steps=['The coins must add to 90¢, and there are 6 of them.', 'Try 3 coins of 10¢ and 3 coins of 20¢: 30¢ + 60¢ = 90¢.', 'Sam uses three 10¢ coins and three 20¢ coins.'],
      src=['Sam has only 10¢ and 20¢ coins. He pays exactly 90¢ using 6 coins. How many of each coin does he use?']),
    D(id='T3', tier='stretch', no='T3', type='number', skill='fewest coins', answer=3,
      q='What is the fewest number of coins to make 45¢? Use 5¢, 10¢, 20¢ and 50¢ coins.', check=lambda: pieces(fewest(45, COINS4)[0]),
      hint='Use the biggest coins that fit first. Can you do it with fewer coins by changing a coin?',
      steps=['The 50¢ coin is too big. Take two 20¢ coins: 40¢.', '45¢ - 40¢ = 5¢, so one 5¢ coin.', '20¢ + 20¢ + 5¢ is 3 coins. No way with 2 coins makes 45¢.'],
      src=['What is the fewest number of coins to make 45¢?']),
    D(id='T4a', tier='stretch', no='T4 list', label='T4 list', type='selfcheck', open=False, marking_mode='self', skill='listing the ways',
      q='Find ALL the ways to make 30¢ using 20¢, 10¢ and 5¢ coins. Write each way. Then say how you know you have found them all.',
      check=lambda: ways(30, COINS3), sol_fig=lambda f: ways_table(f, COINS3, 'The ways to make 30 cents with 20, 10 and 5 cent coins'),
      hint='Start with the biggest coin that fits. Then change one coin at a time. A table can show that no way is missing.',
      steps=['Start with the biggest coin and work down.', 'The ways are: ' + fmt_ways(ways(30, COINS3), COINS3) + '.', 'You know you have them all because you took each choice of the biggest coin in turn and did not repeat a way.'],
      src=['Find ALL the ways to make 30¢ using 20¢, 10¢ and 5¢ coins.', 'How do you know you have found them all?']),
    D(id='T4b', tier='stretch', no='T4 how many', label='T4 how many', type='number', skill='listing the ways', answer=6,
      q='How many different ways are there to make 30¢ using 20¢, 10¢ and 5¢ coins?', check=lambda: len(ways(30, COINS3)),
      hint='List the ways in order, starting with the biggest coin. Count them. Do not count the same coins twice.',
      steps=['The ways are ' + fmt_ways(ways(30, COINS3), COINS3) + '.', 'Count them: ' + str(len(ways(30, COINS3))) + ' ways.'],
      src=['Find ALL the ways to make 30¢ using 20¢, 10¢ and 5¢ coins.']),
    D(id='T5a', tier='stretch', no='T5(a)', label='T5(a)', type='set', ordered=False, skill='dollars', answer=[10, 5, 2],
      q='Dollars! We also have $1 coins and $2, $5, $10 and $50 notes. A toy costs $17. Pay exactly with the fewest notes and coins. Type the value of each one, with commas.',
      check=lambda: values(min(ways(17, (50, 10, 5, 2, 1)), key=pieces), (50, 10, 5, 2, 1)) if len(fewest(17, (50, 10, 5, 2, 1))) == 1 else None,
      hint='Use the biggest note or coin that fits first. Then the next biggest.',
      steps=['The $50 note is too big. Take a $10 note: $7 left.', 'Take a $5 note: $2 left. Take a $2 note.', '$10 + $5 + $2 = $17, and it is 3 pieces. That is the fewest.'],
      src=['A toy costs $17. Pay exactly with the fewest notes and coins.', 'Dollars! We also have $1 coins and $2, $5, $10 and $50 notes.']),
    D(id='T5b', tier='stretch', no='T5(b)', label='T5(b)', type='choice', skill='dollars', options=['Yes', 'No'], answer='No',
      q='Mei has one $50 note and two $10 notes. A bicycle costs $65 and a helmet costs $8. Does she have enough money for both?',
      check=lambda: 'Yes' if 50 + 10 + 10 >= 65 + 8 else 'No',
      hint='Add up the money Mei has. Then add up what the bicycle and the helmet cost.',
      steps=['Mei has $50 + $10 + $10 = $70.', 'The bicycle and helmet cost $65 + $8 = $73.', '$70 is less than $73, so she does not have enough. She is $3 short.'],
      src=['Mei has one $50 note and two $10 notes. A bicycle costs $65 and a helmet costs $8. Does she have enough money for both? Explain.']),
    D(id='T5c', tier='stretch', no='T5(b) why', label='T5(b) why', type='selfcheck', open=False, marking_mode='self', skill='explaining',
      q='Mei has one $50 note and two $10 notes. A bicycle costs $65 and a helmet costs $8. Explain how you know whether she has enough money for both.',
      check=lambda: (50 + 10 + 10, 65 + 8),
      hint='Say how much money Mei has. Say how much she needs. Which is more?',
      steps=['Mei has $50 + $10 + $10 = $70.', 'She needs $65 + $8 = $73 for both.', 'She has less than she needs, so she is $3 short. Any answer that compares what she has with what she needs is good.'],
      src=['Does she have enough money for both? Explain.']),

    # ================= Go further
    D(id='C1', tier='challenge', no='Go further 1', label='G1', type='fields', skill='different amounts', answer=[15, 31],
      q='You have one 5¢, one 10¢, one 20¢ and one 50¢ coin. How many different amounts can you make using any of them? What if you also had a $1 coin (100¢)?',
      frame='With the 4 coins: {f1} amounts      With the $1 coin too: {f2} amounts', check=lambda: [len(subset_amounts((5, 10, 20, 50))), len(subset_amounts((5, 10, 20, 50, 100)))],
      hint='List the amounts with 1 coin, then with 2 coins, then with 3 coins, then with all 4. Are any amounts the same?',
      steps=['With 1 coin: 5¢, 10¢, 20¢, 50¢ (4 amounts). With 2 coins: 15¢, 25¢, 55¢, 30¢, 60¢, 70¢ (6 amounts).', 'With 3 coins: 35¢, 65¢, 75¢, 80¢ (4 amounts). With all 4 coins: 85¢ (1 amount). That is 4 + 6 + 4 + 1 = 15.',
             'The $1 coin makes 100¢ by itself, and 100¢ plus each of those 15 amounts. 15 + 1 + 15 = 31.'],
      src=['You have one 5¢, one 10¢, one 20¢ and one 50¢ coin. How many different amounts can you make using any of them? What if you also had a $1 coin (100¢)?']),
    D(id='C2', tier='challenge', no='Go further 2', label='G2', type='fields', skill='two prices', answer=[2, 3],
      q='A sweet costs 15¢ and a biscuit costs 20¢. Ben spends exactly 90¢ and buys some of each. How many sweets and how many biscuits does he buy?', frame='Sweets: {f1}      Biscuits: {f2}',
      check=lambda: (lambda sols: list(sols[0]) if len(sols) == 1 else None)([(s, b) for s in range(1, 7) for b in range(1, 5) if 15 * s + 20 * b == 90]),
      hint='Try 1 sweet, then 2 sweets, and so on. How much is left for biscuits? Does it make a whole number of biscuits?',
      steps=['Try 2 sweets: 2 × 15¢ = 30¢, so 60¢ is left for biscuits. 3 biscuits cost 3 × 20¢ = 60¢.', 'That makes exactly 90¢ with some of each.', 'Ben buys 2 sweets and 3 biscuits. No other choice works when he buys some of each.'],
      src=['A sweet costs 15¢ and a biscuit costs 20¢. Ben spends exactly 90¢ and buys some of each. How many sweets and biscuits does he buy?']),
    D(id='C3', tier='challenge', no='Go further 3', label='G3', type='selfcheck', open=True, marking_mode='open', skill='making up a puzzle',
      q='Make up your own coin puzzle that has exactly ONE answer (for example: "exactly 3 coins that make 35¢"). Write it, swap with a partner and check their answer by listing every possibility.',
      hint='Pick the coins first, then write the puzzle. Try every possibility to be sure there is only one answer.',
      steps=['Here is one example: "exactly 2 coins that make 60¢" with 5¢, 10¢, 20¢ and 50¢ coins.', 'List every pair: only 50¢ + 10¢ makes 60¢, so there is exactly one answer.', 'Your own puzzle needs exactly one answer. Check it by listing every possibility.'],
      src=['Make up your own coin puzzle that has exactly ONE answer (for example: "exactly 3 coins that make 35¢").']),
]

# the worked example of C3 is only true if the puzzle really has exactly one answer
assert [w for w in ways(60, COINS4) if pieces(w) == 2] == [(1, 0, 1, 0)], 'C3 example must have exactly one answer'


def _fewest_oracle(e):
    return pieces(fewest(e['n'], COINS4)[0])


VARIANTS = {
    '3a': dict(base=dict(n=85),
               tpl=dict(vars=dict(n=[35, 40, 45, 55, 65, 70, 75, 85, 90, 95]),
                        q='Mei wants to pay exactly {n}¢ using 5¢, 10¢, 20¢ and 50¢ coins. What is the smallest number of coins she can use?',
                        derive=dict(a='n//50', r1='n%50', b='r1//20', r2='r1%20', c='r2//10', r3='r2%10', d='r3//5'), answer='a+b+c+d',
                        hint='Use the big coins first. Which big coins fit into {n}¢ without going over?',
                        steps=['Take the biggest coin that fits, then the next biggest, and so on until you reach {n}¢.', 'Count the coins you took.', 'The smallest number of coins is {ans}.']),
               oracle=_fewest_oracle),
    'T3': dict(base=dict(n=45),
               tpl=dict(vars=dict(n=[35, 40, 55, 60, 65, 70, 75, 85, 95]),
                        q='What is the fewest number of coins to make {n}¢? Use 5¢, 10¢, 20¢ and 50¢ coins.',
                        derive=dict(a='n//50', r1='n%50', b='r1//20', r2='r1%20', c='r2//10', r3='r2%10', d='r3//5'), answer='a+b+c+d',
                        hint='Use the biggest coins that fit first. Can you do it with fewer coins by changing a coin?',
                        steps=['Take the biggest coin that fits, then the next biggest, and so on until you reach {n}¢.', 'Count the coins you took.', 'The fewest number of coins is {ans}.']),
               oracle=_fewest_oracle),
    'T2': dict(base=dict(t=90, k=6),
               tpl=dict(vars=dict(t=[80, 90, 100], k=[6, 7]),
                        q='Sam has only 10¢ and 20¢ coins. He pays exactly {t}¢ using {k} coins. How many of each coin does he use?', frame='Number of 10¢ coins: {f1}      Number of 20¢ coins: {f2}',
                        derive=dict(m='t//10'), answers=dict(f1='2*k-m', f2='m-k'),
                        hint='Try some numbers of each coin that make {k} coins. Add up the money. Is it {t}¢?',
                        steps=['The coins must add to {t}¢, and there are {k} of them.', 'Try different numbers of 10¢ and 20¢ coins that make {k} coins altogether.', 'The answers are {ans}.']),
               oracle=lambda e: dict(zip(('f1', 'f2'), [list(p) for p in itertools.product(range(e['k'] + 1), repeat=2) if sum(p) == e['k'] and p[0] * 10 + p[1] * 20 == e['t']][0]))),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and not _d.get('open') and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
