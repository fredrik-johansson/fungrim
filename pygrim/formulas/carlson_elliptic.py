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
    Subsection("Degenerate cases"),
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
    Section("Specific values"),
    SeeTopics("Specific values of Carlson symmetric elliptic integrals"),
    Entries(
        "5ada5f",
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
    Subsection("Multivariate hypergeometric series representations"),
    Entries(
        "b576e6",
        "8f71cb",
        "fda084",
        "b2cd79",
        "8d304b",
        "7ded8f",
    ),
    Subsection("Explicit truncated series approximations"),
    Entries(
        "799894",
        "618a9f",
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
    Title("Specific values of Carlson symmetric elliptic integrals"),
    SeeTopics("Carlson symmetric elliptic integrals"),
    Section("The elementary integral RC"),
    Subsection("Particular constant values"),
    Entries(
        "5c2b08",
        "1acb07",
        "e464ec",
        "d38c27",
        "eac389",
        "a15c03",
        "35cb93",
        "56d1bc",
        "25435b",
        "7ea1ad",
    ),
    Subsection("Specialized values"),
    Entries(
        "7cbe17",
        "ff58cf",
        "ad96f4",
        "09a494",
        "b136bd",
        "8c9ba1",
    ),
    Subsection("General formulas for real variables"),
    Entries(
        "5ada5f",
        "de0638",
        "00cdb7",
        "bc2f88",
        "4becdd",
    ),
    Subsection("General formulas for one or more complex variables"),
    Entries(
        "7b5755",
        "0cf60d",
        "eb1d4f",
        "157ebb",
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
    Section("Approximations by truncated series"),
    Entries(
        "926b36",
        "799894",
        "618a9f",
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
    SymbolDefinition(CarlsonRD, CarlsonRD(x, y, z), "Degenerate case of Carlson symmetric elliptic integral of the third kind"))

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

# NOTE:
# Without strong assumptions, the following formulas are mutually incompatible when some parameters are in the left half-plane:
# 1) integral representations for CarlsonHypergeometricR
# 2) representations of the individual CarlsonRX functions in terms of CarlsonHypergeometricR
# 3) series representation of CarlsonHypergeometricR

# Two possible solutions:
# * Define CarlsonHypergeometricR universally in terms of its series representation, and add assumptions for 1) and 2)
# * Define CarlsonHypergeometricR consistently with the integral representations and other functions, and add assumptions for 3)

# For now, we use the second solution as it requires less work...

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
    Variables(a, beta, z_, n),
    Assumptions(And(Element(a, RR),
        Element(beta, OpenInterval(0, Infinity)),
        Element(n, ZZGreaterEqual(1)),
        All(And(Element(z_(k), CC), Less(Abs(1 - n * z_(k) / Sum(z_(j), For(j, 1, n))), 1)), ForElement(k, Range(1, n))),
        All(Greater(Re(z_(k)), 0), ForElement(k, Range(1, n))),  # Condition for consistency -- see NOTE (could probably be relaxed, e.g. look at all |arg(z_i)-arg(z_j)|)
    )))

make_entry(ID("4cb707"),
    Formula(Where(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        Sum(RisingFactorial(a, N) / RisingFactorial(c, N) * CarlsonHypergeometricT(N, List(b_(k), For(k, 1, n)), List(1 - z_(k), For(k, 1, n))),
            For(N, 0, Infinity))), Def(c, Sum(b_(k), For(k, 1, n))))),
    Variables(a, b_, z_, n),
    Assumptions(And(Element(a, RR), Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(And(Element(z_(k), CC), Less(Abs(1 - z_(k)), 1)), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), 0),
        All(Greater(Re(z_(k)), 0), ForElement(k, Range(1, n))),  # Condition for consistency -- see NOTE (could probably be relaxed, e.g. look at all |arg(z_i)-arg(z_j)|)
    )))

