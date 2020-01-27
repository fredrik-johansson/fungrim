# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Sinc function"),
    Section("Definitions"),
    Entries(
        "4cbfd4",
    ),
    Section("Illustrations"),
    Entries(
        "639d7b",
        "baf960",
    ),
    Section("Domain"),
    Entries(
        "a527c4",
        "89be58",
        "2379e6",
        "41998e",
    ),
    Section("Primary formula"),
    Entries(
        "fa9283",
        "b18020",
        "01422b",
    ),
    Section("Zeros"),
    Entries(
        "af4516",
        "1349b5",
    ),
    Section("Specific values"),
    Entries(
        "593e63",
        "fdc94c",
        "340936",
        "c9ead2",
        "45740a",
    ),
    Section("Functional equations"),
    Subsection("Even symmetry"),
    Entries(
        "f19e0a",
    ),
    Subsection("Conjugate symmetry"),
    Entries(
        "3a428f",
    ),
    Subsection("Multiplication formulas"),
    Entries(
        "b41d08",
        "d5000a",
    ),
    Section("Derivatives and differential equations"),
    Subsection("First derivatives"),
    Entries(
        "768c77",
        "90c66a",
    ),
    Subsection("Linear ordinary differential equations"),
    Entries
    (
        "c6e6b2",
        "aa15f0",
    ),
    Subsection("Higher derivatives"),
    Entries
    (
        "1c3766",
        "ff5e82",
    ),
    Section("Series and product representations"),
    Entries(
        "4f9844",
        "f64eef",
        "24c17b",
    ),
    Section("Representation by special functions"),
    Entries(
        "d16cb4",
        "e2878f",
        "50f72f",
        "19d7d9",
    ),
    Section("Integral representations"),
    Entries(
        "6e4f58",
        "e2c10d",
        "729c78",
        "08583a",
        "b1d132",
        "99ad29",
        "45f05f",
    ),
    Section("Integrals"),
    Subsection("Sine integral"),
    Entries(
        "122e3d",
        "d6c29e",
        "8ef3d7",
        "2b7b1d",
        "f0f0a6",
    ),
    Subsection("Gibbs constant"),
    Entries(
        "81f531",
    ),
    Subsection("Integrals on the real line"),
    Entries(
        "a0b0b3",
        "cb152f",
        "1a7e22",
        "be0f54",
        "1596d2",
        "af8328",
        "3fe2b0",
        "108daa",
        "f5887b",
    ),
    Subsection("Integral transforms"),
    Entries(
        "2a69ce",
        "38dc04",
        "78fca3",
    ),
    Subsection("Other definite integrals"),
    Entries(
        "c2976e",
        "4a5b9a",
        "dad27b",
        "5c9675",
    ),
    Section("Summation"),
    Subsection("Infinite series"),
    Entries(
        "2a8ec9",
        "005478",
        "4d5410",
        "1f9beb",
        "8814ad",
        "49514d",
        "0c847f",
        "b894a3",
        "4a1b00",
    ),
    Section("Extreme points and limits"),
    Subsection("Extreme points"),
    Entries(
        "632d1c",
        "b1a260",
        "1e6344",
        "da7fb1",
        "95c04c",
        "2ac5eb",
    ),
    Subsection("Limits at infinity"),
    Entries(
        "5e0c58",
        "a2f5a9",
        "2f09ad",
        "6c28fa",
        "aa404c",
        "088fdb",
        "f4fd7d",
    ),
    Section("Bounds and inequalities"),
    Subsection("Real variable"),
    Entries(
        "20f069",
        "4d3f04",
        "f0325d",
        "d8d286",
        "a934d1",
        "351d87",
        "5d16e5",
    ),
    Subsection("Complex variable"),
    Entries(
        "c7c483",
        "51f9b4",
    ),
)

# Definitions

make_entry(ID("4cbfd4"),
    SymbolDefinition(Sinc, Sinc(z), "Sinc function"),
    CodeExample(Sinc(z), "represents the sinc function of argument", z, "."))

# Illustrations

