# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Legendre polynomials"),
    Section("Particular values"),
    Entries(
        "9bdf22",
        "217521",
        "d77f0a",
        "9b7f05",
        "a17386",
        "13f971",
        "a7ac51",
        "3df748",
        "674afa",
        "85eebc",
    ),
    Section("Recurrence and functional equations"),
    Entries(
        "0010f3",
        "367ac2",
        "27688e",
        "925fdf",
    ),
    Section("Generating functions"),
    Entries(
        "d84519",
    ),
    Section("Rodrigues' formula"),
    Entries(
        "4cfeac",
    ),
    Section("Integrals"),
    Entries(
        "e36542",
    ),
    Section("Sum representations"),
    Entries(
        "c5dd9b",
        "f0569a",
        "7a85b7",
    ),
    Section("Hypergeometric representations"),
    Entries(
        "9395fc",
        "f55f0a",
        "3c87b9",
        "6cd4a1",
        "859445",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "1ba9a5",
        "155343",
        "ef4b53",
        "b786ad",
        "60ac50",
        "59e5df",
        "3b175b",
        "6476bd",
    ),
    Section("Analytic properties"),
    Entries(
        "40fa59",
        "d36fd7",
        "99e62f",
        "7680d3",
        "22a42f",
        "415911",
        "df439e",
        "0745ee",
        "b2d723",
    ),
    Section("Gauss-Legendre quadrature"),
    SeeTopics("Gaussian quadrature"),
    Entries(
        "ea4754",
        "47b181",
    ),
)

make_entry(ID("0010f3"),
    Formula(Equal(LegendrePolynomial(n,-z), (-1)**n * LegendrePolynomial(n,z))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0))), Element(z, CC)))

make_entry(ID("367ac2"),
    Formula(Equal((n+1)*LegendrePolynomial(n+1,z) - (2*n+1)*z*LegendrePolynomial(n,z) + n*LegendrePolynomial(n-1,z), 0)),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(1))), Element(z, CC)))

make_entry(ID("27688e"),
    Formula(Equal((1-z**2)*Derivative(LegendrePolynomial(n,z), Tuple(z,z,2)) - 2*z*Derivative(LegendrePolynomial(n,z), Tuple(z,z,1)) + n*(n+1)*LegendrePolynomial(n,z), 0)),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0))), Element(z, CC)))

make_entry(ID("925fdf"),
    Formula(Equal((1-z**2)*Derivative(LegendrePolynomial(n,z), Tuple(z,z,1)) + n*z*LegendrePolynomial(n,z) - n*LegendrePolynomial(n-1,z), 0)),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(1))), Element(z, CC)))

