# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Exponential function"),
    Section("Definitions"),
    Entries(
        "dfbcd9",
        "f758c6",
    ),
    Section("Illustrations"),
    Entries(
        "6ef3d1",
    ),
    Section("Particular values"),
    Entries(
        "27ca8d",
        "9a944c",
        "54aaf1",
        "a90f35",
    ),
    Section("Functional equations and connection formulas"),
    Entries(
        "812707",
        "e51ec3",
        "2f4f74",
        "77d6bf",
        "97ba8d",
        "1fa6b7",
        "1568e1",
        "e103e7",
    ),
    Section("Analytic properties"),
    Entries(
        "28d158",
        "0901a1",
        "be4b28",
        "184c11",
        "b62d05",
        "bceb84",
    ),
    Section("Complex parts"),
    Entries(
        "1b3014",
        "caf706",
        "b7d62b",
        "e2fac7",
        "a0d93c",
        "52d827",
    ),
    Section("Taylor series"),
    Entries(
        "1635f5",
        "bad502",
    ),
    Section("Derivatives and integrals"),
    Entries(
        "935b2f",
        "96af56",
        "4491b8",
    ),
    Section("Approximations"),
    Entries(
        "3c4480",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "2f57ad",
        "3ac8a5",
    ),
)

make_entry(ID("dfbcd9"),
    SymbolDefinition(Exp, Exp(z), "Exponential function"),
    Description("The exponential function", Exp(z), "is a function of one complex variable", z, ".",
        "It can be defined by the Taylor series", EntryReference("1635f5"), "."),
    Description("In rendered formulas,", SourceForm(Exp(z)), "is shown as", Exp(z), "or as", Call(Exp, z), "depending on the typographical requirements; no semantic difference is implied."),
    Description("The following table lists all conditions such that", SourceForm(Exp(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, Set(0)), Element(Exp(z), Set(1))),
        Tuple(Element(z, RR), Element(Exp(z), OpenInterval(0,Infinity))),
        Tuple(Element(z, CC), Element(Exp(z), SetMinus(CC, Set(0)))),
        TableSection("Infinities"),
        Tuple(Element(z, Set(Infinity)), Element(Exp(z), Set(Infinity))),
        Tuple(Element(z, Set(-Infinity)), Element(Exp(z), Set(0))),
        TableSection("Formal power series"),
        Tuple(And(Element(z, FormalPowerSeries(QQ, x)), Equal(SeriesCoefficient(z, x, 0), 0)),
            And(Element(Exp(z), FormalPowerSeries(QQ, x)), Equal(SeriesCoefficient(Exp(z), x, 0), 1))),
        Tuple(Element(z, FormalPowerSeries(RR, x)),
            And(Element(Exp(z), FormalPowerSeries(RR, x)), Unequal(SeriesCoefficient(Exp(z), x, 0), 0))),
        Tuple(Element(z, FormalPowerSeries(CC, x)),
            And(Element(Exp(z), FormalPowerSeries(CC, x)), Unequal(SeriesCoefficient(Exp(z), x, 0), 0))),
      )))

make_entry(ID("f758c6"),
    SymbolDefinition(ConstE, ConstE, "The constant e (2.718...)"),
    Description("The real number giving the base of the natural logarithm, also known as Euler's number."))