make_entry(ID("639d7b"),
    Image(Description("Plot of", Sinc(x), "and", Sinc(Pi*x), "on", Element(x, ClosedInterval(-(3*Pi), 3*Pi))),
        ImageSource("plot_sinc")),
    )

make_entry(ID("baf960"),
    Image(Description("X-ray of", Sinc(z), "on", Element(z, ClosedInterval(-8,8) + ClosedInterval(-8,8)*ConstI)),
        ImageSource("xray_sinc")),
    description_xray,
    )

# Domain

make_entry(ID("a527c4"),
    Formula(IsHolomorphic(Sinc(z), ForElement(z, CC))))

make_entry(ID("89be58"),
    Formula(Implies(Element(x, RR), Element(Sinc(x), RR))),
    Variables(x))

make_entry(ID("2379e6"),
    Formula(Implies(Element(z, CC), Element(Sinc(z), CC))),
    Variables(z))

make_entry(ID("41998e"),
    Formula(Implies(Element(x, RR), Element(Sinc(x), OpenClosedInterval(Decimal("-0.217234"), 1)))),
    Variables(x))

# Primary formula

make_entry(ID("fa9283"),
    Formula(Equal(Sinc(z), Sin(z) / z)),
    Variables(z),
    Assumptions(And(Element(z, CC), NotEqual(z, 0))))

make_entry(ID("b18020"),
    Formula(Equal(Sinc(0), 1)))

