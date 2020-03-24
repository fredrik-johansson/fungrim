# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Exponential function"),
    Section("Definitions"),
    Entries(
        "dfbcd9",
        "f758c6",
    ),
    Section("Illustrations"),
    Entries(
        "e74de0",
        "6ef3d1",
    ),
    Section("Domain and range"),
    Subsection("Numbers"),
    Entries(
        "be1092",
        "819b5f",
        "ca8b0a",
    ),
    Subsection("Infinities"),
    Entries(
        "66f4c8",
        "424db5",
    ),
    Subsection("Formal power series"),
    Entries(
        "a807a7",
        "0d82d4",
        "148f96",
    ),
    Subsection("Matrices"),
    Entries(
        "9e388b",
        "2ea614",
    ),
    Section("Particular values"),
    Entries(
        "27ca8d",
        "9a944c",
        "54aaf1",
        "a90f35",
        "bb7d22",
        "8f9143",
        "71a0b8",
        "e2b379",
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
        "296627",
        "987e3c",
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
    Description("In rendered formulas,", SourceForm(Exp(z)), "is shown as", Exp(z), "or as", Call(Exp, z), "depending on the typographical requirements; no semantic difference is implied."))

make_entry(ID("f758c6"),
    SymbolDefinition(ConstE, ConstE, "The constant e (2.718...)"),
    Description("The real number giving the base of the natural logarithm, also known as Euler's number."))

make_entry(ID("e74de0"),
    Image(Description("Plot of", Exp(x), "on", Element(x, ClosedInterval(-4,4))),
        ImageSource("plot_exp")),
    description_xray,
    )

make_entry(ID("6ef3d1"),
    Image(Description("X-ray of", Exp(z), "on", Element(z, ClosedInterval(-5,5) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_exp")),
    description_xray,
    )

# Domain and range

make_entry(ID("be1092"),
    Formula(Implies(Element(z, Set(0)), Element(Exp(z), Set(1)))),
    Variables(z))

make_entry(ID("819b5f"),
    Formula(Implies(Element(z, RR), Element(Exp(z), OpenInterval(0,Infinity)))),
    Variables(z))

make_entry(ID("ca8b0a"),
    Formula(Implies(Element(z, CC), Element(Exp(z), SetMinus(CC, Set(0))))),
    Variables(z))

make_entry(ID("66f4c8"),
    Formula(Implies(Element(z, Set(Infinity)), Element(Exp(z), Set(Infinity)))),
    Variables(z))

make_entry(ID("424db5"),
    Formula(Implies(Element(z, Set(-Infinity)), Element(Exp(z), Set(0)))),
    Variables(z))

make_entry(ID("a807a7"),
    Formula(Implies(And(Element(z, PowerSeries(QQ, SerX)), Equal(Coefficient(z, SerX, 0), 0)),
        And(Element(Exp(z), PowerSeries(QQ, SerX)), Equal(Coefficient(Exp(z), SerX, 0), 1)))),
    Variables(z))

make_entry(ID("0d82d4"),
    Formula(Implies(Element(z, PowerSeries(RR, SerX)),
        And(Element(Exp(z), PowerSeries(RR, SerX)), NotEqual(Coefficient(Exp(z), SerX, 0), 0)))),
    Variables(z))

make_entry(ID("148f96"),
    Formula(Implies(Element(z, PowerSeries(CC, SerX)),
            And(Element(Exp(z), PowerSeries(CC, SerX)), NotEqual(Coefficient(Exp(z), SerX, 0), 0)))),
    Variables(z))

make_entry(ID("9e388b"),
#    Formula(All(Element(Exp(A), GeneralLinearGroup(n, RR)), ForElement(A, Matrices(RR, n, n)))),
#    Variables(n),
#    Assumptions(Element(n, ZZGreaterEqual(0))))
    Formula(Implies(Element(A, Matrices(RR, n, n)), Element(Exp(A), GeneralLinearGroup(n, RR)))),
    Variables(A, n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("2ea614"),
#    Formula(All(Element(Exp(A), GeneralLinearGroup(n, CC)), ForElement(A, Matrices(CC, n, n)))),
#    Variables(n),
#    Assumptions(Element(n, ZZGreaterEqual(0))))
    Formula(Implies(Element(A, Matrices(CC, n, n)), Element(Exp(A), GeneralLinearGroup(n, CC)))),
    Variables(A, n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Particular values

make_entry(ID("27ca8d"),
    Formula(Equal(Exp(0), 1)))

make_entry(ID("9a944c"),
    Formula(Equal(Exp(1), ConstE)))

make_entry(ID("54aaf1"),
    Formula(Equal(Exp(Pi*ConstI), -1)))

make_entry(ID("a90f35"),
    Formula(Equal(Exp(Pi*ConstI/2), ConstI)))

make_entry(ID("bb7d22"),
    Formula(NotElement(ConstE, QQ)))

make_entry(ID("8f9143"),
    Formula(NotElement(ConstE, AlgebraicNumbers)))

make_entry(ID("71a0b8"),
    Formula(All(NotElement(Exp(alpha), QQ), ForElement(alpha, SetMinus(QQ, Set(0))))))

make_entry(ID("e2b379"),
    Formula(All(NotElement(Exp(alpha), AlgebraicNumbers), ForElement(alpha, SetMinus(AlgebraicNumbers, Set(0))))))

# Functional equations

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
    Formula(Equal(Exp(z+n*Pi*ConstI), (-1)**n * Exp(z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZ))))

make_entry(ID("1fa6b7"),
    Formula(Equal(Exp(z+2*n*Pi*ConstI), Exp(z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZ))))

make_entry(ID("296627"),
    Formula(Equal(Exp(Log(z)), z)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("987e3c"),
    Formula(Implies(Element(Im(z), OpenClosedInterval(-Pi, Pi)), Equal(Log(Exp(z)), z))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("28d158"),
    Formula(IsHolomorphic(Exp(z), ForElement(z, CC))))

make_entry(ID("0901a1"),
    Formula(Equal(Poles(Exp(z), ForElement(z, Union(CC, Set(UnsignedInfinity)))), Set())))

make_entry(ID("be4b28"),
    Formula(Equal(EssentialSingularities(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("184c11"),
    Formula(Equal(BranchPoints(Exp(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("b62d05"),
    Formula(Equal(BranchCuts(Exp(z), z, CC), Set())))

make_entry(ID("bceb84"),
    Formula(Equal(Zeros(Exp(z), ForElement(z, CC)), Set())))

make_entry(ID("1635f5"),
    Formula(Equal(Exp(z), Sum(z**k/Factorial(k), For(k, 0, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("bad502"),
    Formula(Equal(Exp(c+z), Exp(c) * Sum(z**k/Factorial(k), For(k, 0, Infinity)))),
    Variables(c, z),
    Assumptions(And(Element(c, CC), Element(z, CC))))

make_entry(ID("935b2f"),
    Formula(Equal(Integral(Exp(z), For(z, a, b)), Exp(b) - Exp(a))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("96af56"),
    Formula(Equal(ComplexDerivative(Exp(z), For(z, z, 1)), Exp(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("4491b8"),
    Formula(Equal(ComplexDerivative(Exp(z), For(z, z, n)), Exp(z))),
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
    Assumptions(And(Element(z, CC), Element(Im(z), OpenClosedInterval(-Pi, Pi)))))

make_entry(ID("52d827"),
    Formula(Equal(Exp(Conjugate(z)), Conjugate(Exp(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Approximations

make_entry(ID("3c4480"),
    Formula(LessEqual(Abs(Exp(z) - Sum(z**k/Factorial(k), For(k, 0, N-1))),
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


