# -*- coding: utf-8 -*-

from ..expr import *

# todo: fix setbuilder variable

def_Topic(
    Title("Complex plane"),
    Section("Main regions"),
    Entries(
        "77ef0c",
        "a65a14",   # HH symbol
        "d7962e",   # HH
        "fc0d55",
        "912ff9",
    ),
    Section("Disks"),
    Entries(
        "c98bad",
        "d1cf0c",
    ),
    Section("Bernstein ellipses"),
    Entries(
        "40baa9",
    ),
)

make_entry(ID("77ef0c"),
    Formula(Equal(CC, SetBuilder(x+y*ConstI, Tuple(x, y), And(Element(x, RR), Element(y, RR))))))

make_entry(ID("a65a14"),
    SymbolDefinition(HH, HH, "Upper complex half-plane"),
    Description("Represents the set of complex numbers with strictly positive imaginary part."))

make_entry(ID("d7962e"),
    Formula(Equal(HH, SetBuilder(tau, tau, And(Element(tau, CC), Greater(Im(tau), 0))))))

make_entry(ID("fc0d55"),
    Formula(Equal(UnitCircle, SetBuilder(z, z, And(Element(z, CC), Equal(Abs(z), 1))))))

make_entry(ID("912ff9"),
    Formula(Equal(UnitCircle, SetBuilder(Exp(ConstI*theta), theta, Element(theta, ClosedOpenInterval(0, 2*ConstPi))))))

make_entry(ID("c98bad"),
    Formula(Equal(OpenDisk(z, r), SetBuilder(t, t, And(Element(t, CC), Less(Abs(z-t), r))))),
    Variables(z, r),
    Assumptions(And(Element(z, CC), Element(r, RR), Greater(r, 0))))

make_entry(ID("d1cf0c"),
    Formula(Equal(ClosedDisk(z, r), SetBuilder(t, t, And(Element(t, CC), LessEqual(Abs(z-t), r))))),
    Variables(z, r),
    Assumptions(And(Element(z, CC), Element(r, RR), GreaterEqual(r, 0))))


make_entry(ID("40baa9"),
    Formula(Equal(BernsteinEllipse(rho), SetBuilder(Div(rho*Exp(ConstI*theta) + rho**(-1)*Exp(-(ConstI*theta)), 2), theta, Element(theta, ClosedOpenInterval(0, 2*ConstPi))))),
    Variables(rho),
    Assumptions(And(Element(rho, RR), Greater(rho, 1))))


