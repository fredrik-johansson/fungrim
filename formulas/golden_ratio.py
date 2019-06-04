# -*- coding: utf-8 -*-

from .expr import *

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
    ),
    Section("Limit representations"),
    Entries(
        "2b6e60",
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
    Formula(Equal(Zeros(x**2-x-1, x, Element(x, CC)), Set(GoldenRatio, 1-GoldenRatio))))

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

# Limit representations

make_entry(ID("2b6e60"),
    Formula(Equal(GoldenRatio, Limit(Fibonacci(n+1)/Fibonacci(n), n, Infinity))))



"""


1e4f62


1667b8

550373
a232c0
192ed5

f12cee
6f9f43
7995a7
ae311a
374813



make_entry(ID("0c9939"),
    Formula(Equal(ConstPi, 4*Atan(1))))

make_entry(ID("f8d280"),
    Formula(Equal(ConstPi, 16*Acot(5) - 4*Acot(239))))

make_entry(ID("590136"),
    Formula(Equal(ConstPi, -(ConstI * Log(-1)))))

make_entry(ID("464961"),
    Formula(Equal(ConstPi, 2 * Integral(Sqrt(1-x**2), Tuple(x, -1, 1)))))

make_entry(ID("04cd99"),
    Formula(Equal(ConstPi, Integral(1/(x**2+1), Tuple(x, -Infinity, Infinity)))))

make_entry(ID("dae4a7"),
    Formula(Equal(ConstPi, Integral(Exp(-x**2), Tuple(x, -Infinity, Infinity))**2)))

make_entry(ID("f617c0"),
    Formula(Equal(ConstPi, 4*Sum((-1)**k / (2*k+1), Tuple(k, 0, Infinity)))))

make_entry(ID("fddfe6"),
    Formula(Equal(ConstPi, Sum((1 / 16**k) * (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)), Tuple(k, 0, Infinity)))),
    References("D. H. Bailey and P. B. Borwein and S. Plouffe (1997). On the rapid computation of various polylogarithmic constants. Mathematics of Computation. vol 66, no 218, p. 903–913. DOI:10.1090/S0025-5718-97-00856-9"))

make_entry(ID("69fe63"),
    Formula(Equal(ConstPi, 2*Product((4*k**2)/(4*k**2-1), Tuple(k, 1, Infinity)))))

make_entry(ID("e1e106"),
    Formula(Equal(ConstPi, Limit(16**k/(k*Binomial(2*k,k)**2), k, Infinity))))

make_entry(ID("2516c2"),
    Formula(Less(Abs(ConstPi - Div(22,7)), Decimal("0.00127"))))

make_entry(ID("1e3a25"),
    Formula(Less(Abs(ConstPi - Div(355,113)), Decimal("2.67e-7"))))

make_entry(ID("fdc3a3"),
    Formula(Less(Abs(ConstPi - Log(Pow(640320,3)+744)/Sqrt(163)), Decimal("2.24e-31"))))

make_entry(ID("4c0698"),
    Formula(Less(Abs(1/ConstPi -
        Parentheses(12*Sum((-1)**k*Factorial(6*k)*(13591409+545140134*k)/(Factorial(3*k)*Factorial(k)**3*640320**(3*k+Div(3,2))),
            Tuple(k, 0, N-1)))), Div(1,151931373056000**N))),
    Variables(N),
    Assumptions(Element(N, ZZGreaterEqual(0))))

"""
