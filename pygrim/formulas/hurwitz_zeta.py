# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Hurwitz zeta function"),
    Section("Definitions"),
    Entries(
        "04217b",
    ),
    Section("Domain and range"),
    Entries(
        "56dcbd",
        "ad269f",
        "e7224b",
        "b0f500",
        "cc523f",
        "ec2dd5",
        "a5980a",
        "d0b234",
        "c5d844",
    ),
    Subsection("As a function of the argument"),
    Entries(
        "4bf3da",
        "ea271f",
        "26418b",
    ),
    Subsection("As a function of the parameter"),
    Entries(
        "93e149",
        "8c7cdb",
        "05c2dd",
        "f045b3",
    ),
    Section("Series representations"),
    Subsection("Dirichlet series"),
    Entries(
        "448d90",
        "77e507",
    ),
    Subsection("Laurent series"),
    Description("Related topic: ", TopicReference("Stieltjes constants")),
    Entries(
        "60c6da",
    ),
    Section("Integral representations"),
    Entries(
        "1699a9",
    ),
    Section("Representation of other functions"),
    Subsection("Riemann zeta function"),
    Description("Related topic: ", TopicReference("Riemann zeta function")),
    Entries(
        "febdd2",
    ),
    Subsection("Bernoulli polynomials"),
    Description("Related topic: ", TopicReference("Bernoulli numbers and polynomials")),
    Entries(
        "4228cd",
    ),
    Subsection("Polygamma and related functions"),
    Description("Related topics: ", TopicReference("Digamma function"), ", ", TopicReference("Barnes G-function")),
    Entries(
        "693e0e",
        "bba4ec",  # included from digamma
        "e05807",  # included from barnes_g
    ),
    Subsection("Dirichlet L-functions"),
    Description("Related topic: ", TopicReference("Dirichlet L-functions")),
    Entries(
        "c31c10",  # included from dirichlet...
        "4c3678",  # included from dirichlet...
    ),
)

# Definitions

make_entry(ID("04217b"),
    SymbolDefinition(HurwitzZeta, HurwitzZeta(s, a), "Hurwitz zeta function"),
    CodeExample(HurwitzZeta(s, a), "represents the Hurwitz zeta function of argument", s, "and parameter", a, "."),
    CodeExample(HurwitzZeta(s, a, 1), "represents the Hurwitz zeta function of argument", s, "and parameter", a, ", differentiated once with respect to", s, "."),
    CodeExample(HurwitzZeta(s, a, r), "represents the Hurwitz zeta function of argument", s, "and parameter", a, ", differentiated to order", r, "with respect to", s, "."))

# Domain and range

make_entry(ID("56dcbd"),
    Formula(Implies(And(Element(s, SetMinus(CC, Set(1))), Element(a, SetMinus(CC, ZZLessEqual(0)))), Element(HurwitzZeta(s, a), CC))),
    Variables(s, a))

make_entry(ID("ad269f"),
    Formula(Implies(And(Element(s, CC), Less(Re(s), 0), Element(a, CC)), Element(HurwitzZeta(s, a), CC))),
    Variables(s, a))

make_entry(ID("e7224b"),
    Formula(Implies(And(Element(s, SetMinus(RR, Set(1))), Element(a, OpenInterval(0, Infinity))), Element(HurwitzZeta(s, a), RR))),
    Variables(s, a))

make_entry(ID("b0f500"),
    Formula(Implies(And(Element(s, SetMinus(ZZ, Set(1))), Element(a, SetMinus(RR, ZZLessEqual(0)))), Element(HurwitzZeta(s, a), RR))),
    Variables(s, a))

make_entry(ID("cc523f"),
    Formula(Implies(And(Element(s, ZZLessEqual(0)), Element(a, QQ)), Element(HurwitzZeta(s, a), QQ))),
    Variables(s, a))

make_entry(ID("ec2dd5"),
    Formula(Implies(And(Element(s, ZZLessEqual(0)), Element(a, RR)), Element(HurwitzZeta(s, a), RR))),
    Variables(s, a))

