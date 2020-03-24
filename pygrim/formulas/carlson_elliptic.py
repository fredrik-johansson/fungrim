# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Carlson symmetric elliptic integrals"),
    Section("Definitions"),
    Entries(
        "5cd377",
        "8f7c2a",
        "bac745",
        "663d75",
        "132ec5",
    ),
    Section("Integral representations"),
    Subsection("Defining algebraic integrals"),
    Entries(
        "9357b9",
        "dab889",
        "02a8d7",
        "944a14",
        "f3b8dc",
    ),
    Subsection("Trigonometric integrals"),
    Entries
    (
        "da16db",
        "7fbbe8",
        "9a0bc8",
        "8f0a91",
        "0d8639",
    ),
    Section("Domain"),
    Subsection("Complex variables"),
    Entries(
        "655f6b",
        "c90834",
        "8bac89",
        "ba7b32",
        "7aa9be",
    ),
    Subsection("Real variables"),
    Entries(
        "cc4cd8",
        "9c9173",
        "671fcb",
        "8236ff",
        "da33ce",
    ),
    Section("Representation of other functions"),
    Subsection("Legendre complete elliptic integrals"),
    Entries(
        "0cc11f",
        "6520e7",
        "9ccaef",
        "41cf8e",
        "94f646",
        "55d23d",
    ),
    Subsection("Legendre incomplete elliptic integrals"),
    Entries(
        "e2445d",
        "f48f54",
        "8f4e31",
    ),
    Section("Series representations"),
    Subsection("Definitions"),
    Entries(
        "b576e6",
        "a82bd6",
    ),
    Subsection("Incomplete integrals"),
    Entries(
        "8f71cb",
        "fda084",
        "b2cd79",
        "e93f43",
        "7ded8f",
        "42c7f1",
        "8d304b",
        "e1a3fb",
    ),
    Subsection("Complete integrals"),
    Entries(
        "cbcad9",
        "d0c9ff",
        "00c331",
        "37ffb7",
        "5a8f57",
        "7314c4",
        "b4a735",
    ),
    Subsection("General formulas for the series"),
    Entries(
        "da47f6",
        "4cb707",
        "2443de",
    ),
    Subsection("Symmetric formulas"),
    Entries(
        "13f252",
        "a21395",
        "0a7f30",
        "2c1df7",
        "b81ca0",
    ),
    Subsection("Integral representations"),
    Entries(
        "a1f7ea",
        "c5d388",
    ),
)


# Definitions

make_entry(ID("5cd377"),
    SymbolDefinition(CarlsonRF, CarlsonRF(x, y, z), "Carlson symmetric elliptic integral of the first kind"))

make_entry(ID("8f7c2a"),
    SymbolDefinition(CarlsonRG, CarlsonRG(x, y, z), "Carlson symmetric elliptic integral of the second kind"))

make_entry(ID("bac745"),
    SymbolDefinition(CarlsonRJ, CarlsonRJ(x, y, z, w), "Carlson symmetric elliptic integral of the third kind"))

# name? it is also an "integral of the second kind" (but not completely symmetric like RG)
make_entry(ID("663d75"),
    SymbolDefinition(CarlsonRD, CarlsonRD(x, y, z), "Special case of Carlson symmetric elliptic integral of the third kind"))

make_entry(ID("132ec5"),
    SymbolDefinition(CarlsonRC, CarlsonRC(x, y), "Carlson elementary elliptic integral"))

# Domain

make_entry(ID("655f6b"),
    Formula(Implies(And(Element(x, CC), Element(y, CC), Element(z, CC),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))),
        Element(CarlsonRF(x, y, z), CC))),
    Variables(x, y, z))

make_entry(ID("cc4cd8"),
    Formula(Implies(And(Element(x, ClosedOpenInterval(0, Infinity)),
                    Element(y, ClosedOpenInterval(0, Infinity)),
                    Element(z, ClosedOpenInterval(0, Infinity)),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))),
        Element(CarlsonRF(x, y, z), OpenInterval(0, Infinity)))),
    Variables(x, y, z))

make_entry(ID("c90834"),
    Formula(Implies(And(Element(x, CC), Element(y, CC), Element(z, CC)),
        Element(CarlsonRG(x, y, z), CC))),
    Variables(x, y, z))

make_entry(ID("9c9173"),
    Formula(Implies(And(Element(x, ClosedOpenInterval(0, Infinity)),
                    Element(y, ClosedOpenInterval(0, Infinity)),
                    Element(z, ClosedOpenInterval(0, Infinity))),
        Element(CarlsonRG(x, y, z), OpenInterval(0, Infinity)))),
    Variables(x, y, z))

