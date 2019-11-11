# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Illustrations of Eisenstein series"),
    SeeTopics("Eisenstein series"),
    Section("X-ray plots"),
    Entries(
        "7e1850",
        "dac0bb",
        "54951a",
        "356d7a",
        "626026",
        "a14cfc",
    ),
)

def_Topic(
    Title("Eisenstein series"),
    Section("Definitions"),
    Entries(
        "9bb960",
        "df3334",
    ),
    Section("Illustrations"),
    SeeTopics("Illustrations of Eisenstein series"),
    Entries(
        "54951a",
    ),
    Section("Normalization"),
    Entries(
        "0a2120",
    ),
    Section("Lattice series"),
    Entries(
        "2246a7",
        "c1ffd4",
        "b07750",
    ),
    Section("Modular transformations"),
    Entries(
        "0b5b04",
        "8ffe07",
        "23a5e0",
        "d56eb6",
    ),
    Subsection("Quasi-modular transformations for weight 2"),
    Entries(
        "5161ab",
        "7f4c85",
    ),
    Subsection("Weight 2 quasi-holomorphic modular form"),
    Entries(
        "b1a5e4",
    ),
    Section("Fourier series (q-series)"),
    Subsection("First cases"),
    Entries(
        "10cdf4",
        "f8dfaf",
        "e20db0",
    ),
    Subsection("General case"),
    Entries(
        "7c00e6",
        "848d97",
        "15b347",
    ),
    Section("Trigonometric series"),
    Entries(
        "18a4d1",
        "7b62e4",
        "a92c1a",
        "171724",
    ),
    Section("Theta function representations"),
    Entries(
        "cc579c",
        "10f3b2",
        "6d2880",
        "a0dff6",
        "bd7d8e",
    ),
    Section("Dedekind eta function representations"),
    Entries(
        "dbf388",
        "03ad5a",
        "4da2cd",
        "0a5ef4",
    ),
    Section("Elliptic function representations"),
    Entries(
        "b52b6f",
        "3bf702",
    ),
    Section("Products and recurrence relations"),
    Entries(
        "044128",
        "adaf5a",
        "e60fd4",
        "9e1f83",
        "feb95e",
        "36fff2",
        "5540a1",
    ),
    Section("Generating functions"),
    Entries(
        "9bf0ad",
        "3e84e3",
    ),
    Section("Derivatives"),
    Entries(
        "7cda09",
        "af2ea9",
        "3bfced",
    ),
    Section("Specific values"),
    Subsection("Fourth root of unity"),
    Entries(
        "570399",
        "a691b3",
        "e03b7c",
        "53fcdd",
        "a4109c",
    ),
    Subsection("Third root of unity"),
    Entries(
        "9ea739",
        "30a054",
        "3102a7",
        "0fda1b",
        "6c71c0",
    ),
    Subsection("Infinity"),
    Entries(
        "c6be24",
        "ad9ba2",
    ),
    Section("Zeros"),
    Subsection("Distribution"),
    Entries(
        "e46697",
        "2f6805",
        "a50278",
        "13cac5",
        "097efc",
    ),
    Subsection("Specific values"),
    Entries(
        "4a200a",
        "ec4f56",
        "83566f",
        "26faf3",
        "6ae250",
        "ad91ae",
    ),
    Subsection("Weight 2 series"),
    Entries(
        "cae067",
        "f33f09",
        "67f2ef",
        "be9790",
    ),
)

# Definitions

make_entry(ID("9bb960"),
    SymbolDefinition(EisensteinG, EisensteinG(k,tau), "Eisenstein series"),
    Description("The Eisenstein series", EisensteinG(k,tau), "is defined for even integers", GreaterEqual(k, 2), "and", tau, "in the upper half-plane."),
    Description("The functions", EisensteinG(k,tau), "and", EisensteinE(k,tau), "are the same up to a normalizing factor."))

make_entry(ID("df3334"),
    SymbolDefinition(EisensteinE, EisensteinE(k,tau), "Normalized Eisenstein series"),
    Description("The normalized Eisenstein series", EisensteinE(k,tau), "is defined for even integers", GreaterEqual(k, 2), "and", tau, "in the upper half-plane."),
    Description("The functions", EisensteinG(k,tau), "and", EisensteinE(k,tau), "are the same up to a normalizing factor."))

