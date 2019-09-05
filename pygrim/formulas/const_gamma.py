# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Euler's constant"),
    Entries(
        "39e0cb",
    ),
    Section("Numerical value"),
    Entries(
        "e876e8",
        "28bf9a",
    ),
    Section("Limit representations"),
    Entries(
        "4644c0",
    ),
    Section("Special function representations"),
    Subsection("Direct values"),
    Entries(
        "cf3977",
        "d17d0b",
    ),
    Subsection("Limits at singularities"),
    Entries(
        "a1f1ec",
        "79d6ba",
        "9d5c86",
        "0888b3",
        "e8af68",
    ),
    Subsection("Infinite series"),
    Entries(
        "818008",
    ),
    Section("Integral representations"),
    Entries(
        "39fe5f",
        "a1ca3e",
    ),
    Section("Approximations"),
    Entries(
        "014c4e",
    ),
    Section("Related topics"),
    SeeTopics("Gamma function", "Riemann zeta function"),
)

make_entry(ID("39e0cb"),
    SymbolDefinition(ConstGamma, ConstGamma, "The constant gamma (0.577...)"),
    Description("The real number giving the limiting difference between the harmonic series and the natural logarithm, also known as Euler's constant or the Euler-Mascheroni constant."))

make_entry(ID("e876e8"),
    Formula(Element(ConstGamma,
        RealBall(Decimal("0.57721566490153286060651209008240243104215933593992"), Decimal("3.60e-51")))))

make_entry(ID("4644c0"),
    Formula(Equal(ConstGamma, SequenceLimit(Sum(1/k, Tuple(k, 1, n)) - Log(n), n, Infinity))))

make_entry(ID("28bf9a"),
    Formula(NotElement(ConstGamma, SetBuilder(p/q, Tuple(p, q), And(Element(p,ZZ), Element(q, ZZGreaterEqual(1)), LessEqual(q, Pow(10,242080)))))),
    References("J. Havil (2003): Exploring Euler's Constant. Princeton University Press. Page 97."))

make_entry(ID("cf3977"),
    Formula(Equal(ConstGamma, -Derivative(GammaFunction(z), Tuple(z, 1, 1)))))

make_entry(ID("d17d0b"),
    Formula(Equal(ConstGamma, -DigammaFunction(1))))

make_entry(ID("a1f1ec"),
    Formula(Equal(ConstGamma, ComplexLimit(Brackets(RiemannZeta(s) - 1/(s-1)), s, 1))))

make_entry(ID("79d6ba"),
    Formula(Equal(ConstGamma, -ComplexLimit(Brackets(GammaFunction(z) - 1/z), z, 0))))

make_entry(ID("9d5c86"),
    Formula(Equal(ConstGamma, -ComplexLimit(Brackets(DigammaFunction(z) + 1/z), z, 0))))

make_entry(ID("0888b3"),
    Formula(Equal(ConstGamma, RightLimit(Brackets((ConstPi/2) * BesselY(0,x) - Log(x/2)), x, 0))))

make_entry(ID("e8af68"),
    Formula(Equal(ConstGamma, RightLimit(Brackets(-BesselK(0,x) - Log(x/2)), x, 0))))

make_entry(ID("818008"),
    Formula(Equal(ConstGamma, 1-Sum((RiemannZeta(k)-1) / k, Tuple(k, 2, Infinity)))))

make_entry(ID("39fe5f"),
    Formula(Equal(ConstGamma, -Integral(Exp(-x)*Log(x), Tuple(x, 0, Infinity)))))

make_entry(ID("a1ca3e"),
    Formula(Equal(ConstGamma, -Integral(Log(Log(1/x)), Tuple(x, 0, 1)))))

make_entry(ID("014c4e"),
    Formula(Where(Less(Abs(ConstGamma - (S/I - T/I**2 - Log(n))), 24*Exp(-(8*n))),
        Equal(Tuple(S, I, T), Tuple(Sum(HarmonicNumber(k) * n**(2*k) / Factorial(k)**2, Tuple(k, 0, 5*n)),
                Sum(n**(2*k) / Factorial(k)**2, Tuple(k, 0, 5*n)),
                Div(1,4*n) * Sum(Factorial(2*k)**3 / (Factorial(k)**4 * 8**(2*k) * (2*n)**(2*k)), Tuple(k, 0, 2*n-1)))))),
#    Formula(Where(Element(ConstGamma, RealBall(Parentheses(S/I - T/I**2 - Log(n)), 24*Exp(-(8*n)))),
#        Equal(Tuple(S, I, T), Tuple(Sum(HarmonicNumber(k) * n**(2*k) / Factorial(k)**2, Tuple(k, 0, N - 1)),
#                Sum(n**(2*k) / Factorial(k)**2, Tuple(k, 0, N - 1)),
#                Div(1,4*n) * Sum(Factorial(2*k)**3 / (Factorial(k)**4 * 8**(2*k) * (2*n)**(2*k)), Tuple(k, 0, 2*n-1)))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))),
    References("R. Brent and F. Johansson. A bound for the error term in the Brent-McMillan algorithm. Mathematics of Computation 2015, 84(295). DOI: 10.1090/S0025-5718-2015-02931-7"))

