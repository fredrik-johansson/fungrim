# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Bessel functions"),
    Entries(
        "b4165c",
        "5bb42e",
        "8ac81d",
        "ff93d0",
    ),
    Section("Hypergeometric representations"),
    Entries(
        "ecd36f",
        "81eec6",
        "b049dc",
        "7efe21",
        "98703d",
        "9ad254",
        "32e162",
        "127f05",
    ),
    Section("Connection formulas"),
    Entries(
        "86bc7d",
        "15bbb1",
        "2a4195",
        "d5b7e8",
    ),
    Section("Functional equations"),
    Entries(
        "54bce2",
        "afbd22",
    ),
    Section("Hankel functions"),
    Entries(
        "24d383",
        "d154dd",
        "6a6a09",
        "1dce21",
    ),
    Section("Integral representations"),
    Entries(
        "99c077",
        "cac83e",
        "7ae3ed",
        "c29d6f",
    ),
)

make_entry(ID("b4165c"),
    SymbolDefinition(BesselJ, BesselJ(nu, z), "Bessel function of the first kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselJ(nu, z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, ZZ), Element(z, RR)), Element(BesselJ(nu, z), RR)),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity))), Element(BesselJ(nu, z), RR)),
        Tuple(And(Element(nu, ZZ), Element(z, CC)), Element(BesselJ(nu, z), CC)),
        Tuple(And(Element(nu, CC), Element(z, SetMinus(CC, Set(0)))), Element(BesselJ(nu, z), CC)),
      )),
    )

make_entry(ID("5bb42e"),
    SymbolDefinition(BesselY, BesselY(nu, z), "Bessel function of the second kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselY(nu, z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity))), Element(BesselY(nu, z), RR)),
        Tuple(And(Element(nu, SetMinus(CC, Set(0))), Element(z, CC)), Element(BesselY(nu, z), CC)),
      )),
    )

make_entry(ID("8ac81d"),
    SymbolDefinition(BesselI, BesselI(nu, z), "Modified Bessel function of the first kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselI(nu, z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, ZZ), Element(z, RR)), Element(BesselI(nu, z), RR)),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity))), Element(BesselI(nu, z), RR)),
        Tuple(And(Element(nu, ZZ), Element(z, CC)), Element(BesselI(nu, z), CC)),
        Tuple(And(Element(nu, CC), Element(z, SetMinus(CC, Set(0)))), Element(BesselI(nu, z), CC)),
      )),
    )

make_entry(ID("ff93d0"),
    SymbolDefinition(BesselK, BesselK(nu, z), "Modified Bessel function of the second kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselK(nu, z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity))), Element(BesselK(nu, z), RR)),
        Tuple(And(Element(nu, SetMinus(CC, Set(0))), Element(z, CC)), Element(BesselK(nu, z), CC)),
      )),
    )

make_entry(ID("ecd36f"),
    Formula(Equal(BesselJ(nu, z), (z/2)**nu * Hypergeometric0F1Regularized(nu+1, -(z**2/4)))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, ZZGreaterEqual(0)), Element(z, CC)),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("81eec6"),
    Formula(Equal(BesselI(nu, z), (z/2)**nu * Hypergeometric0F1Regularized(nu+1, (z**2/4)))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, ZZGreaterEqual(0)), Element(z, CC)),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("b049dc"),
    Formula(Equal(BesselY(nu, z),
        (1/Sin(ConstPi*nu)) * (Cos(ConstPi*nu) * (z/2)**nu * Hypergeometric0F1Regularized(nu+1, -(z**2/4))
            - (z/2)**(-nu) * Hypergeometric0F1Regularized(1-nu, -(z**2/4))))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, SetMinus(CC, ZZ)), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("7efe21"),
    Formula(Equal(BesselK(nu, z), ((2*z)/ConstPi)**(-Div(1,2)) * Exp(-z) * HypergeometricUStar(nu+Div(1,2), 2*nu+1, 2*z))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("98703d"),
    Formula(Equal(BesselK(nu, z),
        Div(1,2) * (ConstPi/Sin(ConstPi*nu)) * (Div(z,2)**(-nu) * Hypergeometric0F1Regularized(1-nu, z**2/4)
            - Div(z,2)**nu * Hypergeometric0F1Regularized(1+nu, z**2/4)))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, SetMinus(CC, ZZ)), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("9ad254"),
    Formula(Equal(BesselJ(nu, z),
            (z/2)**nu * (Exp(-(ConstI*z)) / GammaFunction(nu+1)) * Hypergeometric1F1(nu+Div(1,2), 2*nu+1, 2*ConstI*z))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, ZZGreaterEqual(0)), Element(z, CC)),
        And(Element(nu, CC), NotElement(nu, ZZLessEqual(-1)), Element(z, SetMinus(CC, Set(0))))
    ))

_Ap = (ConstI*z)**(-Div(1,2)-nu)
_Am = (-(ConstI*z))**(-Div(1,2)-nu)
_Bp = Exp(ConstI*z) * HypergeometricUStar(nu+Div(1,2), 2*nu+1, -(2*ConstI*z))
_Bm = Exp(-(ConstI*z)) * HypergeometricUStar(nu+Div(1,2), 2*nu+1, (2*ConstI*z))

