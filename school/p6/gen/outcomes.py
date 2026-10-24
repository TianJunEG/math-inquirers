"""The Primary 6 (Standard track) outcome lines, four lines of the Primary 6 Foundation track used by some pages, the two semester booklets and the page order of each.
SOURCE. The Ministry of Education's Primary Mathematics Syllabus (2021 edition, updated October 2025): Primary 6 pages 43 and 44 (outcome numbers and wording checked against the PDF
on 23 Oct 2026: Fractions 1.1 and 1.2; Percentage 1.1 and 1.2; Ratio 1.1 to 1.7; Algebra 1.1 to 1.5; Area and Circumference of Circle 1.1 to 1.3; Volume of Cube and Cuboid 2.1 to 2.5;
Special Quadrilaterals 1.1; Average of a Set of Data 1.1 and 1.2) and the Primary 6 Foundation pages 49 and 50. Only the outcome lines are used, in their wording; nothing else of the PDF is copied.
The ids AV (Area and Circumference of Circle 1.x), VO (Volume of Cube and Cuboid 2.x), GE and ST are our short ids for those strands; the numbers shown on the key are the PDF's.
Plan: docs/school_books/p6_semester_booklets_plan.md. Wording also kept in docs/school_books/p6_outcome_wording.md."""

# id -> (strand heading used on the key, outcome wording: summary wording, our own words)
OUTCOMES = {
    "FR1.1": ("Fractions", "dividing a proper fraction by a whole number without calculator"),
    "FR1.2": ("Fractions", "dividing a whole number/proper fraction by a proper fraction without calculator"),
    "PC1.1": ("Percentage", "finding the whole given a part and the percentage"),
    "PC1.2": ("Percentage", "finding percentage increase/decrease"),
    "RA1.1": ("Ratio", "notation, representations and interpretation of a:b and a:b:c, where a, b and c are whole numbers, excluding ratios involving fractions and decimals"),
    "RA1.2": ("Ratio", "equivalent ratios"),
    "RA1.3": ("Ratio", "dividing a quantity in a given ratio"),
    "RA1.4": ("Ratio", "expressing a ratio in its simplest form"),
    "RA1.5": ("Ratio", "finding the ratio of two or three given quantities"),
    "RA1.6": ("Ratio", "finding the missing term in a pair of equivalent ratios"),
    "RA1.7": ("Ratio", "relationship between fraction and ratio"),
    "AL1.1": ("Algebra", "using a letter to represent an unknown number"),
    "AL1.2": ("Algebra", "notation, representations and interpretation of simple algebraic expressions such as a + 3, a - 3, 3a or a x 3, a ÷ 3 or a/3"),
    "AL1.3": ("Algebra", "simplifying simple linear expressions excluding brackets"),
    "AL1.4": ("Algebra", "evaluating simple linear expressions by substitution"),
    "AL1.5": ("Algebra", "simple linear equations involving whole number coefficient only"),
    "AV1.1": ("Area and Volume", "area and circumference of circle"),
    "AV1.2": ("Area and Volume", "finding the area and perimeter of semicircle and quarter circle"),
    "AV1.3": ("Area and Volume", "finding the area and perimeter of composite figures made up of square, rectangle, triangle, semicircle and quarter circle"),
    "VO2.1": ("Area and Volume", "finding one dimension of a cuboid given its volume and the other dimensions"),
    "VO2.2": ("Area and Volume", "finding the length of one edge of a cube given its volume"),
    "VO2.3": ("Area and Volume", "finding the height of a cuboid given its volume and base area"),
    "VO2.4": ("Area and Volume", "finding the area of a face of a cuboid given its volume and one dimension"),
    "VO2.5": ("Area and Volume", "use of the square-root and cube-root signs"),
    "GE1.1": ("Geometry", "finding unknown angles, without additional construction of lines, in composite geometric figures involving square, rectangle, triangle, parallelogram, rhombus, trapezium"),
    "ST1.1": ("Statistics", "average as total value ÷ number of data"),
    "ST1.2": ("Statistics", "relationship between average, total value and number of data"),
    # lines of the Primary 6 FOUNDATION track (pages 49 and 50 of the syllabus PDF) that the Standard-track pages also use; tagged "Primary 6 Foundation"
    "PF.ST": ("Primary 6 Foundation Statistics 1.1", "reading and interpreting data from pie charts"),
    "PF.DE": ("Primary 6 Foundation Decimals 1.1", "multiplying and dividing decimals"),
    "PF.PC": ("Primary 6 Foundation Percentage 1.3 and 1.4", "finding a percentage part of a whole; finding discount, GST and annual interest"),
    "PF.VO": ("Primary 6 Foundation Area and Volume 2.1 to 2.3", "volume of a cube/cuboid; finding the volume of liquid in a rectangular tank; relationship between litre (or ml) and cm3"),
}
# a short phrase for the coverage list of the front matter (the full outcome lines are above)
SHORT = {
    "FR1.1": "dividing a proper fraction by a whole number", "FR1.2": "dividing a whole number or proper fraction by a proper fraction",
    "PC1.1": "finding the whole given a part and the percentage", "PC1.2": "percentage increase or decrease",
    "RA1.1": "a:b and a:b:c with whole numbers", "RA1.2": "equivalent ratios", "RA1.3": "dividing a quantity in a given ratio", "RA1.4": "simplest form of a ratio",
    "RA1.5": "ratio of two or three quantities", "RA1.6": "missing term in equivalent ratios", "RA1.7": "relationship between fraction and ratio",
    "AL1.1": "a letter for an unknown number", "AL1.2": "notation of simple expressions", "AL1.3": "simplifying linear expressions (no brackets)", "AL1.4": "evaluating by substitution", "AL1.5": "simple linear equations",
    "AV1.1": "area and circumference of a circle", "AV1.2": "semicircle and quarter circle", "AV1.3": "composite figures",
    "VO2.1": "a missing dimension of a cuboid", "VO2.2": "the edge of a cube from its volume", "VO2.3": "height from volume and base area", "VO2.4": "a face area from volume and one dimension", "VO2.5": "square-root and cube-root signs",
    "GE1.1": "unknown angles in composite figures", "ST1.1": "average: total divided by number of data", "ST1.2": "average, total and number of data",
    "PF.ST": "pie charts", "PF.DE": "decimals: multiplying and dividing", "PF.PC": "percentage part of a whole; discount, GST, interest", "PF.VO": "volume of liquid in a tank; litres and cm3",
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
    """short outcome label for the key: 'Ratio 1.3', 'Primary 6 Foundation Statistics 1.1' """
    if i.startswith("PF"): return OUTCOMES[i][0]
    return f"{OUTCOMES[i][0]} {i[2:]}"
