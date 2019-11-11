# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Halphen's constant"),
    Section("Definitions"),
    Entries(
        "6161c7",
    ),
    Section("Numerical value"),
    Entries(
        "e2bfdb",
        "f5e0b0",
        "d0993b",
    ),
    Section("Approximation theory"),
    Entries(
        "5c1e44",
    ),
    Section("Formulas"),
    Entries(
        "9758ac",
        "31adf6",
        "831ea4",
        "c26bc9",
        "06c468",
    ),
)

# Definitions

make_entry(ID("6161c7"),
    SymbolDefinition(HalphenConstant, HalphenConstant, "Halphen's constant (one-ninth constant) 0.10765..."),
    CodeExample(HalphenConstant, "Represents Halphen's constant, also known as the one-ninth constant."),
    CodeExample(1/HalphenConstant, "Represents the reciprocal of Halphen's constant, also called Varga's constant."),
    References("S. Finch (2003), Mathematical Constants, Cambridge University Press, section 4.5",
        "https://www.chebfun.org/examples/approx/Halphen.html",
        "http://mathworld.wolfram.com/One-NinthConstant.html"))

# Numerical value

make_entry(ID("e2bfdb"),
    Formula(EqualNearestDecimal(HalphenConstant, 
        Decimal("0.10765391922648457661532344509094719058797656329012"), 50)),
    References(SloaneA("A072558")))

make_entry(ID("f5e0b0"),
    Formula(EqualNearestDecimal(1/HalphenConstant, 
        Decimal("9.2890254919208189187554494359517450610316948677501"), 50)),
    References(SloaneA("A073007")))

make_entry(ID("d0993b"),
    Formula(Unequal(HalphenConstant, Div(1,9))))

# Approximation theory

make_entry(ID("5c1e44"),
    Formula(Equal(HalphenConstant,
        Where(SequenceLimit(Pow(Subscript(lamda, n), 1/n), For(n, Infinity)),
            Equal(R, Set(r, ForElement(r, RationalFunctions(RR, t)), LessEqual(RationalFunctionDegree(r), Tuple(n, n)))),
            Equal(Subscript(lamda, n), Infimum(
                Supremum(Abs(Exp(x) - r(x)), ForElement(x, OpenClosedInterval(-Infinity, 0))),
                ForElement(r, R)))))))


# Formulas

make_entry(ID("9758ac"),
    Formula(Equal(HalphenConstant,
        UniqueZero(-Div(1,8) + Sum(n*x**n/(1-(-x)**n), For(n, 1, Infinity)),
            ForElement(x, OpenInterval(0, 1))))))

make_entry(ID("31adf6"),
    Formula(Equal(HalphenConstant,
        UniqueZero(Brackets(Sum((2*n+1)**2 * (-x)**(n*(n+1)/2), For(n, 0, Infinity))), ForElement(x, OpenInterval(0, 1))))))

make_entry(ID("831ea4"),
    Formula(Equal(HalphenConstant,
        UniqueZero(-Div(1,8) + Sum(Abs(DivisorSum((-1)**d * d, For(d, n))) * x**n, For(n, 1, Infinity)),
            ForElement(x, OpenInterval(0, 1))))))

make_entry(ID("c26bc9"),
    Formula(Equal(HalphenConstant,
        Where(Exp(-(Pi*EllipticK(1-c)/EllipticK(c))),
            Equal(c, UniqueZero(EllipticK(m) - 2*EllipticE(m), ForElement(m, OpenInterval(0, 1))))))))

make_entry(ID("06c468"),
    Formula(Equal(HalphenConstant,
        UniqueZero(Brackets(JacobiTheta(2, 0, Log(-x)/(2*Pi*ConstI), 2)), ForElement(x, OpenInterval(0, 1))))))

