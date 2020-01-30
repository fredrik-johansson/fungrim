# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Coulomb wave functions"),
    Section("Definitions"),
    Entries(
        "8b2cb9",
        "f25e3d",
        "16a4e7",
        "2b12f4",
        "512063",
    ),
    Section("Differential equations"),
    Entries(
        "ad8df6",
        "74274a",
    ),
    Section("Connection formulas"),
    Entries(
        "192a3e",
        "8547ab",
        "01af55",
        "e20938",
        "304559",
    ),
    Section("Normalization functions"),
    Entries(
        "4a4739",
        "ed2bf6",
    ),
    Section("Derivatives"),
    Entries(
        "a51a4b",
        "2fec14",
        "07a654",
        "faa118",
        "eca10b",
    ),
    Section("Hypergeometric representations"),
    Subsection("Kummer function"),
    Entries(
        "d280c5",
        "2a2f18",
    ),
    Subsection("Tricomi function"),
    Entries(
        "1976e1",
        "e2efbf",
        "8027e8",
        "69e5fb",
        "bcdfc6",
        "f0414a",
        "781eae",
        "0cc301",
    ),

)

# Definitions

make_entry(ID("8b2cb9"),
    SymbolDefinition(CoulombF, CoulombF(ell,eta,z), "Regular Coulomb wave function"))

make_entry(ID("f25e3d"),
    SymbolDefinition(CoulombG, CoulombG(ell,eta,z), "Irregular Coulomb wave function"))

make_entry(ID("16a4e7"),
    SymbolDefinition(CoulombH, CoulombH(omega,ell,eta,z), "Outgoing and ingoing Coulomb wave function"))

make_entry(ID("2b12f4"),
    SymbolDefinition(CoulombC, CoulombC(ell,eta), "Coulomb wave function Gamow factor"))

make_entry(ID("512063"),
    SymbolDefinition(CoulombSigma, CoulombSigma(ell,eta), "Coulomb wave function phase shift"))

coulomb_param_condition = And(NotElement(1+ell+ConstI*eta, ZZLessEqual(0)), NotElement(1+ell-ConstI*eta, ZZLessEqual(0)))

# Differential equations

C1 = Subscript(c, 1)
C2 = Subscript(c, 2)

make_entry(ID("ad8df6"),
    Formula(Where(Equal(ComplexDerivative(y(z), For(z, z, 2)) + (1 - (2*eta)/z - (ell*(ell+1))/z**2)*y(z), 0), Equal(y(z), C1*CoulombF(ell,eta,z) + C2*CoulombG(ell,eta,z)))),
    Variables(ell, eta, z, C1, C2),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))), Element(C1, CC), Element(C2, CC))))

