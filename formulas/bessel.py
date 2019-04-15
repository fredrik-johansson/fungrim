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
    Section("Differential equations"),
    Entries(
        "0fea28",
        "727f67",
        "ad9caa",
        "62f23c",
        "522c1a",
        "ddfb97",
        "95e561",
        "fd9add",
    ),
    Section("Derivatives and recurrence relations"),
    SeeTopics("Recurrence relations for Bessel functions"),
    Entries(
        "d56914",
        "b6d600",
        "4fb391",
        "9d98f8",
        "5aceb9",
        "40aeb6",
        "58d91f",
        "a0ff0b",
    ),
    Section("Hypergeometric representations"),
    SeeTopics("Hypergeometric representations of Bessel functions"),
    Entries(
        "ecd36f",
        "81eec6",
        "7efe21",
    ),
    Section("Connection formulas"),
    Entries(
        "54bce2",
        "afbd22",
        "86bc7d",
        "15bbb1",
        "2a4195",
        "d5b7e8",
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

def_Topic(
    Title("Recurrence relations for Bessel functions"),
    SeeTopics("Bessel functions"),
    Section("Consecutive orders"),
    Entries(
        "d56914",
        "b6d600",
        "4fb391",
        "9d98f8",
    ),
    Section("Derivatives in terms of the direct functions"),
    Entries(
        "f1afc0",
        "8b6264",
        "c0247f",
        "81ffcd",
        "5aceb9",
        "40aeb6",
        "58d91f",
        "a0ff0b",
        "2488bb",
        "68cc2f",
        "e284d7",
        "807f3f",
    ),
    Section("Consecutive derivatives"),
    Entries(
        "15ac84",
        "f303c9",
        "9b2f38",
        "e85dee",
        "e233b0",
        "7377c8",
    ),
)

def_Topic(
    Title("Hypergeometric representations of Bessel functions"),
    SeeTopics("Bessel functions", "Confluent hypergeometric functions"),
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

make_entry(ID("0fea28"),
    SymbolDefinition(BesselJDerivative, BesselJDerivative(nu, z, r), "Differentiated Bessel function of the first kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselJDerivative(nu, z, r)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, ZZ), Element(z, RR), Element(r, ZZGreaterEqual(0))), Element(BesselJDerivative(nu, z, r), RR)),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity)), Element(r, ZZGreaterEqual(0))), Element(BesselJDerivative(nu, z, r), RR)),
        Tuple(And(Element(nu, ZZ), Element(z, CC), Element(r, ZZGreaterEqual(0))), Element(BesselJDerivative(nu, z, r), CC)),
        Tuple(And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0))), Element(BesselJDerivative(nu, z, r), CC)),
      )),
    )

make_entry(ID("727f67"),
    SymbolDefinition(BesselYDerivative, BesselYDerivative(nu, z, r), "Differentiated Bessel function of the second kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselYDerivative(nu, z, r)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity)), Element(r, ZZGreaterEqual(0))), Element(BesselYDerivative(nu, z, r), RR)),
        Tuple(And(Element(nu, SetMinus(CC, Set(0))), Element(z, CC), Element(r, ZZGreaterEqual(0))), Element(BesselYDerivative(nu, z, r), CC)),
      )),
    )

make_entry(ID("ad9caa"),
    Formula(Equal(z**2 * BesselJDerivative(nu,z,2) + z * BesselJDerivative(nu,z,1) + (z**2 - nu**2) * BesselJ(nu,z), 0)),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC)),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("62f23c"),
    Formula(Equal(z**2 * BesselYDerivative(nu,z,2) + z * BesselYDerivative(nu,z,1) + (z**2 - nu**2) * BesselY(nu,z), 0)),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("522c1a"),
    SymbolDefinition(BesselIDerivative, BesselIDerivative(nu, z, r), "Differentiated modified Bessel function of the first kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselIDerivative(nu, z, r)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, ZZ), Element(z, RR), Element(r, ZZGreaterEqual(0))), Element(BesselIDerivative(nu, z, r), RR)),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity)), Element(r, ZZGreaterEqual(0))), Element(BesselIDerivative(nu, z, r), RR)),
        Tuple(And(Element(nu, ZZ), Element(z, CC), Element(r, ZZGreaterEqual(0))), Element(BesselIDerivative(nu, z, r), CC)),
        Tuple(And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0))), Element(BesselIDerivative(nu, z, r), CC)),
      )),
    )

