# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Legendre elliptic integrals"),
    Section("Definitions"),
    Entries(
        "e8ae42",
        "723fd0",
        "34482b",
        "107140",
        "afdf5d",
        "53b1e7",
    ),
    Section("Illustrations"),
    Entries(
        "89d93c",
        "210213",
        "4704f9",
        "20d72c",
    ),
#    Section("Domain"),
#    Entries(
#    ),
    Section("Integral representations"),
    Subsection("Trigonometric forms of the complete integrals"),
    Entries(
        "0455b3",
        "190843",
        "83a535",
    ),
    Subsection("Algebraic forms of the complete integrals"),
    Entries(
        "47dead",
        "fa8666",
        "c10014",
        "7cd257",
    ),
    Subsection("Trigonometric forms of the incomplete integrals"),
    Entries(
        "81fb10",
        "2ff7e7",
        "60f858",
    ),
    Subsection("Algebraic forms of the incomplete integrals"),
    Entries(
        "33ee4a",
        "5e869b",
        "06223c",
    ),
    Section("Specific values"),
    Subsection("Complete elliptic integrals"),
    Entries(
        "bb4501",
        "1d62a7",
        "45b157",
        "958a3f",
        "afb22a",
        "cc22bf",
        "630eca",
        "9f3474",
        "3b272e",
        "5d2c01",
        "2991b5",
        "4b040d",
        "618a54",
        "18e226",
        "061c49",
        "3c4979",
        "124d02",
        "9b0385",
        "ce4df4",
        "e9c797",
        "5d8804",
        "dd67fb",
        "9227bf",
    ),
    Subsection("Incomplete integral of the first kind"),
    Entries(
        "ba1965",
        "4268fc",
        "d2adb6",
        "0b8fd6",
        "81f7db",
        "afabeb",
        "c0ad12",
        "ace837",
        "16612f",
        "04c829",
        "c584c3",
        "f5d489",
        "a91f8d",
        "b7cfb3",
        "8b4be6",
        "aac129",
        "087a7c",
    ),
    Subsection("Incomplete integral of the second kind"),
    Entries(
        "a6c07e",
        "be3e09",
        "efc7a4",
        "1b881e",
        "2ef763",
        "a14442",
        "75e141",
        "f35a37",
        "51a946",
        "2573ba",
        "b62aae",
        "dec0d2",
        "2245df",
        "3aed02",
        "d88dd1",
        "4dabda",
        "eba27c",
        "f0bcb5",
    ),
    Section("Functional equations"),
    Subsection("Conjugate symmetry"),
    Entries(
        "713966",
        "8e5c81",
    ),
    Subsection("Odd symmetry"),
    Entries(
        "b0eb37",
        "aa1b8e",
        "255d81",
    ),
    Subsection("Quasi-periodicity"),
    Entries(
        "685126",
        "c28288",
        "5f84d9",
    ),
    Section("Representation by other functions"),
    Subsection("Hypergeometric functions"),
    Entries(
        "b760d1",
        "16d2e1",
        "752619",
    ),
    Subsection("Arithmetic-geometric mean"),
    Entries(
        "e15f43",
    ),
    Subsection("Carlson symmetric elliptic integrals"),
    Entries(
        "0cc11f",
        "6520e7",
        "9ccaef",
        "41cf8e",
        "94f646",
        "55d23d",
        "e2445d",
        "f48f54",
        "8f4e31",
    ),
    Section("Representation of other functions"),
    Entries(
        "71a0ff",
    ),
#    Section("Functional equations"),
#    Entries(
#    ),
#    Section("Derivatives and differential equations"),
#    Entries(
#    ),
)



make_entry(ID("e8ae42"),
    SymbolDefinition(EllipticK, EllipticK(m), "Legendre complete elliptic integral of the first kind"))

make_entry(ID("723fd0"),
    SymbolDefinition(EllipticE, EllipticE(m), "Legendre complete elliptic integral of the second kind"))

