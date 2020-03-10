# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Confluent hypergeometric functions"),
    Entries(
        "316533",
        "f565f5",
        "512bea",
        "cee331",
        "d6add6",
        "1b9cc5",
        "b9cc75",
    ),
    Section("Hypergeometric series"),
    Entries(
        "4c41ad",
        "0a0aec",
        "a61f01",
        "dec042",
        "70111e",
    ),
    Section("Differential equations"),
    Entries(
        "06f229",
        "bb5d67",
    ),
    Section("Kummer's transformation"),
    Entries(
        "be533c",
        "a047eb",
        "9d3147",
    ),
    Section("Connection formulas"),
    Entries(
        "c8fcc7",  # ustar as u
        "4cf1e9",  # ustar as 2f0
        "f7f84e",  # 1f1r as ustar
        "6cf802",  # u as 1f1
        "18ef23",  # u as 1f1, integer
        "2df3e3",  # 0f1 as 1f1
        "325a0e",  # 0f1 as J
        "00dfd1",  # 0f1 as I
    ),
    Section("Asymptotic expansions"),
    Entries(
        "d1b3b5",
        "99f69c",
        "876844",
        "279e4f",
        "461a54",
        "7b91b4",
    ),
)


make_entry(ID("316533"),
    SymbolDefinition(Hypergeometric0F1, Hypergeometric0F1(a,z), "Confluent hypergeometric limit function"))

make_entry(ID("f565f5"),
    SymbolDefinition(Hypergeometric0F1Regularized, Hypergeometric0F1Regularized(a,z), "Regularized confluent hypergeometric limit function"))

make_entry(ID("512bea"),
    SymbolDefinition(Hypergeometric1F1, Hypergeometric1F1(a,b,z), "Kummer confluent hypergeometric function"))

make_entry(ID("cee331"),
    SymbolDefinition(Hypergeometric1F1Regularized, Hypergeometric1F1Regularized(a,b,z), "Regularized Kummer confluent hypergeometric function"))

make_entry(ID("d6add6"),
    SymbolDefinition(HypergeometricU, HypergeometricU(a,b,z), "Tricomi confluent hypergeometric function"))

make_entry(ID("1b9cc5"),
    SymbolDefinition(HypergeometricUStar, HypergeometricUStar(a,b,z), "Scaled Tricomi confluent hypergeometric function"))

make_entry(ID("b9cc75"),
    SymbolDefinition(Hypergeometric2F0, Hypergeometric2F0(a,b,z), "Tricomi confluent hypergeometric function, alternative notation"))


make_entry(ID("4c41ad"),
    Formula(Equal(Hypergeometric0F1(a,z), Sum(1/RisingFactorial(a,k) * (z**k / Factorial(k)), For(k, 0, Infinity)))),
    Variables(a,z),
    Assumptions(And(Element(a,SetMinus(CC,ZZLessEqual(0))), Element(z,CC))))

make_entry(ID("0a0aec"),
    Formula(Equal(Hypergeometric0F1Regularized(a,z), Sum(1/Gamma(a+k) * (z**k / Factorial(k)), For(k, 0, Infinity)))),
    Variables(a,z),
    Assumptions(And(Element(a,CC), Element(z,CC))))

make_entry(ID("a61f01"),
    Formula(Equal(Hypergeometric1F1(a,b,z), Sum(RisingFactorial(a,k)/RisingFactorial(b,k) * (z**k / Factorial(k)), For(k, 0, Infinity)))),
    Variables(a,b,z),
    Assumptions(And(Element(a,CC), Element(b, SetMinus(CC, ZZLessEqual(0))), Element(z,CC))))

make_entry(ID("dec042"),
    Formula(Equal(Hypergeometric1F1(-n,b,z), Sum(RisingFactorial(-n,k)/RisingFactorial(b,k) * (z**k / Factorial(k)), For(k, 0, n)))),
    Variables(n,b,z),
    #Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(b, SetMinus(CC, Range(-n+1, 0))), Element(z,CC))))
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(b, CC), Not(And(Element(b, ZZLessEqual(0)), Greater(b, -n))), Element(z,CC))))

