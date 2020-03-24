# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Carlson symmetric elliptic integrals"),
    Section("Definitions"),
    Entries(
        "5cd377",
        "8f7c2a",
        "bac745",
    ),
    Subsection("Specialized versions"),
    Entries(
        "132ec5",
        "61f98d",
        "663d75",
        "409873",
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
    Section("Symmetry"),
    Entries(
        "f29729",
        "b478a1",
        "655a2b",
        "1e8061",
    ),
    Section("Scale invariance"),
    Entries(
        "7a168a",
        "f9ca94",
        "4e21c7",
        "197a91",
        "a839d5",
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
    SeeTopics("Legendre elliptic integrals"),
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
    Section("Derivatives and differential equations"),
    Entries(
        "5f0adb",
        "638fa6",
        "ce327b",
        "3e1435",
        "644d75",
        "de8485",
        "741859",
    ),
    Section("Series representations"),
    SeeTopics("Series representations of Carlson symmetric elliptic integrals"),
    Entries(
        "b576e6",
        "8f71cb",
        "fda084",
        "b2cd79",
        "8d304b",
        "7ded8f",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "c03f78",
        "1d2811",
        "07584a",
        "edcf6c",
        "a4e47f",
        "d3b39c",
        "230a49",
        "34e932",
        "688efb",
        "978287",
    ),
)

def_Topic(
    Title("Series representations of Carlson symmetric elliptic integrals"),
    SeeTopics("Carlson symmetric elliptic integrals"),
    Section("Definitions"),
    Entries(
        "b576e6",
        "a82bd6",
    ),
    Section("Incomplete integrals"),
    Entries(
        "8f71cb",
        "fda084",
        "b2cd79",
        "e93f43",
        "8d304b",
        "e1a3fb",
        "7ded8f",
        "42c7f1",
    ),
    Section("Complete integrals"),
    Entries(
        "cbcad9",
        "d0c9ff",
        "00c331",
        "37ffb7",
        "5a8f57",
        "7314c4",
        "b4a735",
    ),
    Section("General formulas for the series"),
    Entries(
        "da47f6",
        "4cb707",
        "2443de",
    ),
    Section("Symmetric formulas"),
    Entries(
        "13f252",
        "a21395",
        "0a7f30",
        "2c1df7",
        "b81ca0",
    ),
    Section("Integral representations"),
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

# Specializations

make_entry(ID("61f98d"),
    Formula(Equal(CarlsonRC(x, y), CarlsonRF(x, y, y))),
    Variables(x, y),
    Assumptions(And(Element(x, CC), Element(y, CC))))

make_entry(ID("409873"),
    Formula(Equal(CarlsonRD(x, y, z), CarlsonRJ(x, y, z, z))),
    Variables(x, y, z),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC))))

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
        Element(CarlsonRG(x, y, z), ClosedOpenInterval(0, Infinity)))),
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

make_entry(ID("f29729"),
    Formula(Equal(CarlsonRF(x, y, z), CarlsonRF(x, z, y),
            CarlsonRF(y, x, z), CarlsonRF(y, z, x),
            CarlsonRF(z, x, y), CarlsonRF(z, y, x))),
    Variables(x, y, z),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC))))

make_entry(ID("b478a1"),
    Formula(Equal(CarlsonRG(x, y, z), CarlsonRG(x, z, y),
            CarlsonRG(y, x, z), CarlsonRG(y, z, x),
            CarlsonRG(z, x, y), CarlsonRG(z, y, x))),
    Variables(x, y, z),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC))))

make_entry(ID("655a2b"),
    Formula(Equal(CarlsonRJ(x, y, z, w), CarlsonRJ(x, z, y, w),
            CarlsonRJ(y, x, z, w), CarlsonRJ(y, z, x, w),
            CarlsonRJ(z, x, y, w), CarlsonRJ(z, y, x, w))),
    Variables(x, y, z, w),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC), Element(w, CC))))

make_entry(ID("1e8061"),
    Formula(Equal(CarlsonRD(x, y, z), CarlsonRD(y, x, z))),
    Variables(x, y, z),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC))))

# Scale invariance

