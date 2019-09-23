# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Dedekind eta function"),
    Section("Definitions"),
    Entries(
        "a203bb",
        "82a63c",
    ),
    Section("Fourier series (q-series)"),
    Entries(
        "1dc520",
        "ff587a",
        "2e7fdb",
        "8f10b0",
    ),
    Section("Specific values"),
    Subsection("Limiting values"),
    Entries(
        "6b9935",
        "d8025b",
    ),
    Subsection("Imaginary quadratic points"),
    Entries(
        "9b8c9f",
        "5706ab",
        "87e9ed",
        "9ce413",
        "3a56d8",
        "d2900f",
        "62ffb3",
        "7cc3d3",
        "be2f32",
        "0701dc",
        "e3e4c5",
    ),
    Subsection("Third roots of unity"),
    Entries(
        "204acd",
        "4af6db",
    ),
    Section("Connection formulas"),
    Entries(
        "737805",
    ),
    Section("Modular transformations"),
    SeeTopics("Modular transformations"),
    Entries(
        "f4dc79",
        "1bae52",
        "acee1a",
        "3b806f",
        "29d9ab",
        "9f19c1",
        "f04e01",
        "921ef0",
        "a1a3d4",
    ),
    Section("Derivatives"),
    Entries(
        "871996",
        "1c25d3",
        "02d14f",
        "df5f38",
    ),
    Section("Analytic properties"),
    Entries(
        "e06d87",
        "04f4a0",
        "f2e2c2",
        "6d7668",
        "39fb36",
    ),
    Section("Dedekind sums"),
    Entries(
        "7af83f",
        "23961e",
    ),
    Section("Related topics"),
    SeeTopics("Partition function"),
)

# Definitions

make_entry(ID("a203bb"),
    SymbolDefinition(DedekindEta, DedekindEta(tau), "Dedekind eta function"),
    Description("The Dedekind eta function", DedekindEta(tau), "is a function of one variable", tau, "in the upper half-plane."))

make_entry(ID("82a63c"),
    SymbolDefinition(EulerQSeries, EulerQSeries(q), "Euler's q-series"),
    Description("Euler's q-series", EulerQSeries(q), "is a function of one variable", q, "in the unit disk."))

# Fourier series (q-series)