make_entry(ID("70111e"),
    Formula(Equal(Hypergeometric1F1Regularized(a,b,z), Sum(RisingFactorial(a,k)/Gamma(b+k) * (z**k / Factorial(k)), For(k, 0, Infinity)))),
    Variables(a,b,z),
    Assumptions(And(Element(a,CC), Element(b, CC), Element(z,CC))))

make_entry(ID("be533c"),
    Formula(Equal(Hypergeometric1F1(a,b,z), Exp(z) * Hypergeometric1F1(b-a, b, -z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, SetMinus(CC, ZZLessEqual(0))), Element(z, CC))))

make_entry(ID("a047eb"),
    Formula(Equal(Hypergeometric1F1Regularized(a,b,z), Exp(z) * Hypergeometric1F1Regularized(b-a, b, -z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC))))

make_entry(ID("9d3147"),
    Formula(Equal(HypergeometricU(a,b,z), z**(1-b) * HypergeometricU(1+a-b, 2-b, z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), NotEqual(z, 0))))

make_entry(ID("06f229"),
    Formula(Where(Equal(z * ComplexDerivative(y(z), For(z, z, 2)) + (b-z) * ComplexDerivative(y(z), For(z, z, 1)) - a*y(z), 0), Equal(y(z),
        C*Hypergeometric1F1Regularized(a,b,z) + D*HypergeometricU(a,b,z)))),
    Variables(z, a, b, C, D),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Element(C, CC), Element(D, CC),
        Or(Equal(D, 0), NotEqual(z, 0), Element(-a, ZZGreaterEqual(0))))))

make_entry(ID("bb5d67"),
    Formula(Where(Equal(z * ComplexDerivative(y(z), For(z, z, 2)) + a * ComplexDerivative(y(z), For(z, z, 1)) - y(z), 0), Equal(y(z),
        C*Hypergeometric0F1Regularized(a,z) + D*z**(1-a)*Hypergeometric0F1Regularized(2-a,z)))),
    Variables(z, a, C, D),
    Assumptions(And(Element(a, CC), Element(z, CC), Element(C, CC), Element(D, CC),
        Or(NotEqual(z, 0), Element(1-a, ZZGreaterEqual(0))))))

make_entry(ID("c8fcc7"),
    Formula(Equal(HypergeometricUStar(a,b,z), z**a * HypergeometricU(a,b,z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), NotEqual(z, 0))))

make_entry(ID("4cf1e9"),
    Formula(Equal(HypergeometricUStar(a,b,z), Hypergeometric2F0(a, a-b+1, -(1/z)))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), NotEqual(z, 0))))

# todo: requires reciprocal gamma function
make_entry(ID("f7f84e"),
    Formula(Equal(Hypergeometric1F1Regularized(a,b,z),
        Div((-z)**(-a), Gamma(b-a)) * HypergeometricUStar(a,b,z) + Div(z**(a-b) * Exp(z), Gamma(a)) * HypergeometricUStar(b-a, b, -z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), NotEqual(z, 0))))

make_entry(ID("6cf802"),
    Formula(Equal(HypergeometricU(a,b,z),
        Gamma(1-b) / Gamma(a-b+1) * Hypergeometric1F1(a,b,z) + Gamma(b-1)/Gamma(a) * z**(1-b) * Hypergeometric1F1(a-b+1, 2-b, z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), NotEqual(z, 0), NotElement(b, ZZ))))

make_entry(ID("18ef23"),
    Formula(Equal(HypergeometricU(a,n,z),
        ComplexLimit(
        Gamma(1-b) / Gamma(a-b+1) * Hypergeometric1F1(a,b,z) + Gamma(b-1)/Gamma(a) * z**(1-b) * Hypergeometric1F1(a-b+1, 2-b, z),
            For(b, n)))),
    Variables(a, n, z),
    Assumptions(And(Element(a, CC), Element(n, ZZ), Element(z, CC), NotEqual(z, 0))))

make_entry(ID("2df3e3"),
    Formula(Equal(Hypergeometric0F1(a,z), Exp(-(2*Sqrt(z))) * Hypergeometric1F1(a-Div(1,2), 2*a-1, 4*Sqrt(z)))),
    Variables(a, z),
    Assumptions(And(Element(a, CC), Element(z, CC), NotElement(2*a, ZZLessEqual(1)))))

