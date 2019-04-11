# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Gamma function"),
#    DefinitionsTable(GammaFunction, LogGamma),
#    Section("Definitions"),
    Entries(
        "09e2ed",
        "c6038c",
    ),
    Section("Particular values"),
    Entries(
        "f1d31a",
        "e68d11",
        "19d480",
        "f826a6",
        "48ac55",
    ),
    Section("Functional equations"),
    Entries(
        "78f1f4",
        "639d91",
        "14af98",
        "56d710",
        "b510b6",
        "a787eb",
        "90a1e1",
        "a26ac7",
        "774d37",
    ),
    Section("Integral representations"),
    Entries(
        "4e4e0f",
    ),
    Section("Series expansions"),
    Entries(
        "661054",
        "37a95a",
        "8cf1fd",
        "53a2a1",
    ),
    Section("Analytic properties"),
    Entries(
        "798c5d",
        "2870f0",
        "34d6ae",
        "d086bd",
        "9a44c5",
        "a76328",
    ),
    Section("Complex parts"),
    Entries(
        "d7d2a0",
    ),
)


make_entry(ID("09e2ed"),
    SymbolDefinition(GammaFunction, GammaFunction(z), "Gamma function"),
    Description("The gamma function", GammaFunction(z), "is a function of one complex variable", z,
        ". It is a meromorphic function with simple poles at the nonpositive integers and no zeros.",
        "It can be defined by the integral representation", EntryReference("4e4e0f"),
        "in the right half-plane, together with the functional equation", EntryReference("78f1f4"), "for analytic continuation.",
        "The following table lists all conditions such that", SourceForm(GammaFunction(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, ZZGreaterEqual(1)), Element(GammaFunction(z), ZZGreaterEqual(1))),
        Tuple(Element(z, OpenInterval(0, Infinity)), Element(GammaFunction(z), OpenInterval(Decimal("0.8856"), Infinity))),
        Tuple(Element(z, SetMinus(RR, ZZLessEqual(0))), Element(GammaFunction(z), SetMinus(RR, Set(0)))),
        Tuple(Element(z, SetMinus(CC, ZZLessEqual(0))), Element(GammaFunction(z), SetMinus(CC, Set(0)))),
        TableSection("Infinities"),
        Tuple(Element(z, ZZLessEqual(0)), Element(GammaFunction(z), Set(UnsignedInfinity))),
        Tuple(Element(z, Set(Infinity)), Element(GammaFunction(z), Set(Infinity))),
        Tuple(Element(z, Set(ConstI*Infinity, -(ConstI*Infinity))), Element(GammaFunction(z), Set(0))),
        TableSection("Formal power series"),
        Tuple(And(Element(z, FormalPowerSeries(RR, x)), NotElement(SeriesCoefficient(z, x, 0), ZZLessEqual(0))),
            And(Element(GammaFunction(z), FormalPowerSeries(RR, x)), Unequal(SeriesCoefficient(GammaFunction(z), x, 0), 0))),
        Tuple(And(Element(z, FormalPowerSeries(CC, x)), NotElement(SeriesCoefficient(z, x, 0), ZZLessEqual(0))),
            And(Element(GammaFunction(z), FormalPowerSeries(CC, x)), Unequal(SeriesCoefficient(GammaFunction(z), x, 0), 0))),
        Tuple(And(Element(z, FormalLaurentSeries(RR, x)), NotElement(z, ZZLessEqual(0))),
            Element(GammaFunction(z), FormalLaurentSeries(RR, x))),
        Tuple(And(Element(z, FormalLaurentSeries(CC, x)), NotElement(z, ZZLessEqual(0))),
            Element(GammaFunction(z), FormalLaurentSeries(CC, x))),
      )),
    )

make_entry(ID("c6038c"),
    SymbolDefinition(LogGamma, LogGamma(z), "Logarithmic gamma function"),
    Description("The logarithmic gamma function", LogGamma(z), "is a function of one complex variable", z, ".",
        "It satisfies", Equal(LogGamma(x), Log(GammaFunction(x))), "for real", Greater(x, 0), "and is defined on the complex plane",
        "through analytic continuation, with branch cuts on", OpenClosedInterval(-Infinity, 0), ".",
        "An explicit construction uses", EntryReference("37a95a"), "combined with", EntryReference("774d37"), "for analytic continuation.",
        "In general,", Unequal(LogGamma(z), Log(GammaFunction(z))), " as the latter has an infinite set of branch cuts off the real line.",
        "The following table lists all conditions such that", SourceForm(LogGamma(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, OpenInterval(0, Infinity)), Element(LogGamma(z), OpenInterval(Decimal("-0.1215"), Infinity))),
        Tuple(Element(z, SetMinus(CC, ZZLessEqual(0))), Element(LogGamma(z), CC)),
        TableSection("Infinities"),
        Tuple(Element(z, Set(Infinity)), Element(LogGamma(z), Set(Infinity))),
        TableSection("Formal power series"),
        Tuple(And(Element(z, FormalPowerSeries(RR, x)), Greater(SeriesCoefficient(z, x, 0), 0)),
            And(Element(LogGamma(z), FormalPowerSeries(RR, x)))),
        Tuple(And(Element(z, FormalPowerSeries(CC, x)), NotElement(SeriesCoefficient(z, x, 0), ZZLessEqual(0))),
            And(Element(LogGamma(z), FormalPowerSeries(CC, x)))),
      )),
    )