make_entry(ID("2e7fdb"),
    Formula(Equal(EulerQSeries(q), Product(Parentheses(1 - q**k), For(k, 1, Infinity)))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("8f10b0"),
    Formula(Equal(EulerQSeries(q), Sum((-1)**k * q**(k*(3*k-1)/2), For(k, -Infinity, Infinity)))),
    Variables(q),
    Assumptions(And(Element(q, CC), Less(Abs(q), 1))))

make_entry(ID("ff587a"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * EulerQSeries(Exp(2*ConstPi*ConstI*tau)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("1dc520"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * Product(Parentheses(1 - Exp(2*ConstPi*ConstI*k*tau)), For(k, 1, Infinity)))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Specific values

# Limiting values

make_entry(ID("6b9935"),
    Formula(Equal(DedekindEta(ConstI*Infinity), ComplexLimit(DedekindEta(tau), Var(tau), ConstI*Infinity), 0)))

make_entry(ID("d8025b"),
    Formula(Equal(RightLimit(DedekindEta(ConstI*epsilon), Var(epsilon), 0), 0)))

# Imaginary points

rc = GammaFunction(Div(1,4)) / (2 * ConstPi ** Div(3,4))

make_entry(ID("9b8c9f"),
    Formula(Equal(DedekindEta(ConstI), rc)))

make_entry(ID("5706ab"),
    Formula(Equal(ComplexDerivative(DedekindEta(tau), For(tau, ConstI)),
         -Div(ConstI,4)*DedekindEta(ConstI))))

make_entry(ID("87e9ed"),
    Formula(Equal(DedekindEta(2 * ConstI), Div(DedekindEta(ConstI), Pow(2,Div(3,8))))))

make_entry(ID("9ce413"),
    Formula(Equal(DedekindEta(3 * ConstI), Div(DedekindEta(ConstI), Pow(3,Div(3,8)) * (2+Sqrt(3))**Div(1,12)))))

make_entry(ID("3a56d8"),
    Formula(Equal(DedekindEta(4 * ConstI), Div(DedekindEta(ConstI), Pow(2,Div(13,16)) * (1+Sqrt(2))**Div(1,4)))))

make_entry(ID("d2900f"),
    Formula(Equal(DedekindEta(5 * ConstI), Div(DedekindEta(ConstI), Sqrt(5 * GoldenRatio)))),
    References("https://math.stackexchange.com/questions/1334684/what-is-the-exact-value-of-eta6i/1334940"))

make_entry(ID("62ffb3"),
    Formula(Equal(DedekindEta(6 * ConstI), (1/Pow(6, Div(3, 8))) * ((5-Sqrt(3))/2 - Pow(3, Div(3,4))/Sqrt(2))**Div(1,6) * DedekindEta(ConstI))),
    References("https://math.stackexchange.com/questions/1334684/what-is-the-exact-value-of-eta6i/1334940"))

make_entry(ID("7cc3d3"),
    Formula(Equal(DedekindEta(7 * ConstI), (1/Sqrt(7)) * (-Div(7,2) + Sqrt(7) + Div(1,2) * Sqrt(-7 + 4*Sqrt(7)))**Div(1,4) * DedekindEta(ConstI))),
    References("https://math.stackexchange.com/questions/1334684/what-is-the-exact-value-of-eta6i/1334940"))

make_entry(ID("be2f32"),
    Formula(Equal(DedekindEta(8 * ConstI), (1/Pow(2, Div(41,32))) * (Pow(Pow(2, Div(1,4)) - 1, Div(1,2)) / (1 + Sqrt(2))**Div(1,8)) * DedekindEta(ConstI))),
    References("https://math.stackexchange.com/questions/1334684/what-is-the-exact-value-of-eta6i/1334940"))

make_entry(ID("0701dc"),
    Formula(Equal(DedekindEta(16 * ConstI), (1/Pow(2, Div(113,64))) * ((Pow(2, Div(1,4)) - 1)**Div(1,4) / (1 + Sqrt(2))**Div(1,16)) * (-Pow(2,Div(5,8)) + Sqrt(1 + Sqrt(2)))**Div(1,2) * DedekindEta(ConstI))),
    References("https://math.stackexchange.com/questions/1334684/what-is-the-exact-value-of-eta6i/1334940"))

make_entry(ID("e3e4c5"),
    Formula(Equal(DedekindEta(Sqrt(3) * ConstI), Pow(3,Div(1,8)) / Pow(2,Div(4,3)) * (GammaFunction(Div(1,3))**Div(3,2) / ConstPi))),
    References("https://math.stackexchange.com/questions/1334684/what-is-the-exact-value-of-eta6i/1334940"))

# Third roots of unity

make_entry(ID("204acd"),
    Formula(Equal(DedekindEta(Exp(2*ConstPi*ConstI/3)), Exp(-(ConstPi*ConstI/24)) * (Pow(3,Div(1,8)) * Pow(GammaFunction(Div(1,3)), Div(3,2)) / (2 * ConstPi)))))

make_entry(ID("4af6db"),
    Formula(Equal(ComplexDerivative(DedekindEta(tau), For(tau, Exp(2*ConstPi*ConstI/3))),
        ((ConstI*Sqrt(3))/6) * DedekindEta(Exp(2*ConstPi*ConstI/3)))))
# Connection formulas

make_entry(ID("737805"),
    Formula(Equal(DedekindEta(tau), Exp(ConstPi*ConstI*tau/12) * JacobiTheta(3,(tau+1)/2, 3*tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Modular transformations

make_entry(ID("f4dc79"),
    SymbolDefinition(DedekindEtaEpsilon, DedekindEtaEpsilon(a,b,c,d), "Root of unity in the functional equation of the Dedekind eta function"))

make_entry(ID("1bae52"),
    Formula(Equal(DedekindEta(tau+1), Exp(ConstPi*ConstI/12) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("acee1a"),
    Formula(Equal(DedekindEta(tau+24), DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("3b806f"),
    Formula(Equal(DedekindEta(-(1/tau)), (-(ConstI*tau))**Div(1,2) * DedekindEta(tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("29d9ab"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)) ** 24, (c*tau+d)**12 * DedekindEta(tau)**24)),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), SL2Z))))

make_entry(ID("9f19c1"),
    Formula(Equal(DedekindEta((a*tau+b)/(c*tau+d)), DedekindEtaEpsilon(a,b,c,d) * (c*tau+d)**Div(1,2) * DedekindEta(tau))),
    Variables(tau,a,b,c,d),
    Assumptions(And(Element(tau, HH), Element(Matrix2x2(a, b, c, d), PSL2Z))))

make_entry(ID("f04e01"),
    Formula(Equal(DedekindEtaEpsilon(1,b,0,1), Exp((ConstPi*ConstI*b)/12))),
    Variables(b),
    Element(b, ZZ))

make_entry(ID("921ef0"),
    Formula(Equal(DedekindEtaEpsilon(a,b,c,d), Exp((ConstPi*ConstI*((a+d)/(12*c) - DedekindSum(d,c) - Div(1,4)))))),
    Variables(a,b,c,d),
    Assumptions(And(Element(a, ZZ), Element(b, ZZ), Element(c, ZZ), Element(d, ZZ), Equal(a*d-b*c, 1), Greater(c, 0))))

make_entry(ID("a1a3d4"),
    Formula(Equal(DedekindEta(tau+Div(1,2)), Exp(ConstPi*ConstI/24) * (DedekindEta(2*tau)**3 / (DedekindEta(tau) * DedekindEta(4*tau))))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

# Derivatives

make_entry(ID("871996"),
    Formula(Equal(ComplexDerivative(DedekindEta(tau), For(tau, tau)),
        ((ConstI * ConstPi) / 12) * DedekindEta(tau) * EisensteinE(2, tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("1c25d3"),
    Formula(Equal(ComplexDerivative(DedekindEta(tau), For(tau, tau)),
        (ConstI / (2 * ConstPi)) * DedekindEta(tau) * WeierstrassZeta(Div(1,2), tau))),
    Variables(tau),
    Assumptions(Element(tau, HH)))

make_entry(ID("02d14f"),
    Formula(Where(
        Equal(36*ComplexDerivative(y(tau), For(tau, tau))**2 - 24*ComplexDerivative(y(tau), For(tau, tau, 2))*y(tau) + ComplexDerivative(y(tau), For(tau, tau, 3)), 0),
        Equal(y(tau), ComplexDerivative(DedekindEta(tau), For(tau, tau)) / DedekindEta(tau)))),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References("http://functions.wolfram.com/EllipticFunctions/DedekindEta/13/01/0002/"))

make_entry(ID("df5f38"),
    Formula(
        Equal(
            DedekindEta(tau)**2*(33*ComplexDerivative(DedekindEta(tau), For(tau,tau,2))**2
            + DedekindEta(tau)*ComplexDerivative(DedekindEta(tau), For(tau,tau,4)))
            - 18*ComplexDerivative(DedekindEta(tau), For(tau,tau))**4
            + 12*DedekindEta(tau)*ComplexDerivative(DedekindEta(tau), For(tau,tau,2))*ComplexDerivative(DedekindEta(tau), For(tau,tau))**2
            - 28*DedekindEta(tau)**2*ComplexDerivative(DedekindEta(tau), For(tau,tau,3))*ComplexDerivative(DedekindEta(tau), For(tau,tau)), 0)),
    Variables(tau),
    Assumptions(Element(tau, HH)),
    References("http://functions.wolfram.com/EllipticFunctions/DedekindEta/13/01/0001/"))

# Analytic properties

make_entry(ID("e06d87"),
    Formula(Equal(HolomorphicDomain(DedekindEta(tau), tau, HH), HH)))

make_entry(ID("04f4a0"),
    Formula(Equal(Poles(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("f2e2c2"),
    Formula(Equal(BranchPoints(DedekindEta(tau), tau, Union(HH, Set(UnsignedInfinity))), Set())))

make_entry(ID("6d7668"),
    Formula(Equal(BranchCuts(DedekindEta(tau), tau, HH), Set())))

make_entry(ID("39fb36"),
    Formula(Equal(Zeros(DedekindEta(tau), Var(tau), Element(tau, HH)), Set())))

# Dedekind sums

make_entry(ID("7af83f"),
    SymbolDefinition(DedekindSum, DedekindSum(n,k), "Dedekind sum"))

make_entry(ID("23961e"),
    Formula(Equal(DedekindSum(n,k), Sum((r/k) * ((n*r/k) - Floor(n*r/k) - Div(1,2)), For(r, 1, k-1)))),
    Variables(n,k),
    Assumptions(And(Element(n, ZZ), Element(k, ZZ), Greater(k, 0), Equal(GCD(n, k), 1))))