make_entry(ID("74274a"),
    Formula(Equal(CoulombG(ell,eta,z) * Parentheses(ComplexDerivative(CoulombF(ell,eta,z), For(z, z, 1))) - 
                  Parentheses(ComplexDerivative(CoulombG(ell,eta,z), For(z, z, 1))) * CoulombF(ell,eta,z), 1)),
    Variables(ell, eta, z),
    Assumptions(And(coulomb_param_condition, Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

# Connection formulas

make_entry(ID("192a3e"),
    Formula(Equal(CoulombF(ell, eta, z), (CoulombH(1, ell, eta, z) - CoulombH(-1, ell, eta, z))/(2*ConstI))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("8547ab"),
    Formula(Equal(CoulombG(ell, eta, z), (CoulombH(1, ell, eta, z) + CoulombH(-1, ell, eta, z))/2)),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("01af55"),
    Formula(Equal(CoulombH(omega, ell, eta, z), CoulombG(ell, eta, z) + omega*ConstI*CoulombF(ell, eta, z))),
    Variables(omega, ell, eta, z),
    Assumptions(And(Element(omega, Set(-1,1)), Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("e20938"),
    Formula(Where(Equal(CoulombG(ell, eta, z),
        (CoulombF(ell,eta,z)*Cos(chi) - CoulombF(-ell-1,eta,z))/Sin(chi)),
            Equal(chi, CoulombSigma(ell,eta) - CoulombSigma(-ell-1,eta) - (ell+Div(1,2))*Pi))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC),
        NotElement(2*ell, ZZ),
        NotElement(1+ell+ConstI*eta, ZZLessEqual(0)),
        NotElement(1+ell-ConstI*eta, ZZLessEqual(0)),
        NotElement(-ell+ConstI*eta, ZZLessEqual(0)),
        NotElement(-ell-ConstI*eta, ZZLessEqual(0)), Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("304559"),
    Formula(Where(Equal(CoulombH(omega, ell, eta, z),
        (CoulombF(ell,eta,z)*Exp(omega*ConstI*chi) - CoulombF(-ell-1,eta,z))/Sin(chi)),
            Equal(chi, CoulombSigma(ell,eta) - CoulombSigma(-ell-1,eta) - (ell+Div(1,2))*Pi))),
    Variables(omega, ell, eta, z),
    Assumptions(And(Element(omega, Set(-1,1)), Element(ell, CC), Element(eta, CC),
        NotElement(2*ell, ZZ),
        NotElement(1+ell+ConstI*eta, ZZLessEqual(0)),
        NotElement(1+ell-ConstI*eta, ZZLessEqual(0)),
        NotElement(-ell+ConstI*eta, ZZLessEqual(0)),
        NotElement(-ell-ConstI*eta, ZZLessEqual(0)), Element(z, SetMinus(CC, Set(0))))))

# Normalization functions

make_entry(ID("4a4739"),
    Formula(Equal(CoulombC(ell, eta), (2**ell / Gamma(2*ell+2)) * Exp((LogGamma(1+ell+ConstI*eta) + LogGamma(1+ell-ConstI*eta) - Pi*eta)/2))),
    Variables(ell, eta),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition)))

make_entry(ID("ed2bf6"),
    Formula(Equal(CoulombSigma(ell, eta), (LogGamma(1+ell+ConstI*eta) - LogGamma(1+ell-ConstI*eta))/(2*ConstI))),
    Variables(ell, eta),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition)))

# Derivatives

make_entry(ID("a51a4b"),
    Formula(Equal(ComplexDerivative(CoulombF(ell, eta, z), For(z, z, 1)),
        ((ell+1)/z + eta/(ell+1)) * CoulombF(ell,eta,z) - ((Sqrt(1+ell+ConstI*eta)*Sqrt(1+ell-ConstI*eta))/(ell+1)) * CoulombF(ell+1,eta,z))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), NotEqual(ell, -1), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("2fec14"),
    Formula(Equal(ComplexDerivative(CoulombG(ell, eta, z), For(z, z, 1)),
        ((ell+1)/z + eta/(ell+1)) * CoulombG(ell,eta,z) - ((Sqrt(1+ell+ConstI*eta)*Sqrt(1+ell-ConstI*eta))/(ell+1)) * CoulombG(ell+1,eta,z))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), NotEqual(ell, -1), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("07a654"),
    Formula(Where(Equal(ComplexDerivative(f(z), For(z, z, 2)),
        ((2*eta)/z + (ell*(ell+1))/z**2 - 1) * f(z)), Equal(f(z), C1 * CoulombF(ell,eta,z) + C2 * CoulombG(ell,eta,z)))),
    Variables(ell, eta, C1, C2, z),
    Assumptions(And(Element(C1, CC), Element(C2, CC), Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("faa118"),
    Formula(Where(Equal(ComplexDerivative(f(z), For(z, z, 3)),
        ((2*eta)/z + (ell*(ell+1))/z**2 - 1) * ComplexDerivative(f(z), For(z, z, 1))
            - 2*(eta/z**2 + (ell*(ell+1))/z**3) * f(z)), Equal(f(z), C1 * CoulombF(ell,eta,z) + C2 * CoulombG(ell,eta,z)))),
    Variables(ell, eta, C1, C2, z),
    Assumptions(And(Element(C1, CC), Element(C2, CC), Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("eca10b"),
    Formula(Where(Equal(
        ComplexDerivative(f(z), For(z, z, r+4)) / Factorial(r+4),
        (-1/(z**2 * (r**2+7*r+12))) *
        (2*(r**2+5*r+6)*z*(ComplexDerivative(f(z), For(z, z, r+3)) / Factorial(r+3)) + 
         (r**2+3*r + z**2 - 2*z*eta - ell*(ell+1) + 2)*(ComplexDerivative(f(z), For(z, z, r+2)) / Factorial(r+2)) + 
         2*(z-eta) * (ComplexDerivative(f(z), For(z, z, r+1)) / Factorial(r+1)) + 
         (ComplexDerivative(f(z), For(z, z, r)) / Factorial(r)))),
            Equal(f(z), C1 * CoulombF(ell,eta,z) + C2 * CoulombG(ell,eta,z)))),
    Variables(r, ell, eta, C1, C2, z),
    Assumptions(And(Element(r, ZZGreaterEqual(0)),
        Element(C1, CC), Element(C2, CC), Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))))

# Hypergeometric representations

make_entry(ID("d280c5"),
    Formula(Equal(CoulombF(ell, eta, z), CoulombC(ell,eta) * z**(ell+1) * Exp(omega*ConstI*z) * Hypergeometric1F1(1+ell+omega*ConstI*eta, 2*ell+2, -(2*omega*ConstI*z)))),
    Variables(omega, ell, eta, z),
    Assumptions(And(Element(omega, Set(-1,1)), Element(ell, CC), Element(eta, CC), coulomb_param_condition, NotElement(2*ell+2, ZZLessEqual(0)), Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("2a2f18"),
    Formula(Equal(CoulombF(ell, eta, z), 2**ell * Exp((LogGamma(1+ell+ConstI*eta) + LogGamma(1+ell-ConstI*eta) - Pi*eta)/2) * z**(ell+1) * Exp(omega*ConstI*z) * Hypergeometric1F1Regularized(1+ell+omega*ConstI*eta, 2*ell+2, -(2*omega*ConstI*z)))),
    Variables(omega, ell, eta, z),
    Assumptions(And(Element(omega, Set(-1,1)), Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))))))


_U1 = HypergeometricUStar(u, 2*ell+2, -(2*ConstI*z))
_U2 = HypergeometricUStar(v, 2*ell+2, 2*ConstI*z)

make_entry(ID("1976e1"),
    Formula(Equal(CoulombF(ell, eta, z), Where(
        2**ell * z**(ell+1) * Exp((LogGamma(u)+LogGamma(v)-Pi*eta)/2) * 
            (
                ((Exp(ConstI*z) * _U1) / ((2*ConstI*z)**u * Gamma(v))) +
                ((Exp(-ConstI*z) * _U2) / ((-(2*ConstI*z))**v * Gamma(u)))
            ),
        Equal(u, 1+ell+ConstI*eta), Equal(v, 1+ell-ConstI*eta)))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))))))

