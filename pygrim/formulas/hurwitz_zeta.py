# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Hurwitz zeta function"),
    Section("Definitions"),
    Entries(
        "04217b",
    ),
    Section("Illustrations"),
    Entries(
        "855201",
        "583bf9",
        "0e2bcb",
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
    Section("Specific values"),
    Entries(
        "af23f7",
        "b721b4",
        "fc6fe0",
        "6e69fc",
        "af7d3d",
        "c6d6e2",
        "6c3523",
        "575b8f",
        "ac8d3c",
        "b4ed44",
        "4dd87c",
        "2d4828",
        "33690e",
        "868061",
        "9417f4",
        "4064f5",
        "3e82c3",
        "951f86",
        "eda0f3",
        "b347d3",
        "2fabeb",
        "edad97",
        "84196a",
        "532f31",
        "5bdba2",
        "7dab87",
        "d99808",
        "150b3e",
        "3db90c",
    ),
    Section("Series representations"),
    Subsection("Dirichlet series"),
    Entries(
        "448d90",
        "77e507",
        "0bd6aa",
    ),
    Subsection("Laurent series"),
    Description("Related topic: ", TopicReference("Stieltjes constants")),
    Entries(
        "60c6da",
    ),
    Section("Integral representations"),
    Entries(
        "1699a9",
        "498036",
    ),
    Section("Functional equations"),
    Subsection("Recurrence relations"),
    Entries(
        "ed4f6f",
        "bed7ee",
        "95e270",
    ),
    Subsection("Multiplication formula"),
    Entries(
        "ba7f85",
        "ebc49c",
        "7d9feb",
    ),
    Subsection("Reflection formula"),
    Entries(
        "69a1a9",
    ),
    Section("Derivatives and differential equations"),
    Subsection("Argument derivatives"),
    Entries(
        "3ba544",
        "d0d03b",
    ),
    Subsection("Parameter derivatives"),
    Entries(
        "83065e",
        "40c3e2",
    ),
    Section("Euler-Maclaurin formula"),
    Entries(
        "d25d10",
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
    Subsection("Gamma and related functions"),
    Description("Related topics: ", TopicReference("Digamma function"), ", ", TopicReference("Barnes G-function")),
    Entries(
        "53026a",
        "f3b870",
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
    Subsection("Polylogarithms"),
    Entries(
        "52ea5f",
    ),
)

# Definitions

make_entry(ID("04217b"),
    SymbolDefinition(HurwitzZeta, HurwitzZeta(s, a), "Hurwitz zeta function"),
    CodeExample(HurwitzZeta(s, a), "represents the Hurwitz zeta function of argument", s, "and parameter", a, "."),
    CodeExample(HurwitzZeta(s, a, 1), "represents the Hurwitz zeta function of argument", s, "and parameter", a, ", differentiated once with respect to", s, "."),
    CodeExample(HurwitzZeta(s, a, r), "represents the Hurwitz zeta function of argument", s, "and parameter", a, ", differentiated to order", r, "with respect to", s, "."),
    References("https://dlmf.nist.gov/25.11", "http://functions.wolfram.com/ZetaFunctionsandPolylogarithms/Zeta2/"))

# Illustrations

make_entry(ID("855201"),
    Image(Description("Plot of", HurwitzZeta(s, a), "on", Element(s, ClosedInterval(-25,11)), "for",  Element(a, Set(Decimal("0.6"), Decimal("0.8"), Decimal("1.4")))),
        ImageSource("plot_hurwitz_zeta")))

make_entry(ID("583bf9"),
    Image(Description("X-ray of", HurwitzZeta(s, 1+ConstI/2), "on", Element(s, ClosedInterval(-20,20) + ClosedInterval(-20,20)*ConstI)),
        ImageSource("xray_hurwitz_zeta")),
    description_xray,
    )

make_entry(ID("0e2bcb"),
    Image(Description("X-ray of", HurwitzZeta(2+3*ConstI, a), "on", Element(a, ClosedInterval(-5,5) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_hurwitz_zeta_param")),
    description_xray,
    )

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

make_entry(ID("af23f7"),
    Formula(Equal(HurwitzZeta(s, 1), RiemannZeta(s))),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("b721b4"),
    Formula(Equal(HurwitzZeta(s, 2), RiemannZeta(s) - 1)),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("fc6fe0"),
    Formula(Equal(HurwitzZeta(s, 3), RiemannZeta(s) - 1 - 1/2**s)),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("6e69fc"),
    Formula(Equal(HurwitzZeta(s, n), RiemannZeta(s) - Sum(1/k**s, For(k, 1, n-1)))),
    Variables(s, n),
    Assumptions(And(Element(s, CC), Element(n, ZZGreaterEqual(1)))))

make_entry(ID("af7d3d"),
    Formula(Equal(HurwitzZeta(s, Div(1,2)), (2**s-1) * RiemannZeta(s))),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("c6d6e2"),
    Formula(Equal(HurwitzZeta(s, Div(3,2)), (2**s-1) * RiemannZeta(s) - 2**s)),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("6c3523"),
    Formula(Equal(HurwitzZeta(s, Div(1,2) + n), (2**s-1) * RiemannZeta(s) - 2**s * Sum(1/(2*k+1)**s, For(k, 0, n-1)))),
    Variables(s, n),
    Assumptions(And(Element(s, CC), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("575b8f"),
    Formula(Equal(HurwitzZeta(2, 1), Pi**2 / 6)))

make_entry(ID("ac8d3c"),
    Formula(Equal(HurwitzZeta(2, 2), Pi**2 / 6 - 1)))

make_entry(ID("b4ed44"),
    Formula(Equal(HurwitzZeta(3, 1), RiemannZeta(3))))

make_entry(ID("4dd87c"),
    Formula(Equal(HurwitzZeta(3, 2), RiemannZeta(3) - 1)))

make_entry(ID("2d4828"),
    Formula(Equal(HurwitzZeta(4, 1), Pi**4/90)))

make_entry(ID("33690e"),
    Formula(Equal(HurwitzZeta(4, 2), Pi**4/90 - 1)))

make_entry(ID("868061"),
    Formula(Equal(HurwitzZeta(2, Div(1,2)), Pi**2 / 2)))

make_entry(ID("9417f4"),
    Formula(Equal(HurwitzZeta(3, Div(1,2)), 7 * RiemannZeta(3))))

make_entry(ID("4064f5"),
    Formula(Equal(HurwitzZeta(4, Div(1,2)), Pi**4 / 6)))

make_entry(ID("3e82c3"),
    Formula(Equal(HurwitzZeta(2, Div(1,4)), Pi**2 + 8*ConstCatalan)))

make_entry(ID("951f86"),
    Formula(Equal(HurwitzZeta(2, Div(3,4)), Pi**2 - 8*ConstCatalan)))

make_entry(ID("eda0f3"),
    Formula(Equal(HurwitzZeta(3, Div(1,4)), 28*RiemannZeta(3)+Pi**3)))

make_entry(ID("b347d3"),
    Formula(Equal(HurwitzZeta(3, Div(3,4)), 28*RiemannZeta(3)-Pi**3)))

make_entry(ID("2fabeb"),
    Formula(Equal(HurwitzZeta(3, Div(1,6)), 91*RiemannZeta(3)+2*Sqrt(3)*Pi**3)))

make_entry(ID("edad97"),
    Formula(Equal(HurwitzZeta(3, Div(5,6)), 91*RiemannZeta(3)-2*Sqrt(3)*Pi**3)))

make_entry(ID("84196a"),
    Formula(Equal(HurwitzZeta(n, a), (-1)**n / Factorial(n-1) * DigammaFunction(a, n-1))),
    Variables(n, a),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(a, CC))))

make_entry(ID("532f31"),
    Formula(Equal(HurwitzZeta(1, a), UnsignedInfinity)),
    Variables(a),
    Assumptions(Element(a, SetMinus(CC, ZZLessEqual(0)))))

make_entry(ID("5bdba2"),
    Formula(Equal(HurwitzZeta(-n, a), -(BernoulliPolynomial(n+1, a)/(n+1)))),
    Variables(n, a),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC))))

make_entry(ID("7dab87"),
    Formula(Equal(HurwitzZeta(-n, 0), -(BernoulliB(n+1)/(n+1)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("d99808"),
    Formula(Equal(HurwitzZeta(0, a), Div(1,2)-a)),
    Variables(a),
    Assumptions(Element(a, CC)))

make_entry(ID("150b3e"),
    Formula(Equal(HurwitzZeta(0, 0), Div(1,2))))

make_entry(ID("3db90c"),
    Formula(Equal(HurwitzZeta(0, Div(1,2)), 0)))



# Series representations

make_entry(ID("448d90"),
    Formula(Equal(HurwitzZeta(s, a), Sum(1/(n+a)**s, For(n, 0, Infinity)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1), Element(a, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("77e507"),
    Formula(Equal(HurwitzZeta(s, a, r), (-1)**r * Sum(Log(n+a)**r/(n+a)**s, For(n, 0, Infinity)))),
    Variables(s, a, r),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1), Element(a, SetMinus(CC, ZZLessEqual(0))), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("0bd6aa"),
    Formula(Equal(HurwitzZeta(s, N), Sum(1/n**s, For(n, N, Infinity)))),
    Variables(s, N),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1), Element(N, ZZGreaterEqual(1)))))

# Integral representations

make_entry(ID("1699a9"),
    Formula(Equal(HurwitzZeta(s, a), (Pi/(2*(s-1))) * Integral((a-Div(1,2)+ConstI*x)**(1-s) / Cosh(Pi*x)**2, For(x, -Infinity, Infinity)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Unequal(s, 1), Element(a, CC), Greater(Re(a), Div(1,2)))),
    References("https://doi.org/10.1090/mcom/3401"))

make_entry(ID("498036"),
    Formula(Equal(HurwitzZeta(s, a), (1/Gamma(s)) * Integral((x**(s-1) * Exp(-(a*x))) / (1 - Exp(-x)), For(x, 0, Infinity)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Greater(Re(s), 1), Element(a, CC), Greater(Re(a), 0))))

# Functional equatons

## Recurrence relations

# note: 1/a**s vs a**-s -- assumes 0**(negative + c*i) = some infinity
make_entry(ID("ed4f6f"),
    Formula(Equal(HurwitzZeta(s, a+1), HurwitzZeta(s, a) - 1/a**s)),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Element(a, CC), Unequal(s, 1), Or(NotElement(a, ZZLessEqual(0)), Less(Re(s), 0), Equal(s, 0)))))

make_entry(ID("bed7ee"),
    Formula(Equal(HurwitzZeta(s, a+N), HurwitzZeta(s, a) - Sum(1/(n+a)**s, For(n, 0, N-1)))),
    Variables(s, a, N),
    Assumptions(And(Element(s, CC), Element(a, CC), Unequal(s, 1), Or(NotElement(a, ZZLessEqual(0)), Less(Re(s), 0), Equal(s, 0)), Element(N, ZZGreaterEqual(1)))))

make_entry(ID("95e270"),
    Formula(Equal(HurwitzZeta(s, a+N, r), HurwitzZeta(s, a, r) + (-1)**(r+1) * Sum(Log(a+k)**r / (a+k)**s, For(k, 0, N-1)))),
    Variables(s, a, N, r),
    Assumptions(And(Element(s, CC), Element(a, CC), Unequal(s, 1), Or(NotElement(a, ZZLessEqual(0)), Less(Re(s), 0)), Element(N, ZZGreaterEqual(1)), Element(r, ZZGreaterEqual(0)))))

## Multiplication formula

# todo: relax assumptions on a
make_entry(ID("ebc49c"),
    Formula(Equal(HurwitzZeta(s, a), (1/2**s) * (HurwitzZeta(s, a/2) + HurwitzZeta(s, (a+1)/2)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Element(a, CC), Unequal(s, 1), Greater(Re(a), 0))))

make_entry(ID("7d9feb"),
    Formula(Equal(HurwitzZeta(s, a), (1/N**s) * Sum(HurwitzZeta(s, (a + k)/N), For(k, 0, N-1)))),
    Variables(s, a, N),
    Assumptions(And(Element(s, CC), Element(a, CC), Unequal(s, 1), Greater(Re(a), 0), Element(N, ZZGreaterEqual(1)))))

make_entry(ID("ba7f85"),
    Formula(Equal(HurwitzZeta(s, N*a), (1/N**s) * Sum(HurwitzZeta(s, a + k/N), For(k, 0, N-1)))),
    Variables(s, a, N),
    Assumptions(And(Element(s, CC), Element(a, CC), Unequal(s, 1), Greater(Re(a), 0), Element(N, ZZGreaterEqual(1)))))

## Reflection formula

# todo: relax assumptions on a
make_entry(ID("69a1a9"),
    Formula(Equal(HurwitzZeta(1-s, p/q), (2*Gamma(s))/(2*Pi*q)**s * Sum(Cos(Pi*s/2 - 2*Pi*k*p/q) * HurwitzZeta(s, k/q), For(k, 1, q)))),
    Variables(s, p, q),
    Assumptions(And(Element(s, CC), NotElement(s, ZZ), Element(q, ZZGreaterEqual(1)), Element(p, Range(1, q)))))

# Derivatives and differential equations

# todo: relax assumptions on a
make_entry(ID("3ba544"),
    Formula(Equal(ComplexDerivative(HurwitzZeta(s, a), For(s, s)), HurwitzZeta(s, a, 1))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), Unequal(s, 1), Element(a, CC), Greater(Re(a), 0))))

# todo: relax assumptions on a
make_entry(ID("d0d03b"),
    Formula(Equal(ComplexDerivative(HurwitzZeta(s, a), For(s, s, r)), HurwitzZeta(s, a, r))),
    Variables(s, a, r),
    Assumptions(And(Element(s, CC), Unequal(s, 1), Element(a, CC), Greater(Re(a), 0), Element(r, ZZGreaterEqual(0)))))

# todo: relax assumptions on a
make_entry(ID("83065e"),
    Formula(Equal(ComplexDerivative(HurwitzZeta(s, a), For(a, a)), -(s*HurwitzZeta(s+1, a)))),
    Variables(s, a),
    Assumptions(And(Element(s, CC), NotElement(s, Set(0, 1)), Element(a, CC), Greater(Re(a), 0))))

# todo: relax assumptions on a
make_entry(ID("40c3e2"),
    Formula(Equal(ComplexDerivative(HurwitzZeta(s, a), For(a, a, r)), RisingFactorial(1-s-r, r) * HurwitzZeta(s+r, a))),
    Variables(s, a, r),
    Assumptions(And(Element(s, CC), Unequal(s, 1), Unequal(s+r, 1), Element(a, CC), Greater(Re(a), 0), Element(r, ZZGreaterEqual(0)))))

# Euler-Maclaurin formula

make_entry(ID("d25d10"),
    Formula(Equal(HurwitzZeta(s, a),
        Sum(1/(a+k)**s, For(k, 0, N-1)) +
        (a+N)**(1-s) / (s-1) +
        1/(a+N)**s * (Div(1,2) + Sum((BernoulliB(2*k)/Factorial(2*k)) * (RisingFactorial(s,2*k-1)/(a+N)**(2*k-1)), For(k, 1, M))) -
        Integral((BernoulliPolynomial(2*M, t - Floor(t)) / Factorial(2*M)) * (RisingFactorial(s, 2*M) / (a+t)**(s+2*M)), For(t, N, Infinity)))),
    Variables(s, a, N, M),
    Assumptions(And(Element(s, CC), Unequal(s, 1), Element(a, CC), Element(N, ZZGreaterEqual(1)), Element(M, ZZGreaterEqual(1)),
        Greater(Re(a+N), 0), Greater(Re(s+2*M-1), 0), Or(NotElement(a, ZZLessEqual(0)), Less(Re(s), 0), Equal(s, 0)))),
    References("http://dx.doi.org/10.1007/s11075-014-9893-1"))

# Representation of other functions

make_entry(ID("febdd2"),
    Formula(Equal(RiemannZeta(s), HurwitzZeta(s,1))),
    Variables(s),
    Assumptions(Element(s, CC)))

make_entry(ID("4228cd"),
    Formula(Equal(BernoulliPolynomial(n,z), -(n*HurwitzZeta(1-n,z)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(z, CC))))

make_entry(ID("f3b870"),
    Formula(Equal(LogGamma(z), HurwitzZeta(0, z, 1) + Log(2*Pi)/2)),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZLessEqual(0)))))

make_entry(ID("53026a"),
    Formula(Equal(Gamma(z), Sqrt(2*Pi) * Exp(HurwitzZeta(0, z, 1)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZLessEqual(0)))))

make_entry(ID("693e0e"),
    Formula(Equal(DigammaFunction(z), ComplexLimit(Brackets(1/(s-1) - HurwitzZeta(s,z)), For(s, 1)))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, ZZLessEqual(0)))))

make_entry(ID("52ea5f"),
    Formula(Equal(PolyLog(s, z), (Gamma(1-s) / (2*Pi)**(1-s)) * (ConstI**(1-s) * HurwitzZeta(s, Div(1,2) + Log(-z) / (2*Pi*ConstI))
        + ConstI**(s-1) * HurwitzZeta(1-s, Div(1,2) - Log(-z) / (2*Pi*ConstI))))),
    Variables(s, z),
    Assumptions(And(Element(s, CC), Element(z, CC), NotElement(z, Set(0, 1)), NotElement(s, ZZGreaterEqual(0)))))