make_entry(ID("01422b"),
    Formula(Equal(Sinc(z), Cases(Tuple(Sin(z)/z, NotEqual(z, 0)), Tuple(1, Equal(z, 0))))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Zeros

make_entry(ID("af4516"),
    Formula(Equal(Zeros(Sinc(z), ForElement(z, CC)), Set(Pi*n, ForElement(n, ZZ), NotEqual(n, 0)))))

make_entry(ID("1349b5"),
    Formula(Equal(Zeros(Sinc(Pi*z), ForElement(z, CC)), Set(n, ForElement(n, ZZ), NotEqual(n, 0)))))

# Specific values

make_entry(ID("593e63"),
    Formula(Equal(Sinc(Pi*n), Cases(Tuple(1, Equal(n, 0)), Tuple(0, NotEqual(n, 0))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("fdc94c"),
    Formula(Equal(Sinc(Pi/2), 2/Pi)))

make_entry(ID("340936"),
    Formula(Equal(Sinc(Pi/3), 3*Sqrt(3)/(2*Pi))))

make_entry(ID("c9ead2"),
    Formula(Equal(Sinc(Pi/4), 2*Sqrt(2)/Pi)))

make_entry(ID("45740a"),
    Formula(Equal(Sinc(Pi/6), 3/Pi)))

# Functional equations

## Even symmetry

make_entry(ID("f19e0a"),
    Formula(Equal(Sinc(-z), Sinc(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

## Conjugate symmetry

make_entry(ID("3a428f"),
    Formula(Equal(Sinc(Conjugate(z)), Conjugate(Sinc(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

## Multiplication formulas

make_entry(ID("b41d08"),
    Formula(Equal(Sinc(ConstI*z), Sinh(z)/z)),
    Variables(z),
    Assumptions(And(Element(z, CC), NotEqual(z, 0))))

make_entry(ID("d5000a"),
    Formula(Equal(Sinc(2*z), Sinc(z)*Cos(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Derivatives and differential equations

make_entry(ID("768c77"),
    Formula(Equal(ComplexDerivative(Sinc(z), For(z, z)), Cases(Tuple(Cos(z)/z - Sin(z)/z**2, NotEqual(z, 0)), Tuple(0, Equal(z, 0))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("90c66a"),
    Formula(Equal(ComplexDerivative(Sinc(z), For(z, z, 2)), Cases(Tuple((2/z**3-1/z)*Sin(z) - 2*Cos(z)/z**2, NotEqual(z, 0)), Tuple(-Div(1,3), Equal(z, 0))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("c6e6b2"),
    Formula(Equal(z * ComplexDerivative(Sinc(z), For(z, z, 2)) + 2 * ComplexDerivative(Sinc(z), For(z, z)) + z * Sinc(z), 0)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("aa15f0"),
    Formula(Where(Equal(z * ComplexDerivative(f(z), For(z, z, 2)) + 2 * ComplexDerivative(f(z), For(z, z)) + A**2 * z * f(z), 0),
        Equal(f(z), Subscript(C, 1) * Sinc(A*z) + Subscript(C, 2) * (Cos(A*z) / z)))),
    Variables(C, A, z),
    Assumptions(And(Element(z, CC), NotEqual(z, 0), Element(A, CC), Element(Subscript(C, 1), CC), Element(Subscript(C, 2), CC))))

make_entry(ID("1c3766"),
    Formula(Equal(ComplexDerivative(Sinc(z), For(z, 0, n)), Cases(Tuple((-1)**Floor(n/2) * (1/(n+1)), Even(n)), Tuple(0, Odd(n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("ff5e82"),
    Formula(Where(Equal((z*(n**2 + 5*n + 6))*a_(n+3) + (n**2 + 5*n + 6)*a_(n+2) + z*a_(n+1) + a_(n), 0),
        Equal(a_(n), ComplexDerivative(Sinc(z), For(z, z, n)) / Factorial(n)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(0)))))

# Series and product representations

make_entry(ID("4f9844"),
    Formula(Equal(Sinc(z), Sum((-1)**n * z**(2*n) / Factorial(2*n+1), For(n, 0, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("f64eef"),
    Formula(Equal(Sinc(Pi*z), Product(Parentheses(1-z**2/n**2), For(n, 1, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("24c17b"),
    Formula(Equal(Sinc(z), Product(Cos(z/2**n), For(n, 1, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Representation by special functions

# d16cb4 included from gamma

make_entry(ID("e2878f"),
    Formula(Equal(Sinc(z), Hypergeometric0F1(Div(3, 2), -(z**2 / 4)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("50f72f"),
    Formula(Equal(Derivative(Sinc(z), For(z, z)), -((z/3)*Hypergeometric0F1(Div(5, 2), -(z**2 / 4))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("19d7d9"),
    Formula(Equal(Sinc(z), ((2*z)/Pi)**(-(Div(1,2))) * (BesselJ(Div(1,2), z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotEqual(z, 0))))

# Integral representations

make_entry(ID("6e4f58"),
    Formula(Equal(Sinc(z), Integral(Cos(z*x), For(x, 0, 1)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e2c10d"),
    Formula(Equal(Sinc(a*z), (1/a) * Integral(Cos(z*x), For(x, 0, a)))),
    Variables(a, z),
    Assumptions(And(Element(z, CC), Element(a, CC), NotEqual(a, 0))))

make_entry(ID("729c78"),
    Formula(Equal(Sinc(Pi*z), Integral(Cos(Pi*z*x), For(x, 0, 1)))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("08583a"),
    Formula(Equal(Sinc(z), Div(1,2) * Integral(Exp(ConstI*z*x), For(x, -1, 1)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("b1d132"),
    Formula(Equal(Sinc(a*z), Div(1,(2*a)) * Integral(Exp(ConstI*z*x), For(x, -a, a)))),
    Variables(a, z),
    Assumptions(And(Element(z, CC), Element(a, CC), NotEqual(a, 0))))

make_entry(ID("99ad29"),
    Formula(Equal(Sinc(Pi*z), Integral(Exp(2*Pi*ConstI*z*x), For(x, -Div(1,2), Div(1,2))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("45f05f"),
    Formula(Equal(1/Sinc(Pi/z), Integral(1/(x**z+1), For(x, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 1))))


# Integrals

make_entry(ID("122e3d"),
    Formula(Equal(Integral(Sinc(x), For(x, 0, z)), SinIntegral(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("d6c29e"),
    Formula(Equal(Integral(Sinc(x), For(x, a, b)), SinIntegral(b) - SinIntegral(a))),
    Variables(a),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("8ef3d7"),
    Formula(Equal(Integral(Sinc(x), For(x, -Infinity, z)), SinIntegral(z) + Pi/2)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("2b7b1d"),
    Formula(Equal(Integral(Sinc(x), For(x, z, Infinity)), Pi/2 - SinIntegral(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("f0f0a6"),
    Formula(Equal(Integral(Sinc(x), For(x, -Infinity, Infinity)), Pi)))

make_entry(ID("81f531"),
    Formula(EqualNearestDecimal(Integral(Sinc(x), For(x, 0, Pi)), 
        Decimal("1.85193705198246617036105337016"), 30)))

make_entry(ID("f5887b"),
    Formula(Equal(Integral(Sinc(x + Pi*n) * Sinc(x + Pi*m), For(x, -Infinity, Infinity)), Cases(Tuple(Pi, Equal(n, m)), Tuple(0, NotEqual(n, m))))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZ), Element(m, ZZ))))

make_entry(ID("108daa"),
    Formula(Equal(Integral(Sinc(a*x) * Sinc(b*x), For(x, -Infinity, Infinity)), (Pi/2) * ((Abs(a+b)-Abs(a-b))/(a*b)))),
    Variables(a, b),
    Assumptions(And(Element(a, RR), Element(b, RR), NotEqual(a, 0), NotEqual(b, 0))))

make_entry(ID("3fe2b0"),
    Formula(Equal(Integral(Sinc(x+a) * Sinc(x+b), For(x, -Infinity, Infinity)), Pi * Sinc(a-b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("2a69ce"),
    Formula(Equal(Integral(Exp(ConstI*a*x) * Sinc(x), For(x, -Infinity, Infinity)),
            Integral(Cos(a*x) * Sinc(x), For(x, -Infinity, Infinity)),
        Cases(Tuple(Pi, Less(Abs(a), 1)),
            Tuple(Pi/2, Equal(Abs(a), 1)),
            Tuple(0, Greater(Abs(a), 1))))),
    Variables(a),
    Assumptions(Element(a, RR)))

make_entry(ID("38dc04"),
    Formula(Equal(Integral(Exp(-(a*x)) * Sinc(x), For(x, 0, Infinity)), Acot(a))),
    Variables(a),
    Assumptions(And(Element(a, CC), Greater(Re(a), 0))))

make_entry(ID("78fca3"),
    Formula(Equal(Integral(Exp(-(a*x**2)) * Sinc(x), For(x, 0, Infinity)), (Pi/2) * Erf(1/(2*Sqrt(a))))),
    Variables(a),
    Assumptions(And(Element(a, CC), Greater(Re(a), 0))))

make_entry(ID("a0b0b3"),
    Formula(Equal(Integral(Abs(Sinc(x)), For(x, 0, Infinity)), +Infinity)))

make_entry(ID("cb152f"),
    Formula(Equal(Integral(Sinc(x), For(x, 0, Infinity)), Pi/2)))

make_entry(ID("1a7e22"),
    Formula(Equal(Integral(Sinc(x)**2, For(x, 0, Infinity)), Pi/2)))

make_entry(ID("be0f54"),
    Formula(Equal(Integral(Sinc(x)**3, For(x, 0, Infinity)), 3*Pi/8)))

make_entry(ID("1596d2"),
    Formula(Equal(Integral(Sinc(x)**n, For(x, 0, Infinity)), (Pi / (2**n * Factorial(n-1))) * Sum((-1)**k * Binomial(n,k) * (n-2*k)**(n-1), For(k, 0, Floor(n/2))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("af8328"),
    Formula(Equal(Integral(Product(Sinc(x/(2*k+1)), For(k, 0, n)), For(x, 0, Infinity)),
        Cases(Tuple(Pi/2, Element(n, Range(0, 6))), Tuple(
            Div(467807924713440738696537864469,467807924720320453655260875000)*(Pi/2), Equal(n, 7))))),
    Variables(n),
    Assumptions(Element(n, Range(0, 7))))


make_entry(ID("c2976e"),
    Formula(Equal(Integral(1/Sinc(x), For(x, 0, Pi/2)), 2*ConstCatalan)))

make_entry(ID("4a5b9a"),
    Formula(Equal(Integral(x/Sinc(x), For(x, 0, Pi/2)), 2*Pi*ConstCatalan - 7*RiemannZeta(3)/2)))

make_entry(ID("dad27b"),
    Formula(Equal(Integral(1/Sinc(x)**2, For(x, 0, Pi/2)), Pi*Log(2))))

make_entry(ID("5c9675"),
    Formula(Equal(Integral(1/Sinc(x)**2, For(x, 0, Pi/4)), Pi*Log(2)/4 + ConstCatalan - Pi**2/16)))

# Extreme points

make_entry(ID("632d1c"),
    Formula(Equal(Maximum(Sinc(x), ForElement(x, RR)), 1)))

make_entry(ID("b1a260"),
    Formula(Equal(ArgMaxUnique(Sinc(x), ForElement(x, RR)), 0)))

make_entry(ID("1e6344"),
    Formula(Equal(ArgMin(Sinc(x), ForElement(x, RR)), Where(Set(-a,a),
        Equal(a, BesselJZero(Div(3,2), 1))))))

make_entry(ID("da7fb1"),
    Formula(Equal(Minimum(Sinc(x), ForElement(x, RR)),
        Sinc(BesselJZero(Div(3,2), 1)))))

make_entry(ID("95c04c"),
    Formula(EqualNearestDecimal(ArgMinUnique(Sinc(x), ForElement(x, OpenClosedInterval(0, Infinity))),
        Decimal("4.49340945790906417530788092728"), 30)))

make_entry(ID("2ac5eb"),
    Formula(EqualNearestDecimal(Minimum(Sinc(x), ForElement(x, RR)),
        Decimal("-0.217233628211221657408279325562"), 30)))

## Limits

make_entry(ID("5e0c58"),
    Formula(Equal(Sinc(Infinity), RealLimit(Sinc(x), For(x, Infinity)), 0)))

make_entry(ID("a2f5a9"),
    Formula(Equal(Sinc(-Infinity), RealLimit(Sinc(x), For(x, -Infinity)), 0)))

make_entry(ID("2f09ad"),
    Formula(Equal(Sinc(Infinity), RealLimit(Sinc(a*ConstI+x), For(x, Infinity)), 0)),
    Variables(a),
    Assumptions(Element(a, CC)))

make_entry(ID("6c28fa"),
    Formula(Equal(Sinc(-Infinity), RealLimit(Sinc(a*ConstI+x), For(x, -Infinity)), 0)),
    Variables(a),
    Assumptions(Element(a, CC)))

make_entry(ID("aa404c"),
    Formula(Equal(Sinc(ConstI*Infinity), RealLimit(Sinc(ConstI*x), For(x, Infinity)), Infinity)))

make_entry(ID("088fdb"),
    Formula(Equal(Sinc(-(ConstI*Infinity)), RealLimit(Sinc(ConstI*x), For(x, -Infinity)), Infinity)))

make_entry(ID("f4fd7d"),
    Formula(Equal(Abs(Sinc(Exp(ConstI*theta)*Infinity)), RealLimit(Abs(Sinc(Exp(ConstI*theta)*x)), For(x, Infinity)),
        Cases(Tuple(0, Element(Exp(ConstI*theta), Set(-1,1))), Tuple(Infinity, Otherwise)))),
    Variables(theta),
    Assumptions(Element(theta, RR)))


# Bounds and inequalities

## Real variable

make_entry(ID("20f069"),
    Formula(LessEqual(Abs(Sinc(x)), 1)),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("4d3f04"),
    Formula(Greater(Sinc(x), Decimal("-0.217234"))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("f0325d"),
    Formula(LessEqual(Abs(Sinc(x)), 1/Abs(x))),
    Variables(x),
    Assumptions(And(Element(x, RR), NotEqual(x, 0))))

make_entry(ID("d8d286"),
    Formula(LessEqual(Abs(Sinc(x)), (1+Abs(x))/(1+x**2))),
    Variables(x),
    Assumptions(And(Element(x, RR))))

make_entry(ID("a934d1"),
    Formula(Less(Abs(Sinc(x)), Asinh(x)/x)),
    Variables(x),
    Assumptions(And(Element(x, RR), NotEqual(x, 0))))

make_entry(ID("351d87"),
    Formula(Less(Abs(Sinc(x)), (Sqrt(2)/x) * Tanh(x/Sqrt(2)))),
    Variables(x),
    Assumptions(And(Element(x, RR), NotEqual(x, 0))))

make_entry(ID("5d16e5"),
    Formula(LessEqual(Abs(Derivative(Sinc(x), For(x, x, n))), 1)),
    Variables(x, n),
    Assumptions(And(Element(x, RR), Element(n, ZZGreaterEqual(0)))))

## Complex variable

make_entry(ID("c7c483"),
    Formula(LessEqual(Abs(Sinc(z)), Exp(Abs(Im(z))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("51f9b4"),
    Formula(LessEqual(Abs(Sinc(z)), Sinc(ConstI*Abs(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Summation

# todo: semantic subscripts
make_entry(ID("2a8ec9"),
    Formula(Implies(
        Cases(
            Tuple(Less(Sum(Subscript(a,k), For(k,0,N)), 2*Pi), Equal(N, 0)),
            Tuple(LessEqual(Sum(Subscript(a,k), For(k,0,N)), 2*Pi), GreaterEqual(N, 1)),
        ),
        Equal(Sum(Product(Sinc(Subscript(a,k)*n), For(k, 0, N)), For(n, -Infinity, Infinity)),
        Integral(Product(Sinc(Subscript(a,k)*x), For(k, 0, N)), For(x, -Infinity, Infinity))))),
    Variables(N, a),
    Assumptions(And(Element(N, ZZGreaterEqual(0)), Element(Subscript(a, k), OpenInterval(0, Infinity)))),
    References("https://www.carma.newcastle.edu.au/resources/jon/sinc-sums.pdf"))

# todo: semantic subscripts
make_entry(ID("005478"),
    Formula(Implies(
        Cases(
            Tuple(Less(Sum(Subscript(a,k), For(k,0,N)), 2*Pi), Equal(N, 0)),
            Tuple(LessEqual(Sum(Subscript(a,k), For(k,0,N)), 2*Pi), GreaterEqual(N, 1)),
        ),
        Equal(Sum(Product(Sinc(Subscript(a,k)*n), For(k, 0, N)), For(n, 1, Infinity)),
        -Div(1,2) + Integral(Product(Sinc(Subscript(a,k)*x), For(k, 0, N)), For(x, 0, Infinity))))),
    Variables(N, a),
    Assumptions(And(Element(N, ZZGreaterEqual(0)), Element(Subscript(a, k), OpenInterval(0, Infinity)))),
    References("https://www.carma.newcastle.edu.au/resources/jon/sinc-sums.pdf"))

make_entry(ID("4d5410"),
    Formula(Equal(Sum(Sinc(n), For(n, -Infinity, Infinity)), Pi)))

make_entry(ID("1f9beb"),
    Formula(Equal(Sum(Sinc(n)**2, For(n, -Infinity, Infinity)), Pi)))

make_entry(ID("8814ad"),
    Formula(Equal(Sum(Sinc(n)**3, For(n, -Infinity, Infinity)), 3*Pi/4)))

make_entry(ID("49514d"),
    Formula(Equal(Sum(Sinc(n)**4, For(n, -Infinity, Infinity)), 2*Pi/3)))

make_entry(ID("0c847f"),
    Formula(Equal(Sum(Sinc(n)**5, For(n, -Infinity, Infinity)), 115*Pi/192)))

make_entry(ID("b894a3"),
    Formula(Equal(Sum(Sinc(n)**6, For(n, -Infinity, Infinity)), 11*Pi/20)))

make_entry(ID("4a1b00"),
    Formula(Equal(Sum(Sinc(n)**7, For(n, -Infinity, Infinity)),
        (129423*Pi-201684*Pi**2+144060*Pi**3-54880*Pi**4+11760*Pi**5-1344*Pi**6+64*Pi**7)/23040)))