make_entry(ID("9bdf22"),
    Formula(Equal(LegendrePolynomial(0,z), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("217521"),
    Formula(Equal(LegendrePolynomial(1,z), z)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("d77f0a"),
    Formula(Equal(LegendrePolynomial(2,z), Div(1,2)*(3*z**2 - 1))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("9b7f05"),
    Formula(Equal(LegendrePolynomial(3,z), Div(1,2)*(5*z**3 - 3*z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("a17386"),
    Formula(Equal(LegendrePolynomial(4,z), Div(1,8)*(35*z**4 - 30*z**2 + 3))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("13f971"),
    Formula(Equal(LegendrePolynomial(5,z), Div(1,8)*(63*z**5 - 70*z**3 + 15*z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("a7ac51"),
    Formula(Equal(LegendrePolynomial(n,1), 1)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("3df748"),
    Formula(Equal(LegendrePolynomial(n,-1), (-1)**n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("674afa"),
    Formula(Equal(LegendrePolynomial(2*n,0), ((-1)**n / 4**n) * Binomial(2*n,n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("85eebc"),
    Formula(Equal(LegendrePolynomial(2*n+1,0), 0)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("d84519"),
    Formula(Equal(Sum(LegendrePolynomial(n,x) * z**n, Tuple(n, 0, Infinity)),
        1 / Sqrt(1 - 2*x*z + z**2))),
    Variables(x, z),
    Assumptions(And(Element(x, ClosedInterval(-1,1)), Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("4cfeac"),
    Formula(Equal(LegendrePolynomial(n,z),
        Div(1,2**n * Factorial(n)) * Derivative((t**2-1)**n, Tuple(t, z, n)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0))), Element(z, CC)))

make_entry(ID("e36542"),
    Formula(Equal(Integral(LegendrePolynomial(n, x) * LegendrePolynomial(m, x), Tuple(x, -1, 1)), Div(2,2*n+1) * KroneckerDelta(n, m))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))))



make_entry(ID("c5dd9b"),
    Formula(Equal(LegendrePolynomial(n, z), Div(1,2**n) * Sum(Binomial(n,k)**2 * (z-1)**(n-k) * (z+1)**k, Tuple(k, 0, n)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("f0569a"),
    Formula(Equal(LegendrePolynomial(n, z), Sum(Binomial(n,k) * Binomial(n+k,k) * Div(z-1,2)**k, Tuple(k, 0, n)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("7a85b7"),
    Formula(Equal(LegendrePolynomial(n, z), Div(1,2**n) * Sum((-1)**k * Binomial(n,k) * Binomial(2*n-2*k,n) * z**(n-2*k), Tuple(k, 0, Floor(n/2))))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("9395fc"),
    Formula(Equal(LegendrePolynomial(n, z), Hypergeometric2F1(-n, n+1, 1, (1-z)/2))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("f55f0a"),
    Formula(Equal(LegendrePolynomial(n, z), Binomial(2*n,n) * (z/2)**n * Hypergeometric2F1(-(n/2), (1-n)/2, Div(1,2)-n, 1/z**2))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, SetMinus(CC, Set(0))))))

make_entry(ID("3c87b9"),
    Formula(Equal(LegendrePolynomial(n, z), Div(z-1,2)**n * Hypergeometric2F1(-n, -n, 1, (z+1)/(z-1)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, SetMinus(CC, Set(1))))))

make_entry(ID("6cd4a1"),
    Formula(Equal(LegendrePolynomial(2*n, z), Div((-1)**n, 4**n) * Binomial(2*n,n) * Hypergeometric2F1(-n, n+Div(1,2), Div(1,2), z**2))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, SetMinus(CC)))))

make_entry(ID("859445"),
    Formula(Equal(LegendrePolynomial(2*n+1, z), Div((-1)**n, 4**n) * (2*n+1) * Binomial(2*n,n) * z * Hypergeometric2F1(-n, n+Div(3,2), Div(3,2), z**2))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, SetMinus(CC)))))

make_entry(ID("1ba9a5"),
    Formula(LessEqual(Abs(LegendrePolynomial(n,x)), 1)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), LessEqual(-1, x, 1))))

# todo: also valid on CC?
make_entry(ID("155343"),
    Formula(LessEqual(Abs(LegendrePolynomial(n,x)), 2*BesselI(0,2*n*Sqrt(Abs(x-1)/2)), 2*Exp(2*n*Sqrt(Abs(x-1)/2)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, RR))))

make_entry(ID("ef4b53"),
    Formula(LessEqual(Abs(LegendrePolynomial(n,z)), Abs(LegendrePolynomial(n, Abs(z)*ConstI)), (Abs(z)+Sqrt(1+Abs(z)**2))**n)),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("b786ad"),
    Formula(LessEqual(Abs(Derivative(LegendrePolynomial(n,x), Tuple(x, x, 1))), (n*(n+1))/2)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), LessEqual(-1, x, 1))))

make_entry(ID("60ac50"),
    Formula(LessEqual(Abs(Derivative(LegendrePolynomial(n,x), Tuple(x, x, 1))), (2**Div(3,2) / Sqrt(ConstPi)) * (n**Div(1,2) / (1 - x**2)**Div(3,4)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Less(-1, x, 1))))

make_entry(ID("59e5df"),
    Formula(LessEqual(Abs(Derivative(LegendrePolynomial(n,x), Tuple(x, x, 2))), ((n-1)*n*(n+1)*(n+2))/8)),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), LessEqual(-1, x, 1))))

make_entry(ID("3b175b"),
    Formula(LessEqual(Abs(Derivative(LegendrePolynomial(n,x), Tuple(x, x, 2))), (2**Div(5,2) / Sqrt(ConstPi)) * (n**Div(3,2) / (1 - x**2)**Div(5,4)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Less(-1, x, 1))))

make_entry(ID("6476bd"),
    Formula(LessEqual(Abs(Derivative(LegendrePolynomial(n,x), Tuple(x, x, r))), (2**(r+Div(1,2)) / Sqrt(ConstPi)) * (n**(r-Div(1,2)) / (1 - x**2)**((2*n+1)/4)))),
    Variables(n, r, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(r, ZZGreaterEqual(0)), Less(-1, x, 1))))

make_entry(ID("40fa59"),
    Formula(Equal(HolomorphicDomain(LegendrePolynomial(n,z), z, Union(CC, Set(UnsignedInfinity))), CC)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("d36fd7"),
    Formula(Equal(Poles(LegendrePolynomial(n,z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("99e62f"),
    Formula(Equal(EssentialSingularities(LegendrePolynomial(n,z), z, Union(CC, Set(UnsignedInfinity))), Set())),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("7680d3"),
    Formula(Equal(BranchPoints(LegendrePolynomial(n,z), z, Union(CC, Set(UnsignedInfinity))), Set())),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("22a42f"),
    Formula(Equal(BranchCuts(LegendrePolynomial(n,z), z, CC), Set())),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("415911"),
    Formula(Equal(Cardinality(Zeros(LegendrePolynomial(n,z), z, Element(z, CC))), n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("df439e"),
    Formula(Subset(Zeros(LegendrePolynomial(n,z), z, Element(z, CC)), OpenInterval(-1,1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("0745ee"),
    Formula(Equal(Zeros(LegendrePolynomial(n,z), z, Element(z, CC)), SetBuilder(LegendrePolynomialZero(n,k), k, Element(k, ZZBetween(1, n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("b2d723"),
    Formula(Equal(LegendrePolynomial(n, Conjugate(z)), Conjugate(LegendrePolynomial(n, z)))),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