make_entry(ID("8bac89"),
    Formula(Implies(And(
        Element(x, CC),
        Element(y, CC),
        Element(z, CC),
        Element(w, SetMinus(CC, Set(0))),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))),
        Element(CarlsonRJ(x, y, z, w), CC))),
    Variables(x, y, z, w))

make_entry(ID("671fcb"),
    Formula(Implies(And(
        Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, ClosedOpenInterval(0, Infinity)),
        Element(z, ClosedOpenInterval(0, Infinity)),
        Element(w, OpenInterval(0, Infinity)),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))),
        Element(CarlsonRJ(x, y, z, w), OpenInterval(0, Infinity)))),
    Variables(x, y, z, w))

make_entry(ID("7aa9be"),
    Formula(Implies(And(
        Element(x, CC),
        Element(y, SetMinus(CC, Set(0)))),
        Element(CarlsonRC(x, y), CC))),
    Variables(x, y))

make_entry(ID("da33ce"),
    Formula(Implies(And(
        Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, OpenInterval(0, Infinity))),
        Element(CarlsonRC(x, y), OpenInterval(0, Infinity)))),
    Variables(x, y))

make_entry(ID("ba7b32"),
    Formula(Implies(And(
        Element(x, CC),
        Element(y, CC),
        Element(z, SetMinus(CC, Set(0))),
        Or(NotEqual(x, 0), NotEqual(y, 0))),
        Element(CarlsonRD(x, y, z), CC))),
    Variables(x, y, z))

make_entry(ID("8236ff"),
    Formula(Implies(And(
        Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, ClosedOpenInterval(0, Infinity)),
        Element(z, OpenInterval(0, Infinity)),
        Or(NotEqual(x, 0), NotEqual(y, 0))),
        Element(CarlsonRD(x, y, z), OpenInterval(0, Infinity)))),
    Variables(x, y, z))

# Symmetry

# Interrepresentations

# Scaling

# Branch cuts?

# Special values -- including infinities

# Elementary cases

# Integral representations

make_entry(ID("9357b9"),
    Formula(Equal(CarlsonRF(x, y, z), Div(1,2) * Integral(1/(Sqrt(t+x)*Sqrt(t+y)*Sqrt(t+z)), For(t, 0, Infinity)))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))
    )))

make_entry(ID("dab889"),
    Formula(Equal(CarlsonRG(x, y, z), Div(1,4) * Integral(1/(Sqrt(t+x)*Sqrt(t+y)*Sqrt(t+z)) * (x/(t+x)+y/(t+y)+z/(t+z)), For(t, 0, Infinity)))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenInterval(-Infinity, 0))),
    )))

make_entry(ID("02a8d7"),
    Formula(Equal(CarlsonRJ(x, y, z, w), Div(3,2) * Integral(1/((t+w)*Sqrt(t+x)*Sqrt(t+y)*Sqrt(t+z)), For(t, 0, Infinity)))),
    Variables(x, y, z, w),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(w, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))
    )))

make_entry(ID("f3b8dc"),
    Formula(Equal(CarlsonRC(x, y), Div(1,2) * Integral(1/((t+y)*Sqrt(t+x)), For(t, 0, Infinity)))),
    Variables(x, y),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))
    )))

make_entry(ID("944a14"),
    Formula(Equal(CarlsonRD(x, y, z), Div(3,2) * Integral(1/((t+x)*(t+y)*(t+z)**Div(3,2)), For(t, 0, Infinity)))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Or(NotEqual(x, 0), NotEqual(y, 0))
    )))

make_entry(ID("da16db"),
    Formula(Equal(CarlsonRF(0, y, z), Integral(1/Sqrt(y*Cos(theta)**2 + z*Sin(theta)**2), For(theta, 0, Pi/2)))),
    Variables(y, z),
    Assumptions(And(
        Element(y, CC),
        Element(z, CC),
        Greater(Re(y), 0),
        Greater(Re(z), 0),
    )))

make_entry(ID("7fbbe8"),
    Formula(Equal(CarlsonRG(0, y, z), Div(1,2) * Integral(Sqrt(y*Cos(theta)**2 + z*Sin(theta)**2), For(theta, 0, Pi/2)))),
    Variables(y, z),
    Assumptions(And(
        Element(y, CC),
        Element(z, CC),
        GreaterEqual(Re(y), 0),
        GreaterEqual(Re(z), 0),
    )))

