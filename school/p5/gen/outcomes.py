"""The Primary 5 (Standard) outcome lines, the two semester booklets and the page order of each.
Plan: docs/school_books/p5_semester_booklets_plan.md.

IMPORTANT (honest note): the syllabus PDF itself is not in the repository. The wording below is the repository's own summary of pages 41 and 42
(docs/moe/syllabus_by_level.md, section "Primary 5, Standard"), in our own words, with the outcome numbers that summary prints (Whole Numbers 2.2 and 2.3,
Fractions 1.1 to 2.5, Decimals 1.1 and 1.2, Percentage 1.4, Volume 2.1 to 2.6, Geometry 1.1 to 1.4). Lines whose number the summary does not print carry no number
here. Nothing in this file is a copy of the PDF's wording and the key says so. Before any use of the PDF's own wording, the owner must supply the PDF."""

# id -> (strand heading used on the key, outcome line in our own words, label printed on the key)
OUTCOMES = {
    "WN.NUM": ("Whole Numbers", "reading and writing numbers up to 10 million", "Whole Numbers: numbers to 10 million"),
    "WN.X10": ("Whole Numbers", "multiplying and dividing by 10, 100, 1000 and their multiples, without a calculator", "Whole Numbers: multiply and divide by 10, 100, 1000 and multiples"),
    "WN2.2": ("Whole Numbers", "order of operations, without a calculator", "Whole Numbers 2.2"),
    "WN2.3": ("Whole Numbers", "use of brackets, without a calculator", "Whole Numbers 2.3"),
    "FR1.1": ("Fractions", "dividing a whole number by a whole number, with a fraction as the quotient", "Fractions 1.1"),
    "FR1.2": ("Fractions", "expressing fractions as decimals", "Fractions 1.2"),
    "FR2.1": ("Fractions", "adding and subtracting mixed numbers", "Fractions 2.1"),
    "FR2.2": ("Fractions", "multiplying a proper or improper fraction by a whole number", "Fractions 2.2"),
    "FR2.3": ("Fractions", "multiplying a proper fraction by a proper or improper fraction", "Fractions 2.3"),
    "FR2.4": ("Fractions", "multiplying two improper fractions", "Fractions 2.4"),
    "FR2.5": ("Fractions", "multiplying a mixed number by a whole number", "Fractions 2.5"),
    "DE1.1": ("Decimals", "multiplying and dividing decimals (up to 3 decimal places) by 10, 100, 1000 and their multiples", "Decimals 1.1"),
    "DE1.2": ("Decimals", "converting a measure to a larger or smaller unit in decimal form (km and m, m and cm, kg and g, ℓ and mℓ)", "Decimals 1.2"),
    "PC.PART": ("Percentage", "expressing a part of a whole as a percentage, and the sign %", "Percentage: a part of a whole as a percentage"),
    "PC.OF": ("Percentage", "finding a percentage part of a whole", "Percentage: a percentage part of a whole"),
    "PC1.4": ("Percentage", "finding discount, GST and annual interest", "Percentage 1.4"),
    "RA": ("Rate", "rate as the amount of one quantity per unit of another quantity; finding the rate, the total or the number of units", "Rate"),
    "AR.TRI": ("Area and Volume", "area of a triangle (base and height)", "Area of triangle: base, height and area"),
    "AR.COMP": ("Area and Volume", "area of composite figures made of rectangles, squares and triangles", "Area of triangle: composite figures"),
    "VO2.1": ("Area and Volume", "building cubes and cuboids with unit cubes", "Volume 2.1"),
    "VO.UNIT": ("Area and Volume", "cubic units cm³ and m³", "Volume: cubic units (cm³, m³)"),
    "VO2.3": ("Area and Volume", "drawing cubes and cuboids on an isometric grid", "Volume 2.3"),
    "VO2.4": ("Area and Volume", "volume of a cube or cuboid", "Volume 2.4"),
    "VO2.5": ("Area and Volume", "volume of liquid in a rectangular tank", "Volume 2.5"),
    "VO2.6": ("Area and Volume", "the relationship between ℓ or mℓ and cm³", "Volume 2.6"),
    "GE1.1": ("Geometry", "angles on a straight line", "Geometry 1.1"),
    "GE1.2": ("Geometry", "angles at a point", "Geometry 1.2"),
    "GE1.3": ("Geometry", "vertically opposite angles", "Geometry 1.3"),
    "GE1.4": ("Geometry", "finding unknown angles", "Geometry 1.4"),
    "GE.TRI": ("Geometry", "properties of isosceles, equilateral and right-angled triangles", "Geometry: properties of triangles"),
    "GE.SUM": ("Geometry", "angle sum of a triangle; unknown angles of a triangle", "Geometry: angle sum of a triangle"),
    "GE.QUAD": ("Geometry", "properties of a parallelogram, rhombus and trapezium; their unknown angles", "Geometry: parallelogram, rhombus, trapezium"),
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
