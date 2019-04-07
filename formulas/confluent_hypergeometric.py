from .expr import *

def_Topic(
    Title("Confluent hypergeometric functions"),
    Section("Differential equations"),
    Entries(
        "06f229",
        "bb5d67",
    ),
    Section("Kummer's transformation"),
    Entries(
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
        "876844",
        "279e4f",
        "461a54",
        "7b91b4",
    ),
)

make_entry(ID("a047eb"),
    Formula(Equal(Hypergeometric1F1Regularized(a,b,z), Exp(z) * Hypergeometric1F1Regularized(b-a, b, -z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC))))

make_entry(ID("9d3147"),
    Formula(Equal(HypergeometricU(a,b,z), z**(1-b) * HypergeometricU(1+a-b, 2-b, z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Unequal(z, 0))))

make_entry(ID("06f229"),
    Formula(Where(Equal(z * Derivative(y(z), Tuple(z, z, 2)) + (b-z) * Derivative(y(z), Tuple(z, z, 1)) - a*y(z), 0), Equal(y(z),
        C*Hypergeometric1F1Regularized(a,b,z) + D*HypergeometricU(a,b,z)))),
    Variables(z, a, b, C, D),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Element(C, CC), Element(D, CC),
        Or(Equal(D, 0), Unequal(z, 0), Element(-a, ZZGreaterEqual(0))))))

make_entry(ID("bb5d67"),
    Formula(Where(Equal(z * Derivative(y(z), Tuple(z, z, 2)) + a * Derivative(y(z), Tuple(z, z, 1)) - y(z), 0), Equal(y(z),
        C*Hypergeometric0F1Regularized(a,z) + D*z**(1-a)*Hypergeometric0F1Regularized(2-a,z)))),
    Variables(z, a, C, D),
    Assumptions(And(Element(a, CC), Element(z, CC), Element(C, CC), Element(D, CC),
        Or(Equal(D, 0), Unequal(z, 0), Element(1-a, ZZGreaterEqual(0))))))

make_entry(ID("c8fcc7"),
    Formula(Equal(HypergeometricUStar(a,b,z), z**a * HypergeometricU(a,b,z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Unequal(z, 0))))

make_entry(ID("4cf1e9"),
    Formula(Equal(HypergeometricUStar(a,b,z), Hypergeometric2F0(a, a-b+1, -(1/z)))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Unequal(z, 0))))

# todo: requires reciprocal gamma function
make_entry(ID("f7f84e"),
    Formula(Equal(Hypergeometric1F1Regularized(a,b,z),
        Div((-z)**(-a), GammaFunction(b-a)) * HypergeometricUStar(a,b,z) + Div(z**(a-b) * Exp(z), GammaFunction(a)) * HypergeometricUStar(b-a, b, -z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Unequal(z, 0))))

make_entry(ID("6cf802"),
    Formula(Equal(HypergeometricU(a,b,z),
        GammaFunction(1-b) / GammaFunction(a-b+1) * Hypergeometric1F1(a,b,z) + GammaFunction(b-1)/GammaFunction(a) * z**(1-b) * Hypergeometric1F1(a-b+1, 2-b, z))),
    Variables(a, b, z),
    Assumptions(And(Element(a, CC), Element(b, CC), Element(z, CC), Unequal(z, 0), NotElement(b, ZZ))))

make_entry(ID("18ef23"),
    Formula(Equal(HypergeometricU(a,n,z),
        Limit(
        GammaFunction(1-b) / GammaFunction(a-b+1) * Hypergeometric1F1(a,b,z) + GammaFunction(b-1)/GammaFunction(a) * z**(1-b) * Hypergeometric1F1(a-b+1, 2-b, z),
            b, n))),
    Variables(a, n, z),
    Assumptions(And(Element(a, CC), Element(n, ZZ), Element(z, CC), Unequal(z, 0))))

make_entry(ID("2df3e3"),
    Formula(Equal(Hypergeometric0F1(a,z), Exp(-(2*Sqrt(z))) * Hypergeometric1F1(a-Div(1,2), 2*a-1, 4*Sqrt(z)))),
    Variables(a, z),
    Assumptions(And(Element(a, CC), Element(z, CC), NotElement(a, ZZLessEqual(0)))))

make_entry(ID("325a0e"),
    Formula(Equal(Hypergeometric0F1Regularized(a,z), (-z)**((1-a)/2) * BesselJ(a-1, 2*Sqrt(-z)))),
    Variables(a, z),
    Assumptions(And(Element(a, CC), Element(z, CC), Unequal(z, 0))))

make_entry(ID("00dfd1"),
    Formula(Equal(Hypergeometric0F1Regularized(a,z), z**((1-a)/2) * BesselI(a-1, 2*Sqrt(z)))),
    Variables(a, z),
    Assumptions(And(Element(a, CC), Element(z, CC), Unequal(z, 0))))

make_entry(ID("d1b3b5"),
    Formula(Equal(HypergeometricUStar(a,b,z),
        Sum(RisingFactorial(a,k) * RisingFactorial(a-b+1,k) / (Factorial(k) * (-z)**k), Tuple(k, 0, n-1))
        + HypergeometricUStarRemainder(n,a,b,z))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), Unequal(z,0), Element(n,ZZGreaterEqual(0)))))