make_entry(ID("7a168a"),
    Formula(Equal(CarlsonRF(lamda * x, lamda * y, lamda * z), lamda**(-Div(1,2)) * CarlsonRF(x, y, z))),
    Variables(x, y, z, lamda),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC), Element(lamda, OpenInterval(0, Infinity)))))

make_entry(ID("f9ca94"),
    Formula(Equal(CarlsonRG(lamda * x, lamda * y, lamda * z), lamda**(Div(1,2)) * CarlsonRG(x, y, z))),
    Variables(x, y, z, lamda),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC), Element(lamda, OpenInterval(0, Infinity)))))

make_entry(ID("4e21c7"),
    Formula(Equal(CarlsonRJ(lamda * x, lamda * y, lamda * z, lamda * w), lamda**(-Div(3,2)) * CarlsonRJ(x, y, z, w))),
    Variables(x, y, z, w, lamda),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC), Element(w, CC), Element(lamda, OpenInterval(0, Infinity)))))

make_entry(ID("197a91"),
    Formula(Equal(CarlsonRD(lamda * x, lamda * y, lamda * z), lamda**(-Div(3,2)) * CarlsonRD(x, y, z))),
    Variables(x, y, z, lamda),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(z, CC), Element(lamda, OpenInterval(0, Infinity)))))

make_entry(ID("a839d5"),
    Formula(Equal(CarlsonRC(lamda * x, lamda * y), lamda**(-Div(1,2)) * CarlsonRC(x, y))),
    Variables(x, y, lamda),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(lamda, OpenInterval(0, Infinity)))))

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

# Specific values

'''
TODO: (+more elementary cases...)

make_entry(ID(""),
    Formula(Equal(CarlsonRG(x, y, y), (y * CarlsonRC(x, y) + Sqrt(x)) / 2)))

make_entry(ID(""),
    Formula(Equal(CarlsonRD(x, x, z), (3 / (z-x)) * (CarlsonRC(z, x) - 1 / Sqrt(x)))))

'''

# TODO: both lemniscate constants (check symbolic evaluation)



# Derivatives and differential equations

make_entry(ID("5f0adb"),
    Equal(ComplexDerivative(CarlsonRF(x, y, z), For(x, x)), -(Div(1,6) * CarlsonRD(y, z, x))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("638fa6"),
    Equal(ComplexDerivative(CarlsonRG(x+t, y+t, z+t), For(t, t)), Div(1,2) * CarlsonRF(x + t, y + t, z + t)),
    Variables(x, y, z, t),
    Assumptions(And(
        Element(x, CC),
        Element(y, CC),
        Element(z, CC),
        Element(t, CC),
        NotElement(x + t, OpenClosedInterval(-Infinity, 0)),
        NotElement(y + t, OpenClosedInterval(-Infinity, 0)),
        NotElement(z + t, OpenClosedInterval(-Infinity, 0)))))

make_entry(ID("ce327b"),
    Equal(ComplexDerivative(CarlsonRF(x, y, z), For(x, x)) + ComplexDerivative(CarlsonRF(x, y, z), For(y, y)) + ComplexDerivative(CarlsonRF(x, y, z), For(z, z)),
        -Div(1, Sqrt(x)*Sqrt(y)*Sqrt(z))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("3e1435"),
    Equal(ComplexDerivative(CarlsonRG(x, y, z), For(x, x)) + ComplexDerivative(CarlsonRG(x, y, z), For(y, y)) + ComplexDerivative(CarlsonRG(x, y, z), For(z, z)),
        Div(1,2) * CarlsonRF(x, y, z)),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("644d75"),
    Equal(x * ComplexDerivative(CarlsonRF(x, y, z), For(x, x)) + y * ComplexDerivative(CarlsonRF(x, y, z), For(y, y)) + z * ComplexDerivative(CarlsonRF(x, y, z), For(z, z)),
        -(Div(1,2) * CarlsonRF(x, y, z))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("de8485"),
    Equal(ComplexDerivative(CarlsonRC(x, y), For(x, x)), Cases(
        Tuple(1/(2*(y-x)) * (CarlsonRC(x,y) - 1/(Sqrt(x))), NotEqual(x, y)),
        Tuple(-(Div(1,6) * x**(-Div(3,2))), Equal(x, y)))),
    Variables(x, y),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("741859"),
    Equal(ComplexDerivative(CarlsonRC(x, y), For(y, y)), Cases(
        Tuple(1/(2*(x-y)) * (CarlsonRC(x,y) - Sqrt(x)/y), NotEqual(x, y)),
        Tuple(-(Div(1,3) * x**(-Div(3,2))), Equal(x, y)))),
    Variables(x, y),
    Assumptions(And(
        Element(x, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        Element(y, SetMinus(CC, OpenClosedInterval(-Infinity, 0))),
        NotEqual(x, y))))

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

# TODO: recurrence (3.9) for the terms in https://doi.org/10.6028/jres.107.034
# TODO: generic bounds

# Bounds and inequalities

make_entry(ID("c03f78"),
    Formula(LessEqual(CarlsonRF(x, y, z), 1/(x*y*z)**Div(1,6))),
    Variables(x, y, z),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)),
        Element(y, OpenInterval(0, Infinity)),
        Element(z, OpenInterval(0, Infinity)))),
    References("https://dlmf.nist.gov/19.24"))