make_entry(ID("2443de"),
    Formula(Where(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        z_(n)**(-a) * 
        Sum(RisingFactorial(a, N) / RisingFactorial(c, N) * CarlsonHypergeometricT(N, List(b_(k), For(k, 1, n - 1)), List(1 - z_(k) / z_(n), For(k, 1, n - 1))),
            For(N, 0, Infinity))), Def(c, Sum(b_(k), For(k, 1, n))))),
    Variables(a, b_, z_, n),
    Assumptions(And(Element(a, RR), Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        Element(z_(n), SetMinus(CC, Set(0))),
        All(And(Element(z_(k), CC), Less(Abs(1 - z_(k) / z_(n)), 1)), ForElement(k, Range(1, n - 1))),
        Greater(Sum(b_(k), For(k, 1, n)), 0),
        All(Greater(Re(z_(k)), 0), ForElement(k, Range(1, n))),  # Condition for consistency -- see NOTE (could probably be relaxed, e.g. look at all |arg(z_i)-arg(z_j)|)
    )))

make_entry(ID("a21395"),
    Formula(Where(Equal(CarlsonHypergeometricR(-a, List(Repeat(beta, n)), List(z_(k), For(k, 1, n))),
        A**(-a) * 
        Sum(RisingFactorial(a, N) / RisingFactorial(n*beta, N) * CarlsonHypergeometricT(N, List(Repeat(beta, n)), List(1 - z_(k) / A, For(k, 1, n))),
            For(N, 0, Infinity))),
        Def(A, (1/n) * Sum(z_(k), For(k, 1, n))))),
    Variables(a, beta, z_, n),
    Assumptions(And(Element(a, RR),
        Element(beta, OpenInterval(0, Infinity)),
        Element(n, ZZGreaterEqual(1)),
        All(And(Element(z_(k), CC), Less(Abs(1 - n * z_(k) / Sum(z_(j), For(j, 1, n))), 1)), ForElement(k, Range(1, n))),
        All(Greater(Re(z_(k)), 0), ForElement(k, Range(1, n))),  # Condition for consistency -- see NOTE (could probably be relaxed, e.g. look at all |arg(z_i)-arg(z_j)|)
    )))

make_entry(ID("da47f6"),
    Formula(Equal(CarlsonHypergeometricT(N, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))),
        Sum(Product(RisingFactorial(b_(k), m_(k)) / Factorial(m_(k)) * z_(k)**m_(k), For(k, 1, n)),
            ForElement(Tuple(m_(k), For(k, 1, n)), CartesianPower(Parentheses(ZZGreaterEqual(0)), n)), Equal(Sum(m_(k), For(k, 1, n)), N)))),
    Variables(n, N, b_, z_),
    Assumptions(And(Element(n, ZZGreaterEqual(1)),
        Element(N, ZZGreaterEqual(0)),
        All(Element(b_(k), CC), ForElement(k, Range(1, n))),
        All(Element(z_(k), CC), ForElement(k, Range(1, n))))))

make_entry(ID("0a7f30"),
    Formula(Equal(CarlsonHypergeometricT(N, List(Repeat(beta, n)), List(z_(k), For(k, 1, n))),
        Sum(Where((-1)**(M+N) * RisingFactorial(beta, M) * Product(SymmetricPolynomial(k, List(z_(k), For(k, 1, n)))**m_(k) / Factorial(m_(k)), For(k, 1, n)),
                Def(M, Sum(m_(k), For(k, 1, n)))),
            ForElement(Tuple(m_(k), For(k, 1, n)), CartesianPower(Parentheses(ZZGreaterEqual(0)), n)), Equal(Sum(k * m_(k), For(k, 1, n)), N)))),
    Variables(n, beta, N, z_),
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

# todo: sufficient conditions?
make_entry(ID("cbcad9"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)),
        List(0, Step(z_(k), For(k, 2, n)))),
        Where(
            BetaFunction(a, c - b_(1)) / BetaFunction(a, c) *
            CarlsonHypergeometricR(-a, List(b_(k), For(k, 2, n)),
                List(z_(k), For(k, 2, n)))),
            Def(c, -a + Sum(b_(k), For(k, 1, n))))),
    Variables(a, b_, z_, n),
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
    Variables(a, b_, z_, n),
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
    Variables(a, b_, z_, n),
    Assumptions(And(Element(a, RR),
        Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(Element(z_(k), SetMinus(CC, OpenClosedInterval(-Infinity, 0))), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), a, 0))))

