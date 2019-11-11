# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Gamma function"),
    Section("Definitions"),
    Entries(
        "09e2ed",
        "c6038c",
    ),
    Section("Illustrations"),
    Entries(
        "7ddf69",
        "aa967b",
        "b0f293",
        "c7d4c2",
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
        "6d0a95",
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
    Section("Bounds and inequalities"),
    SeeTopics("Bounds and inequalities for the gamma function"),
    Entries(
        "a0ca3e",
        "b7fec0",
    ),
    Section("Representation of other functions"),
    Subsection("Factorials and binomial coefficients"),
    Entries(
        "62c6c9", # included from factorials
        "e87c43", # included from factorials
        "c733f7", # included from factorials
    ),
    Subsection("Beta function"),
    Entries(
        "888581", # included from beta
    ),
    Subsection("Elementary functions"),
    Entries(
        "d38a03", # included from sine
        "b7a578",
        "ee56b9",
        "d16cb4",
        "6430cc",
    ),
)


make_entry(ID("09e2ed"),
    SymbolDefinition(Gamma, Gamma(z), "Gamma function"),
    Description("The gamma function", Gamma(z), "is a function of one complex variable", z,
        ". It is a meromorphic function with simple poles at the nonpositive integers and no zeros.",
        "It can be defined by the integral representation", EntryReference("4e4e0f"),
        "in the right half-plane, together with the functional equation", EntryReference("78f1f4"), "for analytic continuation.",
        "The following table lists all conditions such that", SourceForm(Gamma(z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, ZZGreaterEqual(1)), Element(Gamma(z), ZZGreaterEqual(1))),
        Tuple(Element(z, OpenInterval(0, Infinity)), Element(Gamma(z), OpenInterval(Decimal("0.8856"), Infinity))),
        Tuple(Element(z, SetMinus(RR, ZZLessEqual(0))), Element(Gamma(z), SetMinus(RR, Set(0)))),
        Tuple(Element(z, SetMinus(CC, ZZLessEqual(0))), Element(Gamma(z), SetMinus(CC, Set(0)))),
        TableSection("Infinities"),
        Tuple(Element(z, ZZLessEqual(0)), Element(Gamma(z), Set(UnsignedInfinity))),
        Tuple(Element(z, Set(Infinity)), Element(Gamma(z), Set(Infinity))),
        Tuple(Element(z, Set(ConstI*Infinity, -(ConstI*Infinity))), Element(Gamma(z), Set(0))),
        TableSection("Formal power series"),
        Tuple(And(Element(z, FormalPowerSeries(RR, x)), NotElement(SeriesCoefficient(z, x, 0), ZZLessEqual(0))),
            And(Element(Gamma(z), FormalPowerSeries(RR, x)), Unequal(SeriesCoefficient(Gamma(z), x, 0), 0))),
        Tuple(And(Element(z, FormalPowerSeries(CC, x)), NotElement(SeriesCoefficient(z, x, 0), ZZLessEqual(0))),
            And(Element(Gamma(z), FormalPowerSeries(CC, x)), Unequal(SeriesCoefficient(Gamma(z), x, 0), 0))),
        Tuple(And(Element(z, FormalPowerSeries(RR, x)), NotElement(z, ZZLessEqual(0))),
            Element(Gamma(z), FormalLaurentSeries(RR, x))),
        Tuple(And(Element(z, FormalPowerSeries(CC, x)), NotElement(z, ZZLessEqual(0))),
            Element(Gamma(z), FormalLaurentSeries(CC, x))),
      )),
    )