make_entry(ID("6ef3d1"),
    Image(Description("X-ray of", Exp(z), "on", Element(z, ClosedInterval(-5,5) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_exp")),
    description_xray,
    )

make_entry(ID("27ca8d"),
    Formula(Equal(Exp(0), 1)))

make_entry(ID("9a944c"),
    Formula(Equal(Exp(1), ConstE)))

make_entry(ID("54aaf1"),
    Formula(Equal(Exp(ConstPi*ConstI), -1)))

make_entry(ID("a90f35"),
    Formula(Equal(Exp(ConstPi*ConstI/2), ConstI)))

make_entry(ID("812707"),
    Formula(Equal(Exp(a+b), Exp(a) * Exp(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("e51ec3"),
    Formula(Equal(Exp(z)**n, Exp(n*z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZ))))

make_entry(ID("2f4f74"),
    Formula(Equal(Exp(-z), 1 / Exp(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("77d6bf"),
    Formula(Equal(Exp(a+b*ConstI), Exp(a) * (Cos(b) + Sin(b)*ConstI))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("97ba8d"),
    Formula(Equal(Exp(z+n*ConstPi*ConstI), (-1)**n * Exp(z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZ))))

make_entry(ID("1fa6b7"),
    Formula(Equal(Exp(z+2*n*ConstPi*ConstI), Exp(z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZ))))

make_entry(ID("28d158"),
    Formula(Equal(HolomorphicDomain(Exp(z), z, Union(CC, Set(UnsignedInfinity))), CC)))

make_entry(ID("0901a1"),
    Formula(Equal(Poles(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("be4b28"),
    Formula(Equal(EssentialSingularities(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("184c11"),
    Formula(Equal(BranchPoints(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("b62d05"),
    Formula(Equal(BranchCuts(Exp(z), z, CC), Set())))

make_entry(ID("bceb84"),
    Formula(Equal(Zeros(Exp(z), z, Element(z, CC)), Set())))

make_entry(ID("1635f5"),
    Formula(Equal(Exp(z), Sum(z**k/Factorial(k), Tuple(k, 0, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("bad502"),
    Formula(Equal(Exp(c+z), Exp(c) * Sum(z**k/Factorial(k), Tuple(k, 0, Infinity)))),
    Variables(c, z),
    Assumptions(And(Element(c, CC), Element(z, CC))))

make_entry(ID("935b2f"),
    Formula(Equal(Integral(Exp(z), Tuple(z, a, b)), Exp(b) - Exp(a))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("96af56"),
    Formula(Equal(Derivative(Exp(z), Tuple(z, z, 1)), Exp(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("4491b8"),
    Formula(Equal(Derivative(Exp(z), Tuple(z, z, n)), Exp(z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(0)))))


make_entry(ID("1568e1"),
    Formula(Equal(Exp(z), Cosh(z) + Sinh(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e103e7"),
    Formula(Equal(Exp(ConstI*z), Cos(z) + ConstI*Sin(z))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("1b3014"),
    Formula(Equal(Abs(Exp(z)), Exp(Re(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("caf706"),
    Formula(Equal(Sign(Exp(z)), Exp(Im(z)*ConstI))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("b7d62b"),
    Formula(Equal(Re(Exp(z)), Exp(Re(z))*Cos(Im(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e2fac7"),
    Formula(Equal(Im(Exp(z)), Exp(Re(z))*Sin(Im(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("a0d93c"),
    Formula(Equal(Arg(Exp(z)), Im(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(Im(z), OpenClosedInterval(-ConstPi, ConstPi)))))

make_entry(ID("52d827"),
    Formula(Equal(Exp(Conjugate(z)), Conjugate(Exp(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Approximations

make_entry(ID("3c4480"),
    Formula(LessEqual(Abs(Exp(z) - Sum(z**k/Factorial(k), Tuple(k, 0, N-1))),
        Abs(z)**N/(Factorial(N)*(1-Abs(z)/N)))),
    Variables(z, N),
    Assumptions(And(Element(z, CC), Element(N, ZZ), Greater(N, Abs(z)))))

# Bounds and inequalities

make_entry(ID("2f57ad"),
    Formula(LessEqual(Abs(Exp(z)), Exp(Abs(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("3ac8a5"),
    Formula(LessEqual(Abs(Exp(x+a)-Exp(x)), Exp(x)*(Exp(Abs(a))-1))),
    Variables(x, a),
    Assumptions(And(Element(x, RR), Element(a, RR))))


