# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Complex parts"),
    Entries(
        "5e639e",
        "920cc8",
        "b7d740",
        "f5e62c",
        "9086c6",
        "da5d5e",
        "ce8ee4",
    ),
    Section("Basic formulas"),
    Entries(
        "26565c",
        "4f0049",
        "b2a880",
        "8e6867",
        "ba6d81",
        "acda23",
        "18d335",
        "59a5d6",
        "e9465d",
    ),
    Section("Specific values"),
    Entries(
        "c423d2",
        "735409",
        "089f85",
        "a8b41c",
    ),
    Section("Connection formulas"),
    Entries(
        "3866dc",
        "f1a29b",
        "54340e",
        "60772e",
    ),
    Section("Functional equations"),
    Entries(
        "bcd22f",
        "8cac46",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "98efc1",
        "a6e081",
        "48fe10",
        "6a894d",
        "ebf8cc",
        "fc427b",
        "12664e",
        "432926",
        "08268d",
    ),
)

make_entry(ID("5e639e"),
    SymbolDefinition(Sign, Sign(z), "Sign function"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(z, RR), Element(Sign(z), Set(-1, 0, 1))),
        Tuple(Element(z, SetMinus(CC, Set(0))), Element(Sign(z), UnitCircle)),
        Tuple(Element(z, Set(Infinity)), Element(Sign(z), Set(1))),
        Tuple(Element(z, Set(-Infinity)), Element(Sign(z), Set(-1))),
      )))

make_entry(ID("920cc8"),
    SymbolDefinition(Abs, Abs(z), "Absolute value"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(z, RR), Element(Abs(z), ClosedOpenInterval(0, Infinity))),
        Tuple(Element(z, CC), Element(Abs(z), ClosedOpenInterval(0, Infinity))),
        Tuple(Element(z, Set(Infinity,-Infinity,UnsignedInfinity)), Element(Abs(z), Set(Infinity))),
      )))

make_entry(ID("b7d740"),
    SymbolDefinition(Arg, Arg(z), "Complex argument"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(z, RR), Element(Arg(z), Set(0, ConstPi))),
        Tuple(Element(z, CC), Element(Arg(z), OpenClosedInterval(-ConstPi, ConstPi))),
        Tuple(Element(z, Set(Infinity)), Element(Arg(z), Set(0))),
        Tuple(Element(z, Set(-Infinity)), Element(Arg(z), Set(ConstPi))),
      )))

make_entry(ID("f5e62c"),
    SymbolDefinition(Re, Re(z), "Real part"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(z, RR), Element(Re(z), RR)),
        Tuple(Element(z, CC), Element(Re(z), RR)),
      )))

make_entry(ID("9086c6"),
    SymbolDefinition(Im, Im(z), "Imaginary part"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(z, RR), Element(Im(z), Set(0))),
        Tuple(Element(z, CC), Element(Im(z), RR)),
      )))


make_entry(ID("da5d5e"),
    SymbolDefinition(Conjugate, Conjugate(z), "Complex conjugate"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(z, RR), Element(Conjugate(z), RR)),
        Tuple(Element(z, CC), Element(Conjugate(z), CC)),
      )))

make_entry(ID("ce8ee4"),
    SymbolDefinition(Csgn, Csgn(z), "Real-valued sign function for complex numbers"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(z, CC), Element(Csgn(z), Set(-1, 0, 1))),
      )),
    References("https://www.maplesoft.com/support/help/maple/view.aspx?path=csgn"))


make_entry(ID("26565c"),
    Formula(Equal(Sign(z), z / Abs(z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0))))),

make_entry(ID("4f0049"),
    Formula(Equal(Abs(x+y*ConstI), Sqrt(x**2 + y**2))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("b2a880"),
    Formula(Equal(Arg(x+y*ConstI), Atan2(y, x))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("8e6867"),
    Formula(Equal(Re(x+y*ConstI), x)),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("ba6d81"),
    Formula(Equal(Im(x+y*ConstI), y)),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("acda23"),
    Formula(Equal(Conjugate(x+y*ConstI), x-y*ConstI)),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("18d335"),
    Formula(Equal(Sign(x), Cases(Tuple(1, Greater(x, 0)), Tuple(-1, Less(x, 0)), Tuple(0, Equal(x, 0))))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("59a5d6"),
    Formula(Equal(Csgn(z), Cases(Tuple(Sign(Im(z)), Equal(Re(z), 0)), Tuple(Sign(Re(z)), Otherwise)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e9465d"),
    Formula(Equal(Csgn(z), Sqrt(z**2) / z)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))


make_entry(ID("c423d2"),
    Formula(Equal(Arg(1), 0)))

make_entry(ID("735409"),
    Formula(Equal(Arg(ConstI), ConstPi/2)))

make_entry(ID("089f85"),
    Formula(Equal(Arg(-ConstI), -(ConstPi/2))))

make_entry(ID("a8b41c"),
    Formula(Equal(Arg(-1), ConstPi)))



make_entry(ID("3866dc"),
    Formula(Equal(Re(z), (z + Conjugate(z))/2)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("f1a29b"),
    Formula(Equal(Im(z), (z - Conjugate(z))/(2*ConstI))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("bcd22f"),
    Formula(Equal(z*Conjugate(z), Abs(z)**2)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("8cac46"),
    Formula(Equal(Arg(c * z), Arg(z))),
    Variables(z, c),
    Assumptions(And(Element(z, SetMinus(CC, Set(0))), Element(c, OpenInterval(0, Infinity)))))


make_entry(ID("98efc1"),
    Formula(Equal(Abs(a*b), Abs(a)*Abs(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("a6e081"),
    Formula(LessEqual(Abs(a+b), Abs(a)+Abs(b))),
    Description("This relation is known as the triangle inequality."),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("48fe10"),
    Formula(LessEqual(Abs(Abs(a)-Abs(b)), Abs(a-b))),
    Description("This relation is known as the reverse triangle inequality."),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("6a894d"),
    Formula(Equal(Abs(Conjugate(z)), Abs(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("ebf8cc"),
    Formula(LessEqual(Abs(Re(z)), Abs(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("fc427b"),
    Formula(LessEqual(Abs(Im(z)), Abs(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("12664e"),
    Formula(LessEqual(Abs(z), Abs(Re(z)) + Abs(Im(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("432926"),
    Formula(LessEqual(Abs(Sign(z)), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("08268d"),
    Formula(LessEqual(Abs(Arg(z)), ConstPi)),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("54340e"),
    Formula(Equal(Sign(z), Exp(ConstI*Arg(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("60772e"),
    Formula(Equal(Arg(z), -(ConstI*Log(Sign(z))))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))