make_entry(ID("9a0bc8"),
    Formula(Equal(CarlsonRD(0, y, z), 3 * Integral(Sin(theta)**2/(y*Cos(theta)**2 + z*Sin(theta)**2)**Div(3,2), For(theta, 0, Pi/2)))),
    Variables(y, z),
    Assumptions(And(
        Element(y, CC),
        Element(z, CC),
        Greater(Re(y), 0),
        Greater(Re(z), 0),
    )))


# todo: Carlson gives a better condition: "the closed convex of hull {x,y,z} lies in the union of 0 and the cut plane" (plus at most one of x, y, z is 0)
make_entry(ID("8f0a91"),
    Formula(Equal(CarlsonRF(x, y, z), Div(1,4*Pi) * Integral(
        Integral(Sin(theta) / Sqrt(x*Sin(theta)**2*Cos(phi)**2 + y*Sin(theta)**2*Sin(phi)**2 + z*Cos(theta)**2), For(theta, 0, Pi)),
        For(phi, 0, 2*Pi)))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, CC),
        Element(y, CC),
        Element(z, CC),
        GreaterEqual(Re(x), 0),
        GreaterEqual(Re(y), 0),
        GreaterEqual(Re(z), 0),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))
    )))

# todo: Carlson gives a better condition: "the closed convex of hull {x,y,z} lies in the union of 0 and the cut plane"
make_entry(ID("0d8639"),
    Formula(Equal(CarlsonRG(x, y, z), Div(1,4*Pi) * Integral(
        Integral(Sqrt(x*Sin(theta)**2*Cos(phi)**2 + y*Sin(theta)**2*Sin(phi)**2 + z*Cos(theta)**2) * Sin(theta), For(theta, 0, Pi)),
        For(phi, 0, 2*Pi)))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, CC),
        Element(y, CC),
        Element(z, CC),
        GreaterEqual(Re(x), 0),
        GreaterEqual(Re(y), 0),
        GreaterEqual(Re(z), 0),
    )))

# Functional equations


# TODO: both lemniscate constants (check symbolic evaluation)

# Series representations

make_entry(ID("b576e6"),
    SymbolDefinition(CarlsonHypergeometricR, CarlsonHypergeometricR(-a, b, z), "Carlson multivariate hypergeometric function"),
    References("https://dlmf.nist.gov/19.19",
        "https://doi.org/10.6028/jres.107.034"
    ))

make_entry(ID("a82bd6"),
    SymbolDefinition(CarlsonHypergeometricT, CarlsonHypergeometricT(N, b, z), "Term in expansion of Carlson multivariate hypergeometric function"))

make_entry(ID("13f252"),
    Formula(Where(Equal(CarlsonHypergeometricR(-a, List(Repeat(beta, n)), List(z_(k), For(k, 1, n))),
        A**(-a) * CarlsonHypergeometricR(-a, List(Repeat(beta, n)), List(z_(k) / A, For(k, 1, n)))),
        Def(A, (1/n) * Sum(z_(k), For(k, 1, n))))),
    Variables(a, beta, z, n),
    Assumptions(And(Element(a, RR),
        Element(beta, OpenInterval(0, Infinity)),
        Element(n, ZZGreaterEqual(1)),
        All(And(Element(z_(k), CC), Less(Abs(1 - n * z_(k) / Sum(z_(j), For(j, 1, n))), 1)), ForElement(k, Range(1, n))))))

make_entry(ID("4cb707"),
    Formula(Where(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        Sum(RisingFactorial(a, N) / RisingFactorial(c, N) * CarlsonHypergeometricT(N, List(b_(k), For(k, 1, n)), List(1 - z_(k), For(k, 1, n))),
            For(N, 0, Infinity))), Def(c, Sum(b_(k), For(k, 1, n))))),
    Variables(a, b, z, n),
    Assumptions(And(Element(a, RR), Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(And(Element(z_(k), CC), Less(Abs(1 - z_(k)), 1)), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), 0))))

make_entry(ID("2443de"),
    Formula(Where(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        z_(n)**(-a) * 
        Sum(RisingFactorial(a, N) / RisingFactorial(c, N) * CarlsonHypergeometricT(N, List(b_(k), For(k, 1, n - 1)), List(1 - z_(k) / z_(n), For(k, 1, n - 1))),
            For(N, 0, Infinity))), Def(c, Sum(b_(k), For(k, 1, n))))),
    Variables(a, b, z, n),
    Assumptions(And(Element(a, RR), Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        Element(z_(n), SetMinus(CC, Set(0))),
        All(And(Element(z_(k), CC), Less(Abs(1 - z_(k) / z_(n)), 1)), ForElement(k, Range(1, n - 1))),
        Greater(Sum(b_(k), For(k, 1, n)), 0))))

