# -*- coding: utf-8 -*-

from .expr import *

index_DedekindEta = ("DedekindEta", "Dedekind eta function",
    [("Fourier series (q-series)", ["1dc520","ff587a","2e7fdb","8f10b0"]),
     ("Special values", ["9b8c9f", "204acd"]),
     ("Modular transformations", ["1bae52","acee1a","3b806f","29d9ab","9f19c1","f04e01","921ef0"]),
     ("Analytic properties", ["e06d87","04f4a0","f2e2c2","6d7668","39fb36"]),
     ("Dedekind sums", ["23961e"])])

make_entry(ID("2e7fdb"),
    Formula(Equal(EulerQSeries(q), Product((1 - q**k), Tuple(k, 1, Infinity)))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("8f10b0"),
    Formula(Equal(EulerQSeries(q), Sum((-1)**k * q**(k*(3*k-1)/2), Tuple(k, -Infinity, Infinity)))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("ff587a"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * EulerQSeries(Exp(2*ConstPi*ConstI*tau)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("1dc520"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * Product((1 - Exp(2*ConstPi*ConstI*k*tau)), Tuple(k, 1, Infinity)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("9b8c9f"),
    Formula(Equal(DedekindEta(ConstI), GammaFunction(Div(1,4)) / (2 * ConstPi ** Div(3,4)))))

make_entry(ID("204acd"),
    Formula(Equal(DedekindEta(Exp(2*ConstPi*ConstI/3)), Exp(-(ConstPi*ConstI/24)) * (Pow(3,Div(1,8)) * Pow(GammaFunction(Div(1,3)), Div(3,2)) / (2 * ConstPi)))))

make_entry(ID("1bae52"),
    Formula(Equal(DedekindEta(tau+1), Exp(ConstPi*ConstI/12) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("acee1a"),
    Formula(Equal(DedekindEta(tau+24), DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("3b806f"),
    Formula(Equal(DedekindEta(-(1/tau)), (-(ConstI*tau))**Div(1,2) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("29d9ab"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)) ** 24, (c*tau+d)**12 * DedekindEta(tau)**24)),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH),
        Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1))))

make_entry(ID("9f19c1"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)), DedekindEtaEpsilon(a,b,c,d) * (c*tau+d)**Div(1,2) * DedekindEta(tau))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH),
        Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1), Or(Greater(c, 0), And(Equal(c, 0), Equal(d, 1))))))

make_entry(ID("f04e01"),
    Formula(Equal(DedekindEtaEpsilon(1,b,0,1), Exp((ConstPi*ConstI*b)/12))),
    Variables(b),
    Element(b, ZZ))

make_entry(ID("921ef0"),
    Formula(Equal(DedekindEtaEpsilon(a,b,c,d), Exp((ConstPi*ConstI*((a+d)/(12*c) - DedekindSum(d,c) - Div(1,4)))))),
    Variables(a,b,c,d),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1), Greater(c, 0))))

make_entry(ID("23961e"),
    Formula(Equal(DedekindSum(n,k), Sum((r/k) * ((n*r/k) - Floor(n*r/k) - Div(1,2)), Tuple(r, 1, k-1)))),
    Variables(n,k),
    Assumptions(And(Element(n, ZZ), Element(k, ZZ), Greater(k, 0), Equal(GCD(n, k), 1))))

make_entry(ID("e06d87"),
    Formula(Equal(HolomorphicDomain(DedekindEta(tau), tau, HH), HH)))

make_entry(ID("04f4a0"),
    Formula(Equal(Poles(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("f2e2c2"),
    Formula(Equal(BranchPoints(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("6d7668"),
    Formula(Equal(BranchCuts(DedekindEta(tau), tau, HH), Set())))

make_entry(ID("39fb36"),
    Formula(Equal(Zeros(DedekindEta(tau), tau, HH), Set())))

