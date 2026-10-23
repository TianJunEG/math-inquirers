"""The Primary 6 (Standard track) outcome lines, the revision lines from earlier years, the two semester booklets and the page order of each.
SOURCE AND LIMIT. The Ministry of Education's syllabus PDF is NOT in this repository. The wording below comes from our own summary in
docs/moe/syllabus_by_level.md (pages 43 and 44 of the 2021 edition, updated Oct 2025, summarised in our own words with a few short quoted phrases);
it is a SUMMARY WORDING, not the PDF's text, and it is not copied from the PDF. Where the summary gives an outcome number (Fractions 1.1, 1.2; Percentage 1.1, 1.2;
Ratio 1.1 to 1.7; Algebra 1.1 to 1.5; Volume 2.5) the id uses it; the summary gives the Ratio lines in one list, so the order 1.1 to 1.7 follows the order of
that list and is to be checked against the PDF. Lines whose number the summary does not give (circles, composite figures, the other volume lines, angles, average) carry
ids of our own (AV, VO, GE, ST). Plan: docs/school_books/p6_semester_booklets_plan.md. Wording also kept in docs/school_books/p6_outcome_wording.md."""

# id -> (strand heading used on the key, outcome wording: summary wording, our own words)
OUTCOMES = {
    "FR1.1": ("Fractions", "dividing a proper fraction by a whole number"),
    "FR1.2": ("Fractions", "dividing a whole number or a proper fraction by a proper fraction"),
    "PC1.1": ("Percentage", "finding the whole given a part and the percentage"),
    "PC1.2": ("Percentage", "percentage increase or decrease"),
    "RA1.1": ("Ratio", "ratio a:b and a:b:c with whole numbers"),
    "RA1.2": ("Ratio", "equivalent ratios"),
    "RA1.3": ("Ratio", "dividing a quantity in a given ratio"),
    "RA1.4": ("Ratio", "ratio in simplest form"),
    "RA1.5": ("Ratio", "ratio of two or three quantities"),
    "RA1.6": ("Ratio", "finding the missing term in a pair of equivalent ratios"),
    "RA1.7": ("Ratio", "relationship between fraction and ratio"),
    "AL1.1": ("Algebra", "using a letter to stand for an unknown number"),
    "AL1.2": ("Algebra", "notation of simple expressions such as a + 3, a - 3, 3a and a ÷ 3"),
    "AL1.3": ("Algebra", "simplifying simple linear expressions (no brackets)"),
    "AL1.4": ("Algebra", "evaluating a simple expression by substitution"),
    "AL1.5": ("Algebra", "solving simple linear equations with whole-number coefficients"),
    "AV1.1": ("Area and Volume", "area and circumference of a circle"),
    "AV1.2": ("Area and Volume", "area and perimeter of a semicircle and a quarter circle"),
    "AV1.3": ("Area and Volume", "composite figures made of squares, rectangles, triangles, semicircles and quarter circles"),
    "VO2.1": ("Area and Volume", "finding a missing dimension of a cuboid given its volume and the other dimensions"),
    "VO2.2": ("Area and Volume", "finding the edge of a cube given its volume"),
    "VO2.3": ("Area and Volume", "finding the height of a cuboid given its volume and base area"),
    "VO2.4": ("Area and Volume", "finding the area of a face of a cuboid given its volume and one dimension"),
    "VO2.5": ("Area and Volume", "use of the square-root and cube-root signs"),
    "GE1.1": ("Geometry", "finding unknown angles in composite figures (square, rectangle, triangle, parallelogram, rhombus, trapezium), without additional construction"),
    "ST1.1": ("Statistics", "average as total value ÷ number of data"),
    "ST1.2": ("Statistics", "relationship between average, total value and number of data"),
    # lines from earlier years that Primary 6 pupils meet again (the Foundation and Standard syllabus both revisit them); tagged "Revisits"
    "RV4.ST": ("Revisits Primary 4 Statistics", "reading and interpreting pie charts"),
    "RV4.NET": ("Revisits Primary 4 Geometry", "identifying nets of a cube and a cuboid"),
    "RV4.DE": ("Revisits Primary 4 Decimals", "adding, subtracting, multiplying and dividing decimals"),
    "RV5.FR": ("Revisits Primary 5 Fractions", "adding and subtracting mixed numbers; multiplying a fraction by a whole number or a fraction"),
    "RV5.PC": ("Revisits Primary 5 Percentage", "a percentage part of a whole; discount, GST and annual interest"),
    "RV5.RA": ("Revisits Primary 5 Rate", "rate as the amount of one quantity per unit of another; finding the rate, the total or the number of units"),
    "RV5.VO": ("Revisits Primary 5 Volume", "volume of a cuboid; volume of liquid in a rectangular tank; litres and cm³"),
}
N_OUTCOMES = len(OUTCOMES)

# page number (P6-nn) -> outcome ids exercised (filled from the pages when build.py runs)
PAGE_OC = {}

# the two booklets: page numbers in booklet order (S1-01 .. S1-20, S2-01 .. S2-20). The P6 number is the reading order.
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
    """footer / key code with both numbers, e.g. 'S1-07 (P6-07)'"""
    k, pos = booklet_of(no)
    return f"{k}-{pos:02d} (P6-{no:02d})"

def oc_label(i):
    """short outcome label for the key: 'Ratio 1.3', 'Revisits Primary 5 Fractions' """
    if i.startswith("RV"): return OUTCOMES[i][0]
    return f"{OUTCOMES[i][0]} {i[2:]}"