GammaFunction_domain = SetMinus(CC, ZZLessEqual(0))
GammaFunction_sub1_domain = SetMinus(CC, ZZLessEqual(1))



make_entry(ID("f1d31a"),
    Formula(Equal(GammaFunction(n), Factorial(n-1))),
    Variables(n),
    Assumptions(Element(n, GammaFunction_domain)))

make_entry(ID("e68d11"),
    Formula(Equal(GammaFunction(1), 1)))

make_entry(ID("19d480"),
    Formula(Equal(GammaFunction(2), 1)))

make_entry(ID("f826a6"),
    Formula(Equal(GammaFunction(Div(1,2)), Sqrt(ConstPi))))

make_entry(ID("48ac55"),
    Formula(Equal(GammaFunction(Div(3,2)), Sqrt(ConstPi)/2)))

make_entry(ID("78f1f4"),
    Formula(Equal(GammaFunction(z+1), z * GammaFunction(z))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_domain)))

make_entry(ID("639d91"),
    Formula(Equal(GammaFunction(z), (z-1) * GammaFunction(z-1))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_sub1_domain)))

make_entry(ID("14af98"),
    Formula(Equal(GammaFunction(z-1), GammaFunction(z) / (z-1))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_sub1_domain)))

make_entry(ID("56d710"),
    Formula(Equal(GammaFunction(z+n), RisingFactorial(z, n) * GammaFunction(z))),
    Variables(z, n),
    Assumptions(And(Element(z, GammaFunction_domain), Element(n, ZZGreaterEqual(0)))))



make_entry(ID("b510b6"),
    Formula(Equal(GammaFunction(z), (ConstPi/Sin(ConstPi*z)) * (1/GammaFunction(1-z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZ))))

make_entry(ID("a787eb"),
    Formula(Equal(GammaFunction(z) * GammaFunction(z+Div(1,2)), 2**(1-2*z) * Sqrt(ConstPi) * GammaFunction(2*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(2*z, ZZLessEqual(0)))))

make_entry(ID("90a1e1"),
    Formula(Equal(Product(GammaFunction(z+Div(k,m)), Tuple(k, 0, m-1)), (2*pi)**((m-1)/2) * m**(Div(1,2)-m*z) * GammaFunction(m*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(m, ZZGreaterEqual(1)), NotElement(m*z, ZZLessEqual(0)))))


make_entry(ID("a26ac7"),
    Formula(Equal(GammaFunction(z), Exp(LogGamma(z)))),
    Variables(z),
    Assumptions(And(Element(z, GammaFunction_domain))))

make_entry(ID("774d37"),
    Formula(Equal(LogGamma(z+1), LogGamma(z) + Log(z))),
    Variables(z),
    Assumptions(And(Element(z, GammaFunction_domain))))


make_entry(ID("4e4e0f"),
    Formula(Equal(GammaFunction(z), Integral(t**(z-1) * Exp(-t), Tuple(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("661054"),
    Formula(Equal(LogGamma(1+z), -(ConstGamma*z) + Sum(RiemannZeta(k)/k * (-z)**k, Tuple(k, 2, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("37a95a"),
    Formula(Equal(LogGamma(z), (z-Div(1,2))*Log(z) - z + Log(2*ConstPi)/2
        + Sum(BernoulliB(2*k)/(2*k*(2*k-1)*z**(2*k-1)), Tuple(k, 1, n-1)) + StirlingSeriesRemainder(n, z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("8cf1fd"),
    SymbolDefinition(StirlingSeriesRemainder, StirlingSeriesRemainder(n, z), "Remainder term in the Stirling series for the logarithmic gamma function"))

make_entry(ID("53a2a1"),
    Formula(Equal(StirlingSeriesRemainder(n, z), Integral((BernoulliB(2*n) - BernoulliPolynomial(2*n, t-Floor(t)))/(2*n*(z+t)**(2*n)), Tuple(t, 0, Infinity)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("798c5d"),
    Formula(Equal(HolomorphicDomain(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), GammaFunction_domain)))

make_entry(ID("2870f0"),
    Formula(Equal(Poles(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), ZZLessEqual(0))))

make_entry(ID("34d6ae"),
    Formula(Equal(EssentialSingularities(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("d086bd"),
    Formula(Equal(BranchPoints(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("9a44c5"),
    Formula(Equal(BranchCuts(GammaFunction(z), z, CC), Set())))

make_entry(ID("a76328"),
    Formula(Equal(Zeros(GammaFunction(z), z, CC), Set())))

make_entry(ID("d7d2a0"),
    Formula(Equal(GammaFunction(Conjugate(z)), Conjugate(GammaFunction(z)))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_domain)))

