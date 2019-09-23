# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Catalan's constant"),
    Entries(
        "f7b6aa",
    ),
    Section("Numerical value"),
    Entries(
        "6a83ad",
    ),
    Section("Special function representations"),
    Entries(
        "2744d4",
        "e85723",
        "1d65c2",
        "9e9922",
        "4c166d",
        "a766f2",
    ),
    Section("Series representations"),
    Entries(
        "33aa62",
        "d43f30",
        "0bd544",
        "37fb5f",
        "a8657e",
    ),
    Section("Integral representations"),
    Subsection("Involving elementary functions"),
    Entries(
        "ba58e0",
        "d864b2",
        "49df16",
        "997777",
        "d6703a",
        "fd82ab",
        "38c2d5",
        "c54c85",
        "ec1435",
        "79f20e",
    ),
    Subsection("Involving compositions of elementary functions"),
    Entries(
        "fc5ea9",
        "08cda4",
        "270e67",
        "4dec89",
        "d6415e",
        "e09b77",
        "6d3591",
    ),
    Subsection("Involving special functions"),
    Entries(
        "1f1fb4",
        "d3cfc2",
        "937fa9",
    ),
    Subsection("Double integrals"),
    Entries(
        "5b31ee",
        "ed4cca",
    ),
)

make_entry(ID("f7b6aa"),
    SymbolDefinition(ConstCatalan, ConstCatalan, "Catalan's constant"),
    References(
        "David M. Bradley, Representations of Catalan's constant, https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.26.1879",
        "https://en.wikipedia.org/wiki/Catalan's_constant",
        "http://mathworld.wolfram.com/CatalansConstant.html",
        "https://doi.org/10.1017/mag.2017.4"))

# Numerical value

make_entry(ID("6a83ad"),
    Formula(Element(ConstCatalan,
        RealBall(Decimal("0.91596559417721901505460351493238411077414937428167"), Decimal("2.14e-51")))))

# Special function representations

make_entry(ID("2744d4"),
    Formula(Equal(ConstCatalan, Div(1,8)*(PolyGamma(1, Div(1,4)) - ConstPi**2))))

make_entry(ID("e85723"),
    Formula(Equal(ConstCatalan, Div(1,16)*(HurwitzZeta(2,Div(1,4))-HurwitzZeta(2,Div(3,4))))))

make_entry(ID("1d65c2"),
    Formula(Equal(ConstCatalan, Im(PolyLog(2,ConstI)))))

make_entry(ID("9e9922"),
    Formula(Equal(ConstCatalan, DirichletL(2, DirichletCharacter(4, 3)))))

make_entry(ID("4c166d"),
    Formula(Equal(ConstCatalan, Div(1,4) * LerchPhi(-1,2,Div(1,2)))))

make_entry(ID("a766f2"),
    Formula(Equal(ConstCatalan, Hypergeometric3F2(Div(1,2), Div(1,2), 1, Div(3,2), Div(3,2), -1))))

# Series representations

make_entry(ID("33aa62"),
    Formula(Equal(ConstCatalan, Sum((-1)**n/(2*n+1)**2, For(n, 0, Infinity)))))

make_entry(ID("d43f30"),
    Formula(Equal(ConstCatalan, Div(1,2) * Sum(4**n / ((2*n+1)**2 * Binomial(2*n,n)), For(n, 0, Infinity)))))

make_entry(ID("0bd544"),
    Formula(Equal(ConstCatalan, (ConstPi/8) * Log(2 + Sqrt(3)) + Div(3,8) * Sum(1/((2*n+1)**2*Binomial(2*n,n)), For(n, 0, Infinity)))))

make_entry(ID("37fb5f"),
    Formula(Equal(ConstCatalan, Div(1,64) * Sum((256**n * (580*n**2-184*n+15))/(n**3*(2*n-1)*Binomial(6*n,3*n)*Binomial(6*n,4*n)*Binomial(4*n,2*n)), For(n, 1, Infinity)))),
    References("https://hal.inria.fr/hal-00990465/"))

make_entry(ID("a8657e"),
    Formula(Equal(ConstCatalan, 1-Sum((n * RiemannZeta(2*n+1)) / 16**n, For(n, 1, Infinity)))))