_H1 = (2*z)**(-(ConstI*eta)) * Exp(ConstI*(z-ell*Pi/2 + CoulombSigma(ell,eta))) * HypergeometricUStar(1+ell+ConstI*eta, 2*ell+2, -(2*ConstI*z))
_H2 = (2*z)**((ConstI*eta)) * Exp(-(ConstI*(z-ell*Pi/2 + CoulombSigma(ell,eta)))) * HypergeometricUStar(1+ell-ConstI*eta, 2*ell+2, (2*ConstI*z))

make_entry(ID("e2efbf"),
    Formula(Equal(CoulombG(l,eta,z), Div(1,2) * (_H1 + _H2))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))),
        Greater(Re(z), 0))))

make_entry(ID("8027e8"),
    Formula(Equal(CoulombG(l,eta,z), _H1 - ConstI*CoulombF(ell,eta,z))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))),
        Or(GreaterEqual(Im(z), 0), Greater(Re(z), 0)))))

make_entry(ID("69e5fb"),
    Formula(Equal(CoulombG(l,eta,z), _H2 + ConstI*CoulombF(ell,eta,z))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))),
        Or(Less(Im(z), 0), GreaterEqual(Re(z), 0)))))

make_entry(ID("bcdfc6"),
    Formula(Equal(CoulombH(1,l,eta,z), _H1)),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))),
        Or(GreaterEqual(Im(z), 0), Greater(Re(z), 0)))))

make_entry(ID("f0414a"),
    Formula(Equal(CoulombH(1,l,eta,z), _H2 + 2*ConstI*CoulombF(ell,eta,z))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))),
        Or(Less(Im(z), 0), GreaterEqual(Re(z), 0)))))

make_entry(ID("781eae"),
    Formula(Equal(CoulombH(-1,l,eta,z), _H2)),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))),
        Or(Less(Im(z), 0), GreaterEqual(Re(z), 0)))))

make_entry(ID("0cc301"),
    Formula(Equal(CoulombH(-1,l,eta,z), _H1 - 2*ConstI*CoulombF(ell,eta,z))),
    Variables(ell, eta, z),
    Assumptions(And(Element(ell, CC), Element(eta, CC), coulomb_param_condition, Element(z, SetMinus(CC, Set(0))),
        Or(GreaterEqual(Im(z), 0), Greater(Re(z), 0)))))

