# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Dedekind eta function"),
    Section("Definitions"),
    Entries(
        "a203bb",
        "82a63c",
    ),
    Section("Fourier series (q-series)"),
    Entries(
        "1dc520",
        "ff587a",
        "2e7fdb",
        "8f10b0",
    ),
    Section("Specific values"),
    Entries(
        "9b8c9f",
        "5706ab",
        "204acd",
        "6b9935",
        "d8025b",
    ),
    Section("Connection formulas"),
    Entries(
        "737805",
    ),
    Section("Modular transformations"),
    SeeTopics("Modular transformations"),
    Entries(
        "f4dc79",
        "1bae52",
        "acee1a",
        "3b806f",
        "29d9ab",
        "9f19c1",
        "f04e01",
        "921ef0",
    ),
    Section("Derivatives"),
    Entries(
        "1c25d3",
    ),
    Section("Analytic properties"),
    Entries(
        "e06d87",
        "04f4a0",
        "f2e2c2",
        "6d7668",
        "39fb36",
    ),
    Section("Dedekind sums"),
    Entries(
        "7af83f",
        "23961e",
    ),
    Section("Related topics"),
    SeeTopics("Partition function"),
)

# Definitions

make_entry(ID("a203bb"),
    SymbolDefinition(DedekindEta, DedekindEta(tau), "Dedekind eta function"),
    Description("The Dedekind eta function", DedekindEta(tau), "is a function of one variable", tau, "in the upper half-plane."))

make_entry(ID("82a63c"),
    SymbolDefinition(EulerQSeries, EulerQSeries(q), "Euler's q-series"),
    Description("Euler's q-series", EulerQSeries(q), "is a function of one variable", q, "in the unit disk."))

# Fourier series (q-series)

make_entry(ID("2e7fdb"),
    Formula(Equal(EulerQSeries(q), Product(Parentheses(1 - q**k), Tuple(k, 1, Infinity)))),
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
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * Product(Parentheses(1 - Exp(2*ConstPi*ConstI*k*tau)), Tuple(k, 1, Infinity)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Specific values

make_entry(ID("9b8c9f"),
    Formula(Equal(DedekindEta(ConstI), GammaFunction(Div(1,4)) / (2 * ConstPi ** Div(3,4)))))

make_entry(ID("5706ab"),
    Formula(Equal(Derivative(DedekindEta(tau), tau, ConstI),
         GammaFunction(Div(1,4)) / (8 * ConstPi**Div(3,4)) * ConstI)))

make_entry(ID("204acd"),
    Formula(Equal(DedekindEta(Exp(2*ConstPi*ConstI/3)), Exp(-(ConstPi*ConstI/24)) * (Pow(3,Div(1,8)) * Pow(GammaFunction(Div(1,3)), Div(3,2)) / (2 * ConstPi)))))

make_entry(ID("6b9935"),
    Formula(Equal(DedekindEta(ConstI*Infinity), 0)))

make_entry(ID("d8025b"),
    Formula(Equal(RightLimit(DedekindEta(ConstI*epsilon), epsilon, 0), 0)))

# Connection formulas

make_entry(ID("737805"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * JacobiTheta3((tau+1)/2, 3*tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Modular transformations

make_entry(ID("f4dc79"),
    SymbolDefinition(DedekindEtaEpsilon, DedekindEtaEpsilon(a,b,c,d), "Root of unity in the functional equation of the Dedekind eta function"))

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
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

make_entry(ID("9f19c1"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)), DedekindEtaEpsilon(a,b,c,d) * (c*tau+d)**Div(1,2) * DedekindEta(tau))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), PSL2Z))))

make_entry(ID("f04e01"),
    Formula(Equal(DedekindEtaEpsilon(1,b,0,1), Exp((ConstPi*ConstI*b)/12))),
    Variables(b),
    Element(b, ZZ))

make_entry(ID("921ef0"),
    Formula(Equal(DedekindEtaEpsilon(a,b,c,d), Exp((ConstPi*ConstI*((a+d)/(12*c) - DedekindSum(d,c) - Div(1,4)))))),
    Variables(a,b,c,d),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1), Greater(c, 0))))

# Derivatives

make_entry(ID("1c25d3"),
    Formula(Equal(Derivative(DedekindEta(tau), tau, tau),
        (ConstI / (2 * ConstPi)) * DedekindEta(tau) * WeierstrassZeta(Div(1,2), tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# todo: using eisenstein series

# Analytic properties

make_entry(ID("e06d87"),
    Formula(Equal(HolomorphicDomain(DedekindEta(tau), tau, HH), HH)))

make_entry(ID("04f4a0"),
    Formula(Equal(Poles(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("f2e2c2"),
    Formula(Equal(BranchPoints(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("6d7668"),
    Formula(Equal(BranchCuts(DedekindEta(tau), tau, HH), Set())))

make_entry(ID("39fb36"),
    Formula(Equal(Zeros(DedekindEta(tau), tau, Element(tau, HH)), Set())))

# Dedekind sums

make_entry(ID("7af83f"),
    SymbolDefinition(DedekindSum, DedekindSum(n,k), "Dedekind sum"))

make_entry(ID("23961e"),
    Formula(Equal(DedekindSum(n,k), Sum((r/k) * ((n*r/k) - Floor(n*r/k) - Div(1,2)), Tuple(r, 1, k-1)))),
    Variables(n,k),
    Assumptions(And(Element(n, ZZ), Element(k, ZZ), Greater(k, 0), Equal(GCD(n, k), 1))))


