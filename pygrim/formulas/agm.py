# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Arithmetic-geometric mean"),
    Section("Definitions"),
    Entries(
        "b0d256",
    ),
    Section("Illustrations"),
    Entries(
        "00d5df",
        "c941c4",
    ),
    Section("Single parameter"),
    Entries(
        "21f412",
    ),
    Section("Domain"),
    Entries(
        "32b3b4",
        "c38209",
        "f9caac",
        "098757",
    ),
    Section("Specific values"),
    Entries(
        "08329d",
        "8f176c",
        "3e1398",
        "b41bdd",
        "0d9352",
        "e3896e",
        "361801",
        "f9190b",
        "69d0a3",
        "5174ea",
        "7b362f",
    ),
    Section("Functional equations"),
    Entries(
        "59fab1",
        "c0dea0",
        "7189d6",
        "ce2395",
        "ea1d58",
    ),
#    Section("Representation by other functions"),
#    Section("Representation of other functions"),
#    Section("Differential equations"),
#    Section("Bounds and inequalities"),
)

make_entry(ID("b0d256"),
    SymbolDefinition(AGM, AGM(a,b), "Arithmetic-geometric mean"),
    Description("This function can be called with one or two arguments, with", Equal(AGM(z), AGM(1,z)), "."))

# Illustrations

make_entry(ID("00d5df"),
    Image(Description("Plot of", AGM(1,x), "on", Element(x, ClosedInterval(-2,2))),
        ImageSource("plot_agm")))

make_entry(ID("c941c4"),
    Image(Description("X-ray of", AGM(1,z), "on", Element(z, ClosedInterval(-4,4) + ClosedInterval(-4,4)*ConstI)),
        ImageSource("xray_agm")),
    description_xray)

# Single parameter

make_entry(ID("21f412"),
    Formula(Equal(AGM(z), AGM(1, z), AGM(z, 1))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Domain

make_entry(ID("32b3b4"),
    Formula(Implies(And(Element(a, CC), Element(b, CC)), Element(AGM(a, b), CC))),
    Variables(a, b))

make_entry(ID("c38209"),
    Formula(Implies(And(Element(a, ClosedOpenInterval(0, Infinity)), Element(b, ClosedOpenInterval(0, Infinity))), Element(AGM(a, b), ClosedOpenInterval(0, Infinity)))),
    Variables(a, b))

make_entry(ID("f9caac"),
    Formula(Implies(Element(x, CC), Element(AGM(x), CC))),
    Variables(x))

make_entry(ID("098757"),
    Formula(Implies(Element(x, ClosedOpenInterval(0, Infinity)), Element(AGM(x), ClosedOpenInterval(0, Infinity)))),
    Variables(x))

# Specific values

make_entry(ID("08329d"),
    Formula(Equal(AGM(0, b), 0)),
    Variables(b),
    Assumptions(Element(b, CC)))

make_entry(ID("8f176c"),
    Formula(Equal(AGM(a, 0), 0)),
    Variables(a),
    Assumptions(Element(a, CC)))

make_entry(ID("3e1398"),
    Formula(Equal(AGM(a, -a), 0)),
    Variables(a),
    Assumptions(Element(a, CC)))

make_entry(ID("b41bdd"),
    Formula(Equal(AGM(a, a), a)),
    Variables(a),
    Assumptions(Element(a, CC)))

make_entry(ID("0d9352"),
    Formula(Equal(AGM(1, Sqrt(2)), Div(Mul(2, Sqrt(2), Pow(Pi, Div(3, 2))), Pow(Gamma(Div(1, 4)), 2)))))

make_entry(ID("e3896e"),
    Formula(Equal(AGM(1, Sqrt(2)/2), Div(Mul(2, Pow(Pi, Div(3, 2))), Pow(Gamma(Div(1, 4)), 2)))))

make_entry(ID("361801"),
    Formula(Equal(AGM(1, 3+2*Sqrt(2)), Div(Mul(2, Add(2, Sqrt(2)), Pow(Pi, Div(3, 2))), Pow(Gamma(Div(1, 4)), 2)))))

make_entry(ID("f9190b"),
    Formula(Equal(AGM(1, 3-2*Sqrt(2)), Div(Mul(2, Sub(2, Sqrt(2)), Pow(Pi, Div(3, 2))), Pow(Gamma(Div(1, 4)), 2)))))

make_entry(ID("69d0a3"),
    Formula(Equal(AGM(1, ConstI), ((Sqrt(2) * (1+ConstI) * Pi**Div(3,2)) / Pow(Gamma(Div(1, 4)), 2)))))

make_entry(ID("5174ea"),
    Formula(Equal(AGM(1, -ConstI), ((Sqrt(2) * (1-ConstI) * Pi**Div(3,2)) / Pow(Gamma(Div(1, 4)), 2)))))

make_entry(ID("7b362f"),
    Formula(Equal(AGM(1, Sqrt(2)), (1/JacobiTheta(4, 0, ConstI)**2))))

# Functional equations

make_entry(ID("59fab1"),
    Formula(Equal(AGM(a, b), AGM(b, a))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("c0dea0"),
    Formula(Equal(AGM(Conjugate(a), Conjugate(b)), Conjugate(AGM(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), Or(Equal(a, 0), NotElement(b / a, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("7189d6"),
    Formula(Equal(AGM(-a, -b), -AGM(a, b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), Or(Equal(a, 0), NotElement(b / a, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("ce2395"),
    Formula(Equal(AGM(a, b), a * AGM(1, b / a))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotEqual(a, 0), NotElement(b / a, OpenClosedInterval(-Infinity, 0)))))

make_entry(ID("ea1d58"),
    Formula(Equal(AGM(a, b), b * AGM(1, a / b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotEqual(b, 0), NotElement(a / b, OpenClosedInterval(-Infinity, 0)))))



