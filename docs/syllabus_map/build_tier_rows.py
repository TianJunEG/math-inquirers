#!/usr/bin/env python3
"""Write tier_rows.json: how Start here / Think harder / Go further relate to the school syllabus, per level.

Evidence, not invention (all year placements checked against the MOE syllabus PDF, Oct 2025, see docs/moe/):
  * item counts: pN/content/lN.js qbank (L2-L6) and hp/qbank.json (L1)
  * where each tier goes beyond the syllabus: docs/audit/moe_alignment_p1_p3.md (lesson tables, exceptions
    column, Levels 1-3) and docs/audit/moe_alignment_p4_p6.md (lesson tables + section 3 item lists, Levels 4-6)
  * the other countries' view: docs/audit/intl_mapping_*.md (only used for the "other places" remark, via intl_rows.json)
rating: AT = at the school year; NEW = school-year ideas in unfamiliar settings, with a few previews;
        AHEAD = reaches into later years or topics the primary syllabus does not name; MIX = a mixture.
confidence: good = lesson-by-lesson exceptions listed by tier in the audit; some = exceptions listed by item
            but no per-tier verdict; thin = tiers not audited separately.
"""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
T = ['Start here', 'Think harder', 'Go further']
AGES = {1: 'ages 6 to 8', 2: 'ages 7 to 9', 3: 'ages 8 to 10', 4: 'ages 9 to 11', 5: 'ages 10 to 12', 6: 'ages 11 to 13'}
YEAR = {1: 'Primary 1', 2: 'Primary 2', 3: 'Primary 3', 4: 'Primary 4', 5: 'Primary 5', 6: 'Primary 6'}
ITEMS = {1: (74, 102, 58), 2: (60, 87, 90), 3: (60, 84, 90), 4: (60, 89, 90), 5: (60, 89, 90), 6: (60, 80, 90)}
CONF = {1: 'good', 2: 'good', 3: 'good', 4: 'some', 5: 'some', 6: 'thin'}  # years for 4-6 now confirmed against the syllabus PDF
# (rating, headline, detail, evidence)
C = {
 1: [('AT', 'At the Primary 1 level',
      'Almost all use Primary 1 skills: skip counting, number bonds, coins, 2D shapes, centimetres.',
      'Audit: Core items are "almost all ON-level or consolidation".'),
     ('NEW', 'Same ideas, new settings, a few previews',
      'Numbers that two counts share (Primary 4), picture graphs where one picture stands for 2 (Primary 2), a letter for a missing number (Primary 6), places past 10th.',
      'Audit lists these as Primary 2 to 6 ideas in Think harder items (lessons 1 to 4).'),
     ('AHEAD', 'Reaches past Primary 1',
      'Growing number patterns, "how many ways" puzzles, comparison problems and logic orderings that the syllabus does not name.',
      'Audit: Go further items in lessons 1, 2, 4, 5, 8, 9, 10 (and shared multiples again in 10).')],
 2: [('AT', 'At the Primary 2 level, with some early letters',
      'Numbers to 1000, add and subtract, tables of 2 to 10, fractions, money. A few Start here items use a letter for a missing digit.',
      'Audit: lesson 2 Core uses A and B for digits (a Primary 6 idea); lesson 3 has sharing with leftovers.'),
     ('NEW', 'Primary 2 ideas, plus previews',
      'Remainders (Primary 3), fraction of a set (Primary 4), finding a start time (Primary 3).',
      'Audit: Think harder items in lessons 3, 5, 6, 9.'),
     ('AHEAD', 'Reaches into Primary 4 to 6',
      'Shared multiples (Primary 4), fraction of a fraction (Primary 5), unknown on both sides of an equation (Primary 6).',
      'Audit: Go further items in lessons 2, 3, 4, 5, 7.')],
 3: [('AT', 'At the Primary 3 level',
      'Numbers to 10 000, tables of 6 to 9, division with remainders, fractions, area, angles. Letters for digits appear in some items.',
      'Audit: each lesson main topic is "ON" for Primary 3 (checked against the syllabus).'),
     ('NEW', 'Primary 3 ideas, some Primary 4 previews',
      'Finding a side from the area or perimeter (Primary 4), shared multiples (Primary 4), heavier two-unknown word problems.',
      'Audit: Think harder items in lessons 3 to 7. Bar-model problems are "heavier than Primary 3 outcomes imply".'),
     ('AHEAD', 'Reaches into Primary 4 and past the syllabus',
      'Shapes with cut-outs (Primary 4), a sum of three fractions with different denominators (more than the primary syllabus allows), "find a fraction between", last-digit patterns and logic puzzles the syllabus does not name.',
      'Audit: Go further items in lessons 3, 5, 6, 7, 9, 10.')],
 4: [('AT', 'At the Primary 4 level',
      'Factors, 5-digit numbers, fractions (including two different denominators), decimals, protractor angles, area, nets, line graphs. The compass-turn items are not in the 2021 Primary 4 syllabus.',
      'Checked against the syllabus: every lesson main topic is Primary 4 except lesson 3 (order of operations is Primary 5).'),
     ('NEW', 'Primary 4 ideas in new settings, a few previews',
      'Mostly Primary 4 content. A few items use letters as unknowns (Primary 6), find unknown angles (Primary 5) or divide by a fraction by counting quarters (Primary 6).',
      'Audit section 3 lists these items by number; it gives no tier-wide verdict.'),
     ('AHEAD', 'Some items reach toward Primary 5 and 6',
      'Order of operations with brackets (Primary 5) and a letter for an unknown (Primary 6). The fraction puzzles that add unrelated denominators are Primary 4, not ahead.',
      'Audit: lesson 3 (order of operations); lesson 3 Go further 4 (letter); lesson 4 Go further 2, 5, 6, 7 checked as Primary 4.')],
 5: [('AT', 'At the Primary 5 level',
      'Numbers to 10 million, fractions, triangle area, volume, rate, percentage, angles.',
      'Checked against the syllabus: every lesson main topic is Primary 5, with items listed by number.'),
     ('NEW', 'Primary 5 ideas, a few Primary 6 previews',
      'Mostly Primary 5. Dividing a fraction by a whole number is correctly labelled a Primary 6 preview; percentage increase and decrease and finding the original are Primary 6.',
      'Audit: lesson 2 Think harder 6 and lesson 7 Think harder 1; years now confirmed.'),
     ('AHEAD', 'Reaches toward Primary 6 and past the syllabus',
      'Percentage change and "find the original" (Primary 6), water-level problems (Primary 6), painted-cube counts and shaded-area puzzles that the syllabus does not name. Long products of fractions use Primary 5 skills.',
      'Audit: Go further items in lessons 2, 5 and 7; years now confirmed.')],
 6: [('MIX', 'Primary 6 revision plus first steps into Secondary 1',
      'Algebra with a letter and averages are Primary 6. Lessons on sequences, primes and negative numbers are not in the primary syllabus at all.',
      'Audit compares whole lessons with Primary 6 and Secondary 1, not tier by tier. Primary 6 content checked against the syllabus.'),
     ('MIX', 'Evidence is thin',
      'The audit did not separate this tier. Algebra items with brackets are beyond Primary 6, which excludes brackets in expressions.',
      'Audit section 3, Level 6 item notes; brackets exclusion confirmed in the syllabus.'),
     ('AHEAD', 'Beyond the primary syllabus',
      'Counting rules, probability, clock arithmetic and codes are not primary topics. The Secondary 1 years could not be read from an MOE document.',
      'Audit lessons 5, 6, 8 marked "not in syllabus" or "secondary"; absence from the primary syllabus confirmed.')],
}
rows = []
for L in range(1, 7):
    for i, (rating, head, detail, ev) in enumerate(C[L]):
        rows.append(dict(level=L, ages=AGES[L], year=YEAR[L], tier=T[i], tier_order=i + 1, rating=rating,
                         headline=head, detail=detail, evidence=ev, confidence=CONF[L], items=ITEMS[L][i]))
json.dump(rows, open(os.path.join(H, 'tier_rows.json'), 'w'), ensure_ascii=False, indent=0)
print(len(rows))