make_entry(ID("34482b"),
    SymbolDefinition(EllipticPi, EllipticPi(n, m), "Legendre complete elliptic integral of the third kind"))

make_entry(ID("107140"),
    SymbolDefinition(IncompleteEllipticF, IncompleteEllipticF(phi, m), "Legendre incomplete elliptic integral of the first kind"))

make_entry(ID("afdf5d"),
    SymbolDefinition(IncompleteEllipticE, IncompleteEllipticE(phi, m), "Legendre incomplete elliptic integral of the second kind"))

make_entry(ID("53b1e7"),
    SymbolDefinition(IncompleteEllipticPi, IncompleteEllipticPi(n, phi, m), "Legendre incomplete elliptic integral of the third kind"))

# Illustrations

make_entry(ID("89d93c"),
    Image(Description("Plot of", EllipticK(m), "on", Element(m, ClosedInterval(-2,2))),
        ImageSource("plot_elliptic_k")))

make_entry(ID("210213"),
    Image(Description("Plot of", EllipticE(m), "on", Element(m, ClosedInterval(-2,2))),
        ImageSource("plot_elliptic_e")))

make_entry(ID("4704f9"),
    Image(Description("Plot of", IncompleteEllipticF(phi, m), "on", Element(phi, ClosedInterval(-(2*Pi),2*Pi))),
        ImageSource("plot_incomplete_elliptic_f")))

make_entry(ID("20d72c"),
    Image(Description("Plot of", IncompleteEllipticE(phi, m), "on", Element(phi, ClosedInterval(-(2*Pi),2*Pi))),
        ImageSource("plot_incomplete_elliptic_e")))

# Integral representations

make_entry(ID("0455b3"),
    Formula(Equal(EllipticK(m), Integral(1/Sqrt(1-m*Sin(x)**2), For(x, 0, Pi / 2)))),
    Variables(m),
    Assumptions(Element(m, SetMinus(CC, ClosedOpenInterval(1, Infinity)))))

