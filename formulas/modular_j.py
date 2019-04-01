# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Modular j-invariant"),
    Section("Modular transformations"),
    Entries(
        "a997f2",
        "42a909",
        "d5f569",
    ),
    Section("Special values"),
    Entries(
        "9aa62c",
        "ad228f",
        "229c97",
        "1356e4",
        "8be46c",
        "3189b9",
        "29c095",
        "a498dd",
        "3ee358",
        "5b108e",
        "951017",
        "1cb24e",
    ),
    Section("Connection formulas"),
    Entries(
        "cedcfc",
        "664b4c",
    ),
    Section("Analytic properties"),
    Entries(
        "27f9d2",
        "ea3e3c",
        "1b2d8a",
        "dcc8b1",
        "441301",
    )
)

make_entry(ID("a997f2"),
    Formula(Equal(ModularJ(tau+1), ModularJ(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("42a909"),
    Formula(Equal(ModularJ(-(1/tau)), ModularJ(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("d5f569"),
    Formula(Equal(ModularJ((a*tau+b)/(c*tau+d)), ModularJ(tau))),
    Variables(a, b, c, d, tau),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

make_entry(ID("9aa62c"),
    Formula(Equal(ModularJ(Exp(ConstPi*ConstI/3)), 0)))

make_entry(ID("ad228f"),
    Formula(Equal(ModularJ(ConstI), 1728)))

make_entry(ID("229c97"),
    Formula(Equal(ModularJ(2*ConstI), Pow(66, 3), 287496)))

make_entry(ID("1356e4"),
    Formula(Equal(ModularJ(Sqrt(2)*ConstI), Pow(20, 3), 8000)))

make_entry(ID("8be46c"),
    Formula(Equal(ModularJ(3*ConstI), 64 * (2+Sqrt(3))**2 * (21 + 20*Sqrt(3))**3)))

make_entry(ID("3189b9"),
    Formula(Equal(ModularJ(4*ConstI), 27 * (724 + 513*Sqrt(2))**3)))


# redundant?
# make_entry(ID(""),
#     Formula(Equal(ModularJ(Div(1,2)*(1+Sqrt(3)*ConstI)), 0)))

make_entry(ID("29c095"),
    Formula(Equal(ModularJ(Div(1,2)*(1+Sqrt(7)*ConstI)), -Pow(15,3))))

make_entry(ID("a498dd"),
    Formula(Equal(ModularJ(Div(1,2)*(1+Sqrt(11)*ConstI)), -Pow(32,3))))

make_entry(ID("3ee358"),
    Formula(Equal(ModularJ(Div(1,2)*(1+Sqrt(19)*ConstI)), -Pow(96,3))))

make_entry(ID("5b108e"),
    Formula(Equal(ModularJ(Div(1,2)*(1+Sqrt(43)*ConstI)), -Pow(960,3))))

make_entry(ID("951017"),
    Formula(Equal(ModularJ(Div(1,2)*(1+Sqrt(67)*ConstI)), -Pow(5280,3))))

make_entry(ID("1cb24e"),
    Formula(Equal(ModularJ(Div(1,2)*(1+Sqrt(163)*ConstI)), -Pow(640320,3))))


make_entry(ID("cedcfc"),
    Formula(Equal(ModularJ(tau), 32 * (JacobiTheta2(0,tau)**8 + JacobiTheta3(0,tau)**8 + JacobiTheta4(0,tau)**8)**3 /
        (JacobiTheta2(0,tau) * JacobiTheta3(0,tau) * JacobiTheta4(0,tau))**8)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("664b4c"),
    Formula(Equal(ModularJ(tau), ((DedekindEta(tau)/DedekindEta(2*tau))**8 + Pow(2,8) * (DedekindEta(2*tau)/DedekindEta(tau))**16)**3)),
    Variables(tau),
    Assumptions(Element(tau, HH)))




make_entry(ID("27f9d2"),
    Formula(Equal(HolomorphicDomain(ModularJ(tau), tau, HH), HH)))

make_entry(ID("ea3e3c"),
    Formula(Equal(Zeros(ModularJ(tau), tau, ModularGroupFundamentalDomain), Set(Exp(ConstPi*ConstI/3)))))

make_entry(ID("1b2d8a"),
    Formula(Equal(Zeros(ModularJ(tau), tau, HH), SetBuilder(ModularGroupAction(gamma, Exp(ConstPi*ConstI/3)), Element(gamma, PSL2Z)))))

make_entry(ID("dcc8b1"),
    Formula(Equal(SetBuilder(ModularJ(tau), Element(tau, ModularGroupFundamentalDomain)), CC)))

make_entry(ID("441301"),
    Formula(Equal(Cardinality(Zeros(ModularJ(tau) - z, tau, ModularGroupFundamentalDomain)), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

