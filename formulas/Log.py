# -*- coding: utf-8 -*-

from .expr import *

index_Log = ("Log", "Natural logarithm",
    [
        ("Particular values", ["07731b","699c83","c331da","2f1f7b"]),
        ("Functional equations and connection formulas", ["d87f6e","4c1e1e","c43533","f67fa2"]),
        ("Analytic properties", ["4538ba","c464e3","ddc8a1","940c48","b5ded1","1d447b"]),
        ("Complex parts", ["13895b","099b19","fbfb81","dcc1e5"]),
        ("Bounds and inequalities", ["4986ed","792c76"]),
        ("Integral representations", ["0ba9b2"]),
    ])

Log_branch_cut = OpenClosedInterval(-Infinity, 0)
Log_holomorphic_domain = SetMinus(CC, Log_branch_cut)

make_entry(ID("07731b"),
    Formula(Equal(Log(1), 0)))

make_entry(ID("699c83"),
    Formula(Equal(Log(ConstE), 1)))

make_entry(ID("c331da"),
    Formula(Equal(Log(ConstI), ConstPi*ConstI/2)))

make_entry(ID("2f1f7b"),
    Formula(Equal(Log(-1), ConstPi*ConstI)))

make_entry(ID("4538ba"),
    Formula(Equal(HolomorphicDomain(Log(z), z, Union(CC, Set(UnsignedInfinity))), Log_holomorphic_domain)))

make_entry(ID("c464e3"),
    Formula(Equal(Poles(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("ddc8a1"),
    Formula(Equal(EssentialSingularities(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("940c48"),
    Formula(Equal(BranchPoints(Log(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity, 0))))

make_entry(ID("b5ded1"),
    Formula(Equal(BranchCuts(Log(z), z, CC), Set(Log_branch_cut))))

make_entry(ID("1d447b"),
    Formula(Equal(Zeros(Log(z), z, CC), Set(1))))

make_entry(ID("13895b"),
    Formula(Equal(Log(Conjugate(z)), Conjugate(Log(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Log_branch_cut))))

make_entry(ID("099b19"),
    Formula(Equal(Re(Log(z)), Log(Abs(z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("fbfb81"),
    Formula(Equal(Im(Log(z)), Arg(z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("dcc1e5"),
    Formula(Equal(Abs(Log(z)), Sqrt(Log(Abs(z))**2 + Arg(z)**2))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("4986ed"),
    Formula(LessEqual(Log(x), x-1)),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0,Infinity))))

make_entry(ID("792c76"),
    Formula(LessEqual(Abs(Log(z)), Abs(Log(Abs(z))) + ConstPi)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("d87f6e"),
    Formula(Equal(Exp(Log(z)), z)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("4c1e1e"),
    Formula(Equal(Log(Exp(z)), z)),
    Variables(z),
    Assumptions(And(Element(z, CC), Element(Im(z), OpenClosedInterval(-ConstPi, ConstPi)))))

make_entry(ID("c43533"),
    Formula(Equal(Log(z), Log(Abs(z)) + Arg(z)*ConstI)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("f67fa2"),
    Formula(Equal(Log(c*z), Log(c) + Log(z))),
    Variables(c, z),
    Assumptions(And(Element(c, OpenInterval(0, Infinity)), Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("0ba9b2"),
    Formula(Equal(Log(z), Integral(1/t, Tuple(t, 1, z)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Log_branch_cut))))

