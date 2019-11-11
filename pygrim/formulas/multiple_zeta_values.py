# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Multiple zeta values"),
    Section("Definitions"),
    Entries(
        "aab550",
    ),
    Section("Sum representations"),
    Entries(
        "94a39f",
    ),
    Section("Specific values"),
    Entries(
        "345c26",
        "62de01",
        "a5e52e",
        "ef2c71",
        "856317",
        "3a5167",
    ),
    Section("Families of closed forms"),
    Entries(
        "ef8b17",
        "4a23c7",
    ),
    Section("Relations"),
    Entries(
        "da71d3",
        "70c42b",
    ),
),

make_entry(ID("aab550"),
    SymbolDefinition(MultiZetaValue, MultiZetaValue(Subscript(s, 1), Ellipsis, Subscript(s, k)), "Multiple zeta value (MZV)"),
    References("https://www.usna.edu/Users/math/meh/biblio.html"))

# Sum representations

# todo: Cartesian power
# todo: semantic subscript
# todo: render correctly
#       1/Mul(Step(Subscript(n, i)**Subscript(s, i), For(i, 1, k)))
make_entry(ID("94a39f"),
    Formula(Equal(MultiZetaValue(Step(Subscript(s, i), For(i, 1, k))),
        Sum(Product(1/Subscript(n,i)**Subscript(s,i), For(i, 1, k)), ForElement(n, Pow(ZZ, k)), Greater(Step(Subscript(n, i), For(i, 1, k)), 0)))),
    Variables(k, s),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(s, Pow(ZZGreaterEqual(1), k)), Greater(Sum(Subscript(s, i), For(i, 1, k)), k))))

# Specific values

make_entry(ID("345c26"),
    Formula(Equal(MultiZetaValue(2, 1), Sum(HarmonicNumber(n)/(n+1)**2, For(n, 1, Infinity)), RiemannZeta(3))))

make_entry(ID("62de01"),
    Formula(Equal(MultiZetaValue(2, 2), Div(3,4)*RiemannZeta(4))))

make_entry(ID("a5e52e"),
    Formula(Equal(MultiZetaValue(3, 2), 3*RiemannZeta(2)*RiemannZeta(3) - Div(11,2)*RiemannZeta(5))))

make_entry(ID("ef2c71"),
    Formula(Equal(MultiZetaValue(4, 2), RiemannZeta(3)**2 - Div(4,3)*RiemannZeta(6))))

make_entry(ID("856317"),
    Formula(Equal(MultiZetaValue(2, 3), Div(9,2)*RiemannZeta(5) - 2*RiemannZeta(2)*RiemannZeta(3))))

make_entry(ID("3a5167"),
    Formula(Equal(MultiZetaValue(3, 3), Div(1,2)*(RiemannZeta(3)**2 - RiemannZeta(6)))))

# Families of closed forms

make_entry(ID("ef8b17"),
    Formula(Equal(MultiZetaValue(s, s), Div(1,2)*(RiemannZeta(s)**2 - RiemannZeta(2*s)))),
    Variables(s),
    Assumptions(Element(s, ZZGreaterEqual(2))))

make_entry(ID("4a23c7"),
    Formula(Equal(MultiZetaValue(Repeat(2, n)), Pi**(2*n) / Factorial(2*n+1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

# Relations

make_entry(ID("da71d3"),
    Formula(Equal(MultiZetaValue(a, b) + MultiZetaValue(b, a), RiemannZeta(a)*RiemannZeta(b) - RiemannZeta(a+b))),
    Variables(a, b),
    Assumptions(And(Element(a, ZZGreaterEqual(2)), Element(b, ZZGreaterEqual(2)))))

make_entry(ID("70c42b"),
    Formula(Equal(MultiZetaValue(Repeat(3, 1, n)), 1/(2*n+1) * MultiZetaValue(Repeat(2, 2*n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