make_entry(ID("2c1df7"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(lamda * z_(k), For(k, 1, n))),
        lamda**(-a) * CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(z_(k), For(k, 1, n))))),
    Variables(a, b_, z_, n, lamda),
    Assumptions(And(Element(a, RR),
        Element(n, ZZGreaterEqual(1)),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        All(Element(z_(k), SetMinus(CC, OpenClosedInterval(-Infinity, 0))), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), a, 0),
        Element(lamda, OpenInterval(0, Infinity)))))

make_entry(ID("b81ca0"),
    Formula(Equal(CarlsonHypergeometricR(-a, List(b_(k), For(k, 1, n)), List(Repeat(z, n))),
        z**(-a))),
    Variables(a, b_, n, z),
    Assumptions(And(Element(a, RR),
        All(Element(b_(k), RR), ForElement(k, Range(1, n))),
        Greater(Sum(b_(k), For(k, 1, n)), a, 0),
        Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

# TODO: recurrence (3.9) for the terms in https://doi.org/10.6028/jres.107.034

make_entry(ID("926b36"),
    Formula(Where(LessEqual(Abs(CarlsonHypergeometricR(-a, List(Repeat(beta, n)), List(z_(k), For(k, 1, n))) -
        A**(-a) * Sum(RisingFactorial(a, N) / RisingFactorial(n * beta, N) * CarlsonHypergeometricT(N, List(Repeat(beta, n)), List(z_(k), For(k, 1, n))),
            For(N, 0, K - 1))),
                Abs(A**(-a)) * RisingFactorial(Abs(a), K) * M**K / (Factorial(K) * (1 - M)**Max(Abs(a), 1))),
        Def(A, (1/n) * Sum(z_(k), For(k, 1, n))),
        Def(Z_(k), 1 - z_(k) / A),
        Def(M, Max(Step(Abs(Z_(k)), For(k, 1, n)))))),
    Variables(a, beta, z_, n, K),
    Assumptions(And(Element(a, RR),
        Element(beta, OpenInterval(0, Infinity)),
        Element(n, ZZGreaterEqual(1)),
        Element(K, ZZGreaterEqual(1)),
        All(And(Element(z_(k), CC), Less(Abs(1 - n * z_(k) / Sum(z_(j), For(j, 1, n))), 1)), ForElement(k, Range(1, n))),
        All(Greater(Re(z_(k)), 0), ForElement(k, Range(1, n))),  # Condition for consistency -- see NOTE (could probably be relaxed, e.g. look at all |arg(z_i)-arg(z_j)|)
    )),
    References("https://doi.org/10.6028/jres.107.034"))

# Note: Carlson does not give the argument condition, but numerical
# testing finds counterexamples; e.g. x, y, z = (-1.2377 + 0.79846j), (-3.6404 - 3.0689j), (-3.1749 - 0.16069j).
# Alternatively, a sufficient condition (confirmed by extensive numerical testing)
# is apparently to perform one duplication step before using the series expansion
make_entry(ID("799894"),
    Formula(Where(LessEqual(Abs(CarlsonRF(x, y, z) -
         A**(-Div(1,2)) * (1 - E/10 + F/14 + E**2/24 - 3*E*F/44 - 5*E**3/208 + 3*F**2/104 + E**2*F/16)),
            Decimal("0.2") * Abs(A**(-Div(1,2))) * M**8 / (1 - M)),
        Def(A, (x+y+z)/3),
        Def(X, 1-x/A),
        Def(Y, 1-y/A),
        Def(Z, 1-z/A),
        Def(E, X*Y + X*Z + Y*Z),
        Def(F, X*Y*Z),
        Def(M, Max(Abs(X), Abs(Y), Abs(Z))))),
    Variables(x, y, z),
    Assumptions(And(
        Element(x, CC),
        Element(y, CC),
        Element(z, CC),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0))),
        Less(Max(Abs(Arg(x)-Arg(y)), Abs(Arg(x)-Arg(z)), Abs(Arg(y)-Arg(z))), Pi),
        Less(Abs(1-3*x/(x+y+z)), 1),
        Less(Abs(1-3*y/(x+y+z)), 1),
        Less(Abs(1-3*z/(x+y+z)), 1))),
    References("https://doi.org/10.6028/jres.107.034"))