make_entry(ID("32e162"),
    Formula(Equal(BesselJ(nu, z), (z**nu / (2*ConstPi)**(Div(1,2))) * (_Ap*_Bp + _Am*_Bm))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("127f05"),
    Formula(Where(Equal(BesselJ(nu, z),
        (2*ConstPi*z)**(-Div(1,2)) * (Exp(-(ConstI*theta)) * HypergeometricUStar(nu+Div(1,2), 2*nu+1, -(2*ConstI*z))
            + Exp(ConstI*theta) * HypergeometricUStar(nu+Div(1,2), 2*nu+1, (2*ConstI*z)))), Equal(theta, ConstPi*(2*nu+1)/4-z))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, CC), Greater(Re(z), 0)),
    ))

make_entry(ID("54bce2"),
    Formula(Equal(BesselJ(-n, z), (-1)**n * BesselJ(n, z))),
    Variables(n, z),
    Assumptions(
        And(Element(n, ZZ), Element(z, CC)),
    ))

make_entry(ID("afbd22"),
    Formula(Equal(BesselI(-n, z), BesselI(n, z))),
    Variables(n, z),
    Assumptions(
        And(Element(n, ZZ), Element(z, CC)),
    ))

make_entry(ID("86bc7d"),
    Formula(Equal(BesselI(nu, z), z**nu * (ConstI*z)**(-nu) * BesselJ(nu, ConstI*z))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, ZZGreaterEqual(0)), Element(z, CC)),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("15bbb1"),
    Formula(Equal(BesselI(n, z), ConstI**(-n) * BesselJ(n, ConstI*z))),
    Variables(n, z),
    Assumptions(
        And(Element(n, ZZ), Element(z, CC)),
    ))

make_entry(ID("2a4195"),
    Formula(Equal(BesselY(nu, z), ((Cos(ConstPi*nu)*BesselJ(nu,z) - BesselJ(-nu,z))/Sin(ConstPi*nu)))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, SetMinus(CC, ZZ)), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("d5b7e8"),
    Formula(Equal(BesselY(n, z), -(2/ConstPi) * (ConstI**n * BesselK(n, ConstI*z) + (Log(ConstI*z)-Log(z))*BesselJ(n,z)))),
    Variables(n, z),
    Assumptions(
        And(Element(n, ZZ), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("24d383"),
    SymbolDefinition(HankelH1, HankelH1(nu, z), "Hankel function of the first kind"),
    Description("The following table lists all conditions such that", SourceForm(HankelH1(nu, z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, CC), Element(z, SetMinus(CC, Set(0)))), Element(HankelH1(nu, z), CC)),
      )),
    )

make_entry(ID("d154dd"),
    SymbolDefinition(HankelH2, HankelH2(nu, z), "Hankel function of the second kind"),
    Description("The following table lists all conditions such that", SourceForm(HankelH2(nu, z)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, CC), Element(z, SetMinus(CC, Set(0)))), Element(HankelH2(nu, z), CC)),
      )),
    )

make_entry(ID("6a6a09"),
    Formula(Equal(HankelH1(nu, z), BesselJ(nu, z) + ConstI * BesselY(nu, z))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("1dce21"),
    Formula(Equal(HankelH2(nu, z), BesselJ(nu, z) - ConstI * BesselY(nu, z))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))


make_entry(ID("99c077"),
    Formula(Equal(BesselJ(n,z), (1/ConstPi) * Integral(Cos(n*t - z*Sin(t)), Tuple(t, 0, ConstPi)))),
    Variables(n, z),
    Assumptions(
        And(Element(n, ZZ), Element(z, CC)),
    ))

make_entry(ID("cac83e"),
    Formula(Equal(BesselJ(nu,z), (1/ConstPi) * Integral(Cos(nu*t - z*Sin(t)), Tuple(t, 0, ConstPi)) - Sin(ConstPi*nu)/ConstPi *
        Integral(Exp(-(z*Sinh(t))-nu*t), Tuple(t, 0, Infinity)))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, CC), Greater(Re(z), 0)),
    ))

make_entry(ID("7ae3ed"),
    Formula(Equal(BesselI(nu,z), (1/ConstPi) * Integral(Exp(z*Cos(t))*Cos(nu*t), Tuple(t, 0, ConstPi)) - Sin(ConstPi*nu)/ConstPi *
        Integral(Exp(-(z*Cosh(t))-nu*t), Tuple(t, 0, Infinity)))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, CC), Greater(Re(z), 0)),
    ))

make_entry(ID("c29d6f"),
    Formula(Equal(BesselK(nu,z), Integral(Exp(-(z*Cosh(t)))*Cosh(nu*t), Tuple(t, 0, Infinity)))),
    Variables(nu, z),
    Assumptions(
        And(Element(nu, CC), Element(z, CC), Greater(Re(z), 0)),
    ))