make_entry(ID("a21395"),
    Formula(Where(Equal(CarlsonHypergeometricR(-a, List(Repeat(beta, n)), List(z_(k), For(k, 1, n))),
        A**(-a) * 
        Sum(RisingFactorial(a, N) / RisingFactorial(n*beta, N) * CarlsonHypergeometricT(N, List(Repeat(beta, n)), List(1 - z_(k) / A, For(k, 1, n))),
            For(N, 0, Infinity))),
        Def(A, (1/n) * Sum(z_(k), For(k, 1, n))))),
    Variables(a, beta, z, n),
    Assumptions(And(Element(a, RR),
        Element(beta, OpenInterval(0, Infinity)),
        Element(n, ZZGreaterEqual(1)),
        All(And(Element(z_(k), CC), Less(Abs(1 - n * z_(k) / Sum(z_(j), For(j, 1, n))), 1)), ForElement(k, Range(1, n))))))

make_entry(ID("da47f6"),
    Formula(Equal(CarlsonHypergeometricT(N, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        Sum(Product(RisingFactorial(b_(k), m_(k)) / Factorial(m_(k)) * z_(k)**m_(k), For(k, 1, n)),
            ForElement(Tuple(m_(k), For(k, 1, n)), CartesianPower(Parentheses(ZZGreaterEqual(0)), n)), Equal(Sum(m_(k), For(k, 1, n)), N)))),
    Variables(n, N, b, z),
    Assumptions(And(Element(n, ZZGreaterEqual(1)),
        Element(N, ZZGreaterEqual(0)),
        All(Element(b_(k), CC), ForElement(k, Range(1, n))),
        All(Element(z_(k), CC), ForElement(k, Range(1, n))))))

make_entry(ID("0a7f30"),
    Formula(Equal(CarlsonHypergeometricT(N, List(Repeat(beta, n)), List(z_(k), For(k, 1, n))),
        Sum(Where((-1)**(M+N) * RisingFactorial(beta, M) * Product(SymmetricPolynomial(k, List(z_(k), For(k, 1, n)))**m_(k) / Factorial(m_(k)), For(k, 1, n)),
                Def(M, Sum(m_(k), For(k, 1, n)))),
            ForElement(Tuple(m_(k), For(k, 1, n)), CartesianPower(Parentheses(ZZGreaterEqual(0)), n)), Equal(Sum(k * m_(k), For(k, 1, n)), N)))),
    Variables(n, beta, N, z),
    Assumptions(And(Element(n, ZZGreaterEqual(1)),
        Element(beta, OpenInterval(0, Infinity)),
        Element(N, ZZGreaterEqual(0)),
        All(Element(z_(k), CC), ForElement(k, Range(1, n))))))


make_entry(ID("8f71cb"),
    Formula(Equal(CarlsonRF(x, y, z), CarlsonHypergeometricR(-Div(1,2), [Div(1,2), Div(1,2), Div(1,2)], [x, y, z]))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))
    )))

make_entry(ID("fda084"),
    Formula(Equal(CarlsonRG(x, y, z), CarlsonHypergeometricR(Div(1,2), [Div(1,2), Div(1,2), Div(1,2)], [x, y, z]))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenInterval(-Infinity, 0))),
    )))

make_entry(ID("b2cd79"),
    Formula(Equal(CarlsonRJ(x, y, z, w), CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(1,2), Div(1,2), 1], [x, y, z, w]))),
    Variables(x, y, z, w),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(w, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))
    )))

make_entry(ID("e93f43"),
    Formula(Equal(CarlsonRJ(x, y, z, w), CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(1,2), Div(1,2), Div(1,2), Div(1, 2)], [x, y, z, w, w]))),
    Variables(x, y, z, w),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(w, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))
    )))

make_entry(ID("7ded8f"),
    Formula(Equal(CarlsonRC(x, y), CarlsonHypergeometricR(-Div(1,2), [Div(1,2), 1], [x, y]))),
    Variables(x, y),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))
    )))

make_entry(ID("42c7f1"),
    Formula(Equal(CarlsonRC(x, y), CarlsonHypergeometricR(-Div(1,2), [Div(1,2), Div(1, 2), Div(1, 2)], [x, y, y]))),
    Variables(x, y),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))
    )))