make_entry(ID("618a9f"),
    Formula(Where(LessEqual(Abs(CarlsonRJ(x, y, z, w) -
         A**(-Div(3,2)) * (1 - 3*E/14 + F/6 + 9*E**2/88 - 3*G/22 - 9*E*F/52 + 3*H/26 - E**3/16 + 3*F**2/40 + 3*E*G/20 + 45*E**2*F/272 - 9*F*G/68 - 9*E*H/68)),
            Decimal("3.4") * Abs(A**(-Div(3,2))) * M**8 / (1 - M)**Div(3,2)),
        Def(A, (x+y+z+2*w)/5),
        Def(X, 1-x/A),
        Def(Y, 1-y/A),
        Def(Z, 1-z/A),
        Def(W, Parentheses(-X-Y-Z)/2),   # fixme: printing bug
        Def(E, X*Y + X*Z + Y*Z - 3*W**2),
        Def(F, X*Y*Z + 2*E*W + 4*W**3),
        Def(G, (2*X*Y*Z + E*W + 3*W**3)*W),
        Def(H, X*Y*Z*W**2),
        Def(M, Max(Abs(X), Abs(Y), Abs(Z), Abs(W))))),
    Variables(x, y, z, w),
    Assumptions(And(
        Element(x, CC),
        Element(y, CC),
        Element(z, CC),
        Element(w, CC),
        GreaterEqual(Re(x), 0),
        GreaterEqual(Re(y), 0),
        GreaterEqual(Re(z), 0),
        Greater(Re(w), 0),
        Or(And(NotEqual(x, 0), NotEqual(y, 0)),
           And(NotEqual(x, 0), NotEqual(z, 0)),
           And(NotEqual(y, 0), NotEqual(z, 0))),
        Less(Abs(1-5*x/(x+y+z+2*w)), 1),
        Less(Abs(1-5*y/(x+y+z+2*w)), 1),
        Less(Abs(1-5*z/(x+y+z+2*w)), 1),
        Less(Abs(1-5*z/(x+y+z+2*w)), 1))),
    References("https://doi.org/10.6028/jres.107.034"))


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


# Special values -- including infinities?
# Elementary cases



make_entry(ID("5c2b08"),
    Formula(Equal(CarlsonRC(0, 0), UnsignedInfinity)))

make_entry(ID("1acb07"),
    Formula(Equal(CarlsonRC(1, 0), Infinity)))

make_entry(ID("e464ec"),
    Formula(Equal(CarlsonRC(0, 1), Pi / 2)))

make_entry(ID("d38c27"),
    Formula(Equal(CarlsonRC(1, 1), 1)))

make_entry(ID("eac389"),
    Formula(Equal(CarlsonRC(1, 2), Pi / 4)))

make_entry(ID("a15c03"),
    Formula(Equal(CarlsonRC(2, 1), Log(1 + Sqrt(2)))))

make_entry(ID("35cb93"),
    Formula(Equal(CarlsonRC(0, -1), -((Pi * ConstI) / 2))))

make_entry(ID("56d1bc"),
    Formula(Equal(CarlsonRC(-1, 0), -(ConstI * Infinity))))

make_entry(ID("25435b"),
    Formula(Equal(CarlsonRC(1, -1), ((Sqrt(2) * Log(1+Sqrt(2)))/2 - (Pi*Sqrt(2)/4)*ConstI))))

make_entry(ID("7ea1ad"),
    Formula(Equal(CarlsonRC(-1, 1), (Pi*Sqrt(2)/4 - ((Sqrt(2) * Log(1+Sqrt(2))) / 2) * ConstI))))

make_entry(ID("7cbe17"),
    Formula(Equal(CarlsonRC(x, 0), Cases(
        Tuple(Sign(1/Sqrt(x)) * Infinity, NotEqual(x, 0)),
        Tuple(UnsignedInfinity, Equal(x, 0))))),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("ff58cf"),
    Formula(Equal(CarlsonRC(0, y), Cases(
        Tuple(Pi / (2 * Sqrt(y)), NotEqual(y, 0)),
        Tuple(UnsignedInfinity, Equal(y, 0))))),
    Variables(y),
    Assumptions(Element(y, CC)))

