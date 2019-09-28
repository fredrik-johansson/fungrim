# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Golden ratio"),
    Section("Definitions"),
    Entries(
        "37f505",
    ),
    Section("Numerical value"),
    Entries(
        "08fcaf",
        "77d2f8",
        "e09458",
    ),
    Section("Algebraic equations"),
    Entries(
        "31f52c",
        "b464d3",
        "d774fe",
        "77c324",
        "6d2709",
        "2e0596",
        "ebfcd8",
    ),
    Section("Trigonometric formulas"),
    Entries(
        "98a765",
        "487e35",
        "fad16f",
    ),
    Section("Recurrence relations"),
    Entries(
        "0cd1a4",
        "6a11ce",
    ),
    Section("Limit representations"),
    Entries(
        "2b6e60",
    ),
    Section("Special function representations"),
    Entries(
        "e9a269",
    ),
)

make_entry(ID("37f505"),
    SymbolDefinition(GoldenRatio, GoldenRatio, "The golden ratio (1.618...)"))

# Numerical value

make_entry(ID("08fcaf"),
    Formula(Element(GoldenRatio,
        RealBall(Decimal("1.6180339887498948482045868343656381177203091798058"), Decimal("3.72e-50")))))

make_entry(ID("77d2f8"),
    Formula(Equal(GoldenRatio, (1+Sqrt(5))/2)))

make_entry(ID("e09458"),
    Formula(NotElement(GoldenRatio, QQ)))

# Algebraic equations

make_entry(ID("31f52c"),
    Formula(Equal(1/GoldenRatio, GoldenRatio - 1)))

make_entry(ID("b464d3"),
    Formula(Equal(GoldenRatio**2 - GoldenRatio - 1, 0)))

make_entry(ID("d774fe"),
    Formula(Implies(Equal((a+b)/a, a/b), Equal(a/b, GoldenRatio))),
    Variables(a, b),
    Assumptions(And(Element(a, OpenInterval(0, Infinity)), Element(b, OpenInterval(0, Infinity)))))

make_entry(ID("77c324"),
    Formula(Equal(Zeros(x**2-x-1, ForElement(x, CC)), Set(GoldenRatio, 1-GoldenRatio))))

make_entry(ID("6d2709"),
    Formula(Equal(GoldenRatio, 1+1/GoldenRatio)))

make_entry(ID("2e0596"),
    Formula(Equal(GoldenRatio, 1+1/(1+1/GoldenRatio))))

make_entry(ID("ebfcd8"),
    Formula(Equal(Spectrum(Matrix2x2(1, 1, 1, 0)), Set(GoldenRatio, 1-GoldenRatio))))

# Trigonometric formulas

make_entry(ID("98a765"),
    Formula(Equal(GoldenRatio, 2*Cos(ConstPi/5))))

make_entry(ID("487e35"),
    Formula(Equal(GoldenRatio, 2*Sin(3*ConstPi/10))))

make_entry(ID("fad16f"),
    Formula(Equal(GoldenRatio, 2*Sin(ConstPi/10)+1)))

# Recurrence relations

make_entry(ID("0cd1a4"),
    Formula(Equal(GoldenRatio**(n+1), GoldenRatio**n + GoldenRatio**(n-1))),
    Variables(n),
    Assumptions(Element(n, CC)))

make_entry(ID("6a11ce"),
    Formula(Equal(GoldenRatio**n, Fibonacci(n) * GoldenRatio + Fibonacci(n-1))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Limit representations

make_entry(ID("2b6e60"),
    Formula(Equal(GoldenRatio, SequenceLimit(Fibonacci(n+1)/Fibonacci(n), For(n, Infinity)))))

# Special function representations

make_entry(ID("e9a269"),
    Formula(Equal(GoldenRatio, Div(1,5) * (DedekindEta(ConstI) / DedekindEta(5*ConstI))**2)))

