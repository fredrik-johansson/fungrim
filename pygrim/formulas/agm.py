# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Arithmetic-geometric mean"),
    Section("Definitions"),
    Entries(
        "b0d256",
        "eda1e3",
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
        "eb0661",
        "3da9b7",
        "f178f2",
        "447541",
    ),
    Section("AGM iteration"),
    Subsection("Recurrence and limit"),
    Entries(
        "95fb3e",
        "84b888",
        "08b69d",
        "41f67b",
    ),
    Subsection("Correct square root for complex variables"),
    Entries(
        "a2b0f9",
    ),
    Section("Brent-Salamin algorithm for pi"),
    Entries(
        "6d9ceb",
        "13c539",
        "042551",
    ),
    Section("Functional equations"),
    Entries(
        "59fab1",
        "c0dea0",
        "7189d6",
        "ce2395",
        "ea1d58",
        "d60119",
        "c7f885",
        "fa6ff7",
        "8e80c6",
        "46c021",
        "9d84d8",
    ),
    Section("Representation by other functions"),
    Entries(
        "d6d836",
        "71a0ff",
    ),
    Section("Representation of other functions"),
    Entries(
        "e15f43",
        "26fd1b",
    ),
    Section("Derivatives and differential equations"),
    Entries(
        "20828c",
        "a4cc5a",
    ),
    Section("Series expansions"),
    Entries(
        "cfefa9",
    ),
    Section("Integral representations"),
    Entries(
        "417619",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "162ecf",
        "23ee29",
        "75e692",
    ),
)

make_entry(ID("b0d256"),
    SymbolDefinition(AGM, AGM(a,b), "Arithmetic-geometric mean"),
    Description("This function can be called with one or two arguments, with", Equal(AGM(z), AGM(1,z)), "."))

make_entry(ID("eda1e3"),
    SymbolDefinition(AGMSequence, AGMSequence(n,a,b), "Convergents in AGM iteration"),
    Description("Represents the tuple", Tuple(a_(n), b_(n)), "giving the", n, "-th values in the arithmetic-geometric mean iteration with initial values",
        Equal(Tuple(a_(0), b_(0)), Tuple(a, b)), "."))

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

make_entry(ID("eb0661"),
    Formula(Equal(AGM(1, 1), 1)))

make_entry(ID("3da9b7"),
    Formula(Equal(ComplexDerivative(AGM(1, x), For(x, 1)), Div(1, 2))))

make_entry(ID("f178f2"),
    Formula(Equal(ComplexDerivative(AGM(1, x), For(x, 1, 2)), -Div(1, 8))))