make_entry(ID("ddfb97"),
    SymbolDefinition(BesselKDerivative, BesselKDerivative(nu, z, r), "Differentiated modified Bessel function of the second kind"),
    Description("The following table lists all conditions such that", SourceForm(BesselKDerivative(nu, z, r)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(nu, RR), Element(z, OpenInterval(0, Infinity)), Element(r, ZZGreaterEqual(0))), Element(BesselKDerivative(nu, z, r), RR)),
        Tuple(And(Element(nu, SetMinus(CC, Set(0))), Element(z, CC), Element(r, ZZGreaterEqual(0))), Element(BesselKDerivative(nu, z, r), CC)),
      )),
    )

make_entry(ID("95e561"),
    Formula(Equal(z**2 * BesselIDerivative(nu,z,2) + z * BesselIDerivative(nu,z,1) - (z**2 + nu**2) * BesselI(nu,z), 0)),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC)),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("fd9add"),
    Formula(Equal(z**2 * BesselKDerivative(nu,z,2) + z * BesselKDerivative(nu,z,1) - (z**2 + nu**2) * BesselK(nu,z), 0)),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))



make_entry(ID("f1afc0"),
    Formula(Equal(BesselJDerivative(0,z,1), -BesselJ(1,z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("8b6264"),
    Formula(Equal(BesselYDerivative(0,z,1), -BesselY(1,z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("5aceb9"),
    Formula(Equal(BesselJDerivative(nu,z,1), (BesselJ(nu-1,z) - BesselJ(nu+1,z))/2)),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC)),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("40aeb6"),
    Formula(Equal(BesselYDerivative(nu,z,1), (BesselY(nu-1,z) - BesselY(nu+1,z))/2)),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("2488bb"),
    Formula(Equal(BesselJDerivative(nu,z,r), Div(1,2**r) * Sum((-1)**k * Binomial(r,k) * BesselJ(nu+2*k-r,z), Tuple(k, 0, r)))),
    Variables(nu,z,r),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC), Element(r, ZZGreaterEqual(0))),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0))),
    ))

make_entry(ID("68cc2f"),
    Formula(Equal(BesselYDerivative(nu,z,r), Div(1,2**r) * Sum((-1)**k * Binomial(r,k) * BesselY(nu+2*k-r,z), Tuple(k, 0, r)))),
    Variables(nu,z,r),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0))),
    ))

make_entry(ID("d56914"),
    Formula(Equal(BesselJ(nu,z), (z/(2*nu))*(BesselJ(nu-1,z) + BesselJ(nu+1,z)))),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, SetMinus(ZZ, Set(0))), Element(z, CC)),
        And(Element(nu, SetMinus(CC, Set(0))), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("b6d600"),
    Formula(Equal(BesselY(nu,z), (z/(2*nu))*(BesselY(nu-1,z) + BesselY(nu+1,z)))),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, SetMinus(ZZ, Set(0))), Element(z, CC)),
        And(Element(nu, SetMinus(CC, Set(0))), Element(z, SetMinus(CC, Set(0))))
    ))




make_entry(ID("15ac84"),
    Formula(Equal((r**2+4*r-n**2+4)*BesselJDerivative(n,0,r+2) + (r+1)*(r+2)*BesselJDerivative(n,0,r), 0)),
    Variables(nu,r),
    Assumptions(And(Element(n,ZZ), Element(r, ZZGreaterEqual(0))))) 

make_entry(ID("9b2f38"),
    Formula(Equal(
        z**2*(r**2 + 7*r + 12) * (BesselJDerivative(nu,z,r+4) / Factorial(r+4)) +
        z*(2*r**2+11*r+15) * (BesselJDerivative(nu,z,r+3) / Factorial(r+3)) +
        (r*(r+4) + z**2 - nu**2 + 4) * (BesselJDerivative(nu,z,r+2) / Factorial(r+2)) +
        2*z * (BesselJDerivative(nu,z,r+1) / Factorial(r+1)) +
        (BesselJDerivative(nu,z,r) / Factorial(r)), 0)),
    Variables(nu, z, r),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC), Element(r, ZZGreaterEqual(0))),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0)))
    ))