make_entry(ID("1d2811"),
    Formula(GreaterEqual(CarlsonRF(x, y, z), 3/(Sqrt(x)+Sqrt(y)+Sqrt(z)))),
    Variables(x, y, z),
    Assumptions(And(Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, ClosedOpenInterval(0, Infinity)),
        Element(z, ClosedOpenInterval(0, Infinity))),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0)))))

make_entry(ID("07584a"),
    Formula(LessEqual(CarlsonRG(x, y, z), Min(Sqrt((x+y+z)/3), (x**2+y**2+z**2)/(3*Sqrt(x*y*z))))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, ClosedOpenInterval(0, Infinity)),
        Element(z, ClosedOpenInterval(0, Infinity)))))

make_entry(ID("edcf6c"),
    Formula(GreaterEqual(CarlsonRG(x, y, z), (Sqrt(x)+Sqrt(y)+Sqrt(z))/3)),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, ClosedOpenInterval(0, Infinity)),
        Element(z, ClosedOpenInterval(0, Infinity)))))

make_entry(ID("a4e47f"),
    Formula(LessEqual(CarlsonRJ(x, y, z, w), (x*y*z*w**2)**(-Div(3,10)))),
    Variables(x, y, z, w),
    Assumptions(And(
        Element(x, OpenInterval(0, Infinity)),
        Element(y, OpenInterval(0, Infinity)),
        Element(z, OpenInterval(0, Infinity)),
        Element(w, OpenInterval(0, Infinity)))))

make_entry(ID("d3b39c"),
    Formula(GreaterEqual(CarlsonRJ(x, y, z, w), (5/(Sqrt(x)+Sqrt(y)+Sqrt(z)+2*Sqrt(w)))**3)),
    Variables(x, y, z, w),
    Assumptions(And(
        Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, ClosedOpenInterval(0, Infinity)),
        Element(z, ClosedOpenInterval(0, Infinity)),
        Element(w, OpenInterval(0, Infinity)),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0))))))

make_entry(ID("230a49"),
    Formula(LessEqual(CarlsonRD(x, y, z), (x*y*z**3)**(-Div(3,10)))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, OpenInterval(0, Infinity)),
        Element(y, OpenInterval(0, Infinity)),
        Element(z, OpenInterval(0, Infinity)))))

make_entry(ID("34e932"),
    Formula(GreaterEqual(CarlsonRD(x, y, z), (5/(Sqrt(x)+Sqrt(y)+3*Sqrt(z)))**3)),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, ClosedOpenInterval(0, Infinity)),
        Element(z, OpenInterval(0, Infinity)))))

make_entry(ID("688efb"),
    Formula(LessEqual(CarlsonRC(x, y), 1/(x*y**2)**Div(1,6))),
    Variables(x, y),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)),
        Element(y, OpenInterval(0, Infinity)))))

make_entry(ID("978287"),
    Formula(GreaterEqual(CarlsonRC(x, y), 3/(Sqrt(x)+2*Sqrt(y)))),
    Variables(x, y),
    Assumptions(And(Element(x, ClosedOpenInterval(0, Infinity)),
        Element(y, OpenInterval(0, Infinity)))))


