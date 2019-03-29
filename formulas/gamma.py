# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Gamma function"),
    Section("Particular values"),
    Entries(
        "f1d31a",
        "e68d11",
        "19d480",
        "f826a6",
        "48ac55",
    ),
    Section("Functional equations"),
    Entries(
        "78f1f4",
        "639d91",
        "14af98",
        "56d710",
        "b510b6",
        "a787eb",
        "90a1e1",
    ),
    Section("Integral representations"),
    Entries(
        "4e4e0f",
    ),
    Section("Analytic properties"),
    Entries(
        "798c5d",
        "2870f0",
        "34d6ae",
        "d086bd",
        "9a44c5",
        "a76328",
    ),
    Section("Complex parts"),
    Entries(
        "d7d2a0",
    ),
)

GammaFunction_domain = SetMinus(CC, ZZLessEqual(0))
GammaFunction_sub1_domain = SetMinus(CC, ZZLessEqual(1))

make_entry(ID("f1d31a"),
    Formula(Equal(GammaFunction(n), Factorial(n-1))),
    Variables(n),
    Assumptions(Element(n, GammaFunction_domain)))

make_entry(ID("e68d11"),
    Formula(Equal(GammaFunction(1), 1)))

make_entry(ID("19d480"),
    Formula(Equal(GammaFunction(2), 1)))

make_entry(ID("f826a6"),
    Formula(Equal(GammaFunction(Div(1,2)), Sqrt(ConstPi))))

make_entry(ID("48ac55"),
    Formula(Equal(GammaFunction(Div(3,2)), Sqrt(ConstPi)/2)))

make_entry(ID("78f1f4"),
    Formula(Equal(GammaFunction(z+1), z * GammaFunction(z))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_domain)))

make_entry(ID("639d91"),
    Formula(Equal(GammaFunction(z), (z-1) * GammaFunction(z-1))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_sub1_domain)))

make_entry(ID("14af98"),
    Formula(Equal(GammaFunction(z-1), GammaFunction(z) / (z-1))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_sub1_domain)))

make_entry(ID("56d710"),
    Formula(Equal(GammaFunction(z+n), RisingFactorial(z, n) * GammaFunction(z))),
    Variables(z, n),
    Assumptions(And(Element(z, GammaFunction_domain), Element(n, ZZGreaterEqual(0)))))



make_entry(ID("b510b6"),
    Formula(Equal(GammaFunction(z), (ConstPi/Sin(ConstPi*z)) * (1/GammaFunction(1-z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZ))))

make_entry(ID("a787eb"),
    Formula(Equal(GammaFunction(z) * GammaFunction(z+Div(1,2)), 2**(1-2*z) * Sqrt(ConstPi) * GammaFunction(2*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(2*z, ZZLessEqual(0)))))

make_entry(ID("90a1e1"),
    Formula(Equal(Product(GammaFunction(z+Div(k,m)), Tuple(k, 0, m-1)), (2*pi)**((m-1)/2) * m**(Div(1,2)-m*z) * GammaFunction(m*z))),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(m, ZZGreaterEqual(1)), NotElement(m*z, ZZLessEqual(0)))))

make_entry(ID("4e4e0f"),
    Formula(Equal(GammaFunction(z), Integral(t**(z-1) * Exp(-t), Tuple(t, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))

make_entry(ID("798c5d"),
    Formula(Equal(HolomorphicDomain(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), GammaFunction_domain)))

make_entry(ID("2870f0"),
    Formula(Equal(Poles(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), ZZLessEqual(0))))

make_entry(ID("34d6ae"),
    Formula(Equal(EssentialSingularities(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("d086bd"),
    Formula(Equal(BranchPoints(GammaFunction(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("9a44c5"),
    Formula(Equal(BranchCuts(GammaFunction(z), z, CC), Set())))

make_entry(ID("a76328"),
    Formula(Equal(Zeros(GammaFunction(z), z, CC), Set())))

make_entry(ID("d7d2a0"),
    Formula(Equal(GammaFunction(Conjugate(z)), Conjugate(GammaFunction(z)))),
    Variables(z),
    Assumptions(Element(z, GammaFunction_domain)))

