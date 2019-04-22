# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Square roots"),
    Entries(
        "21d9b8",
    ),
    Section("Quadratic equations"),
    Entries(
        "08d275",
        "e0ac95",
        "fc2582",
    ),
    Section("Series expansions"),
    Entries(
        "b14da0",
        "3c2557",
        "6202cb",
        "5ff181",
    ),
)

Log_branch_cut = OpenClosedInterval(-Infinity, 0)
Log_holomorphic_domain = SetMinus(CC, Log_branch_cut)

make_entry(ID("21d9b8"),
    SymbolDefinition(Sqrt, Sqrt(z), "Principal square root"),
    Description("The principal square root", Sqrt(z), "is a function of one complex variable", z, ".",),
    Description("It has a branch point singularity at", Equal(z, 0),
        "and a branch cut on", OpenClosedInterval(-Infinity, 0), "where the value on",
            OpenInterval(-Infinity, 0), "is taken to be continuous with the upper half plane."),
    Description("The following table lists all conditions such that", SourceForm(Sqrt(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, ClosedOpenInterval(0,Infinity)), Element(Sqrt(z), ClosedOpenInterval(0,Infinity))),
        Tuple(Element(z, CC), Element(Sqrt(z), CC)),
        TableSection("Infinities"),
        Tuple(Element(z, Set(Infinity)), Element(Sqrt(z), Set(Infinity))),
        TableSection("Formal power series"),
        Tuple(And(Element(z, FormalPowerSeries(RR, x)), Element(SeriesCoefficient(z, x, 0), OpenInterval(0,Infinity))),
            And(Element(Sqrt(z), FormalPowerSeries(RR, x)))),
        Tuple(And(Element(z, FormalPowerSeries(CC, x)), Unequal(SeriesCoefficient(z, x, 0), 0)),
            And(Element(Sqrt(z), FormalPowerSeries(CC, x)))),
      )))

make_entry(ID("08d275"),
    Formula(Equal(Zeros(z**2 - c, z, Element(z, CC)), Set(Sqrt(c), -Sqrt(c)))),
    Variables(c),
    Assumptions(Element(c, CC)))

make_entry(ID("e0ac95"),
    Formula(Equal(Zeros(z**2 - c, z, Element(z, CC)), Set(ConstI*Sqrt(-c), -ConstI*Sqrt(-c)))),
    Variables(c),
    Assumptions(Element(c, CC)))

make_entry(ID("fc2582"),
    Formula(Equal(Zeros(a*z**2+b*z+c, z, Element(z, CC)), Set((-b+Sqrt(b**2-4*a*c))/(2*a), (-b-Sqrt(b**2-4*a*c))/(2*a)))),
    Variables(a, b, c),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(c, CC), Unequal(a, 0))))

make_entry(ID("b14da0"),
    Formula(Equal(Sqrt(z+x), Sqrt(z) * Sum(((-1)**k * RisingFactorial(-Div(1,2),k)) / (z**k * Factorial(k)) * x**k, Tuple(k, 0, Infinity)))),
    Variables(z, x),
    Assumptions(And(Element(z, SetMinus(CC, Set(0))), Element(x, CC), And(Less(Abs(x), Abs(z)), Or(Greater(Re(z), 0), Equal(Sign(Im(x)), Sign(Im(z)))))),
        And(Element(z, SetMinus(CC, Set(0))), FormalGenerator(x, FormalPowerSeries(CC, x)))))

make_entry(ID("3c2557"),
    Formula(Equal(1/Sqrt(z+x), (1/Sqrt(z)) * Sum(((-1)**k * RisingFactorial(Div(1,2),k)) / (z**k * Factorial(k)) * x**k, Tuple(k, 0, Infinity)))),
    Variables(z, x),
    Assumptions(And(Element(z, SetMinus(CC, Set(0))), Element(x, CC), And(Less(Abs(x), Abs(z)), Or(Greater(Re(z), 0), Equal(Sign(Im(x)), Sign(Im(z)))))),
        And(Element(z, SetMinus(CC, Set(0))), FormalGenerator(x, FormalPowerSeries(CC, x)))))


make_entry(ID("6202cb"),
    Formula(Where(Equal(Subscript(c, n), 1/(n * Subscript(a, 0)) * Sum((3*k/2-n) * Subscript(a, k) * Subscript(c, n-k), Tuple(k, 1, n))),
        Equal(Subscript(c, n), SeriesCoefficient(Sqrt(A), x, n)), Equal(Subscript(a, n), SeriesCoefficient(A, x, n)))),
    Variables(A, n),
    Assumptions(And(Element(A, FormalPowerSeries(CC, x)), Unequal(SeriesCoefficient(A, x, 0), 0), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("5ff181"),
    Formula(Where(Equal(Subscript(c, n), 1/(n * Subscript(a, 0)) * Sum((k/2-n) * Subscript(a, k) * Subscript(c, n-k), Tuple(k, 1, n))),
        Equal(Subscript(c, n), SeriesCoefficient(1/Sqrt(A), x, n)), Equal(Subscript(a, n), SeriesCoefficient(A, x, n)))),
    Variables(A, n),
    Assumptions(And(Element(A, FormalPowerSeries(CC, x)), Unequal(SeriesCoefficient(A, x, 0), 0), Element(n, ZZGreaterEqual(1)))))

