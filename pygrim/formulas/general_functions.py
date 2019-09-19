# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("General analytic functions"),
    Section("Taylor series"),
    Entries(
        "1b1ec5",
        "b6582a",
        "78bb08",
    ),
    Section("Quadrature"),
    SeeTopics("Gaussian quadrature"),
    Entries(
        "545987",
    ),
    Section("Euler-Maclaurin formula"),
    Entries(
        "ce2272",
        "af2d4b",
    ),
)

make_entry(ID("1b1ec5"),
    Formula(Equal(f(z+x), Sum(Derivative(f(z), Tuple(z, z, k)) / Factorial(k) * x**k, Tuple(k, 0, Infinity)))),
    Variables(f, z, x),
    Assumptions(And(Element(z, CC), Element(x, CC),
        Subset(ClosedDisk(z, Abs(x)), HolomorphicDomain(f(z), z, CC)))))

make_entry(ID("b6582a"),
    Formula(Where(LessEqual(Abs(Derivative(f(z), Tuple(z, z, k)) / Factorial(k)), C / R**k),
        Equal(C, Supremum(Abs(f(t)), Var(t), And(Element(t, CC), Equal(Abs(t-z), R)))))),
    Variables(f, z, k, R),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)),
        Element(R, RR), Greater(R, 0),
        Subset(ClosedDisk(z, R), HolomorphicDomain(f(z), z, CC)))))

make_entry(ID("78bb08"),
    Formula(Where(LessEqual(Abs(f(z+x) - Sum(Derivative(f(z), Tuple(z, z, k)) / Factorial(k) * x**k, Tuple(k, 0, N - 1))), C * D**N / (1 - D)),
        Equal(C, Supremum(Abs(f(t)), Var(t), And(Element(t, CC), Equal(Abs(t-z), R)))), Equal(D, Abs(x)/R))),
    Variables(f, z, x, N, R),
    Assumptions(And(Element(z, CC), Element(x, CC), Element(N, ZZGreaterEqual(1)),
        Element(R, RR), Less(Abs(x), R),
        Subset(ClosedDisk(z, R), HolomorphicDomain(f(z), z, CC)))))

EM_rem = (f(N) + f(U))/2 + Sum(BernoulliB(2*k)/Factorial(2*k) * (Derivative(f(t), Tuple(t, U, 2*k-1)) - Derivative(f(t), Tuple(t, N, 2*k-1))), Tuple(k, 1, M))
EM_tail = Integral(BernoulliPolynomial(2*M,t-Floor(t))/Factorial(2*M) * Derivative(f(t), Tuple(t, t, 2*M)), Tuple(t, N, U))
EM_assumptions = And(Element(N, ZZ), Element(U, ZZ), LessEqual(N, U), Element(M, ZZGreaterEqual(1)), Subset(ClosedInterval(N, U), HolomorphicDomain(f(t), t, CC)))

make_entry(ID("ce2272"),
    Formula(Equal(Sum(f(k), Tuple(k, N, U)), Integral(f(t), Tuple(t, N, U)) + EM_rem + EM_tail)),
    Variables(f, N, U, M),
    Assumptions(EM_assumptions))

make_entry(ID("af2d4b"),
    Formula(LessEqual(Abs(Sum(f(k), Tuple(k, N, U)) - Parentheses(Integral(f(t), Tuple(t, N, U)) + EM_rem)),
            Div(4, (2*ConstPi)**(2*M)) * Integral(Abs(Derivative(f(t), Tuple(t, t, 2 * M))), Tuple(t, N, U)))),
    Variables(f, N, U, M),
    Assumptions(EM_assumptions))