make_entry(ID("e85dee"),
    Formula(Equal(
        z**2*(r**2 + 7*r + 12) * (BesselYDerivative(nu,z,r+4) / Factorial(r+4)) +
        z*(2*r**2+11*r+15) * (BesselYDerivative(nu,z,r+3) / Factorial(r+3)) +
        (r*(r+4) + z**2 - nu**2 + 4) * (BesselYDerivative(nu,z,r+2) / Factorial(r+2)) +
        2*z * (BesselYDerivative(nu,z,r+1) / Factorial(r+1)) +
        (BesselYDerivative(nu,z,r) / Factorial(r)), 0)),
    Variables(nu, z, r),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0)))
    ))


make_entry(ID("c0247f"),
    Formula(Equal(BesselIDerivative(0,z,1), BesselI(1,z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("81ffcd"),
    Formula(Equal(BesselKDerivative(0,z,1), -BesselK(1,z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("58d91f"),
    Formula(Equal(BesselIDerivative(nu,z,1), (BesselI(nu-1,z) + BesselI(nu+1,z))/2)),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC)),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("a0ff0b"),
    Formula(Equal(BesselKDerivative(nu,z,1), -((BesselK(nu-1,z) + BesselK(nu+1,z))/2))),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("e284d7"),
    Formula(Equal(BesselIDerivative(nu,z,r), Div(1,2**r) * Sum(Binomial(r,k) * BesselI(nu+2*k-r,z), Tuple(k, 0, r)))),
    Variables(nu,z,r),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC), Element(r, ZZGreaterEqual(0))),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0))),
    ))

make_entry(ID("807f3f"),
    Formula(Equal(BesselKDerivative(nu,z,r), Div((-1)**r,2**r) * Sum(Binomial(r,k) * BesselK(nu+2*k-r,z), Tuple(k, 0, r)))),
    Variables(nu,z,r),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0))),
    ))

make_entry(ID("4fb391"),
    Formula(Equal(BesselI(nu,z), (z/(2*nu))*(BesselI(nu-1,z) - BesselI(nu+1,z)))),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, SetMinus(ZZ, Set(0))), Element(z, CC)),
        And(Element(nu, SetMinus(CC, Set(0))), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("9d98f8"),
    Formula(Equal(BesselK(nu,z), -((z/(2*nu))*(BesselK(nu-1,z) - BesselK(nu+1,z))))),
    Variables(nu,z),
    Assumptions(
        And(Element(nu, SetMinus(ZZ, Set(0))), Element(z, CC)),
        And(Element(nu, SetMinus(CC, Set(0))), Element(z, SetMinus(CC, Set(0))))
    ))

make_entry(ID("f303c9"),
    Formula(Equal((r**2+4*r-n**2+4)*BesselIDerivative(n,0,r+2) - (r+1)*(r+2)*BesselIDerivative(n,0,r), 0)),
    Variables(nu,r),
    Assumptions(And(Element(n,ZZ), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("e233b0"),
    Formula(Equal(
        z**2*(r**2 + 7*r + 12) * (BesselIDerivative(nu,z,r+4) / Factorial(r+4)) +
        z*(2*r**2+11*r+15) * (BesselIDerivative(nu,z,r+3) / Factorial(r+3)) +
        (r*(r+4) - z**2 - nu**2 + 4) * (BesselIDerivative(nu,z,r+2) / Factorial(r+2)) -
        2*z * (BesselIDerivative(nu,z,r+1) / Factorial(r+1)) -
        (BesselIDerivative(nu,z,r) / Factorial(r)), 0)),
    Variables(nu, z, r),
    Assumptions(
        And(Element(nu, ZZ), Element(z, CC), Element(r, ZZGreaterEqual(0))),
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0)))
    ))

make_entry(ID("7377c8"),
    Formula(Equal(
        z**2*(r**2 + 7*r + 12) * (BesselKDerivative(nu,z,r+4) / Factorial(r+4)) +
        z*(2*r**2+11*r+15) * (BesselKDerivative(nu,z,r+3) / Factorial(r+3)) +
        (r*(r+4) - z**2 - nu**2 + 4) * (BesselKDerivative(nu,z,r+2) / Factorial(r+2)) -
        2*z * (BesselKDerivative(nu,z,r+1) / Factorial(r+1)) -
        (BesselKDerivative(nu,z,r) / Factorial(r)), 0)),
    Variables(nu, z, r),
    Assumptions(
        And(Element(nu, CC), Element(z, SetMinus(CC, Set(0))), Element(r, ZZGreaterEqual(0)))
    ))




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

