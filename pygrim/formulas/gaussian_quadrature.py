# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Gaussian quadrature"),
    Section("Gauss-Legendre quadrature"),
    SeeTopics("Legendre polynomials"),
    Entries(
        "0745ee",   # Legendre polynomial zeros
        "ea4754",   # weights
        "47b181",   # -1,1
        "545987",   # a,b
    ),
)

make_entry(ID("ea4754"),
    Formula(Equal(GaussLegendreWeight(n, k), 2 / ((1 - LegendrePolynomialZero(n,k)**2) * ComplexDerivative(LegendrePolynomial(n, t), For(t, LegendrePolynomialZero(n, k), 1))**2))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(k, ZZBetween(1, n)))))

make_entry(ID("47b181"),
    Formula(Where(LessEqual(Abs(Integral(f(t), For(t, -1, 1)) - Sum(GaussLegendreWeight(n,k) * f(LegendrePolynomialZero(n,k)), For(k, 1, n))),
        64*M/(15*(1-rho**-2)*rho**(2*n))), Equal(M, Supremum(Abs(f(t)), ForElement(t, BernsteinEllipse(rho)))))),
    Variables(f, n, rho),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(rho, RR), Greater(rho, 1),
        IsHolomorphic(f(z), ForElement(z, InteriorClosure(BernsteinEllipse(rho)))))),
    References("L. N. Trefethen, Is Gauss Quadrature Better than Clenshaw-Curtis? SIAM Rev., 50(1), 67-87. DOI:10.1137/060659831"))

make_entry(ID("545987"),
    Formula(Where(LessEqual(Abs(Integral(f(t), For(t, a, b)) - (b-a)/2 * Sum(GaussLegendreWeight(n,k) * f((b-a)/2 * LegendrePolynomialZero(n,k) + (a+b)/2), For(k, 1, n))),
        (Abs(b-a)/2) * (64*M/(15*(1-rho**-2)*rho**(2*n)))), Equal(M, Supremum(Abs(f((b-a)/2 * t + (a+b)/2)), ForElement(t, BernsteinEllipse(rho)))))),
    Variables(f, a, b, n, rho),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(n, ZZGreaterEqual(1)), Element(rho, RR), Greater(rho, 1),
        IsHolomorphic(f(z), ForElement(z, Subset(InteriorClosure(BernsteinEllipse(rho))))))),
    References("L. N. Trefethen, Is Gauss Quadrature Better than Clenshaw-Curtis? SIAM Rev., 50(1), 67-87. DOI:10.1137/060659831"))