# Integral representations

## Involving elementary functions

make_entry(ID("ba58e0"),
    Formula(Equal(ConstCatalan, Integral(Atan(x)/x, For(x, 0, 1)))))

make_entry(ID("d864b2"),
    Formula(Equal(ConstCatalan, -Integral(Log(x)/(x**2+1), For(x, 0, 1)))))

make_entry(ID("49df16"),
    Formula(Equal(ConstCatalan, Integral(Log(x)/(x**2+1), For(x, 1, Infinity)))))

make_entry(ID("997777"),
    Formula(Equal(ConstCatalan,  ConstPi**2/16 + ConstPi*Log(2)/4 - Integral(Atan(x)**2, For(x, 0, 1)))))

make_entry(ID("d6703a"),
    Formula(Equal(ConstCatalan,  7*RiemannZeta(3)/(4*ConstPi) + (2/ConstPi) * Integral(Atan(x)**2/x, For(x, 0, 1)))))

make_entry(ID("fd82ab"),
    Formula(Equal(ConstCatalan, Integral(Acos(x)/Sqrt(x**2+1), For(x, 0, 1)))))

make_entry(ID("38c2d5"),
    Formula(Equal(ConstCatalan, Integral(Asinh(x)/Sqrt(1-x**2), For(x, 0, 1)))))

make_entry(ID("c54c85"),
    Formula(Equal(ConstCatalan, Div(1,2) * Integral(x/Cosh(x), For(x, 0, Infinity)))))

make_entry(ID("ec1435"),
    Formula(Equal(ConstCatalan, Div(1,4) * Integral(x/Sin(x), For(x, -(ConstPi/2), ConstPi/2)))))

make_entry(ID("79f20e"),
    Formula(Equal(ConstCatalan, Integral(x/(Sin(x)*Cos(x)), For(x, 0, ConstPi/4)))))

## Involving compositions of elementary functions

make_entry(ID("fc5ea9"),
    Formula(Equal(ConstCatalan, Integral(Atan(Exp(-x)), For(x, 0, Infinity)))))

make_entry(ID("08cda4"),
    Formula(Equal(ConstCatalan, -Integral(Log(Tan(x)), For(x, 0, ConstPi/4)))))

make_entry(ID("270e67"),
    Formula(Equal(ConstCatalan, Integral(Log(Cot(x)), For(x, 0, ConstPi/4)))))

make_entry(ID("4dec89"),
    Formula(Equal(ConstCatalan, Integral(Asinh(Sin(x)), For(x, 0, ConstPi/2)))))

make_entry(ID("d6415e"),
    Formula(Equal(ConstCatalan, Integral(Asinh(Cos(x)), For(x, 0, ConstPi/2)))))

make_entry(ID("e09b77"),
    Formula(Equal(ConstCatalan, -(2*Integral(Log(2*Sin(x)), For(x, 0, ConstPi/4))))))

make_entry(ID("6d3591"),
    Formula(Equal(ConstCatalan, 2*Integral(Log(2*Cos(x)), For(x, 0, ConstPi/4)))))

## Involving special functions

make_entry(ID("1f1fb4"),
    Formula(Equal(ConstCatalan, Div(1,2) * Integral(EllipticK(m**2), For(m, 0, 1)))))

make_entry(ID("d3cfc2"),
    Formula(Equal(ConstCatalan, Integral(EllipticE(m**2), For(m, 0, 1)) - Div(1,2))))

make_entry(ID("937fa9"),
    Formula(Equal(ConstCatalan, (ConstPi/2) * Integral(GammaFunction(1+x)*GammaFunction(1-x), For(x, 0, Div(1,2))))))

## Double integrals

make_entry(ID("5b31ee"),
    Formula(Equal(ConstCatalan, Integral(Integral(1/(1+x**2*y**2), For(x, 0, 1)), For(y, 0, 1)))))

make_entry(ID("ed4cca"),
    Formula(Equal(ConstCatalan, Div(1,4) * Integral(Integral(1/(((x+y)*Sqrt(1-x)*Sqrt(1-y))), For(x, 0, 1)), For(y, 0, 1)))))