make_entry(ID("325a0e"),
    Formula(Equal(Hypergeometric0F1Regularized(a,z), (-z)**((1-a)/2) * BesselJ(a-1, 2*Sqrt(-z)))),
    Variables(a, z),
    Assumptions(And(Element(a, CC), Element(z, CC), NotEqual(z, 0))))

make_entry(ID("00dfd1"),
    Formula(Equal(Hypergeometric0F1Regularized(a,z), z**((1-a)/2) * BesselI(a-1, 2*Sqrt(z)))),
    Variables(a, z),
    Assumptions(And(Element(a, CC), Element(z, CC), NotEqual(z, 0))))

make_entry(ID("d1b3b5"),
    Formula(Equal(HypergeometricUStar(a,b,z),
        Sum(RisingFactorial(a,k) * RisingFactorial(a-b+1,k) / (Factorial(k) * (-z)**k), For(k, 0, n-1))
        + HypergeometricUStarRemainder(n,a,b,z))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), NotEqual(z,0), Element(n,ZZGreaterEqual(0)))))

make_entry(ID("99f69c"),
    SymbolDefinition(HypergeometricUStarRemainder, HypergeometricUStarRemainder(n,a,b,z), "Error term in asymptotic expansion of Tricomi confluent hypergeometric function"))

make_entry(ID("876844"),
    Formula(Equal(ComplexLimit(Abs(HypergeometricUStarRemainder(n,a,b, Exp(ConstI*theta) * z)), For(z, Infinity)), 0)),
    Variables(a,b,theta,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(theta, RR), Element(n,ZZGreaterEqual(1)))))

make_entry(ID("279e4f"),
    Formula(Where(LessEqual(Abs(HypergeometricUStarRemainder(n,a,b,z)), 
        Abs((RisingFactorial(a,n) * RisingFactorial(a-b+1,n)) / (Factorial(n) * z**n)) *
        (2 / (1 - sigma)) * Exp((2 * rho) / ((1 - sigma) * Abs(z)))),
        Equal(sigma, Abs(b-2*a)/Abs(z)),
        Equal(rho, Abs(a**2-a*b+b/2) + sigma*(1+sigma/4)/(1-sigma)**(2)))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), NotEqual(z,0), Element(n,ZZGreaterEqual(0)), Greater(Re(z), Abs(b-2*a)))),
    References("DLMF section 13.7, https://dlmf.nist.gov/13.7"))

make_entry(ID("461a54"),
    Formula(Where(LessEqual(Abs(HypergeometricUStarRemainder(n,a,b,z)),
        Abs((RisingFactorial(a,n) * RisingFactorial(a-b+1,n)) / (Factorial(n) * z**n)) *
        (2 * Sqrt(1 + Div(1,2)*Pi*n) / (1 - sigma)) * Exp((Pi * rho) / ((1 - sigma) * Abs(z)))),
        Equal(sigma, Abs(b-2*a)/Abs(z)),
        Equal(rho, Abs(a**2-a*b+b/2) + sigma*(1+sigma/4)/(1-sigma)**(2)))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), NotEqual(z,0), Element(n,ZZGreaterEqual(0)), Or(Greater(Abs(Im(z)), Abs(b-2*a)), Greater(Re(z), Abs(b-2*a))))),
    References("DLMF section 13.7, https://dlmf.nist.gov/13.7"))

make_entry(ID("7b91b4"),
    Formula(Where(LessEqual(Abs(HypergeometricUStarRemainder(n,a,b,z)),
        Abs((RisingFactorial(a,n) * RisingFactorial(a-b+1,n)) / (Factorial(n) * z**n)) *
        ((2 * C(n)) / (1 - tau) * Exp(2 * C(1) * rho / ((1 - tau) * Abs(z))))),
        Equal(sigma, Abs(b-2*a)/Abs(z)),
        Equal(nu, 1+2*sigma**2),
        Equal(tau, nu * sigma),
        Equal(rho, Abs(a**2-a*b+b/2) + tau*(1+tau/4)/(1-tau)**(2)),
        Equal(C(m), (Sqrt(1+Pi*m/2) + sigma*nu**2*m) * nu**m))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), NotEqual(z,0), Element(n,ZZGreaterEqual(0)), Greater(Abs(z), 2*Abs(b-2*a)))),
    References("DLMF section 13.7, https://dlmf.nist.gov/13.7"))

