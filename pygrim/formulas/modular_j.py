# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Modular j-invariant"),
    Section("Definitions"),
    Entries(
        "70eb98",
    ),
    Section("Illustrations"),
    Entries(
        "8c2862",
    ),
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
        "dc8251",
    ),
    Section("Derivatives"),
    Entries(
        "f0f53b",
        "348b26",
    ),
    Section("Analytic properties"),
    Entries(
        "27f9d2",
        "ea3e3c",
        "1b2d8a",
        "dcc8b1",
        "441301",
    ),
    Section("Hilbert class polynomials"),
    Entries(
        "36eb82",
        "0b4d4b",
        "fd72e0",
        "dd5681",
        "20b6d2",
    ),
)

make_entry(ID("70eb98"),
    SymbolDefinition(ModularJ, ModularJ(tau), "Modular j-invariant"),
    Description("The modular j-invariant", ModularJ(tau), "is a function of one variable", tau, "in the upper half-plane."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(tau, HH), Element(ModularJ(tau), CC)),
      )))

make_entry(ID("8c2862"),
    Image(Description("X-ray of", ModularJ(tau), "on", Element(tau, ClosedInterval(-1,1) + ClosedInterval(0,2)*ConstI), "with", ModularGroupFundamentalDomain, "highlighted"),
        ImageSource("xray_modular_j")),
    description_xray,
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
    Formula(Equal(ModularJ(tau), 32 * (JacobiTheta(2,0,tau)**8 + JacobiTheta(3,0,tau)**8 + JacobiTheta(4,0,tau)**8)**3 /
        (JacobiTheta(2,0,tau) * JacobiTheta(3,0,tau) * JacobiTheta(4,0,tau))**8)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("664b4c"),
    Formula(Equal(ModularJ(tau), ((DedekindEta(tau)/DedekindEta(2*tau))**8 + Pow(2,8) * (DedekindEta(2*tau)/DedekindEta(tau))**16)**3)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("dc8251"),
    Formula(Equal(ModularJ(tau), EisensteinE(4,tau)**3 / DedekindEta(tau)**24)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("f0f53b"),
    Formula(Equal(ComplexDerivative(ModularJ(tau), For(tau, tau)), -(2*ConstPi*ConstI) * (EisensteinE(14,tau) / DedekindEta(tau)**24))),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))

make_entry(ID("348b26"),
    Formula(Equal(ComplexDerivative(ModularJ(tau), For(tau, tau)), -(2*ConstPi*ConstI) * (EisensteinE(6,tau) / EisensteinE(4,tau)) * ModularJ(tau))),
    Variables(tau),
    Assumptions(And(Element(tau, HH), Unequal(EisensteinE(4,tau), 0))))



make_entry(ID("27f9d2"),
    Formula(IsHolomorphic(ModularJ(tau), ForElement(tau, HH))))

make_entry(ID("ea3e3c"),
    Formula(Equal(Zeros(ModularJ(tau), ForElement(tau, ModularGroupFundamentalDomain)), Set(Exp(2*ConstPi*ConstI/3)))))

make_entry(ID("1b2d8a"),
    Formula(Equal(Zeros(ModularJ(tau), ForElement(tau, HH)), Set(ModularGroupAction(gamma, Exp(2*ConstPi*ConstI/3)), ForElement(gamma, PSL2Z)))))

make_entry(ID("dcc8b1"),
    Formula(Equal(Set(ModularJ(tau), ForElement(tau, ModularGroupFundamentalDomain)), CC)))

make_entry(ID("441301"),
    Formula(Equal(Cardinality(Solutions(Brackets(Equal(ModularJ(tau), z)), ForElement(tau, ModularGroupFundamentalDomain))), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

# Hilbert class polynomials

make_entry(ID("36eb82"),
    SymbolDefinition(PrimitiveReducedPositiveIntegralBinaryQuadraticForms,
        PrimitiveReducedPositiveIntegralBinaryQuadraticForms(D), "Primitive reduced positive integral binary quadratic forms"))

make_entry(ID("0b4d4b"),
    Formula(Equal(PrimitiveReducedPositiveIntegralBinaryQuadraticForms(D),
        Set(Tuple(a,b,c), For(Tuple(a,b,c)), And(Element(a, ZZGreaterEqual(1)), Element(b, ZZ), Element(c, ZZ),
            Equal(b**2 - 4*a*c, D),
            LessEqual(Abs(b), a, c), Parentheses(Implies(Or(Equal(Abs(b), a), Equal(a, c)), GreaterEqual(b, 0))),
            Equal(GCD(a,b,c), 1))))),
    Variables(D),
    Assumptions(And(Element(D, ZZLessEqual(-3)), Element(Mod(-D, 4), Set(0,3)))),
    References("H. Cohen, A Course in Computational Algebraic Number Theory, Springer, 1993, Definition 5.3.2"))

make_entry(ID("fd72e0"),
    SymbolDefinition(HilbertClassPolynomial,
        HilbertClassPolynomial(D, x), "Hilbert class polynomial"))

make_entry(ID("dd5681"),
    Formula(Equal(HilbertClassPolynomial(D, x),
        Product(Parentheses(x - ModularJ((-b+Sqrt(D))/(2*a))), ForElement(Tuple(a,b,c),
            PrimitiveReducedPositiveIntegralBinaryQuadraticForms(D))))),
    Variables(D, x),
    Assumptions(And(Element(D, ZZLessEqual(-3)), Element(Mod(-D, 4), Set(0,3)), Element(x, CC))))

make_entry(ID("20b6d2"),
    Description("Table of", HilbertClassPolynomial(D,x), "for", LessEqual(-D, 68)),
    Table(TableRelation(Tuple(D, p), Equal(HilbertClassPolynomial(D,x), p)),
      TableHeadings(D, HilbertClassPolynomial(D,x)), TableSplit(1),
      List(
    Tuple(-3, x),
    Tuple(-4, x - 1728),
    Tuple(-7, x + 3375),
    Tuple(-8, x - 8000),
    Tuple(-11, x + 32768),
    Tuple(-12, x - 54000),
    Tuple(-15, x**2 + 191025*x - 121287375),
    Tuple(-16, x - 287496),
    Tuple(-19, x + 884736),
    Tuple(-20, x**2 - 1264000*x - 681472000),
    Tuple(-23, x**3 + 3491750*x**2 - 5151296875*x + 12771880859375),
    Tuple(-24, x**2 - 4834944*x + 14670139392),
    Tuple(-27, x + 12288000),
    Tuple(-28, x - 16581375),
    Tuple(-31, x**3 + 39491307*x**2 - 58682638134*x + 1566028350940383),
    Tuple(-32, x**2 - 52250000*x + 12167000000),
    Tuple(-35, x**2 + 117964800*x - 134217728000),
    Tuple(-36, x**2 - 153542016*x - 1790957481984),
    Tuple(-39, x**4 + 331531596*x**3 - 429878960946*x**2 + 109873509788637459*x + 20919104368024767633),
    Tuple(-40, x**2 - 425692800*x + 9103145472000),
    Tuple(-43, x + 884736000),
    Tuple(-44, x**3 - 1122662608*x**2 + 270413882112*x - 653249011576832),
    Tuple(-47, x**5 + 2257834125*x**4 - 9987963828125*x**3 + 5115161850595703125*x**2 - 14982472850828613281250*x + 16042929600623870849609375),
    Tuple(-48, x**2 - 2835810000*x + 6549518250000),
    Tuple(-51, x**2 + 5541101568*x + 6262062317568),
    Tuple(-52, x**2 - 6896880000*x - 567663552000000),
    Tuple(-55, x**4 + 13136684625*x**3 - 20948398473375*x**2 + 172576736359017890625*x - 18577989025032784359375),
    Tuple(-56, x**4 - 16220384512*x**3 + 2059647197077504*x**2 + 2257767342088912896*x + 10064086044321563803648),
    Tuple(-59, x**3 + 30197678080*x**2 - 140811576541184*x + 374643194001883136),
    Tuple(-60, x**2 - 37018076625*x + 153173312762625),
    Tuple(-63, x**4 + 67515199875*x**3 - 193068841781250*x**2 + 4558451243295023437500*x - 6256903954262253662109375),
    Tuple(-64, x**2 - 82226316240*x - 7367066619912),
    Tuple(-67, x + 147197952000),
    Tuple(-68, x**4 - 178211040000*x**3 - 75843692160000000*x**2 - 318507038720000000000*x - 2089297506304000000000000))),
    Variables(x),
    Assumptions(Element(x, CC)))

