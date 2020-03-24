# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Gauss hypergeometric function"),
    Entries(
        "e03016",
        "c43abd",
    ),
    Section("Hypergeometric series"),
    Entries(
        "ad8db2",
        "306ef7",
        "fe6e74",
        "65693e",
    ),
    Section("Differential equations"),
    Entries(
        "f1bd89",
    ),
    Section("Specific values"),
    Entries(
        "18d955",
        "659ce8",
        "a85994",
        "20bf69",
    ),
    Section("Symmetries"),
    Entries(
        "0e0393",
        "3d6d7e",
    ),
    Section("Linear fractional transformations"),
    Entries(
        "651a4a",
        "b25089",
        "504717",
        "90ac58",
        "27bc34",
        "db3eb9",
        "ca9123",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "c60679",
        "853a62",
    ),
)

# Definitions

make_entry(ID("e03016"),
    SymbolDefinition(Hypergeometric2F1, Hypergeometric2F1(a,b,c,z), "Gauss hypergeometric function"))

make_entry(ID("c43abd"),
    SymbolDefinition(Hypergeometric2F1Regularized, Hypergeometric2F1Regularized(a,b,c,z), "Regularized Gauss hypergeometric function"))

# Hypergeometric series

make_entry(ID("ad8db2"),
    Formula(Equal(Hypergeometric2F1(a,b,c,z), Sum((RisingFactorial(a,k) * RisingFactorial(b,k) / RisingFactorial(c,k)) * (z**k / Factorial(k)), For(k, 0, Infinity)))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))), Element(z,CC), Or(Less(Abs(z), 1), Element(a, ZZLessEqual(0)), Element(b, ZZLessEqual(0))))))

make_entry(ID("306ef7"),
    Formula(Equal(Hypergeometric2F1Regularized(a,b,c,z), Sum((RisingFactorial(a,k) * RisingFactorial(b,k) / Gamma(c+k)) * (z**k / Factorial(k)), For(k, 0, Infinity)))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), Or(Less(Abs(z), 1), Element(a, ZZLessEqual(0)), Element(b, ZZLessEqual(0)), Element(c, ZZLessEqual(0))))))

make_entry(ID("fe6e74"),
    Formula(Equal(Hypergeometric2F1Regularized(a,b,c,z), Hypergeometric2F1(a,b,c,z) / Gamma(c))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))), Element(z,CC))))

# todo: when is z = 1 allowed?
make_entry(ID("65693e"),
    Formula(Equal(Hypergeometric2F1Regularized(a,b,-n,z),
        (RisingFactorial(a,n+1) * RisingFactorial(b,n+1) * z**(n+1) / Factorial(n+1)) * Hypergeometric2F1(a+n+1,b+n+1,n+2,z))),
    Variables(a,b,n,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(n, ZZGreaterEqual(0)), Element(z,SetMinus(CC, Set(1))))))


# Differential equations

make_entry(ID("f1bd89"),
    Formula(Where(Equal(z*(1-z) * ComplexDerivative(y(z), For(z, z, 2)) + (c - (a+b+1)*z)*ComplexDerivative(y(z), For(z, z, 1)) - a*b*y(z), 0),
        Equal(y(z), Hypergeometric2F1(a,b,c,z)))),
    Variables(a, b, c, z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))), Element(z, SetMinus(CC, ClosedOpenInterval(1, Infinity))))))

# Specific values

make_entry(ID("18d955"),
    Formula(Equal(Hypergeometric2F1(a,b,c,0), 1)),
    Variables(a,b,c),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))))))

make_entry(ID("659ce8"),
    Formula(Equal(Hypergeometric2F1(a,b,c,1), (Gamma(c)*Gamma(c-a-b))/(Gamma(c-a)*Gamma(c-b)))),
    Variables(a,b,c),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))), Greater(Re(c-a-b), 0))))

make_entry(ID("a85994"),
    Formula(Equal(Hypergeometric2F1(1,1,2,z), -(Log(1-z)/z))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0, 1)))))

# todo: relax assumptions
make_entry(ID("20bf69"),
    Formula(Equal(Hypergeometric2F1(a,b,b,z), (1-z)**(-a))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, SetMinus(CC, ZZLessEqual(0))), Element(z, SetMinus(CC, Set(0, 1))))))

# Symmetries

make_entry(ID("0e0393"),
    Formula(Equal(Hypergeometric2F1(a,b,c,z), Hypergeometric2F1(b,a,c,z))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))), Element(z, CC))))

make_entry(ID("3d6d7e"),
    Formula(Equal(Hypergeometric2F1(a,b,c,z), Conjugate(Hypergeometric2F1(Conjugate(a),Conjugate(b),Conjugate(c),Conjugate(z))))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))), Element(z, SetMinus(CC, ClosedOpenInterval(1, Infinity))))))


# Linear fractional transformations

make_entry(ID("651a4a"),
    Formula(Equal(Hypergeometric2F1Regularized(a,b,c,z),
        (1-z)**(c-a-b) * Hypergeometric2F1Regularized(c-a, c-b, c, z))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), NotEqual(z, 1))))

# todo: valid for all z given right conditions
make_entry(ID("b25089"),
    Formula(Equal(Hypergeometric2F1Regularized(a,b,c,z),
        (1-z)**(-a) * Hypergeometric2F1Regularized(a, c-b, c, z/(z-1)))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), NotElement(z, ClosedOpenInterval(1, Infinity)))))