make_entry(ID("876844"),
    Formula(Equal(Limit(Abs(HypergeometricUStarRemainder(n,a,b, Exp(ConstI*theta) * z)), z, Infinity), 0)),
    Variables(a,b,theta,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(theta, RR), Element(n,ZZGreaterEqual(1)))))

make_entry(ID("279e4f"),
    Formula(Where(LessEqual(Abs(HypergeometricUStarRemainder(n,a,b,z)), 
        Abs((RisingFactorial(a,n) * RisingFactorial(a-b+1,n)) / (Factorial(n) * z**n)) *
        (2 / (1 - sigma)) * Exp((2 * rho) / ((1 - sigma) * Abs(z)))),
        Equal(sigma, Abs(b-2*a)/Abs(z)),
        Equal(rho, Abs(a**2-a*b+b/2) + sigma*(1+sigma/4)/(1-sigma)**(2)))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), Unequal(z,0), Element(n,ZZGreaterEqual(0)), Greater(Re(z), Abs(b-2*a)))),
    References("DLMF section 13.7, https://dlmf.nist.gov/13.7"))

make_entry(ID("461a54"),
    Formula(Where(LessEqual(Abs(HypergeometricUStarRemainder(n,a,b,z)),
        Abs((RisingFactorial(a,n) * RisingFactorial(a-b+1,n)) / (Factorial(n) * z**n)) *
        (2 * Sqrt(1 + Div(1,2)*ConstPi*n) / (1 - sigma)) * Exp((ConstPi * rho) / ((1 - sigma) * Abs(z)))),
        Equal(sigma, Abs(b-2*a)/Abs(z)),
        Equal(rho, Abs(a**2-a*b+b/2) + sigma*(1+sigma/4)/(1-sigma)**(2)))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), Unequal(z,0), Element(n,ZZGreaterEqual(0)), Or(Greater(Abs(Im(z)), Abs(b-2*a)), Greater(Re(z), Abs(b-2*a))))),
    References("DLMF section 13.7, https://dlmf.nist.gov/13.7"))

make_entry(ID("7b91b4"),
    Formula(Where(LessEqual(Abs(HypergeometricUStarRemainder(n,a,b,z)),
        Abs((RisingFactorial(a,n) * RisingFactorial(a-b+1,n)) / (Factorial(n) * z**n)) *
        ((2 * C(n)) / (1 - tau) * Exp(2 * C(1) * rho / ((1 - tau) * Abs(z))))),
        Equal(sigma, Abs(b-2*a)/Abs(z)),
        Equal(nu, 1+2*sigma**2),
        Equal(tau, nu * sigma),
        Equal(rho, Abs(a**2-a*b+b/2) + tau*(1+tau/4)/(1-tau)**(2)),
        Equal(C(m), (Sqrt(1+ConstPi*m/2) + sigma*nu**2*m) * nu**m))),
    Variables(a,b,z,n),
    Assumptions(And(Element(a,CC), Element(b,CC), Element(z,CC), Unequal(z,0), Element(n,ZZGreaterEqual(0)), Greater(Abs(z), 2*Abs(b-2*a)))),
    References("DLMF section 13.7, https://dlmf.nist.gov/13.7"))

