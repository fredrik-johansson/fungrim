# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Beta function"),
    Section("Definitions"),
    Entries(
        "1c46fa",
        "795fe5",
        "6bd011",
    ),
    Section("Main formulas"),
    Entries(
        "888581",
        "c92da4",
        "ba7baf",
        "3141e4",
        "ff613a",
        "6bcfa6",
    ),
    Section("Integral representations"),
    Entries(
        "542cf7",
        "48910b",
        "3e08b6",
        "a1941b",
    ),
    Section("Hypergeometric representations"),
    Entries(
        "5ec9c0",
    ),
    Section("Symmetry"),
    Entries(
        "cc2ebb",
        "315b3d",
        "fd0e48",
    ),
    Section("Integer parameters"),
    Entries(
        "082a69",
        "bb4f41",
        "72db94",
        "a7dbf6",
        "1f72e9",
    ),
    Section("Recurrence relations"),
    Entries(
        "bdea17",
        "e9f966",
    ),
)


# Definitions

make_entry(ID("1c46fa"),
    SymbolDefinition(BetaFunction, BetaFunction(a, b), "Beta function"))

make_entry(ID("795fe5"),
    SymbolDefinition(IncompleteBeta, IncompleteBeta(x, a, b), "Incomplete beta function"))

make_entry(ID("6bd011"),
    SymbolDefinition(IncompleteBetaRegularized, IncompleteBetaRegularized(x, a, b), "Regularized incomplete beta function"))

# Main formulas

make_entry(ID("888581"),
    Formula(Equal(BetaFunction(a, b), (Gamma(a) * Gamma(b)) / Gamma(a + b))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("ba7baf"),
    Formula(Equal(IncompleteBeta(0, a, b), 0)),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("3141e4"),
    Formula(Equal(IncompleteBeta(1, a, b), BetaFunction(a, b))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("c92da4"),
    Formula(Equal(IncompleteBetaRegularized(x, a, b), IncompleteBeta(x, a, b) / BetaFunction(a, b))),
    Variables(x, a, b),
    Assumptions(And(Element(x, CC), Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))), NotElement(a+b, ZZLessEqual(0)))))

make_entry(ID("ff613a"),
    Formula(Equal(IncompleteBetaRegularized(0, a, b), 0)),
    Variables(x, a, b),
    Assumptions(And(Element(x, CC), Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))), NotElement(a+b, ZZLessEqual(0)))))

make_entry(ID("6bcfa6"),
    Formula(Equal(IncompleteBetaRegularized(1, a, b), 1)),
    Variables(x, a, b),
    Assumptions(And(Element(x, CC), Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))), NotElement(a+b, ZZLessEqual(0)))))

# Integral representations

make_entry(ID("542cf7"),
    Formula(Equal(BetaFunction(a, b), Integral(t**(a-1) * (1-t)**(b-1), For(t, 0, 1)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), Greater(Re(a), 0), Greater(Re(b), 0))))

make_entry(ID("48910b"),
    Formula(Equal(BetaFunction(a, b), 2 * Integral(Sin(t)**(2*a-1) * Cos(t)**(2*b-1), For(t, 0, Pi / 2)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), Greater(Re(a), 0), Greater(Re(b), 0))))

make_entry(ID("3e08b6"),
    Formula(Equal(IncompleteBeta(x, a, b), Integral(t**(a-1) * (1-t)**(b-1), For(t, 0, x)))),
    Variables(x, a, b),
    Assumptions(And(Element(x, ClosedInterval(0,1)), Element(a, CC), Element(b, CC), Greater(Re(a), 0), Greater(Re(b), 0))))

make_entry(ID("a1941b"),
    Formula(Equal(IncompleteBetaRegularized(x, a, b), (1/BetaFunction(a,b)) * Integral(t**(a-1) * (1-t)**(b-1), For(t, 0, x)))),
    Variables(x, a, b),
    Assumptions(And(Element(x, ClosedInterval(0,1)), Element(a, CC), Element(b, CC), Greater(Re(a), 0), Greater(Re(b), 0))))

# Hypergeometric representations

make_entry(ID("5ec9c0"),
    Formula(Equal(IncompleteBeta(x, a, b), (x**a / a) * Hypergeometric2F1(a, 1-b, a+1, x))),
    Variables(x, a, b),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, CC), Element(x, SetMinus(CC, Set(1))), Or(NotEqual(x, 0), Greater(Re(a), 0)))))

# Symmetry 

make_entry(ID("cc2ebb"),
    Formula(Equal(BetaFunction(a, b), BetaFunction(b, a))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("315b3d"),
    Formula(Equal(IncompleteBetaRegularized(x, a, b), 1 - IncompleteBetaRegularized(1 - x, b, a))),
    Variables(a, b, x),
    Assumptions(And(Element(x, CC), Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))), NotElement(a+b, ZZLessEqual(0)))))

make_entry(ID("fd0e48"),
    Formula(Equal(BetaFunction(a,b) * BetaFunction(a+b,c), BetaFunction(b,c)*BetaFunction(a,b+c))),
    Variables(a, b, c),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))), Element(c, SetMinus(CC, ZZLessEqual(0))),
        NotElement(a+b, ZZLessEqual(0)), NotElement(b+c, ZZLessEqual(0)))))

# Integer parameters

make_entry(ID("082a69"),
    Formula(Equal(BetaFunction(m, n), (Factorial(m-1) * Factorial(n-1)) / Factorial(m+n-1))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("bb4f41"),
    Formula(Equal(BetaFunction(m, n), 1/(m * Binomial(m+n-1,m)))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZGreaterEqual(1)), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("72db94"),
    Formula(Equal(BetaFunction(n, b), Cases(Tuple(UnsignedInfinity, Element(-b, Range(0, n-1))),
            Tuple(1/(n * Binomial(n+b-1,n)), Otherwise)))),
    Variables(n, b),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(b, CC))))

make_entry(ID("a7dbf6"),
    Formula(Equal(BetaFunction(-n, b), Cases(Tuple((-1)**b / (b * Binomial(n,b)), Element(b, Range(1, n))), Tuple(UnsignedInfinity, Otherwise)))),
    Variables(n, b),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(b, CC))))

make_entry(ID("1f72e9"),
    Formula(Equal(Residue(BetaFunction(z, b), For(z, a)),
        Where(Cases(Tuple(Binomial(n-b, n), Element(n, ZZGreaterEqual(0))),
              Tuple(0, Otherwise)), Equal(n, -a)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, SetMinus(CC, ZZLessEqual(0))))))

# Recurrence relations

make_entry(ID("bdea17"),
    Formula(Equal((a+b) * BetaFunction(a+1,b), a * BetaFunction(a, b))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("e9f966"),
    Formula(Equal(BetaFunction(a,b), BetaFunction(a+1,b) + BetaFunction(a, b+1))),
    Variables(a, b),
    Assumptions(And(Element(a, SetMinus(CC, ZZLessEqual(0))), Element(b, SetMinus(CC, ZZLessEqual(0))))))