make_entry(ID("447541"),
    Formula(Equal(ComplexDerivative(AGM(1, x), For(x, 1, n)), ((-1)**n * Factorial(n) / 8**n) * SloaneA("060691", n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Limit representations

make_entry(ID("95fb3e"),
    Formula(Where(Equal(AGM(a, b), SequenceLimit(a_(n), For(n, Infinity)), SequenceLimit(b_(n), For(n, Infinity))),
        Def(Tuple(a_(n), b_(n)), AGMSequence(n, a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("84b888"),
    Formula(Equal(AGMSequence(0, a, b), Tuple(a, b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

# todo: the destructuring function assignment is not semantic yet

make_entry(ID("08b69d"),
    Formula(Where(Equal(Tuple(a_(n+1), b_(n+1)),
            Tuple((a_(n)+b_(n))/2, Sqrt(a_(n)*b_(n)))),
            Def(Tuple(a_(k), b_(k)), AGMSequence(k, a, b)))),
    Variables(n, a, b),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), Element(b, CC), Or(Equal(a, 0), Equal(b, 0), And(Greater(Re(a), 0), Greater(Re(b), 0)), Less(Abs(Arg(a)) + Abs(Arg(b)), Pi)))))

make_entry(ID("41f67b"),
    Formula(Where(And(Equal(2 * a_(n+1), a_(n) + b_(n)), Equal(b_(n+1)**2, a_(n) * b_(n))),
        Def(Tuple(a_(k), b_(k)), AGMSequence(k, a, b)))),
    Variables(n, a, b),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), Element(b, CC))))

make_entry(ID("a2b0f9"),
    Formula(Where(Equal(Tuple(a_(n+1), b_(n+1)),
            Where(Tuple(x, s*y),
                Def(x, (a_(n)+b_(n))/2), Def(y, Sqrt(a_(n)*b_(n))),
                    Def(s, Cases(Tuple(Pos(1), Or(Equal(y, 0), GreaterEqual(Re(x / y), 0))),
                                 Tuple(Neg(1), Otherwise))))),
            Def(Tuple(a_(k), b_(k)), AGMSequence(k, a, b)))),
    Variables(n, a, b),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), Element(b, CC))))

# Brent-Salamin algorithm

# Note: the algorithm here is slightly different than in Salamin's paper: we 
# include one additional term in the summation for c_(j), which adds a few
# digits of accuracy. The error bound is therefore not tight;
# it would be nice to have an updated bound here.

make_entry(ID("6d9ceb"),
    Formula(Where(Equal(Pi, 4 * AGM(1, 1/Sqrt(2))**2 / (1 - Sum(2**j * c_(j)**2, For(j, 0, Infinity))),
        SequenceLimit(
            ((a_(n)+b_(n))**2)/((1-Sum(2**j * c_(j)**2, For(j, 0, n)))), For(n, Infinity))
        ),
        Def(Tuple(a_(n), b_(n)), AGMSequence(n, 1, 1/Sqrt(2))), Def(c_(n), (a_(n)-b_(n))))))

make_entry(ID("13c539"),
    Formula(Where(LessEqual(Abs(Pi -
            ((a_(n)+b_(n))**2)/((1-Sum(2**j * c_(j)**2, For(j, 0, n))))),
            2**(n+8) * Exp(-(Pi * 2**(n+1)))),
        Def(Tuple(a_(n), b_(n)), AGMSequence(n, 1, 1/Sqrt(2))), Def(c_(n), (a_(n)-b_(n))))),
    References("https://doi.org/10.2307/2005327"))

make_entry(ID("042551"),
    Formula(Equal(Exp(Pi), Where(32 * Product((a_(n+1) / a_(n))**(2**(1-n)), For(n, 0, Infinity)),
        Def(Tuple(a_(n), b_(n)), AGMSequence(n, 1, 1/Sqrt(2)))))),
    References("https://doi.org/10.2307/2005327"))

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

make_entry(ID("d60119"),
    Formula(Equal(AGM(c*a, c*b), c*AGM(a, b))),
    Variables(a, b, c),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(c, CC), Or(Equal(a, 0), Equal(b, 0), Equal(c, 0), NotElement(b / a, OpenClosedInterval(-Infinity, 0))))))

make_entry(ID("c7f885"),
    Formula(Equal(AGM(a, b), AGM((a+b)/2, Sqrt(a*b)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), Or(Equal(a, 0), Equal(b, 0), And(Greater(Re(a), 0), Greater(Re(b), 0)), Less(Abs(Arg(a)) + Abs(Arg(b)), Pi)))))

make_entry(ID("fa6ff7"),
    Formula(Equal(AGM(a, b), Where(AGM(x, s*y),
    Def(x, (a+b)/2), Def(y, Sqrt(a*b)),
        Def(s, Cases(Tuple(Pos(1), Or(Equal(y, 0), GreaterEqual(Re(x / y), 0))),
                     Tuple(Neg(1), Otherwise)))))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("8e80c6"),
    Formula(Equal(AGM(1, b), b * AGM(1, 1 / b))),
    Variables(b),
    Assumptions(And(Element(b, CC), NotElement(b, OpenClosedInterval(-Infinity, 0)))))

make_entry(ID("46c021"),
    Formula(Equal(AGM(1, b), (b+1)/2 * AGM(1, 2*Sqrt(b)/(b+1)))),
    Variables(b),
    Assumptions(Element(b, CC)))

make_entry(ID("9d84d8"),
    Formula(Equal(AGM(1+b, 1-b), AGM(1, Sqrt(1-b**2)))),
    Variables(b),
    Assumptions(Element(b, CC)))

# Representation by other functions

make_entry(ID("d6d836"),
    Formula(Equal(AGM(a, b), (a+b)/(2*Hypergeometric2F1(Div(1,2), Div(1,2), 1, ((a-b)/(a+b))**2)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotEqual(b, 0), NotElement(a / b, OpenClosedInterval(-Infinity, 0)))))

make_entry(ID("71a0ff"),
    Formula(Equal(AGM(a, b), (Pi/4) * ((a+b)/EllipticK(((a-b)/(a+b))**2)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotEqual(b, 0), NotElement(a / b, OpenClosedInterval(-Infinity, 0)))))

# Representation of other functions

make_entry(ID("e15f43"),
    Formula(Equal(EllipticK(m), Pi / (2*AGM(1, Sqrt(1-m))))),
    Variables(m),
    Assumptions(Element(m, CC)))

make_entry(ID("26fd1b"),
    Formula(Equal(Log(1/q), Pi / (AGM(JacobiThetaQ(2,0,q)**2, JacobiThetaQ(3,0,q)**2)))),
    Variables(q),
    Assumptions(Element(q, OpenInterval(0, 1))))

# Derivatives and differential equations

make_entry(ID("20828c"),
    Formula(Equal(ComplexDerivative(AGM(a, b), For(a, a)), AGM(a, b)/(Pi*a*(a-b)) * (Pi*a - 2*AGM(a, b) * EllipticE(((a-b)/(a+b))**2)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotEqual(b, 0), NotEqual(a, b), NotElement(a / b, OpenClosedInterval(-Infinity, 0)))),
    References("http://functions.wolfram.com/09.54.20.0001.01"))

make_entry(ID("a4cc5a"),
    Formula(Where(Equal(2*a*(b**2-a**2) * ComplexDerivative(f(a), For(a, a))**2 - a*f(a)**2 + ((3*a**2-b**2)*ComplexDerivative(f(a), For(a, a))
        + a*(a**2-b**2) * ComplexDerivative(f(a), For(a, a, 2))) * f(a), 0), Def(f(a), AGM(a, b)))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC), NotEqual(b, 0), NotElement(a / b, OpenClosedInterval(-Infinity, 0)))),
    References("http://functions.wolfram.com/09.54.13.0001.01"))

# todo: d-finite equation and series expansion for 1/AGM(1,z)

# Series expansions

make_entry(ID("cfefa9"),
    Formula(Equal(AGM(1, 1+x), Sum(SloaneA("060691", n) / 8**n * (-x)**n, For(n, 0, Infinity)))),
    Variables(x),
    Assumptions(And(Element(x, CC), Less(Abs(x), 1))))

# Integral representations

make_entry(ID("417619"),
    Formula(Equal(AGM(a, b), Where(Pi/(2*I), Def(I, Integral(1/Sqrt(a**2*Cos(x)**2 + b**2*Sin(x)**2), For(x, 0, Pi/2)))))),
    Variables(a, b),
    Assumptions(And(Element(a, OpenInterval(0, Infinity)), Element(b, OpenInterval(0, Infinity)))))

# Bounds and inequalities

make_entry(ID("162ecf"),
    Formula(LessEqual(Sqrt(a*b), AGM(a, b), (a+b)/2)),
    Variables(a),
    Assumptions(And(Element(a, ClosedOpenInterval(0, Infinity)), Element(b, ClosedOpenInterval(0, Infinity)))))

make_entry(ID("23ee29"),
    Formula(LessEqual(AGM(a, b), Abs(AGM(Abs(a), Abs(b))))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("75e692"),
    Formula(Where(LessEqual(Abs(AGM(1, z) - a_(n)), Abs(a_(n) - b_(n))), Def(Tuple(a_(n), b_(n)), AGMSequence(n, 1, z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), GreaterEqual(Re(z), 0))))