make_entry(ID("190843"),
    Formula(Equal(EllipticE(m), Integral(Sqrt(1-m*Sin(x)**2), For(x, 0, Pi / 2)))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("83a535"),
    Formula(Equal(EllipticPi(n, m), Integral(1/((1-n*Sin(x)**2) * Sqrt(1 - m*Sin(x)**2)), For(x, 0, Pi / 2)))),
    Variables(n, m),
    Assumptions(And(Element(n, OpenInterval(-Infinity, 1)), Element(m, OpenInterval(-Infinity, 1)))))

make_entry(ID("47dead"),
    Formula(Equal(EllipticK(m), Integral(1/(Sqrt(1-x**2) * Sqrt(1 - m*x**2)), For(x, 0, 1)))),
    Variables(m),
    Assumptions(Element(m, SetMinus(CC, ClosedOpenInterval(1, Infinity)))))
    
make_entry(ID("fa8666"),
    Formula(Equal(EllipticE(m), Integral(Sqrt(1-m*x**2) / Sqrt(1-x**2), For(x, 0, 1)))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("c10014"),
    Formula(Equal(EllipticPi(n, m), Integral(1/((1-n*x**2)*Sqrt(1-x**2)*Sqrt(1-m*x**2)), For(x, 0, 1)))),
    Variables(n, m),
    Assumptions(And(Element(n, OpenInterval(-Infinity, 1)), Element(m, OpenInterval(-Infinity, 1)))))

make_entry(ID("7cd257"),
    Formula(Equal(EllipticK(m), Integral(1/(Sqrt(x**2-1) * Sqrt(x**2-m)), For(x, 1, Infinity)))),
    Variables(m),
    Assumptions(Element(m, SetMinus(CC, ClosedOpenInterval(1, Infinity)))))

make_entry(ID("81fb10"),
    Formula(Equal(IncompleteEllipticF(phi, m), Integral(1/Sqrt(1-m*Sin(x)**2), For(x, 0, phi)))),
    Variables(phi, m),
    Assumptions(And(Element(phi, ClosedInterval(-Pi/2, Pi/2)), Element(m, SetMinus(CC, ClosedOpenInterval(1, Infinity))))))

make_entry(ID("2ff7e7"),
    Formula(Equal(IncompleteEllipticE(phi, m), Integral(Sqrt(1-m*Sin(x)**2), For(x, 0, phi)))),
    Variables(phi, m),
    Assumptions(And(Element(phi, ClosedInterval(-Pi/2, Pi/2)), Element(m, CC))))

make_entry(ID("60f858"),
    Formula(Equal(IncompleteEllipticPi(n, phi, m), Integral(1/((1-n*Sin(x)**2) * Sqrt(1 - m*Sin(x)**2)), For(x, 0, phi)))),
    Variables(n, phi, m),
    Assumptions(And(Element(phi, ClosedInterval(-Pi/2, Pi/2)), Element(n, OpenInterval(-Infinity, 1)), Element(m, OpenInterval(-Infinity, 1)))))

make_entry(ID("33ee4a"),
    Formula(Equal(IncompleteEllipticF(phi, m), Integral(1/(Sqrt(1-x**2) * Sqrt(1 - m*x**2)), For(x, 0, Sin(phi))))),
    Variables(phi, m),
    Assumptions(And(Element(phi, ClosedInterval(-Pi/2, Pi/2)), Element(m, SetMinus(CC, ClosedOpenInterval(1, Infinity))))))

make_entry(ID("5e869b"),
    Formula(Equal(IncompleteEllipticE(phi, m), Integral(Sqrt(1-m*x**2)/Sqrt(1-x**2), For(x, 0, Sin(phi))))),
    Variables(phi, m),
    Assumptions(And(Element(phi, ClosedInterval(-Pi/2, Pi/2)), Element(m, CC))))

make_entry(ID("06223c"),
    Formula(Equal(IncompleteEllipticPi(n, phi, m), Integral(1/((1-n*x**2) * Sqrt(1-x**2) * Sqrt(1 - m*x**2)), For(x, 0, Sin(phi))))),
    Variables(n, phi, m),
    Assumptions(And(Element(phi, ClosedInterval(-Pi/2, Pi/2)), Element(n, OpenInterval(-Infinity, 1)), Element(m, OpenInterval(-Infinity, 1)))))



# Specific values

# todo: singular values http://functions.wolfram.com/EllipticIntegrals/EllipticK/03/ShowAll.html -- also for modular lambda function

## Complete integrals

make_entry(ID("bb4501"),
    Formula(Equal(EllipticK(0), Pi / 2)))

make_entry(ID("1d62a7"),
    Formula(Equal(EllipticE(0), Pi / 2)))

make_entry(ID("45b157"),
    Formula(Equal(EllipticK(1), Infinity)))

make_entry(ID("958a3f"),
    Formula(Equal(EllipticE(1), 1)))

make_entry(ID("afb22a"),
    Formula(Equal(EllipticK(-1), Div(Pow(Gamma(Div(1, 4)), 2), Mul(4, Sqrt(Mul(2, Pi)))))))

make_entry(ID("cc22bf"),
    Formula(Equal(EllipticK(Div(1,2)), Div(Pow(Gamma(Div(1, 4)), 2), Mul(4, Sqrt(Pi))))))

make_entry(ID("630eca"),
    Formula(Equal(EllipticK(2), Mul(Div(Pow(Gamma(Div(1, 4)), 2), Mul(4, Sqrt(Mul(2, Pi)))), Sub(1, ConstI)))))

make_entry(ID("9f3474"),
    Formula(Equal(EllipticE(-1), Mul(Sqrt(2), Add(Div(Pow(Gamma(Div(1, 4)), 2), Mul(8, Sqrt(Pi))), Div(Pow(Pi, Div(3, 2)), Pow(Gamma(Div(1, 4)), 2)))))))

make_entry(ID("3b272e"),
    Formula(Equal(EllipticE(Div(1, 2)), Add(Div(Pow(Gamma(Div(1, 4)), 2), Mul(8, Sqrt(Pi))), Div(Pow(Pi, Div(3, 2)), Pow(Gamma(Div(1, 4)), 2))))))

make_entry(ID("5d2c01"),
    Formula(Equal(EllipticE(2), Mul(Div(Mul(Sqrt(2), Pow(Pi, Div(3, 2))), Pow(Gamma(Div(1, 4)), 2)), Add(1, ConstI)))))

make_entry(ID("2991b5"),
    Formula(Equal(EllipticK((3-2*Sqrt(2))**2), Div(Mul(Add(2, Sqrt(2)), Pow(Gamma(Div(1, 4)), 2)), Mul(16, Sqrt(Pi))))))

make_entry(ID("4b040d"),
    Formula(Equal(EllipticK((4-3*Sqrt(2))/8), Div(Pow(Gamma(Div(1, 4)), 2), Mul(Mul(4, Pow(2, Div(1, 4))), Sqrt(Pi))))))

make_entry(ID("618a54"),
    Formula(Equal(EllipticPi(0, 0), Pi / 2)))

make_entry(ID("18e226"),
    Formula(Equal(EllipticPi(0, 1), Infinity)))

make_entry(ID("061c49"),
    Formula(Equal(EllipticPi(1, 0), UnsignedInfinity)))

make_entry(ID("3c4979"),
    Formula(Equal(EllipticPi(0, Div(1, 2)), Div(Pow(Gamma(Div(1, 4)), 2), Mul(4, Sqrt(Pi))))))

make_entry(ID("124d02"),
    Formula(Equal(EllipticPi(Div(1, 2), 0), (Pi * Sqrt(2)) / 2)))

make_entry(ID("9b0385"),
    Formula(Equal(EllipticPi(Div(1, 2), Div(1, 2)), Add(Div(Pow(Gamma(Div(1, 4)), 2), Mul(4, Sqrt(Pi))), Div(2 * Pow(Pi, Div(3, 2)), Pow(Gamma(Div(1, 4)), 2))))))

make_entry(ID("ce4df4"),
    Formula(Equal(EllipticPi(1, m), UnsignedInfinity)),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("e9c797"),
    Formula(Equal(EllipticPi(n, 1), Cases(Tuple((1-n)**(-1) * Infinity, NotEqual(n, 1)), Tuple(UnsignedInfinity, Equal(n, 1))))),
    Variables(n),
    Assumptions(Element(n, CC)))

make_entry(ID("5d8804"),
    Formula(Equal(EllipticPi(n, 0), Pi / (2 * Sqrt(1 - n)))),
    Variables(n),
    Assumptions(Element(n, CC)))

make_entry(ID("dd67fb"),
    Formula(Equal(EllipticPi(0, m), EllipticK(m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("9227bf"),
    Formula(Equal(EllipticPi(m, m), EllipticE(m) / (1 - m))),
    Variables(m),
    Assumptions(Element(m, CC)))

## Incomplete integrals

make_entry(ID("ba1965") ,
    Formula(Equal(IncompleteEllipticF(0, 0), 0)))

make_entry(ID("4268fc"),
    Formula(Equal(IncompleteEllipticF(0, m), 0)),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("d2adb6"),
    Formula(Equal(IncompleteEllipticF(phi, 0), phi)),
    Variables(phi),
    Assumptions(Element(phi, CC)))

make_entry(ID("0b8fd6"),
    Formula(Equal(IncompleteEllipticF(Pi / 2, m), EllipticK(m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("81f7db"),
    Formula(Equal(IncompleteEllipticF(-Pi / 2, m), -EllipticK(m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("afabeb"),
    Formula(Equal(IncompleteEllipticF(Pi * k / 2, m), k * EllipticK(m))),
    Variables(m, k),
    Assumptions(And(Element(m, CC), Element(k, ZZ), Or(NotEqual(k, 0), NotEqual(m, 1)))))

make_entry(ID("c0ad12"),
    Formula(Equal(IncompleteEllipticF(Pi / 2, 0), Pi / 2)))

make_entry(ID("ace837"),
    Formula(Equal(IncompleteEllipticF(Pi / 2, -1), Gamma(Div(1,4))**2 / (4*Sqrt(2*Pi)))))

make_entry(ID("16612f"),
    Formula(Equal(IncompleteEllipticF(Pi / 2, 1), Infinity)))

make_entry(ID("04c829"),
    Formula(Equal(IncompleteEllipticF(-Pi / 2, 1), -Infinity)))

make_entry(ID("c584c3"),
    Formula(Equal(IncompleteEllipticF(Pi / 3, 1), Log(2+Sqrt(3)))))

make_entry(ID("f5d489"),
    Formula(Equal(IncompleteEllipticF(Pi / 4, 1), Log(1+Sqrt(2)))))

make_entry(ID("a91f8d"),
    Formula(Equal(IncompleteEllipticF(Pi / 6, 1), Log(3)/2)))

make_entry(ID("8b4be6"),
    Formula(Equal(IncompleteEllipticF(Pi / 4, 2), Div(Mul(Sqrt(2), Pow(Gamma(Div(1, 4)), 2)), Mul(8, Sqrt(Pi))))))

make_entry(ID("aac129"),
    Formula(Equal(IncompleteEllipticF(Pi / 6, 4), (EllipticK(Div(1,4)) / 2))))

make_entry(ID("b7cfb3"),
    Formula(Equal(IncompleteEllipticF(phi, 1), Cases(Tuple(Log((1 + Sin(phi))/Cos(phi)), And(LessEqual(-Pi/2, Re(phi), Pi/2), NotElement(phi, Set(-Pi/2, Pi/2)))),
        Tuple(Sign(phi) * Infinity, Element(phi, Set(-Pi/2, Pi/2))),
        Tuple(UnsignedInfinity, Otherwise)))),
    Variables(phi),
    Assumptions(Element(phi, CC)))

make_entry(ID("087a7c"),
    Formula(Equal(IncompleteEllipticF(Asin(1/Sqrt(m)), m), EllipticK(1/m) / Sqrt(m))),
    Variables(m),
    Assumptions(Element(m, SetMinus(CC, Set(0)))))


make_entry(ID("a6c07e"),
    Formula(Equal(IncompleteEllipticE(0, 0), 0)))

make_entry(ID("be3e09"),
    Formula(Equal(IncompleteEllipticE(0, m), 0)))

make_entry(ID("efc7a4"),
    Formula(Equal(IncompleteEllipticE(phi, 0), phi)),
    Variables(phi),
    Assumptions(Element(phi, CC)))

make_entry(ID("1b881e"),
    Formula(Equal(IncompleteEllipticE(Pi/2, m), EllipticE(m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("2ef763"),
    Formula(Equal(IncompleteEllipticE(-Pi/2, m), -EllipticE(m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("a14442"),
    Formula(Equal(IncompleteEllipticE(Pi*k/2, m), k*EllipticE(m))),
    Variables(m, k),
    Assumptions(And(Element(m, CC), Element(k, ZZ))))

make_entry(ID("75e141"),
    Formula(Equal(IncompleteEllipticE(phi, 1), Sin(phi))),
    Variables(phi),
    Assumptions(And(Element(phi, CC), Or(Element(Re(phi), ClosedOpenInterval(-Pi/2, Pi/2)), Equal(phi, Pi/2)))))

make_entry(ID("f35a37"),
    Formula(Equal(IncompleteEllipticE(phi, 1), (-1)**Floor(Re(phi)/Pi+Div(1,2)) * Sin(phi) + 2*Floor(Re(phi)/Pi+Div(1,2)))),
    Variables(phi),
    Assumptions(Element(phi, CC)))

make_entry(ID("51a946"),
    Formula(Equal(IncompleteEllipticE(Pi / 2, 0), Pi / 2)))

make_entry(ID("2573ba"),
    Formula(Equal(IncompleteEllipticE(Pi / 2, -1), Mul(Sqrt(2), Add(Div(Pow(Gamma(Div(1, 4)), 2), Mul(8, Sqrt(Pi))), Div(Pow(Pi, Div(3, 2)), Pow(Gamma(Div(1, 4)), 2)))))))

make_entry(ID("b62aae"),
    Formula(Equal(IncompleteEllipticE(Pi / 2, 1), 1)))

make_entry(ID("dec0d2"),
    Formula(Equal(IncompleteEllipticE(-Pi / 2, 1), -1)))

make_entry(ID("2245df"),
    Formula(Equal(IncompleteEllipticE(Pi*k/2, 1), k)),
    Variables(k),
    Assumptions(Element(k, ZZ)))

make_entry(ID("3aed02"),
    Formula(Equal(IncompleteEllipticE(Pi/3, 1), Sqrt(3) / 2)))

make_entry(ID("d88dd1"),
    Formula(Equal(IncompleteEllipticE(Pi/6, 1), Div(1, 2))))

make_entry(ID("4dabda"),
    Formula(Equal(IncompleteEllipticE(Pi/4, 2), Div(Mul(Sqrt(2), Pow(Pi, Div(3, 2))), Pow(Gamma(Div(1, 4)), 2)))))

make_entry(ID("eba27c"),
    Formula(Equal(IncompleteEllipticE(Pi/6, 4), 2*EllipticE(Div(1, 4)) - Div(3,2)*EllipticK(Div(1, 4)))))

make_entry(ID("f0bcb5"),
    Formula(Equal(IncompleteEllipticE(Asin(1/Sqrt(m)), m), Sqrt(m) * (EllipticE(1/m) - (1 - 1/m)*EllipticK(1/m)))),
    Variables(m),
    Assumptions(Element(m, SetMinus(CC, Set(0, 1)))))


# Functional equations

make_entry(ID("713966"),
    Formula(Equal(EllipticK(Conjugate(m)), Conjugate(EllipticK(m)))),
    Variables(m),
    Assumptions(Element(m, SetMinus(CC, OpenInterval(1, Infinity)))))

make_entry(ID("8e5c81"),
    Formula(Equal(EllipticE(Conjugate(m)), Conjugate(EllipticE(m)))),
    Variables(m),
    Assumptions(Element(m, SetMinus(CC, OpenInterval(1, Infinity)))))


make_entry(ID("b0eb37"),
    Formula(Equal(IncompleteEllipticF(-phi, m), -IncompleteEllipticF(phi, m))),
    Variables(phi, m),
    Assumptions(And(Element(phi, CC), Element(m, CC))))

make_entry(ID("aa1b8e"),
    Formula(Equal(IncompleteEllipticE(-phi, m), -IncompleteEllipticE(phi, m))),
    Variables(phi, m),
    Assumptions(And(Element(phi, CC), Element(m, CC))))

make_entry(ID("255d81"),
    Formula(Equal(IncompleteEllipticPi(n, -phi, m), -IncompleteEllipticPi(n, phi, m))),
    Variables(n, phi, m),
    Assumptions(And(Element(n, CC), Element(phi, CC), Element(m, CC))))


make_entry(ID("685126"),
    Formula(Equal(IncompleteEllipticF(phi + k*Pi, m), IncompleteEllipticF(phi, m) + 2 * k * EllipticK(m))),
    Variables(phi, m, k),
    Assumptions(And(Element(phi, CC), Element(m, CC), Element(k, ZZ), NotEqual(m, 1))))

make_entry(ID("c28288"),
    Formula(Equal(IncompleteEllipticE(phi + k*Pi, m), IncompleteEllipticE(phi, m) + 2 * k * EllipticE(m))),
    Variables(phi, m, k),
    Assumptions(And(Element(phi, CC), Element(m, CC), Element(k, ZZ))))

make_entry(ID("5f84d9"),
    Formula(Equal(IncompleteEllipticPi(n, phi + k*Pi, m), IncompleteEllipticPi(n, phi, m) + 2 * k * EllipticPi(n, m))),
    Variables(n, phi, m, k),
    Assumptions(And(Element(n, CC), Element(phi, CC), Element(m, CC), Element(k, ZZ), NotEqual(n, 1), NotEqual(m, 1))))


# Representation by other functions

## Hypergeometric functions

make_entry(ID("b760d1"),
    Formula(Equal(EllipticK(m), (Pi/2) * Hypergeometric2F1(Div(1,2), Div(1,2), 1, m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("16d2e1"),
    Formula(Equal(EllipticE(m), (Pi/2) * Hypergeometric2F1(-Div(1,2), Div(1,2), 1, m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("752619"),
    Formula(Equal(2*EllipticE(m) - EllipticK(m), (Pi/2) * Hypergeometric2F1(-Div(1,2), Div(3,2), 1, m))),
    Variables(m),
    Assumptions(Element(m, CC)))

## AGM (see AGM ...)

## Carlson integrals
# todo: check singularities in the following

make_entry(ID("0cc11f"),
    Formula(Equal(EllipticK(m), CarlsonRF(0, 1-m, 1))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("6520e7"),
    Formula(Equal(EllipticE(m), 2 * CarlsonRG(0, 1-m, 1))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("9ccaef"),
    Formula(Equal(EllipticPi(n, m), CarlsonRF(0, 1-m, 1) + (n/3) * CarlsonRJ(0, 1-m, 1, 1-n))),
    Variables(n, m),
    Assumptions(And(Element(n, CC), Element(m, CC), NotEqual(m, 1))))

make_entry(ID("41cf8e"),
    Formula(Equal(EllipticE(m), ((1-m)/3) * (CarlsonRD(0, 1-m, 1) + CarlsonRD(0, 1, 1-m)))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("94f646"),
    Formula(Equal(EllipticK(m) - EllipticE(m), (m / 3) * CarlsonRD(0, 1-m, 1))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("55d23d"),
    Formula(Equal(EllipticE(m) - (1-m) * EllipticK(m), ((m*(1-m)) / 3) * CarlsonRD(0, 1, 1-m))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("e2445d"),
    Formula(Equal(IncompleteEllipticF(phi, m), Sin(phi) * CarlsonRF(Cos(phi)**2, 1 - m*Sin(phi)**2, 1))),
    Variables(phi, m),
    Assumptions(And(Element(phi, CC), Element(m, CC), LessEqual(-Pi/2, Re(phi), Pi/2))))

make_entry(ID("f48f54"),
    Formula(Equal(IncompleteEllipticE(phi, m), Sin(phi) * CarlsonRF(Cos(phi)**2, 1 - m*Sin(phi)**2, 1) - Div(1,3)*m*Sin(phi)**3*CarlsonRD(Cos(phi)**2, 1-m*Sin(phi)**2, 1))),
    Variables(phi, m),
    Assumptions(And(Element(phi, CC), Element(m, CC), LessEqual(-Pi/2, Re(phi), Pi/2))))

make_entry(ID("8f4e31"),
    Formula(Equal(IncompleteEllipticPi(n, phi, m), Sin(phi) * CarlsonRF(Cos(phi)**2, 1 - m*Sin(phi)**2, 1) + Div(1,3)*n*Sin(phi)**3*CarlsonRJ(Cos(phi)**2, 1-m*Sin(phi)**2, 1, 1-n*Sin(phi)**2))),
    Variables(n, phi, m),
    Assumptions(And(Element(n, CC), Element(phi, CC), Element(m, CC), LessEqual(-Pi/2, Re(phi), Pi/2))))

