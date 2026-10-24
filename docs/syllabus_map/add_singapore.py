#!/usr/bin/env python3
"""Add the Singapore (MOE) rows to the intl map data.

Reads intl_rows_12places.json (12 places, 720 rows), appends 60 Singapore rows and writes intl_rows.json.
Source of every verdict: docs/audit/moe_alignment_p1_p3.md and moe_alignment_p4_p6.md, both now verified against the
MOE 2021 Primary Mathematics syllabus PDF (updated Oct 2025; see docs/moe/syllabus_by_level.md and docs/moe/verification_report.md). Same status words as the other places:
  SAME = main topic is in the syllabus for that year (audit "ON"); LATER = the syllabus teaches it in a later year
  (audit "ABOVE"); NOT = no matching topic in the primary syllabus (audit "NOT IN"); MIXED = review lesson, not compared.
unverified=True is now used only where the syllabus confirms the topic is absent from primary but the later (secondary)
year could not be read from an MOE document (6.1, 6.6, 6.7).
Verdicts are for the lesson's main topic; harder Think harder / Go further items that go beyond are in tier_rows.json.
"""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(H, 'intl_rows_12places.json')))
titles = {}
for r in rows: titles.setdefault(r['lesson'], (r['level'], r['lesson_title']))
J = 'Singapore (MOE)'
# lesson: (status, note, unverified)
V = {
 '1.1': ('SAME', 'SAME P1 (number-sequence patterns, skip counting); common multiples are P4', 0),
 '1.2': ('SAME', 'SAME P1 (add/subtract to 20, = sign)', 0),
 '1.3': ('SAME', 'SAME P1 (picture graphs); scales are P2', 0),
 '1.4': ('SAME', 'SAME P1 (number-sequence patterns); shape and colour patterns are P2, growing patterns not named', 0),
 '1.5': ('SAME', 'SAME P1 (add/subtract relationship); number machines not named', 0),
 '1.6': ('SAME', 'SAME P1 (money to $100)', 0),
 '1.7': ('SAME', 'SAME P1 (triangle, square, rectangle, circle); pentagon/hexagon not named in any year', 0),
 '1.8': ('NOT', 'NOT listed (Venn diagrams, logic grids)', 0),
 '1.9': ('SAME', 'SAME P1 (length in cm); non-standard units not listed', 0),
 '2.1': ('SAME', 'SAME P2 (numbers to 1000)', 0),
 '2.2': ('SAME', 'SAME P2 (3-digit add/subtract); letters for unknowns are P6', 0),
 '2.3': ('SAME', 'SAME P2 (tables of 2, 3, 4, 5, 10); remainders are P3', 0),
 '2.4': ('SAME', 'SAME P2 (number patterns); growing patterns with a rule not named', 0),
 '2.5': ('SAME', 'SAME P2 (x and / are inverse); bar models and number machines not named', 0),
 '2.6': ('SAME', 'SAME P2 (dollars and cents)', 0),
 '2.7': ('SAME', 'SAME P2 (fractions, denominators to 12); equivalent fractions P3', 0),
 '2.8': ('SAME', 'SAME P2 (3-D shapes); nets are P4, building with unit cubes P5', 0),
 '2.9': ('SAME', 'SAME P2 (m, cm, g, kg, litres, time to the minute)', 0),
 '3.1': ('SAME', 'SAME P3 (numbers to 10 000)', 0),
 '3.2': ('SAME', 'SAME P3 (4-digit add/subtract); letter puzzles not named', 0),
 '3.3': ('SAME', 'SAME P3 (tables of 6, 7, 8, 9)', 0),
 '3.4': ('SAME', 'SAME P3 (four operations in word problems); bar models are not named in the syllabus', 0),
 '3.5': ('SAME', 'SAME P3 (division with remainder)', 0),
 '3.6': ('SAME', 'SAME P3 (equivalent fractions, add/subtract related fractions)', 0),
 '3.7': ('SAME', 'SAME P3 (area and perimeter of rectangles, squares); composite figures and missing sides P4', 0),
 '3.8': ('SAME', 'SAME P3 (angles, perpendicular, parallel)', 0),
 '3.9': ('SAME', 'SAME P3 (compound units, 24-hour time)', 0),
 '4.1': ('SAME', 'SAME P4 (factors and multiples)', 0),
 '4.2': ('SAME', 'SAME P4 (numbers to 100 000, rounding to 10/100/1000 and the sign for approximately)', 0),
 '4.3': ('LATER', 'LATER P5 (order of operations and brackets, p.41); P4 has the multiplication and division algorithms', 0),
 '4.4': ('SAME', 'SAME P4 (improper/mixed fractions, fraction of a set, adding fractions with up to two denominators)', 0),
 '4.5': ('SAME', 'SAME P4 (decimals)', 0),
 '4.6': ('SAME', 'SAME P4 (angle notation, protractor); compass turns are not in the 2021 syllabus; unknown angles are P5', 0),
 '4.7': ('SAME', 'SAME P4 (area and perimeter of rectilinear figures)', 0),
 '4.8': ('SAME', 'SAME P4 (symmetry; nets moved down to P4 in 2021)', 0),
 '4.9': ('SAME', 'SAME P4 (tables, line graphs)', 0),
 '5.1': ('SAME', 'SAME P5 (numbers to 10 million, order of operations and brackets)', 0),
 '5.2': ('SAME', 'SAME P5 (fraction and division, fractions x fractions); dividing a fraction by a whole number is P6', 0),
 '5.3': ('SAME', 'SAME P5 (fraction operations in word problems); model drawing not named in the syllabus', 0),
 '5.4': ('SAME', 'SAME P5 (area of triangle); parallelogram and trapezium area not in the primary syllabus', 0),
 '5.5': ('SAME', 'SAME P5 (volume of cuboid, liquid in a tank); finding a height from volume is P6', 0),
 '5.6': ('SAME', 'SAME P5 (rate); speed is not named in any primary year', 0),
 '5.7': ('SAME', 'SAME P5 (percentage, discount, GST, interest); percentage change and finding the whole are P6', 0),
 '5.8': ('SAME', 'SAME P5 (angles, triangles, parallelogram, rhombus, trapezium); quadrilateral angle sum not listed', 0),
 '5.9': ('NOT', 'NOT listed at P5 (number patterns end at P4; letters for patterns start P6)', 0),
 '6.1': ('LATER', 'LATER secondary (nth-term formulas); not in the primary syllabus, secondary year not confirmed', 1),
 '6.2': ('LATER', 'LATER Sec 1 (primes, prime factorisation)', 0),
 '6.3': ('LATER', 'LATER Sec 1 (negative numbers)', 0),
 '6.4': ('SAME', 'SAME P6 (algebra, letter as unknown); brackets with letters are excluded in P6', 0),
 '6.5': ('NOT', 'NOT listed (counting rules; only "make a systematic list")', 0),
 '6.6': ('LATER', 'LATER secondary (probability); no primary topic, secondary year not confirmed', 1),
 '6.7': ('LATER', 'LATER secondary (polygon angle sum); P6 has unknown angles in composite figures only', 1),
 '6.8': ('NOT', 'NOT listed (clock arithmetic, ciphers)', 0),
 '6.9': ('SAME', 'SAME P6 (average); median and mode are not in the primary syllabus', 0),
}
out = [r for r in rows if r['jurisdiction'] != J]
for lesson, (lvl, title) in titles.items():
    if lesson.endswith('.10'):
        st, note, u = 'MIXED', 'MIXED review, not compared', 0
    else:
        st, note, u = V[lesson]
    out.append(dict(level=lvl, lesson=lesson, lesson_title=title, region='Singapore',
                    jurisdiction=J, status=st, note=note, unverified=bool(u)))
json.dump(out, open(os.path.join(H, 'intl_rows.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
from collections import Counter
print(len(out), Counter(r['status'] for r in out if r['jurisdiction'] == J))
