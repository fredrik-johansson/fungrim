# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Powers"),
    Entries(
        "ef9f8a",
        "2090c3",
    ),
    Section("Integer exponents"),
    Entries(
        "d316bc",
        "310f36",
        "a249f6",
        "6c2b31",
        "c53d94",
    ),
    Section("Elementary functions"),
    Entries(
        "4d6416",
        "634687",
        "2e0d99",
    ),
    Section("Complex parts"),
    Entries(
        "0aac97",
        "bc4d0a",
        "caf8cf",
        "18873d",
    ),
)

make_entry(ID("ef9f8a"),
    SymbolDefinition(Pow, Pow(a,b), "Power"),
    Description(""),
    Description("The following table lists conditions such that", SourceForm(Pow(a, b)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(a, SetMinus(CC, 0)), Element(b, CC)), Element(Pow(a, b), CC)),
        Tuple(And(Element(a, CC), Element(b, Set(0))), Element(Pow(a, b), Set(1))),
        TableSection("Infinities"),
        Tuple(And(Element(a, Set(Infinity,-Infinity,UnsignedInfinity)), Element(b, ZZLessEqual(-1))), Element(Pow(a, b), Set(0))),
        TableSection("General domains"),
        Tuple(And(Element(a, R), Element(R, Rings), Element(b, ZZGreaterEqual(0))), Element(Pow(a, b), R)),
        Tuple(And(Element(a, SetMinus(K, Set(0))), Element(K, Fields), SubsetEqual(QQ, K), Element(b, ZZ)), Element(Pow(a, b), R)),
      )))

make_entry(ID("d316bc"),
    Formula(Equal(Pow(0, 0), 1)))

make_entry(ID("310f36"),
    Formula(Equal(Pow(z, 0), 1)),
    Variables(z),
    Assumptions(Element(z, CC)),
        And(Element(z, R), Element(R, Rings), SubsetEqual(ZZ, R)))

make_entry(ID("a249f6"),
    Formula(Equal(Pow(z, 1), z)),
    Variables(z),
    Assumptions(Element(z, CC)),
        And(Element(z, R), Element(R, Rings)))

make_entry(ID("6c2b31"),
    Formula(Equal(Pow(z, n + 1), Pow(z, n)) * z),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(0))),
        And(Element(z, R), Element(R, Rings), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("c53d94"),
    Formula(Equal(Pow(z, -1), 1/z)),
    Variables(z),
    Assumptions(Element(z, CC),
        And(Element(z, SetMinus(K, Set(0))), Element(K, Fields), SubsetEqual(QQ, K))))


make_entry(ID("4d6416"),
    Formula(Equal(Pow(a, b), Exp(b*Log(a)))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(CC, Set(0))), Element(b, CC))))

make_entry(ID("634687"),
    Formula(Equal(Pow(z, Div(1,2)), Sqrt(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("2e0d99"),
    Formula(Equal(Pow(z, -Div(1,2)), 1/Sqrt(z)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("0aac97"),
    Formula(Equal(Pow(a+b*ConstI, c+d*ConstI),
        Where(M**c * Exp(-(d*theta)) * (Cos(c*theta + d*Log(M)) + ConstI * Sin(c*theta + d*Log(M))), Equal(M, Abs(a+b*ConstI)), Equal(theta, Arg(a+b*ConstI))))),
    Variables(a, b, c, d),
    Assumptions(And(Element(a, RR), Element(b, RR), Element(c, RR), Element(d, RR), Unequal(a+b*ConstI, 0))))

make_entry(ID("bc4d0a"),
    Formula(Equal(Abs(Pow(a+b*ConstI, c+d*ConstI)),
        Where(M**c * Exp(-(d*theta)), Equal(M, Abs(a+b*ConstI)), Equal(theta, Arg(a+b*ConstI))))),
    Variables(a, b, c, d),
    Assumptions(And(Element(a, RR), Element(b, RR), Element(c, RR), Element(d, RR), Unequal(a+b*ConstI, 0))))

make_entry(ID("caf8cf"),
    Formula(Equal(Re(Pow(a+b*ConstI, c+d*ConstI)),
        Where(M**c * Exp(-(d*theta)) * Cos(c*theta + d*Log(M)), Equal(M, Abs(a+b*ConstI)), Equal(theta, Arg(a+b*ConstI))))),
    Variables(a, b, c, d),
    Assumptions(And(Element(a, RR), Element(b, RR), Element(c, RR), Element(d, RR), Unequal(a+b*ConstI, 0))))

make_entry(ID("18873d"),
    Formula(Equal(Im(Pow(a+b*ConstI, c+d*ConstI)),
        Where(M**c * Exp(-(d*theta)) * Sin(c*theta + d*Log(M)), Equal(M, Abs(a+b*ConstI)), Equal(theta, Arg(a+b*ConstI))))),
    Variables(a, b, c, d),
    Assumptions(And(Element(a, RR), Element(b, RR), Element(c, RR), Element(d, RR), Unequal(a+b*ConstI, 0))))


make_entry(ID("2090c3"),
    Formula(Equal(
        Pow(Mul(x, y), a),
        Mul(Mul(Pow(x, a), Pow(y, a)), Exp(2*ConstPi*ConstI*a \
            * Floor((ConstPi-Arg(x)-Arg(y))/(2*ConstPi))
        ))
    )),
    Variables(x, y, a),
    Assumptions(And(
        Element(x, CC),
        Element(y, CC),
        Element(a, SetMinus(CC, Set(0)))
    ))
)


"""







c8ea9b
13fb19
2f71c6
136b6d
491a81
f98618
ad3212
5577be
3946bb
5d2dad
f9b0ad
2c339c
949b2e
e8ca0d
6b88f2
d89e66
eeeb19
666b07
87c84a
361a2a
d8f3a2
b25c37
144775
38b8c7
d3630a
f1eab0
8ef4b8
9913cb
99e492
c9283f
"""