make_entry(ID("c6038c"),
    SymbolDefinition(LogGamma, LogGamma(z), "Logarithmic gamma function"),
    Description("The logarithmic gamma function", LogGamma(z), "is a function of one complex variable", z, ".",
        "It satisfies", Equal(LogGamma(x), Log(Gamma(x))), "for real", Greater(x, 0), "and is defined on the complex plane",
        "through analytic continuation, with branch cuts on", OpenClosedInterval(-Infinity, 0), ".",
        "An explicit construction uses", EntryReference("37a95a"), "combined with", EntryReference("774d37"), "for analytic continuation.",
        "In general,", Unequal(LogGamma(z), Log(Gamma(z))), " as the latter has an infinite set of branch cuts off the real line.",
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


make_entry(ID("7ddf69"),
    Image(Description("Plot of", Gamma(x), "on", Element(x, ClosedInterval(-4,4))),
        ImageSource("plot_gamma"))
    )

make_entry(ID("aa967b"),
    Image(Description("Plot of", LogGamma(x), "on", Element(x, ClosedInterval(-4,4))),
        ImageSource("plot_log_gamma"))
    )

make_entry(ID("b0f293"),
    Image(Description("X-ray of", Gamma(z), "on", Element(z, ClosedInterval(-5,5) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_gamma")),
    description_xray,
    )

make_entry(ID("c7d4c2"),
    Image(Description("X-ray of", LogGamma(z), "on", Element(z, ClosedInterval(-5,5) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_log_gamma")),
    description_xray,
    )


Gamma_domain = SetMinus(CC, ZZLessEqual(0))
Gamma_sub1_domain = SetMinus(CC, ZZLessEqual(1))




make_entry(ID("f1d31a"),
    Formula(Equal(Gamma(n), Factorial(n-1))),
    Variables(n),
    Assumptions(Element(n, Gamma_domain)))

make_entry(ID("e68d11"),
    Formula(Equal(Gamma(1), 1)))

make_entry(ID("19d480"),
    Formula(Equal(Gamma(2), 1)))

make_entry(ID("f826a6"),
    Formula(Equal(Gamma(Div(1,2)), Sqrt(Pi))))

make_entry(ID("48ac55"),
    Formula(Equal(Gamma(Div(3,2)), Sqrt(Pi)/2)))

make_entry(ID("78f1f4"),
    Formula(Equal(Gamma(z+1), z * Gamma(z))),
    Variables(z),
    Assumptions(Element(z, Gamma_domain)))

make_entry(ID("639d91"),
    Formula(Equal(Gamma(z), (z-1) * Gamma(z-1))),
    Variables(z),
    Assumptions(Element(z, Gamma_sub1_domain)))

make_entry(ID("14af98"),
    Formula(Equal(Gamma(z-1), Gamma(z) / (z-1))),
    Variables(z),
    Assumptions(Element(z, Gamma_sub1_domain)))

make_entry(ID("56d710"),
    Formula(Equal(Gamma(z+n), RisingFactorial(z, n) * Gamma(z))),
    Variables(z, n),
    Assumptions(And(Element(z, Gamma_domain), Element(n, ZZGreaterEqual(0)))))



make_entry(ID("b510b6"),
    Formula(Equal(Gamma(z), (Pi/Sin(Pi*z)) * (1/Gamma(1-z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZ))))

make_entry(ID("a787eb"),
    Formula(Equal(Gamma(z) * Gamma(z+Div(1,2)), 2**(1-2*z) * Sqrt(Pi) * Gamma(2*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(2*z, ZZLessEqual(0)))))

make_entry(ID("90a1e1"),
    Formula(Equal(Product(Gamma(z+Div(k,m)), For(k, 0, m-1)), (2*pi)**((m-1)/2) * m**(Div(1,2)-m*z) * Gamma(m*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(m, ZZGreaterEqual(1)), NotElement(m*z, ZZLessEqual(0)))))


make_entry(ID("a26ac7"),
    Formula(Equal(Gamma(z), Exp(LogGamma(z)))),
    Variables(z),
    Assumptions(And(Element(z, Gamma_domain))))

make_entry(ID("774d37"),
    Formula(Equal(LogGamma(z+1), LogGamma(z) + Log(z))),
    Variables(z),
    Assumptions(And(Element(z, Gamma_domain))))



make_entry(ID("4e4e0f"),
    Formula(Equal(Gamma(z), Integral(t**(z-1) * Exp(-t), For(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("661054"),
    Formula(Equal(LogGamma(1+z), -(ConstGamma*z) + Sum(RiemannZeta(k)/k * (-z)**k, For(k, 2, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("37a95a"),
    Formula(Equal(LogGamma(z), (z-Div(1,2))*Log(z) - z + Log(2*Pi)/2
        + Sum(BernoulliB(2*k)/(2*k*(2*k-1)*z**(2*k-1)), For(k, 1, n-1)) + StirlingSeriesRemainder(n, z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("8cf1fd"),
    SymbolDefinition(StirlingSeriesRemainder, StirlingSeriesRemainder(n, z), "Remainder term in the Stirling series for the logarithmic gamma function"))

make_entry(ID("53a2a1"),
    Formula(Equal(StirlingSeriesRemainder(n, z), Integral((BernoulliB(2*n) - BernoulliPolynomial(2*n, t-Floor(t)))/(2*n*(z+t)**(2*n)), For(t, 0, Infinity)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("6d0a95"),
    Formula(Equal(Gamma(z), (2*Pi)**Div(1,2) * z**(z-Div(1,2)) * Exp(-z) * Exp(Sum((z+n-Div(1,2))*Log((z+n)/(z+n-1))-1, For(n, 1, Infinity))))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, 0)))),
    References("B. C. Carlson (1977), Special functions of applied mathematics, Academic Press. Proposition 3.8-1."))


make_entry(ID("798c5d"),
    Formula(IsHolomorphic(Gamma(z), ForElement(z, Gamma_domain))))

make_entry(ID("2870f0"),
    Formula(Equal(Poles(Gamma(z), ForElement(z, Union(CC, Set(UnsignedInfinity)))), ZZLessEqual(0))))

make_entry(ID("34d6ae"),
    Formula(Equal(EssentialSingularities(Gamma(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("d086bd"),
    Formula(Equal(BranchPoints(Gamma(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("9a44c5"),
    Formula(Equal(BranchCuts(Gamma(z), z, CC), Set())))

make_entry(ID("a76328"),
    Formula(Equal(Zeros(Gamma(z), ForElement(z, CC)), Set())))

make_entry(ID("d7d2a0"),
    Formula(Equal(Gamma(Conjugate(z)), Conjugate(Gamma(z)))),
    Variables(z),
    Assumptions(Element(z, Gamma_domain)))

# Representation of other functions

make_entry(ID("ee56b9"),
    Formula(Equal(Tan(Pi*z), (Gamma(Div(1,2)+z) * Gamma(Div(1,2)-z)) / (Gamma(z)*Gamma(1-z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("b7a578"),
    Formula(Equal(Cos(Pi * z), Pi / (Gamma(Div(1,2)+z) * Gamma(Div(1,2)-z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("d16cb4"),
    Formula(Equal(Sinc(Pi * z), 1 / (Gamma(1+z) * Gamma(1-z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("6430cc"),
    Formula(Equal(Exp(Pi * z), Pi * (1/(Gamma(Div(1,2)+ConstI*z) * Gamma(Div(1,2)-ConstI*z)) + z/(Gamma(1+ConstI*z)*Gamma(1-ConstI*z))))),
#    Formula(Equal(Exp(Pi * z), Pi * (1/(Gamma(Div(1,2)+ConstI*z) * Gamma(Div(1,2)-ConstI*z)) - ConstI/(Gamma(ConstI*z)*Gamma(1-ConstI*z))))),
    Variables(z),
    Assumptions(Element(z, CC)))


def_Topic(
    Title("Bounds and inequalities for the gamma function"),
    SeeTopics("Gamma function"),
    Section("Real argument"),
    Entries(
        "1bbbc7",
        "e010c9",
        "b05f2b",
        "2a47d7",
        "a0ca3e",
        "2398a1",
        "99a9c6",
    ),
    Section("Complex argument"),
    Entries(
        "f50ec9",
        "143002",
        "b7fec0",
        "80f7dc",
        "931d89",
        "1976db",
        "c7b921",
        "94db60",
        "513a30",
        "4a2ac8",
        "dd5e3a",
        "e0b322",
        "7af1b9",
        "06260c",
    ),
    Section("Derivatives"),
    Entries(
        "cb5071",
    ),
),

make_entry(ID("1bbbc7"),
    Formula(Element(ArgMinUnique(Gamma(x), ForElement(x, OpenInterval(0, Infinity))), RealBall(Decimal("1.46163214496836234126265954233"), Decimal("4.28e-30")))))

make_entry(ID("e010c9"),
    Formula(Element(Minimum(Gamma(x), ForElement(x, OpenInterval(0, Infinity))), RealBall(Decimal("0.885603194410888700278815900583"), Decimal("4.12e-31")))))

make_entry(ID("b05f2b"),
    Formula(Element(Minimum(LogGamma(x), ForElement(x, OpenInterval(0, Infinity))), RealBall(Decimal("-0.121486290535849608095514557178"), Decimal("3.09e-31")))))

make_entry(ID("2a47d7"),
    Formula(Greater(Gamma(x), (2*Pi)**Div(1,2) * x**(x-Div(1,2)) * Exp(-x))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))))

make_entry(ID("a0ca3e"),
    Formula(Less(Gamma(x), (2*Pi)**Div(1,2) * x**(x-Div(1,2)) * Exp(-x) * Exp(1/(12*x)))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))))

make_entry(ID("2398a1"),
    Formula(Greater(LogGamma(x), (x-Div(1,2))*Log(x)-x+Log(2*Pi)/2 + Sum(BernoulliB(2*k)/(2*k*(2*k-1)*x**(2*k-1)), For(k, 1, 2*n)))),
    Variables(x, n),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(n, ZZGreaterEqual(0)))),
    References("H. Alzer, On some inequalities for the gamma and psi functions, Math. Comp. 66(217), pp. 373-389. Theorem 8."))

make_entry(ID("99a9c6"),
    Formula(Less(LogGamma(x), (x-Div(1,2))*Log(x)-x+Log(2*Pi)/2 + Sum(BernoulliB(2*k)/(2*k*(2*k-1)*x**(2*k-1)), For(k, 1, 2*n+1)))),
    Variables(x, n),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(n, ZZGreaterEqual(0)))),
    References("H. Alzer, On some inequalities for the gamma and psi functions, Math. Comp. 66(217), pp. 373-389. Theorem 8."))

make_entry(ID("f50ec9"),
    Formula(Greater(Abs(Gamma(z)), 0)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("143002"),
    Formula(Less(Abs(1/Gamma(z)), Infinity)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("b7fec0"),
    Formula(Where(LessEqual(Abs(Gamma(z)), (2*Pi)**Div(1,2) * Abs(z)**(x-Div(1,2)) * Exp(-(Pi*Abs(y)/2)) * Exp(Div(1,6*Abs(z)))), Equal(z, x+y*ConstI))),
    Variables(x, y),
    Assumptions(And(Element(x, ClosedOpenInterval(0, Infinity)), Element(y, RR), Unequal(x+y*ConstI, 0))),
    References("R. B. Paris and D. Kaminski (2001), Asymptotics of Mellin-Barnes integrals, Cambridge University Press. (2.1.19), p. 34."))

make_entry(ID("80f7dc"),
    Formula(LessEqual(Abs(Gamma(z)), (2*Pi)**Div(1,2) * Abs(z**(z-Div(1,2)) * Exp(-z)) * Exp(Div(1,6*Abs(z))))),
    Variables(z),
    Assumptions(And(Element(z, CC), GreaterEqual(Re(z), 0), Unequal(z, 0))),
    References("R. B. Paris and D. Kaminski (2001), Asymptotics of Mellin-Barnes integrals, Cambridge University Press. (2.1.18), p. 34."))

make_entry(ID("931d89"),
    Formula(GreaterEqual(Abs(Gamma(z)), (2*Pi)**Div(1,2) * Abs(z**(z-Div(1,2)) * Exp(-z)) * Exp(-Div(1,6*Abs(z))))),
    Variables(z),
    Assumptions(And(Element(z, CC), GreaterEqual(Re(z), 0), Unequal(z, 0))))


make_entry(ID("1976db"),
    Formula(Equal(Abs(Gamma(y*ConstI)), Sqrt(Pi/(y*Sinh(Pi*y))))),
    Variables(y),
    Assumptions(Element(y, SetMinus(RR, Set(0)))))

make_entry(ID("c7b921"),
    Formula(Equal(Abs(Gamma(Div(1,2)+y*ConstI)), Sqrt(Pi/(Cosh(Pi*y))))),
    Variables(y),
    Assumptions(Element(y, RR)))

make_entry(ID("94db60"),
    Formula(Equal(Abs(Gamma(1+y*ConstI)), Sqrt((Pi*y/(Sinh(Pi*y)))))),
    Variables(y),
    Assumptions(Element(y, SetMinus(RR, Set(0)))))

make_entry(ID("513a30"),
    Formula(Equal(Abs(Gamma(x+y*ConstI)), Abs(Gamma(x)) * Product((1+y**2/(x+k)**2)**(-Div(1,2)), For(k, 0, Infinity)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR), NotElement(x+y*ConstI, ZZLessEqual(0)))),
    References("Abramowitz & Stegun 6.1.25"))

make_entry(ID("4a2ac8"),
    Formula(LessEqual(Abs(Gamma(x+y*ConstI)), Abs(Gamma(x)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))),
    References("B. C. Carlson (1977), Special functions of applied mathematics, Academic Press. Inequality 3.10-3."))

make_entry(ID("dd5e3a"),
    Formula(Less(Abs(Gamma(x+y*ConstI)), Abs(Gamma(x+t*ConstI)))),
    Variables(x, y, t),
    Assumptions(And(Element(x, RR), Element(y, RR), Element(t, RR), Greater(Abs(y), Abs(t)))))

make_entry(ID("e0b322"),
    Formula(GreaterEqual(Abs(Gamma(x+y*ConstI)), Gamma(x) / Sqrt(Cosh(Pi*y)))),
    Variables(x, y),
    Assumptions(And(Element(x, ClosedOpenInterval(Div(1,2),Infinity)), Element(y, RR))),
    References("B. C. Carlson (1977), Special functions of applied mathematics, Academic Press. Inequality 3.10-4."))

make_entry(ID("7af1b9"),
    Formula(GreaterEqual(Abs(Gamma(x+y*ConstI)), Gamma(x) * Exp(-(Pi*Abs(y)/2)))),
    Variables(x, y),
    Assumptions(And(Element(x, ClosedOpenInterval(Div(1,2),Infinity)), Element(y, RR))),
    References("B. C. Carlson (1977), Special functions of applied mathematics, Academic Press. Inequality 3.10-4."))

make_entry(ID("06260c"),
    Formula(LessEqual(Abs(1/Gamma(z)), Where(Exp(Pi*R/2) * R**(R+Div(1,2)), Equal(R, Abs(z))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("cb5071"),
    Formula(LessEqual(Abs((1/Factorial(n)) * ComplexDerivative(1/Gamma(x), For(x, 0, n))), 2/Sqrt(Factorial(n)))),
    #Formula(Where(LessEqual(Abs(SeriesCoefficient(1/Gamma(x), x, n)), 2/Sqrt(Factorial(n))), Equal(x, Gen(FormalPowerSeries(RR, x))))),
    Variables(n),
    Assumptions(And(Element(n, ZZGreaterEqual(0)))),
    References("L. Fekih-Ahmed, On the Power Series Expansion of the Reciprocal Gamma Function, https://arxiv.org/abs/1407.5983 (simplified version of (1.5))"))