# Illustrations

make_entry(ID("7e1850"),
    Image(Description("X-ray of", EisensteinE(2, tau), "on", Element(tau, ClosedInterval(-1,1) + ClosedInterval(0,2)*ConstI), "with", ModularGroupFundamentalDomain, "highlighted"),
        ImageSource("xray_eisenstein_e2")),
    description_xray)

make_entry(ID("dac0bb"),
    Image(Description("X-ray of", EisensteinE(4, tau), "on", Element(tau, ClosedInterval(-1,1) + ClosedInterval(0,2)*ConstI), "with", ModularGroupFundamentalDomain, "highlighted"),
        ImageSource("xray_eisenstein_e4")),
    description_xray)

make_entry(ID("54951a"),
    Image(Description("X-ray of", EisensteinE(6, tau), "on", Element(tau, ClosedInterval(-1,1) + ClosedInterval(0,2)*ConstI), "with", ModularGroupFundamentalDomain, "highlighted"),
        ImageSource("xray_eisenstein_e6")),
    description_xray)

make_entry(ID("356d7a"),
    Image(Description("X-ray of", EisensteinE(8, tau), "on", Element(tau, ClosedInterval(-1,1) + ClosedInterval(0,2)*ConstI), "with", ModularGroupFundamentalDomain, "highlighted"),
        ImageSource("xray_eisenstein_e8")),
    description_xray)

make_entry(ID("626026"),
    Image(Description("X-ray of", EisensteinE(10, tau), "on", Element(tau, ClosedInterval(-1,1) + ClosedInterval(0,2)*ConstI), "with", ModularGroupFundamentalDomain, "highlighted"),
        ImageSource("xray_eisenstein_e10")),
    description_xray)

make_entry(ID("a14cfc"),
    Image(Description("X-ray of", EisensteinE(12, tau), "on", Element(tau, ClosedInterval(-1,1) + ClosedInterval(0,2)*ConstI), "with", ModularGroupFundamentalDomain, "highlighted"),
        ImageSource("xray_eisenstein_e12")),
    description_xray)

# Normalization

make_entry(ID("0a2120"),
    Formula(Equal(EisensteinE(2*k, tau), EisensteinG(2*k, tau) / (2*RiemannZeta(2*k)))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

# Lattice series

# todo: Cartesian power

make_entry(ID("2246a7"),
    Formula(Equal(EisensteinG(2*k, tau), Sum(1/(m*tau+n)**(2*k),
        ForElement(Tuple(m, n), SetMinus(Pow(ZZ, 2), Set(Tuple(0, 0))))))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(2)), Element(tau, HH))))

make_entry(ID("c1ffd4"),
    Formula(Equal(EisensteinG(2*k, tau), RiemannZeta(2*k) * Sum(1/(m*tau+n)**(2*k),
        ForElement(Tuple(m, n), SetMinus(Pow(ZZ, 2), Set(Tuple(0, 0)))), Equal(GCD(m,n),1)))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(2)), Element(tau, HH))))