# todo: valid for all z given right conditions
make_entry(ID("504717"),
    Formula(Equal(Hypergeometric2F1Regularized(a,b,c,z),
        (1-z)**(-b) * Hypergeometric2F1Regularized(c-a, b, c, z/(z-1)))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), NotElement(z, ClosedOpenInterval(1, Infinity)))))

make_entry(ID("90ac58"),
    Formula(Equal((Sin(Pi * (b-a)) / Pi) * Hypergeometric2F1Regularized(a,b,c,z),
        ((-z)**(-a) / (Gamma(b) * Gamma(c-a))) * Hypergeometric2F1Regularized(a, a-c+1, a-b+1, 1/z) - 
        ((-z)**(-b) / (Gamma(a) * Gamma(c-b))) * Hypergeometric2F1Regularized(b, b-c+1, b-a+1, 1/z))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), NotElement(z, ClosedOpenInterval(0, Infinity)))))

make_entry(ID("27bc34"),
    Formula(Equal((Sin(Pi * (b-a)) / Pi) * Hypergeometric2F1Regularized(a,b,c,z),
        ((1-z)**(-a) / (Gamma(b) * Gamma(c-a))) * Hypergeometric2F1Regularized(a, c-b, a-b+1, 1/(1-z)) - 
        ((1-z)**(-b) / (Gamma(a) * Gamma(c-b))) * Hypergeometric2F1Regularized(b, c-a, b-a+1, 1/(1-z)))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), NotElement(z, ClosedOpenInterval(0, Infinity)))))

make_entry(ID("db3eb9"),
    Formula(Equal((Sin(Pi * (c-a-b)) / Pi) * Hypergeometric2F1Regularized(a,b,c,z),
        (1 / (Gamma(c-a) * Gamma(c-b))) * Hypergeometric2F1Regularized(a, b, a+b-c+1, 1-z) - 
        ((1-z)**(c-a-b) / (Gamma(a) * Gamma(b))) * Hypergeometric2F1Regularized(c-a, c-b, c-a-b+1, 1-z))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), NotElement(z, ClosedOpenInterval(1, Infinity)))))

make_entry(ID("ca9123"),
    Formula(Equal((Sin(Pi * (c-a-b)) / Pi) * Hypergeometric2F1Regularized(a,b,c,z),
        (z**(-a) / (Gamma(c-a) * Gamma(c-b))) * Hypergeometric2F1Regularized(a, a-c+1, a+b-c+1, 1-1/z) - 
        ((z**(a-c) * (1-z)**(c-a-b)) / (Gamma(a) * Gamma(b))) * Hypergeometric2F1Regularized(c-a, 1-a, c-a-b+1, 1-1/z))),
    Variables(a,b,c,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, CC), Element(z,CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), NotElement(z, ClosedOpenInterval(1, Infinity)))))

# Bounds and inequalities

# todo: the assumption refers to D which is defined inside the formula; can the markup be improved?
make_entry(ID("c60679"),
    Formula(Where(LessEqual(Abs(Hypergeometric2F1(a,b,c,z) - Sum((RisingFactorial(a,k) * RisingFactorial(b,k) / RisingFactorial(c,k)) * (z**k / Factorial(k)), For(k, 0, N-1))),
        Abs((RisingFactorial(a,N) * RisingFactorial(b,N) / RisingFactorial(c,N)) * (z**N / Factorial(N))) * Cases(Tuple(1/(1-D), Less(D, 1)), Tuple(Infinity, Otherwise))),
            Equal(D, Abs(z) * (1 + Abs(a-c)/Abs(c+N)) * (1 + Abs(b-1)/Abs(1+N)))
            )),
    Variables(a,b,c,z,N),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(c, SetMinus(CC, ZZLessEqual(0))), Element(z,CC), Less(Abs(z), 1), Element(N, ZZGreaterEqual(0)),
        Greater(Re(c)+N, 0))))


make_entry(ID("853a62"),
    Formula(Where(LessEqual(Abs(ComplexDerivative(f(z), For(z, z, k)) / Factorial(k)), A * Binomial(N+k, k) * nu**k),
        Equal(f(z), Hypergeometric2F1Regularized(a,b,c,z)), Equal(nu, Max(1/Abs(z-1),1/Abs(z))),
            Equal(N, 2*Max(Sqrt(nu**(-1)*Abs(a*b)), (Abs(a+b+1)+2*Abs(c)))),
            Equal(A, Max(Abs(f(z)), Abs(ComplexDerivative(f(z), For(z, z, 1)))/(nu*(N+1)))))),
    # todo: consider formalizing the generalization
    Description("Actually valid when", f(z), "is any branch of any solution of the hypergeometric ODE, away from the branch points", Equal(z, 0), "and", Equal(z, 1), ".",
        "The variables", nu, ",", N, ", and", A, "can be replaced by any upper bounds."),
    Variables(a, b, c, z, k),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(c, CC), Element(z, SetMinus(CC, Union(Set(0), ClosedOpenInterval(1, Infinity)))), Element(k, ZZGreaterEqual(0)))),
    References("F. Johansson, Computing hypergeometric functions rigorously, https://arxiv.org/abs/1606.06977"))


