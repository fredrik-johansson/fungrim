from .expr import *

def_Topic(
    Title("Error functions"),
    Section("Integral representations"),
    Entries(
        "2aaba8",
        "36ef64",
        "622772",
    ),
    Section("Connection formulas"),
    Entries(
        "7f355d",
        "bfc86e",
        "01440f",
    ),
    Section("Functional equations"),
    Entries(
        "94db18",
        "603a49",
        "ec0205",
    ),
    Section("Hypergeometric representations"),
    Entries(
        "abadc7",
        "98688d",
        "cb93ea",
        "ae3110",
    ),
    Section("Derivatives"),
    Entries(
        "b5bd5d",
        "fae9d3",
    ),
)

make_entry(ID("2aaba8"),
    Formula(Equal(Erf(z), 2/Sqrt(ConstPi) * Integral(Exp(-(t**2)), Tuple(t, 0, z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("36ef64"),
    Formula(Equal(Erfc(z), 2/Sqrt(ConstPi) * Integral(Exp(-(t**2)), Tuple(t, z, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("622772"),
    Formula(Equal(Erfi(z), 2/Sqrt(ConstPi) * Integral(Exp(t**2), Tuple(t, 0, z)))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("94db18"),
    Formula(Equal(Erf(-z), -Erf(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("ec0205"),
    Formula(Equal(Erfc(-z), 2-Erfc(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("603a49"),
    Formula(Equal(Erfi(-z), -Erfi(z))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("abadc7"),
    Formula(Equal(Erf(z), (2*z)/Sqrt(ConstPi) * Hypergeometric1F1(Div(1,2), Div(3,2), -(z**2)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("98688d"),
    Formula(Equal(Erf(z), (2*z*Exp(-(z**2)))/Sqrt(ConstPi) * Hypergeometric1F1(1, Div(3,2), z**2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("cb93ea"),
    Formula(Equal(Erf(z), z/Sqrt(z**2) - Exp(-(z**2))/(z*Sqrt(ConstPi)) * HypergeometricUStar(Div(1,2), Div(1,2), z**2))),
    Variables(z),
    Assumptions(And(Element(z, CC), Unequal(z, 0))))

make_entry(ID("ae3110"),
    Formula(Equal(Erfc(z), Exp(-(z**2))/(z*Sqrt(ConstPi)) * HypergeometricUStar(Div(1,2), Div(1,2), z**2))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))


make_entry(ID("7f355d"),
    Formula(Equal(Erf(z) + Erfc(z), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("bfc86e"),
    Formula(Equal(Erfc(z), 1 - Erf(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("01440f"),
    Formula(Equal(Erfi(z), -(ConstI*Erf(ConstI*z)))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("b5bd5d"),
    Formula(Equal(Derivative(Erf(z), Tuple(z, z, 1)), 2/Sqrt(ConstPi) * Exp(-(z**2)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("fae9d3"),
    Formula(Equal(Derivative(Erf(z), Tuple(z, z, n)), 2/Sqrt(ConstPi) * (-1)**(k+1) * HermitePolynomial(n-1, z) * Exp(-(z**2)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(1)))))