make_entry(ID("a5980a"),
    Formula(Implies(And(Element(s, ZZLessEqual(0)), Element(a, CC)), Element(HurwitzZeta(s, a), CC))),
    Variables(s, a))

make_entry(ID("d0b234"),
    Formula(Implies(And(Element(s, Set(1)), Element(a, SetMinus(CC, ZZLessEqual(0)))), Element(HurwitzZeta(s, a), Set(UnsignedInfinity)))),
    Variables(s, a))

make_entry(ID("c5d844"),
    Formula(Implies(And(Element(s, ZZGreaterEqual(2)), Element(a, ZZLessEqual(0))), Element(HurwitzZeta(s, a), Set(UnsignedInfinity)))),
    Variables(s, a))

## As a function of s

make_entry(ID("4bf3da"),
    Formula(Implies(Element(a, SetMinus(CC, ZZLessEqual(0))), IsHolomorphic(HurwitzZeta(s, a), ForElement(s, SetMinus(CC, Set(1)))))),
    Variables(a))

make_entry(ID("ea271f"),
    Formula(Implies(Element(a, SetMinus(CC, ZZLessEqual(0))), IsMeromorphic(HurwitzZeta(s, a), ForElement(s, CC)))),
    Variables(a))

# CCLessEqual(0) ?
make_entry(ID("26418b"),
    Formula(Implies(Element(a, CC), IsHolomorphic(HurwitzZeta(s, a), ForElement(s, Set(t, ForElement(t, CC), Less(Re(t), 0)))))),
    Variables(a))

## As a function of a

make_entry(ID("93e149"),
    Formula(Implies(Element(s, SetMinus(CC, Set(1))), IsHolomorphic(HurwitzZeta(s, a), ForElement(a, SetMinus(CC, OpenClosedInterval(-Infinity, 0)))))),
    Variables(s))

make_entry(ID("8c7cdb"),
    Formula(Implies(Element(s, ZZGreaterEqual(2)), IsHolomorphic(HurwitzZeta(s, a), ForElement(a, SetMinus(CC, ZZLessEqual(0)))))),
    Variables(s))

make_entry(ID("05c2dd"),
    Formula(Implies(Element(s, ZZGreaterEqual(2)), IsMeromorphic(HurwitzZeta(s, a), ForElement(a, CC)))),
    Variables(s))

make_entry(ID("f045b3"),
    Formula(Implies(Element(s, ZZLessEqual(0)), IsHolomorphic(HurwitzZeta(s, a), ForElement(a, CC)))),
    Variables(s))



# Specific values

# Series representations

make_entry(ID("448d90"),
    Formula(Equal(HurwitzZeta(s, a), Sum(1/(n+a)**s, For(n, 0, Infinity)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1), Element(a, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("77e507"),
    Formula(Equal(HurwitzZeta(s, a, r), (-1)**r * Sum(Log(n+a)**r/(n+a)**s, For(n, 0, Infinity)))),
    Variables(s, a, r),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1), Element(a, SetMinus(CC, ZZLessEqual(0))), Element(r, ZZGreaterEqual(0)))))

# Integral representations

make_entry(ID("1699a9"),
    Formula(Equal(HurwitzZeta(s, a), (ConstPi/(2*(s-1))) * Integral((a-Div(1,2)+ConstI*x)**(1-s) / Cosh(ConstPi*x)**2, For(x, -Infinity, Infinity)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Unequal(s, 1), Element(a, CC), Greater(Re(a), Div(1,2)))))

# Representation of other functions

make_entry(ID("febdd2"),
    Formula(Equal(RiemannZeta(s), HurwitzZeta(s,1))),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("4228cd"),
    Formula(Equal(BernoulliPolynomial(n,z), -(n*HurwitzZeta(1-n,z)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(z, CC))))

make_entry(ID("693e0e"),
    Formula(Equal(DigammaFunction(z), ComplexLimit(Brackets(1/(s-1) - HurwitzZeta(s,z)), For(s, 1)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZLessEqual(0)))))