make_entry(ID("b07750"),
    Formula(Equal(EisensteinG(2*k, tau), 2 * RiemannZeta(2*k) + 2 * Sum(Sum(1/(m*tau+n)**(2*k), ForElement(n, ZZ)), For(m, 1, Infinity)))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

# Modular transformations

make_entry(ID("0b5b04"),
    Formula(Equal(EisensteinG(2*k, (a*tau+b)/(c*tau+d)), (c*tau+d)**(2*k) * EisensteinG(2*k, tau))),
    Variables(k,tau,a,b,c,d),
    Assumptions(And(Element(k, ZZGreaterEqual(2)), Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

make_entry(ID("8ffe07"),
    Formula(Equal(EisensteinE(2*k, (a*tau+b)/(c*tau+d)), (c*tau+d)**(2*k) * EisensteinE(2*k, tau))),
    Variables(k,tau,a,b,c,d),
    Assumptions(And(Element(k, ZZGreaterEqual(2)), Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

make_entry(ID("23a5e0"),
    Formula(Equal(EisensteinG(2*k, tau+n), EisensteinG(2*k, tau))),
    Variables(k,n,tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("d56eb6"),
    Formula(Equal(EisensteinE(2*k, tau+n), EisensteinE(2*k, tau))),
    Variables(k,n,tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH), Element(n, ZZ))))

make_entry(ID("5161ab"),
    Formula(Equal(EisensteinG(2, (a*tau+b)/(c*tau+d)), (c*tau+d)**2 * EisensteinG(2, tau) - 2 * Pi * ConstI * c * (c*tau+d))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

make_entry(ID("7f4c85"),
    Formula(Equal(EisensteinE(2, (a*tau+b)/(c*tau+d)), (c*tau+d)**2 * EisensteinE(2, tau) - ((6 * ConstI) / Pi) * c * (c*tau+d))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

make_entry(ID("b1a5e4"),
    Formula(Where(Equal(H((a*tau+b)/(c*tau+d)), (c*tau+d)**2 * H(tau)), Equal(H(tau), EisensteinG(2,tau) - Pi/Im(tau)))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

# Fourier series (q-series)

make_entry(ID("10cdf4"),
    Formula(Equal(EisensteinE(2, tau), Where(1 - 24 * Sum(DivisorSigma(1, n) * q**n, For(n, 1, Infinity)), Equal(q, Exp(2*Pi*ConstI*tau))))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

make_entry(ID("f8dfaf"),
    Formula(Equal(EisensteinE(4, tau), Where(1 + 240 * Sum(DivisorSigma(3, n) * q**n, For(n, 1, Infinity)), Equal(q, Exp(2*Pi*ConstI*tau))))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

make_entry(ID("e20db0"),
    Formula(Equal(EisensteinE(6, tau), Where(1 - 504 * Sum(DivisorSigma(5, n) * q**n, For(n, 1, Infinity)), Equal(q, Exp(2*Pi*ConstI*tau))))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

make_entry(ID("7c00e6"),
    Formula(Equal(EisensteinE(2*k, tau), Where(1 - (4*n)/BernoulliB(2*n) * Sum(DivisorSigma(2*k-1, n) * q**n, For(n, 1, Infinity)), Equal(q, Exp(2*Pi*ConstI*tau))))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

make_entry(ID("848d97"),
    Formula(Equal(EisensteinE(2*k, tau), Where(1 - (4*n)/BernoulliB(2*n) * Sum(n**(2*k-1) * q**n / (1 - q**n), For(n, 1, Infinity)), Equal(q, Exp(2*Pi*ConstI*tau))))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

make_entry(ID("15b347"),
    Formula(Equal(EisensteinE(2*k, tau), Where(1 - (4*n)/BernoulliB(2*n) *
        Sum(Sum(n**(2*k-1) * q**(m*n), For(m, 1, Infinity)), For(n, 1, Infinity)), Equal(q, Exp(2*Pi*ConstI*tau))))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(1)), Element(tau, HH))))

# Trigonometric series

make_entry(ID("18a4d1"),
    Formula(Equal(EisensteinE(2, tau), 1 + 6 * Sum(1/Sin(Pi * m * tau)**2, For(m, 1, Infinity)))),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))

make_entry(ID("7b62e4"),
    Formula(Equal(EisensteinE(2, tau), 1 - 12 * Sum(1/(Cos(2 * Pi * m * tau) - 1), For(m, 1, Infinity)))),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))


make_entry(ID("a92c1a"),
    Formula(Equal(EisensteinE(4, tau), 1 + 30 * Sum((Cos(Pi*m*tau)**2 + 1)/Sin(Pi*m*tau)**4, For(m, 1, Infinity)))),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))

make_entry(ID("171724"),
    Formula(Equal(EisensteinE(6, tau), 1 + 63 * Sum((2 * Cos(Pi*m*tau)**4 + 11 * Cos(Pi*m*tau)**2 + 2)/Sin(Pi*m*tau)**6, For(m, 1, Infinity)))),
    Variables(tau),
    Assumptions(And(Element(tau, HH))))

# Theta function representations

_a = JacobiTheta(2,0,tau)
_b = JacobiTheta(3,0,tau)
_c = JacobiTheta(4,0,tau)

make_entry(ID("cc579c"),
    Formula(Equal(EisensteinE(4, tau), Div(1,2) * (_a**8 + _b**8 + _c**8))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("10f3b2"),
    Formula(Equal(EisensteinE(6, tau), Div(1,2) * (_b**12 + _c**12 - 3*_a**8*(_b**4+_c**4)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("6d2880"),
    Formula(Equal(EisensteinE(8, tau), Div(1,2) * (_a**16 + _b**16 + _c**16))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("a0dff6"),
    Formula(Equal(EisensteinE(6, tau)**2, Div(1,8) * ((_a**8 + _b**8 + _c**8)**3 - 54*(_a*_b*_c)**8))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("bd7d8e"),
    Formula(Equal(EisensteinE(4, tau)**3 - EisensteinE(6, tau)**2, Div(27,4) * (_a*_b*_c)**8)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Dedekind eta function representations

make_entry(ID("dbf388"),
    Formula(Equal(EisensteinG(2, tau), -((4*Pi*ConstI) * (ComplexDerivative(DedekindEta(tau), For(tau, tau)) / DedekindEta(tau))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("03ad5a"),
    Formula(Equal(EisensteinE(2, tau), -((12*ConstI)/Pi * (ComplexDerivative(DedekindEta(tau), For(tau, tau)) / DedekindEta(tau))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("4da2cd"),
    Formula(Equal(EisensteinE(4, tau), DedekindEta(tau)**16/DedekindEta(2*tau)**8 + 256 * (DedekindEta(2*tau)**16 / DedekindEta(tau)**8))),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References("K. Ono (2004), Web of Modularity: Arithmetic of the Coefficients of Modular Forms and q-series, American Mathematical Society. Theorem 1.67."))

make_entry(ID("0a5ef4"),
    Formula(Equal(EisensteinE(6, tau), DedekindEta(tau)**24/DedekindEta(2*tau)**12 - 480 * DedekindEta(2*tau)**12
        - 16896 * (DedekindEta(2*tau)**12 * DedekindEta(4*tau)**8 / DedekindEta(tau)**8) + 8192 * (DedekindEta(4*tau)**24 / DedekindEta(2*tau)**12))),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References("K. Ono (2004), Web of Modularity: Arithmetic of the Coefficients of Modular Forms and q-series, American Mathematical Society. Theorem 1.67."))

# Eliptic function representations

make_entry(ID("b52b6f"),
    Formula(Equal(EisensteinG(2, tau), 2 * WeierstrassZeta(Div(1,2), tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("3bf702"),
    Formula(Equal(EisensteinE(2, tau), (6 / Pi**2) * WeierstrassZeta(Div(1,2), tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Products and recurrence relations

make_entry(ID("044128"),
    Formula(Equal(EisensteinE(8, tau), EisensteinE(4, tau)**2)),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("adaf5a"),
    Formula(Equal(EisensteinE(10, tau), EisensteinE(4, tau) * EisensteinE(6, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("e60fd4"),
    Formula(Equal(EisensteinE(14, tau), EisensteinE(4, tau)**2 * EisensteinE(6, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("9e1f83"),
    Formula(Equal(EisensteinE(14, tau), EisensteinE(4, tau) * EisensteinE(10, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("feb95e"),
    Formula(Equal(EisensteinE(14, tau), EisensteinE(6, tau) * EisensteinE(8, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("36fff2"),
    Formula(Equal(EisensteinE(12, tau), Div(1,691) * (441*EisensteinE(4,tau)**3 + 250*EisensteinE(6,tau)**2))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# todo: alt. forms?
make_entry(ID("5540a1"),
    Formula(Equal(EisensteinG(2*k,tau), (3 / ((2*k+1)*(k-3)*(2*k-1)))*Sum((2*r-1)*(2*k-2*r-1)*EisensteinG(2*r,tau)*EisensteinG(2*k-2*r,tau), For(r, 2, k-2)))),
    Variables(k, tau),
    Assumptions(And(Element(k, ZZGreaterEqual(4)), Element(tau, HH))),
    References("T. Apostol (1976), Modular Functions and Dirichlet Series in Number Theory, Springer. Theorem 1.13."))

# Generating functions

make_entry(ID("9bf0ad"),
    Formula(Equal(WeierstrassP(z, tau), 1/z**2 + Sum((2*k+1)*EisensteinG(2*k+2,tau) * z**(2*k), For(k, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), Less(Abs(z), 
        Infimum(Set(Abs(s), ForElement(s, SetMinus(Lattice(1, tau), Set(0)))))))))

make_entry(ID("3e84e3"),
    Formula(Equal(WeierstrassZeta(z, tau), 1/z - Sum(EisensteinG(2*k+2,tau) * z**(2*k+1), For(k, 1, Infinity)))),
    Variables(z, tau),
    Assumptions(And(Element(z, CC), Element(tau, HH), Less(Abs(z), 
        Infimum(Set(Abs(s), ForElement(s, SetMinus(Lattice(1, tau), Set(0)))))))))

# Derivatives

__ref = "B. C. Berndt and A. J. Yee (2002) Ramanujan's Contributions to Eisenstein Series, Especially in His Lost Notebook. In: Kanemitsu S., Jia C. (eds) Number Theoretic Methods. Developments in Mathematics, vol 8. Springer, Boston, MA. https://doi.org/10.1007/978-1-4757-3675-5_3"

make_entry(ID("7cda09"),
    Formula(Equal(ComplexDerivative(EisensteinE(2, tau), For(tau, tau)),
        2 * Pi * ConstI * Parentheses((EisensteinE(2,tau)**2 - EisensteinE(4,tau)) / 12))),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References(__ref))

make_entry(ID("af2ea9"),
    Formula(Equal(ComplexDerivative(EisensteinE(4, tau), For(tau, tau)),
        2 * Pi * ConstI * Parentheses((EisensteinE(2,tau)*EisensteinE(4,tau) - EisensteinE(6,tau)) / 3))),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References(__ref))

make_entry(ID("3bfced"),
    Formula(Equal(ComplexDerivative(EisensteinE(6, tau), For(tau, tau)),
        2 * Pi * ConstI * Parentheses((EisensteinE(2,tau)*EisensteinE(6,tau) - EisensteinE(4,tau)**2) / 2))),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References(__ref))

# Specific values

make_entry(ID("570399"),
    Formula(Equal(EisensteinG(2, ConstI), Pi)))

make_entry(ID("9ea739"),
    Formula(Equal(EisensteinG(2, Exp(2*Pi*ConstI/3)), 2*Pi/Sqrt(3))))

make_entry(ID("a691b3"),
    Formula(Equal(EisensteinE(2, ConstI), 3/Pi)))

make_entry(ID("30a054"),
    Formula(Equal(EisensteinE(2, Exp(2*Pi*ConstI/3)), (2*Sqrt(3))/Pi)))


make_entry(ID("e03b7c"),
    Formula(Equal(EisensteinG(4, ConstI), Gamma(Div(1,4))**8 / (960 * Pi**2))))

make_entry(ID("53fcdd"),
    Formula(Equal(EisensteinE(4, ConstI), (3 * Gamma(Div(1,4))**8) / (64 * Pi**6))))

make_entry(ID("3102a7"),
    Formula(Equal(EisensteinG(4, Exp(2*Pi*ConstI/3)), EisensteinE(4, Exp(2*Pi*ConstI/3)), 0)))

make_entry(ID("0fda1b"),
    Formula(Equal(EisensteinG(6, Exp(2*Pi*ConstI/3)), (Gamma(Div(1,3))**18) / (8960 * Pi**6))))

make_entry(ID("6c71c0"),
    Formula(Equal(EisensteinE(6, Exp(2*Pi*ConstI/3)), (27*Gamma(Div(1,3))**18) / (512 * Pi**12))))

make_entry(ID("a4109c"),
    Formula(Equal(EisensteinG(6, ConstI), EisensteinE(6, ConstI), 0)))

make_entry(ID("c6be24"),
    Formula(Equal(EisensteinG(2*k, ConstI*Infinity), ComplexLimit(EisensteinG(2*k, tau), For(tau, ConstI*Infinity)), 2 * RiemannZeta(2*k))),
    Variables(k),
    Assumptions(And(Element(k, ZZGreaterEqual(1)))))

make_entry(ID("ad9ba2"),
    Formula(Equal(EisensteinE(2*k, ConstI*Infinity), ComplexLimit(EisensteinE(2*k, tau), For(tau, ConstI*Infinity)), 1)),
    Variables(k),
    Assumptions(And(Element(k, ZZGreaterEqual(1)))))

# Zeros

make_entry(ID("e46697"),
    Formula(Equal(Zeros(EisensteinE(2*k, tau), ForElement(tau, HH)),
        Set(ModularGroupAction(gamma, tau), For(Tuple(gamma, tau)), And(Element(tau, Zeros(EisensteinE(2*k, z), ForElement(z, ModularGroupFundamentalDomain))), Element(gamma, PSL2Z))))),
    Variables(k),
    Assumptions(And(Element(k, ZZGreaterEqual(2)))))

make_entry(ID("2f6805"),
    #Formula(Implies(And(Element(tau, ModularGroupFundamentalDomain), Equal(EisensteinE(2*k, tau), 0)), Equal(Abs(tau), 1))),
    #Variables(tau,k),
    #Assumptions(And(Element(k, ZZGreaterEqual(2)), Element(tau, HH))),
    Formula(Subset(Zeros(EisensteinE(2*k, tau), ForElement(tau, ModularGroupFundamentalDomain)), Set(Exp(ConstI*theta), ForElement(theta, ClosedInterval(Pi/2, 2*Pi/3))))),
    Variables(k),
    Assumptions(And(Element(k, ZZGreaterEqual(2)))),
    References("F. K. C. Rankin and H. P. F. Swinnerton-Dyer, On the zeros of Eisenstein Series, Bull. London Math. Soc., 2(1970),169-170."))

make_entry(ID("a50278"),
    Formula(GreaterEqual(Cardinality(Zeros(EisensteinE(2*k, tau), ForElement(tau, ModularGroupFundamentalDomain))), 1)),
    Variables(k),
    Assumptions(And(Element(k, ZZGreaterEqual(2)))),
    References("F. K. C. Rankin and H. P. F. Swinnerton-Dyer, On the zeros of Eisenstein Series, Bull. London Math. Soc., 2(1970),169-170."))

make_entry(ID("13cac5"),
    Formula(Where(Equal(Sum(w(tau) * ComplexZeroMultiplicity(EisensteinE(2*k, z), For(z, tau)), ForElement(tau, ModularGroupFundamentalDomain)), 2*k/12),
        Equal(w(tau), Cases(Tuple(Div(1,2), Equal(tau, ConstI)), Tuple(Div(1,3), Equal(tau, Exp(2*Pi*ConstI/3))), Tuple(1, Otherwise))))),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(2))),
    References("K. Ono and M. A. Papanikolas (2004). p-Adic Properties of Values of the Modular j-Function. In: Hashimoto K., Miyake K., Nakamura H. (eds) Galois Theory and Modular Forms. Developments in Mathematics, vol 11. Springer, Boston, MA, https://doi.org/10.1007/978-1-4613-0249-0_19",
    "S. Garthwaite, L. Long, H. Swisher, S. Treneer. Zeros of classical Eisenstein series and recent developments, Fields Communications Volume 60, WIN - Women In Numbers, Proceedings of the WIN Workshop, (2011), 251-263. http://math.oregonstate.edu/~swisherh/C1P.pdf"))

make_entry(ID("097efc"),
    Formula(Where(Equal(Sum(ModularJ(tau) * w(tau) * ComplexZeroMultiplicity(EisensteinE(2*k, z), For(z, tau)), ForElement(tau, ModularGroupFundamentalDomain)), 120*k - 2/RiemannZeta(1-2*k)),
        Equal(w(tau), Cases(Tuple(Div(1,2), Equal(tau, ConstI)), Tuple(1, Otherwise))))),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(2))),
    References("K. Ono and M. A. Papanikolas (2004). p-Adic Properties of Values of the Modular j-Function. In: Hashimoto K., Miyake K., Nakamura H. (eds) Galois Theory and Modular Forms. Developments in Mathematics, vol 11. Springer, Boston, MA, https://doi.org/10.1007/978-1-4613-0249-0_19",
    "S. Garthwaite, L. Long, H. Swisher, S. Treneer. Zeros of classical Eisenstein series and recent developments, Fields Communications Volume 60, WIN - Women In Numbers, Proceedings of the WIN Workshop, (2011), 251-263. http://math.oregonstate.edu/~swisherh/C1P.pdf"))

# todo: more distribution theorems?

make_entry(ID("4a200a"),
    Formula(Equal(Zeros(EisensteinE(4, tau), ForElement(tau, ModularGroupFundamentalDomain)), Set(Exp(2*Pi*ConstI/3)))))

make_entry(ID("ec4f56"),
    Formula(Equal(Zeros(EisensteinE(6, tau), ForElement(tau, ModularGroupFundamentalDomain)), Set(ConstI))))

make_entry(ID("83566f"),
    Formula(Equal(Zeros(EisensteinE(8, tau), ForElement(tau, ModularGroupFundamentalDomain)), Set(Exp(2*Pi*ConstI/3)))))

make_entry(ID("26faf3"),
    Formula(Equal(Zeros(EisensteinE(10, tau), ForElement(tau, ModularGroupFundamentalDomain)), Set(ConstI, Exp(2*Pi*ConstI/3)))))

make_entry(ID("6ae250"),
    Formula(Equal(Zeros(EisensteinE(12, tau), ForElement(tau, ModularGroupFundamentalDomain)),
        Where(Set(ConstI * Hypergeometric2F1(Div(1,6),Div(5,6),1,a) / Hypergeometric2F1(Div(1,6),Div(5,6),1,1-a)),
            Equal(a, Div(1,2) + 21*Sqrt(10)*ConstI/100)))))

make_entry(ID("ad91ae"),
    Formula(Equal(Zeros(EisensteinE(14, tau), ForElement(tau, ModularGroupFundamentalDomain)), Set(ConstI, Exp(2*Pi*ConstI/3)))))

make_entry(ID("cae067"),
    Formula(Equal(Zeros(EisensteinE(2, tau), ForElement(tau, HH)),
        Set(tau+n, For(Tuple(tau, n)), And(Element(tau, Zeros(EisensteinE(2, z), For(z), And(Element(z, HH), Element(Re(z), ClosedOpenInterval(-Div(1,2), Div(1,2)))))),
            Element(n, ZZ))))))

make_entry(ID("f33f09"),
    Formula(Equal(Zeros(EisensteinE(2, tau), For(tau), And(Element(tau, HH), Element(Re(tau), ClosedOpenInterval(-Div(1,2), Div(1,2))))),
        Where(Set(Parentheses(UniqueZero(EisensteinE(2, z), For(z), Element(z, D(c,d)))),
            For(Tuple(c, d)), And(Element(c, ZZ), Element(d, ZZ), Equal(GCD(c,d),1), Element(-(d/c), ClosedOpenInterval(-Div(1,2), Div(1,2))))),
            Equal(D(c,d), ClosedDisk(-(d/c) + (ConstI*Pi)/(6*c**2), (Decimal("0.000283")*Pi**2)/(36*c**2)))))),
    References("R. Wood and M. P. Young, Zeros of the weight two Eisenstein series, Journal of Number Theory Volume 143, October 2014, Pages 320-333. https://doi.org/10.1016/j.jnt.2014.04.007"))

make_entry(ID("67f2ef"),
    Formula(Element(UniqueZero(EisensteinE(2, ConstI*y), ForElement(y, OpenInterval(0, Infinity))),
        RealBall(Decimal("0.523521700017999266800534404806"), Decimal("1.10e-31")))))

make_entry(ID("be9790"),
    Formula(Element(UniqueZero(EisensteinE(2, -Div(1,2) + ConstI*y), ForElement(y, OpenInterval(0, Infinity))),
        RealBall(Decimal("0.130919030396762446904114826020"), Decimal("2.87e-31")))))



