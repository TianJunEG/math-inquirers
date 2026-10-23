"""The Primary 5 (Standard) outcome lines, the two semester booklets and the page order of each.
Plan: docs/school_books/p5_semester_booklets_plan.md.

Source: Primary Mathematics Syllabus P1 to P6 (2021 edition, updated Oct 2025), Primary 5 Standard, pages 41 and 42. Only the outcome-line wording is copied (lines and numbers as the syllabus prints them); the rest of each key entry is our own text and makes no claim about any school or approval.
"""

# id -> (strand heading used on the key, outcome line in our own words, label printed on the key)
OUTCOMES = {
    "WN1.1": ("Whole Numbers", "reading and writing numbers in numerals and in words (numbers up to 10 million)", "Whole Numbers 1.1"),
    "WN2.1": ("Whole Numbers", "multiplying and dividing by 10, 100, 1000 and their multiples without calculator", "Whole Numbers 2.1"),
    "WN2.2": ("Whole Numbers", "order of operations without calculator", "Whole Numbers 2.2"),
    "WN2.3": ("Whole Numbers", "use of brackets without calculator", "Whole Numbers 2.3"),
    "FR1.1": ("Fractions", "dividing a whole number by a whole number with quotient as a fraction", "Fractions 1.1"),
    "FR1.2": ("Fractions", "expressing fractions as decimals", "Fractions 1.2"),
    "FR2.1": ("Fractions", "adding and subtracting mixed numbers", "Fractions 2.1"),
    "FR2.2": ("Fractions", "multiplying a proper/improper fraction and a whole number without calculator", "Fractions 2.2"),
    "FR2.3": ("Fractions", "multiplying a proper fraction and a proper/improper fraction without calculator", "Fractions 2.3"),
    "FR2.4": ("Fractions", "multiplying two improper fractions", "Fractions 2.4"),
    "FR2.5": ("Fractions", "multiplying a mixed number and a whole number", "Fractions 2.5"),
    "DE1.1": ("Decimals", "multiplying and dividing decimals (up to 3 decimal places) by 10, 100, 1000 and their multiples without calculator", "Decimals 1.1"),
    "DE1.2": ("Decimals", "converting a measurement from a smaller unit to a larger unit in decimal form, and vice versa (kilometres and metres; metres and centimetres; kilograms and grams; litres and millilitres)", "Decimals 1.2"),
    "PC1.1": ("Percentage", "expressing a part of a whole as a percentage", "Percentage 1.1"),
    "PC1.2": ("Percentage", "use of %", "Percentage 1.2"),
    "PC1.3": ("Percentage", "finding a percentage part of a whole", "Percentage 1.3"),
    "PC1.4": ("Percentage", "finding discount, GST and annual interest", "Percentage 1.4"),
    "RA1.1": ("Rate", "rate as the amount of a quantity per unit of another quantity", "Rate 1.1"),
    "RA1.2": ("Rate", "finding rate, total amount or number of units given the other two quantities", "Rate 1.2"),
    "AR1.1": ("Area and Volume", "concepts of base and height of a triangle", "Area of Triangle 1.1"),
    "AR1.2": ("Area and Volume", "area of triangle", "Area of Triangle 1.2"),
    "AR1.3": ("Area and Volume", "finding the area of composite figures made up of rectangles, squares and triangles", "Area of Triangle 1.3"),
    "VO2.1": ("Area and Volume", "building solids with unit cubes", "Volume 2.1"),
    "VO2.2": ("Area and Volume", "measuring volume in cubic units, cm\u00b3/m\u00b3, excluding conversion between cm\u00b3 and m\u00b3", "Volume 2.2"),
    "VO2.3": ("Area and Volume", "drawing cubes and cuboids on isometric grid", "Volume 2.3"),
    "VO2.4": ("Area and Volume", "volume of a cube/cuboid", "Volume 2.4"),
    "VO2.5": ("Area and Volume", "finding the volume of liquid in a rectangular tank", "Volume 2.5"),
    "VO2.6": ("Area and Volume", "relationship between \u2113 (or m\u2113) with cm\u00b3", "Volume 2.6"),
    "GE1.1": ("Geometry", "angles on a straight line", "Geometry 1.1"),
    "GE1.2": ("Geometry", "angles at a point", "Geometry 1.2"),
    "GE1.3": ("Geometry", "vertically opposite angles", "Geometry 1.3"),
    "GE1.4": ("Geometry", "finding unknown angles", "Geometry 1.4"),
    "GE2.1": ("Geometry", "properties of isosceles triangle, equilateral triangle, right-angled triangle", "Geometry 2.1"),
    "GE2.2": ("Geometry", "angle sum of a triangle", "Geometry 2.2"),
    "GE2.3": ("Geometry", "finding unknown angles without additional construction of lines", "Geometry 2.3"),
    "GE3.1": ("Geometry", "properties of parallelogram, rhombus, trapezium", "Geometry 3.1"),
    "GE3.2": ("Geometry", "finding unknown angles without additional construction of lines", "Geometry 3.2"),
}

# page number (P5-nn, the number in the full set of 40) -> outcome ids exercised (filled when build.py runs)
PAGE_OC = {}

# the two booklets: page numbers in booklet order (S1-01 .. S1-20, S2-01 .. S2-20)
BOOKLETS = {
    "S1": dict(name="Semester 1", terms="Terms 1 and 2", n=1, order=list(range(1, 21))),
    "S2": dict(name="Semester 2", terms="Terms 3 and 4", n=2, order=list(range(21, 41))),
}
assert sorted(BOOKLETS["S1"]["order"] + BOOKLETS["S2"]["order"]) == list(range(1, 41))

def booklet_of(no):
    for k, b in BOOKLETS.items():
        if no in b["order"]: return k, b["order"].index(no) + 1
    raise KeyError(no)

def code_of(no):
    """footer / key code with both numbers, e.g. 'S2-07 (P5-27)'"""
    k, pos = booklet_of(no)
    return f"{k}-{pos:02d} (P5-{no:02d})"

def oc_label(i):
    return OUTCOMES[i][2]