make_entry(ID("8d304b"),
    Formula(Equal(CarlsonRD(x, y, z), CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(1,2), Div(3,2)], [x, y, z]))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Or(NotEqual(x, 0), NotEqual(y, 0))
    )))

make_entry(ID("e1a3fb"),
    Formula(Equal(CarlsonRD(x, y, z), CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(1,2), Div(1,2), Div(1,2), Div(1,2)], [x, y, z, z, z]))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Or(NotEqual(x, 0), NotEqual(y, 0))
    )))

# todo: correct conditions?
make_entry(ID("cbcad9"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)),
        List(0, Step(z_(k), For(k, 2, n)))),
        Where(
            BetaFunction(a, c - b_(1)) / BetaFunction(a, c) *
            CarlsonHypergeometricR(-a, List(b_(k), For(k, 2, n)),
                List(z_(k), For(k, 2, n)))),
            Def(c, -a + Sum(b_(k), For(k, 1, n))))),
    Variables(a, b, z, n),
    Assumptions(And(
        Element(a, RR),
        Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(Element(z_(k), CC), ForElement(k, Range(2, n))),
        Greater(Sum(b_(k), For(k, 1, n)), 0),
        Greater(Sum(b_(k), For(k, 2, n)), a))),
    References("https://dlmf.nist.gov/19.16"))

make_entry(ID("d0c9ff"),
    Formula(Equal(CarlsonRF(0, y, z), (Pi / 2) * CarlsonHypergeometricR(-Div(1,2), [Div(1,2), Div(1,2)], [y, z]))),
    Variables(y, z),
    Assumptions(And(
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("00c331"),
    Formula(Equal(CarlsonRD(0, y, z), (3 * Pi / 4) * CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(3,2)], [y, z]))),
    Variables(y, z),
    Assumptions(And(
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("37ffb7"),
    Formula(Equal(CarlsonRD(0, y, z), (3 * Pi / 4) * CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(1,2), Div(1, 2), Div(1, 2)], [y, z, z, z]))),
    Variables(y, z),
    Assumptions(And(
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("5a8f57"),
    Formula(Equal(CarlsonRJ(0, y, z, w), (3 * Pi / 4) * CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(1,2), 1], [y, z, w]))),
    Variables(y, z, w),
    Assumptions(And(
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(w, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("7314c4"),
    Formula(Equal(CarlsonRJ(0, y, z, w), (3 * Pi / 4) * CarlsonHypergeometricR(-Div(3,2), [Div(1,2), Div(1,2), Div(1, 2), Div(1, 2)], [y, z, w, w]))),
    Variables(y, z, w),
    Assumptions(And(
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(w, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("b4a735"),
    Formula(Equal(CarlsonRG(0, y, z), (Pi / 4) * CarlsonHypergeometricR(Div(1,2), [Div(1,2), Div(1,2)], [y, z]))),
    Variables(y, z),
    Assumptions(And(
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("a1f7ea"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        Where(
            (1/BetaFunction(a,c)) * Integral(t**(c-1) * Product((t + z_(k))**(-b_(k)), For(k, 1, n)), For(t, 0, Infinity)),
        Def(c, -a+Sum(b_(j), For(j, 1, n)))))),
    Variables(a, b, z, n),
    Assumptions(And(Element(a, RR),
        Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(Element(z_(k), SetMinus(CC, OpenClosedInterval(-Infinity, 0))), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), a, 0))))

make_entry(ID("c5d388"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        Where(
            (1/BetaFunction(a,c)) * Integral(t**(a-1) * Product((1 + t * z_(k))**(-b_(k)), For(k, 1, n)), For(t, 0, Infinity)),
        Def(c, -a+Sum(b_(j), For(j, 1, n)))))),
    Variables(a, b, z, n),
    Assumptions(And(Element(a, RR),
        Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(Element(z_(k), SetMinus(CC, OpenClosedInterval(-Infinity, 0))), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), a, 0))))

make_entry(ID("2c1df7"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(lamda * z_(k), For(k, 1, n))),
        lamda**(-a) * CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))))),
    Variables(a, b, z, n, lamda),
    Assumptions(And(Element(a, RR),
        Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(Element(z_(k), SetMinus(CC, OpenClosedInterval(-Infinity, 0))), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), a, 0)),
        Element(lamda, OpenInterval(0, Infinity))))

make_entry(ID("b81ca0"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(Repeat(z, n))),
        z**(-a))),
    Variables(a, b, n, z),
    Assumptions(And(Element(a, RR),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), a, 0)),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))))