make_entry(ID("ad96f4"),
    Formula(Equal(CarlsonRC(x, x), 1/Sqrt(x))),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("09a494"),
    Formula(Equal(CarlsonRC(x, 2*x), Pi/(4*Sqrt(x)))),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("b136bd"),
    Formula(Equal(CarlsonRC(2*x, x), Log(1+Sqrt(2))/Sqrt(x))),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("8c9ba1"),
    Formula(Equal(CarlsonRC(x, c*x), Cases(
        (Atan(Sqrt(c-1)) / Sqrt((c-1)*x), Greater(c, 1)),
        (1/Sqrt(x), Equal(c, 1)),
        (Atanh(Sqrt(1-c)) / Sqrt((1-c)*x), Less(c, 1))))),
    Variables(x, c),
    Assumptions(And(Element(x, CC), Element(c, OpenInterval(0, Infinity)))))

make_entry(ID("5ada5f"),
    Formula(Equal(CarlsonRC(x, y),
        Cases((Atan(Sqrt(y/x-1)) / Sqrt(y-x), Less(x, y)),
            (1/Sqrt(x), Equal(x, y)),
            (Atanh(Sqrt(1-y/x)) / Sqrt(x-y), Greater(x, y))))),
    Variables(x, y),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(y, OpenInterval(0, Infinity)))))

make_entry(ID("de0638"),
    Formula(Equal(CarlsonRC(-x, -y), -(ConstI * CarlsonRC(x, y)))),
    Variables(x, y),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(y, OpenInterval(0, Infinity)))))

make_entry(ID("00cdb7"),
    Formula(Equal(CarlsonRC(x, -y), 1/Sqrt(x+y) * (Atanh(Sqrt(x/(x+y))) - Pi*ConstI/2))),
    Variables(x, y),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(y, OpenInterval(0, Infinity)))))

make_entry(ID("bc2f88"),
    Formula(Equal(CarlsonRC(-x, y), (1/Sqrt(x+y)) * (Pi/2 - Atanh(Sqrt(x/(x+y))) * ConstI))),
    Variables(x, y),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(y, OpenInterval(0, Infinity)))))

make_entry(ID("4becdd"),
    Formula(Equal(CarlsonRC(-x, y), Conjugate(ConstI * CarlsonRC(x, -y)))),
    Variables(x, y),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(y, OpenInterval(0, Infinity)))))

# todo: figure out more general conditions of validity
make_entry(ID("7b5755"),
    Formula(Equal(CarlsonRC(x, y), Cases(
        (Atan(Sqrt(y/x-1)) / Sqrt(y-x), NotEqual(x, y)),
        (1/Sqrt(x), Equal(x, y))))),
    Variables(x, y),
    Assumptions(And(Element(x, CC), Element(y, CC), Or(Element(x, OpenInterval(0, Infinity)), And(Element(y, OpenInterval(0, Infinity)), NotElement(x, OpenInterval(-Infinity, 0)))))))

# todo: figure out more general conditions of validity
make_entry(ID("0cf60d"),
    Formula(Equal(CarlsonRC(x, y), Cases(
        (Atanh(Sqrt(1-y/x)) / Sqrt(x-y), NotEqual(x, y)),
        (1/Sqrt(x), Equal(x, y))))),
    Variables(x, y),
    Assumptions(And(Element(x, CC), Element(y, CC), Or(Element(x, OpenInterval(0, Infinity)), And(Element(y, OpenInterval(0, Infinity)), NotElement(x, OpenInterval(-Infinity, 0)))))))

make_entry(ID("eb1d4f"),
    Formula(Equal(CarlsonRC(1, 1+y), Cases(
        (Atan(Sqrt(y)) / Sqrt(y), NotEqual(y, 0)),
        (1, Equal(y, 0))))),
    Variables(y),
    Assumptions(Element(y, CC)))

make_entry(ID("157ebb"),
    Formula(Equal(CarlsonRC(1, 1+y), Hypergeometric2F1(1, Div(1,2), Div(3,2), -y))),
    Variables(y),
    Assumptions(Element(y, CC)))



# Specific values

#make_entry(ID(""),
#    Formula(Equal(CarlsonRG(x, y, y), (y * CarlsonRC(x, y) + Sqrt(x)) / 2)))

#make_entry(ID(""),
#    Formula(Equal(CarlsonRD(x, x, z), (3 / (z-x)) * (CarlsonRC(z, x) - 1 / Sqrt(x)))))

# TODO: both lemniscate constants (check symbolic evaluation)

