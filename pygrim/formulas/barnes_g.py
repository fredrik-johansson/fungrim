# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Barnes G-function"),
    Section("Definitions"),
    Entries(
        "82a1b1",
        "da1509",
    ),
    Section("Illustrations"),
    Entries(
        "488c5c",
        "106bf7",
        "e1497f",
    ),
    Section("Domain"),
    Subsection("Barnes G-function"),
    Entries(
        "971881",
        "3d46ea",
        "f3f0a7",
        "8ec739",
    ),
    Subsection("Logarithmic Barnes G-function"),
    Entries(
        "037342",
        "19b40f",
        "a471d0",
        "62bdb8",
    ),
    Section("Logarithmic form"),
    Entries(
        "b4355e",
        "5a11eb",
        "d9a7a3",
    ),
    Section("Specific values"),
    Subsection("Integers"),
    Entries(
        "33f13a",
        "daef08",
        "5cb675",
        "dbc117",
    ),
    Subsection("Rational arguments"),
    Entries(
        "8b7991",
        "ce66a9",
        "dc507f",
    ),
    Subsection("Derivatives"),
    Entries(
        "90b367",
        "dbfd5b",
        "a54fb0",
        "f50c74",
    ),
    Section("Singularities and zeros"),
    Subsection("Zeros"),
    Entries(
        "e488dc",
        "f77124",
        "2b021c",
    ),
    Subsection("Branch cuts"),
    Entries(
        "c3e340",
        "e1f73d",
        "a044e1",
        "cc3a51",
        "d35c54",
    ),
    Section("Functional equations"),
    Subsection("Recurrence relation"),
    Entries(
        "86b3ec",
        "5261e3",
        "7a36e5",
    ),
    Subsection("Reflection formula, real variables"),
    Entries(
        "541e2e",
        "d1a0ec",
    ),
    Subsection("Reflection formula, complex variables"),
    Entries(
        "b6017f",
        "23ed69",
        "82b410",
    ),
    Subsection("Multiplication theorem"),
    Entries(
        "ea26d4",
    ),
    Subsection("Conjugate symmetry"),
    Entries(
        "147db6",
        "6c6d3e",
    ),
    Section("Derivatives and differential equations"),
    Entries(
        "5babc2",
        "af31ae",
    ),
    Section("Representation by other functions"),
    Entries(
        "e05807",
    ),
    Section("Series and product representations"),
    Subsection("Taylor series"),
    Entries(
        "0ad263",
    ),
    Subsection("Weierstrass product"),
    Entries(
        "54d4e2",
    ),
    Subsection("Asymptotic expansion"),
    Entries(
        "752bde",
        "6f8e14",
        "b16d00",
        "092cee",
        "645c98",
        "1d4638",
    ),
    Section("Integral representations"),
    Entries(
        "8c96a5",
        "95f771",
        "b64782",
        "6395ee",
    ),
    Section("Bounds and inequalities"),
    Subsection("Upper and lower bounds"),
    Entries(
        "4a3612",
        "3544a0",
    ),
    Subsection("Monotonicity and convexity"),
    Entries(
        "7df1c4",
        "1c770c",
        "306699",
    ),
    Section("Matrix formulas"),
    Entries(
        "dc6806",
    ),
)

# Definitions

make_entry(ID("82a1b1"),
    SymbolDefinition(BarnesG, BarnesG(z), "Barnes G-function"),
    Description(SourceForm(BarnesG(z)), ", rendered as", BarnesG(z), ", represents the Barnes G-function of argument", z, "."))

make_entry(ID("da1509"),
    SymbolDefinition(LogBarnesG, LogBarnesG(z), "Logarithmic Barnes G-function"),
    Description(SourceForm(LogBarnesG(z)), ", rendered as", LogBarnesG(z), ", represents the logarithmic Barnes G-function of argument", z, "."))

# Illustrations

make_entry(ID("488c5c"),
    Image(Description("Plot of", BarnesG(x), "on", Element(x, ClosedInterval(-4,6))),
        ImageSource("plot_barnes_g")),
    )

make_entry(ID("106bf7"),
    Image(Description("X-ray of", BarnesG(z), "on", Element(z, ClosedInterval(-4,6) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_barnes_g")),
    description_xray,
    )

make_entry(ID("e1497f"),
    Image(Description("X-ray of", LogBarnesG(z), "on", Element(z, ClosedInterval(-4,6) + ClosedInterval(-5,5)*ConstI)),
        ImageSource("xray_log_barnes_g")),
    description_xray,
    )

# Domain

make_entry(ID("f3f0a7"),
    Formula(Implies(Element(x, RR), Element(BarnesG(x), RR))),
    Variables(x))

make_entry(ID("3d46ea"),
    Formula(Implies(Element(n, ZZ), Element(BarnesG(n), ZZGreaterEqual(0)))),
    Variables(n))

make_entry(ID("8ec739"),
    Formula(Implies(Element(z, CC), Element(BarnesG(z), CC))),
    Variables(z))

make_entry(ID("971881"),
    Formula(IsHolomorphic(BarnesG(z), ForElement(z, CC))))

make_entry(ID("19b40f"),
    Formula(Implies(Element(x, OpenInterval(0,Infinity)), Element(LogBarnesG(x), RR))),
    Variables(x))

make_entry(ID("a471d0"),
    Formula(Implies(Element(z, SetMinus(CC, ZZLessEqual(0))), Element(LogBarnesG(z), CC))),
    Variables(z))

make_entry(ID("037342"),
    Formula(IsHolomorphic(LogBarnesG(z), ForElement(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))),
    Variables(z))

make_entry(ID("62bdb8"),
    Formula(Implies(Element(z, ZZLessEqual(0)), Element(LogBarnesG(z), Set(-Infinity)))),
    Variables(z))

# Logarithmic form

make_entry(ID("b4355e"),
    Formula(Equal(BarnesG(z), Exp(LogBarnesG(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# todo: all R if -inf + c = -inf defined (...)
make_entry(ID("5a11eb"),
    Formula(Equal(LogBarnesG(x), Where(Cases(Tuple(Log(BarnesG(x)), Greater(x, 0)),
        Tuple(Log(Abs(BarnesG(x))) + Div(1,2)*n*(n-1)*ConstPi*ConstI, Otherwise)), Equal(n, Floor(x))))),
    Variables(x),
    Assumptions(And(Element(x, RR), NotElement(x, ZZLessEqual(0)))))

make_entry(ID("d9a7a3"),
    Formula(Implies(Or(Element(z, OpenInterval(0, Infinity)), Less(Abs(z-Decimal("2.5")), Decimal("2.5"))),
        Equal(LogBarnesG(z), Log(BarnesG(z))))),
    Variables(z),
    Assumptions(Element(z, CC)))


# Singularities and zeros

## Zeros

make_entry(ID("e488dc"),
    Formula(Equal(Zeros(BarnesG(z), ForElement(z, CC)), ZZLessEqual(0))))

make_entry(ID("f77124"),
    Formula(Equal(ComplexZeroMultiplicity(BarnesG(z), For(z, -n)), n+1)),
    Variables(n),
    Assumptions(And(Element(n, ZZGreaterEqual(0)))))

make_entry(ID("2b021c"),
    Formula(Equal(Zeros(LogBarnesG(z), ForElement(z, CC)), Set(1, 2, 3))))

## Branch cuts

make_entry(ID("c3e340"),
    Formula(Equal(BranchPoints(LogBarnesG(z), z, CC), ZZLessEqual(0))))

make_entry(ID("e1f73d"),
    Formula(Equal(BranchCuts(LogBarnesG(z), z, CC), Set(OpenInterval(-n-1,-n), ForElement(n, ZZGreaterEqual(0))))))

make_entry(ID("a044e1"),
    Formula(Equal(Im(LogBarnesG(x)), Where((n*(n-1))/2 * ConstPi, Equal(n, Floor(x))))),
    Variables(x),
    Assumptions(And(Element(x, RR), Less(x, 0), NotElement(x, ZZ))))

make_entry(ID("cc3a51"),
    Formula(Equal(RightLimit(Brackets(LogBarnesG(x+epsilon*ConstI)), For(epsilon, 0)), LogBarnesG(x))),
    Variables(x),
    Assumptions(And(Element(x, RR), Less(x, 0), NotElement(x, ZZ))))

make_entry(ID("d35c54"),
    Formula(Equal(RightLimit(Brackets(LogBarnesG(x-epsilon*ConstI)), For(epsilon, 0)), Conjugate(LogBarnesG(x)), Where(LogBarnesG(x) - n*(n-1)*ConstPi*ConstI, Equal(n, Floor(x))))),
    Variables(x),
    Assumptions(And(Element(x, RR), Less(x, 0), NotElement(x, ZZ))))

# Specific values

make_entry(ID("33f13a"),
    Formula(Equal(BarnesG(n), Cases(Tuple(Product(Factorial(k), For(k, 1, n-2)), GreaterEqual(n, 1)),
        Tuple(0, LessEqual(n, 0))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("daef08"),
    Formula(Equal(LogBarnesG(n), Cases(Tuple(Log(BarnesG(n)), GreaterEqual(n, 1)),
        Tuple(-Infinity, LessEqual(n, 0))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("5cb675"),
    Description("Table of", BarnesG(n), "for", LessEqual(0, n, 15)),
    Table(
      Var(n),
      TableValueHeadings(n, BarnesG(n)),
      TableSplit(1),
      List(
    Tuple(0, 0),
    Tuple(1, 1),
    Tuple(2, 1),
    Tuple(3, 1),
    Tuple(4, 2),
    Tuple(5, 12),
    Tuple(6, 288),
    Tuple(7, 34560),
    Tuple(8, 24883200),
    Tuple(9, 125411328000),
    Tuple(10, 5056584744960000),
    Tuple(11, 1834933472251084800000),
    Tuple(12, 6658606584104736522240000000),
    Tuple(13, 265790267296391946810949632000000000),
    Tuple(14, 127313963299399416749559771247411200000000000),
    Tuple(15, 792786697595796795607377086400871488552960000000000000),
    )))

make_entry(ID("dbc117"),
    Description("Table of", BarnesG(10**n), "to 50 digits for", LessEqual(0, n, 10)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(BarnesG(10**n), 50)),
      TableSplit(1),
      List(
    Tuple(0, Decimal("1")),
    Tuple(1, Decimal("5056584744960000")),
    Tuple(2, Decimal("3.1036100626369830847879402668101769402280611882492e+6626")),
    Tuple(3, Decimal("2.0045690761252153894020068969764708165025223902021e+1172113")),
    Tuple(4, Decimal("7.8913000980387915476627721291099032636382430763247e+167396248")),
    Tuple(5, Decimal("6.0203407218068785584794013164002058716523147916958e+21742374725")),
    Tuple(6, Decimal("1.0145655480290378725684376810089100792606395451713e+2674273971959")),
    Tuple(7, Decimal("5.2418488985408575463326646933057662934049190054866e+317427852191102")),
    Tuple(8, Decimal("5.7976150706924830557487583722980527113426519510559e+36742790669064055")),
    Tuple(9, Decimal("4.1978917865925966071745800658793636650835499429177e+4174279130405945548")),
    Tuple(10, Decimal("4.8323663133177075948431502316007152775466606093624e+467427913765589957090")),
    )))

make_entry(ID("8b7991"),
    Formula(Equal(BarnesG(Div(1,2)), (2**Div(1,24) * Exp(Div(1,8))) / (ConstPi**Div(1,4) * ConstGlaisher**Div(3,2)))))

make_entry(ID("ce66a9"),
    Formula(Equal(BarnesG(Div(1,4)), ConstE**(Div(3,32)-ConstCatalan/(4*ConstPi))/(ConstGlaisher**Div(9,8)*GammaFunction(Div(1,4))**Div(3,4)))))

make_entry(ID("dc507f"),
    Formula(Equal(BarnesG(Div(3,4)), (ConstE**(Div(3,32)+ConstCatalan/(4*ConstPi)) * GammaFunction(Div(1,4))**Div(1,4)) / (2**Div(1,8)*ConstPi**Div(1,4)*ConstGlaisher**Div(9,8)))))

make_entry(ID("90b367"),
    Formula(Equal(ComplexDerivative(BarnesG(z), For(z, 0)), 1)))

make_entry(ID("dbfd5b"),
    Formula(Equal(ComplexDerivative(BarnesG(z), For(z, 1)), (Log(2*ConstPi)-1)/2)))

make_entry(ID("a54fb0"),
    Formula(Equal(ComplexDerivative(BarnesG(z), For(z, 2)), (Log(2*ConstPi)-1)/2 - ConstGamma)))

make_entry(ID("f50c74"),
    Formula(Equal(ComplexDerivative(BarnesG(z), For(z, n)), Cases(
        Tuple(0, Less(n, 0)),
        Tuple(1, Equal(n, 0)),
        Tuple(Div(1,2)*(Log(2*ConstPi)-1), Equal(n, 1)),
        Tuple(BarnesG(n)*((Div(1,2)*Log(2*ConstPi)+(n-1)*(HarmonicNumber(n-2)-ConstGamma-1)+Div(1,2))), GreaterEqual(n, 2))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Functional equations

## Recurrence relation

make_entry(ID("86b3ec"),
    Formula(Equal(BarnesG(z+1), GammaFunction(z) * BarnesG(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("5261e3"),
    Formula(Equal(LogBarnesG(z+1), LogGamma(z) + LogBarnesG(z))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("7a36e5"),
    Formula(Equal(BarnesG(z+n), Brackets(Product((z+k-1)**(n-k), For(k, 1, n))) * GammaFunction(z)**n * BarnesG(z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)), Element(n, ZZGreaterEqual(0)))))

## Reflection formula

make_entry(ID("541e2e"),
    Formula(Equal(BarnesG(1-x), (-1)**(Floor((x-1)/2)+1) * BarnesG(1+x) * (Abs(Sin(ConstPi*x))/ConstPi)**x * Exp((1/(2*ConstPi)) * Im(PolyLog(2, Exp(2*ConstPi*ConstI*x)))))),
    Variables(x),
    Assumptions(And(Element(x, RR), NotElement(x, ZZLessEqual(-1)))),
    References("https://doi.org/10.1145/384101.384104"))

make_entry(ID("d1a0ec"),
    Formula(Equal(LogBarnesG(1-x), LogBarnesG(1+x) + Log(Abs(Sin(ConstPi*x))/ConstPi) * (1/(2*ConstPi)) * Im(PolyLog(2, Exp(2*ConstPi*ConstI*x)))
        + Where(Sign(x) * (n*(n+1)) * (ConstPi * ConstI / 2), Equal(n, Floor(x))))),
    Variables(x),
    Assumptions(And(Element(x, RR), NotElement(x, ZZ))))

make_entry(ID("b6017f"),
    Formula(Equal(LogBarnesG(1-z), LogBarnesG(1+z) - Log(2*ConstPi)*z + Integral(ConstPi*x*Cot(ConstPi*x), For(x, 0, z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, Union(OpenClosedInterval(-Infinity, -1), ClosedOpenInterval(1, Infinity))))))

make_entry(ID("23ed69"),
    Formula(Equal(LogBarnesG(1-z), LogBarnesG(1+z) - Log(2*ConstPi)*z + Cases(
        Tuple(Integral(ConstPi*x*Cot(ConstPi*x), For(x, 0, ConstI)) + Integral(ConstPi*x*Cot(ConstPi*x), For(x, ConstI, z)), Or(Less(-1, Re(z), 1), Greater(Im(z), 0), And(Equal(Im(z), 0), Less(Re(z), 1)))),
        Tuple(Integral(ConstPi*x*Cot(ConstPi*x), For(x, 0, -ConstI)) + Integral(ConstPi*x*Cot(ConstPi*x), For(x, -ConstI, z)), Or(Less(-1, Re(z), 1), Less(Im(z), 0), And(Equal(Im(z), 0), Greater(Re(z), -1)))))
    )),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZ))))

make_entry(ID("82b410"),
    Formula(Equal(LogBarnesG(1-z), LogBarnesG(1+z) + Where(Cases(
        Tuple(F(z), Or(Less(0, Re(z), 1), Greater(Im(z), 0), And(Equal(Im(z), 0), Less(Re(z), 1)))),
        Tuple(-F(-z), Or(Less(-1, Re(z), 0), Less(Im(z), 0), And(Equal(Im(z), 0), Greater(Re(z), -1))))),
            Equal(F(z), ((ConstPi*ConstI)/2)*(z**2-z+Div(1,6)) - z*(LogGamma(z)+LogGamma(1-z)) - (ConstI/(2*ConstPi)) * PolyLog(2, Exp(2*ConstPi*ConstI*z)))),
    )),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZ))))

## Multiplication theorem

make_entry(ID("ea26d4"),
    Formula(Equal(BarnesG(n*z), ConstE**((Log(ConstGlaisher)-Div(1,12))*(n**2-1))*n**(n**2*z**2/2-n*z+Div(5,12))*(2*ConstPi)**((n-1)*(1-n*z)/2) *
        Product(Product(BarnesG(z+(i+j)/n), For(j, 0, n-1)), For(i, 0, n-1)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(1)))),
    References("https://arxiv.org/abs/math/0308086"))

## Conjugate symmetry

make_entry(ID("147db6"),
    Formula(Equal(BarnesG(Conjugate(z)), Conjugate(BarnesG(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("6c6d3e"),
    Formula(Equal(LogBarnesG(Conjugate(z)), Cases(
        Tuple(LogBarnesG(z), Element(z, OpenClosedInterval(-Infinity, 0))),
        Tuple(Conjugate(LogBarnesG(z)), Otherwise)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Derivatives and differential equations

make_entry(ID("5babc2"),
    Formula(Equal(ComplexDerivative(BarnesG(z), For(z, z)), BarnesG(z) * ((z-1)*DigammaFunction(z) - z + (Log(2*ConstPi) + 1)/2))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

make_entry(ID("af31ae"),
    Formula(Equal(ComplexBranchDerivative(Brackets(LogBarnesG(z)), For(z, z)), (z-1)*DigammaFunction(z) - z + (Log(2*ConstPi) + 1)/2)),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

# Representation by other functions

make_entry(ID("e05807"),
    Formula(Equal(LogBarnesG(z), (z-1)*LogGamma(z) - Derivative(HurwitzZeta(s,z), For(s,-1)) + Derivative(RiemannZeta(s), For(s,-1)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, ZZLessEqual(0)))))

# Series representations

make_entry(ID("0ad263"),
    Formula(Equal(LogBarnesG(1+z), (Log(2*ConstPi)-1)/2 * z - (1+ConstGamma)/2 * z**2 + Sum((-1)**(n+1) * RiemannZeta(n-1) / n * z**n, For(n, 3, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1))))

make_entry(ID("54d4e2"),
    Formula(Equal(BarnesG(z+1), (2*ConstPi)**(z/2) * Exp(-((z+(ConstGamma+1)*z**2)/2)) * Product(Brackets((1+z/k)**k * Exp(z**2/(2*k)-z)), For(k, 1, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

## Asymptotic expansion

make_entry(ID("752bde"),
    SymbolDefinition(LogBarnesGRemainder, LogBarnesGRemainder(N, z), "Remainder term in asymptotic expansion of logarithmic Barnes G-function"))

make_entry(ID("6f8e14"),
    Formula(Equal(LogBarnesG(z+1), z**2/4 + z*LogGamma(z+1) - (z*(z+1)/2 + Div(1,12)) * Log(z) - Log(ConstGlaisher) + Sum(BernoulliB(2*n+2)/(2*n*(2*n+1)*(2*n+2)*z**(2*n)), For(n, 1, N-1))
        + LogBarnesGRemainder(N, z))),
    Variables(z, N),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), Element(N, ZZGreaterEqual(1)))),
    References("https://dx.doi.org/10.1098/rspa.2014.0534"))

make_entry(ID("b16d00"),
    Formula(Equal(LogBarnesGRemainder(N, z),
        Integral(((t/2)*Coth(t/2) - Sum(BernoulliB(2*k) / Factorial(2*k) * t**(2*k))) * (Exp(-(z*t))/t**3), For(t, 0, Infinity)))),
    Variables(z, N),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0), Element(N, ZZGreaterEqual(1)))),
    References("https://dx.doi.org/10.1098/rspa.2014.0534"))

make_entry(ID("092cee"),
    Formula(Equal(LogBarnesGRemainder(N, z),
        (1/z**(2*N)) * ((-1)**(N+1) / ConstPi) * Integral((t**(2*N-1)/(1+(t/z)**2)) * PolyLog(2, Exp(-(2*ConstPi*t))), For(t, 0, Infinity)))),
    Variables(z, N),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0), Element(N, ZZGreaterEqual(1)))),
    References("https://dx.doi.org/10.1098/rspa.2014.0534"))

# todo: alternative form is also given
make_entry(ID("645c98"),
    Formula(Equal(LogBarnesGRemainder(N, z),
        1/(2*N*(2*N+1)) * Integral(BernoulliPolynomial(2*N+1, t-Floor(t))/(t+z)**(2*N), For(t, 0, Infinity)))),
    Variables(z, N),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0), Element(N, ZZGreaterEqual(1)))),
    References("https://dx.doi.org/10.1098/rspa.2014.0534"))

make_entry(ID("1d4638"),
    Formula(LessEqual(Abs(LogBarnesGRemainder(N, z)),
        Abs(BernoulliB(2*N+2))/(2*N*(2*N+1)*(2*N+2)*Abs(z)**(2*N)) * Cases(Tuple(1, LessEqual(Abs(Arg(z)), ConstPi/4)), Tuple(Sec(Div(1,2)*Arg(z))**(2*N+1), Less(Abs(Arg(z)), ConstPi))))),
    Variables(z, N),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, 0)), Element(N, ZZGreaterEqual(1)))),
    References("https://dx.doi.org/10.1098/rspa.2014.0534"))

# Integral representations

make_entry(ID("8c96a5"),
    Formula(Equal(LogBarnesG(z+1), z*(1-z)/2 + z/2*Log(2*ConstPi) + z*LogGamma(z) - Integral(LogGamma(x), For(x, 0, z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, -1)))),
    References("https://arxiv.org/abs/math/0308086"))

make_entry(ID("95f771"),
    Formula(Equal(LogBarnesG(z+1), z*(1-z)/2 + z/2*Log(2*ConstPi) + Integral(x*DigammaFunction(x), For(x, 0, z)))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, OpenClosedInterval(-Infinity, -1)))),
    References("https://arxiv.org/abs/math/0308086"))

make_entry(ID("b64782"),
    Formula(Equal(LogBarnesG(z+1), z**2/4*(2*Log(z)-3)+z*Log(2*ConstPi)/2+Div(1,12)-Log(ConstGlaisher)-Integral(x*Log(x**2+z**2)/(Exp(2*ConstPi*x)-1), For(x, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))),
    References("https://arxiv.org/abs/math/0308086"))

make_entry(ID("6395ee"),
    Formula(Equal(LogBarnesG(z+1), z*LogGamma(z)+z**2/4-Log(z)/2*BernoulliPolynomial(2,z)-Log(ConstGlaisher)-Integral((Exp(-z*x)/x**2)*(1/(1-Exp(-x))-1/x-Div(1,2)-x/12), For(x, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))),
    References("https://arxiv.org/abs/math/0308086"))

# Bounds and inequalities

make_entry(ID("4a3612"),
    Formula(Less(LogBarnesG(x+1), (x**2/2-Div(1,12))*Log(x) - 3*x**2/4 + (Log(2*ConstPi)/2)*x + Div(1,12) - Log(ConstGlaisher))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))),
    References("https://dx.doi.org/10.1098/rspa.2014.0534"))

make_entry(ID("3544a0"),
    Formula(Greater(LogBarnesG(x+1), (x**2/2-Div(1,12))*Log(x) - 3*x**2/4 + (Log(2*ConstPi)/2)*x + Div(1,12) - Log(ConstGlaisher) - 1/(240*x**2))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))),
    References("https://dx.doi.org/10.1098/rspa.2014.0534"))

make_entry(ID("7df1c4"),
    Formula(Greater(BarnesG(x), 0)),
    Variables(x),
    Assumptions(Element(x, OpenInterval(0, Infinity))))

make_entry(ID("1c770c"),
    Formula(Where(Implies(Greater(x, Subscript(x, 0)), Greater(RealDerivative(BarnesG(x), For(x, x, n)), 0)),
        Equal(Subscript(x, 0), Cases(
            Tuple(0, Equal(n, 0)),
            Tuple(Decimal("2.557664"), Equal(n, 1)),
            Tuple(Decimal("1.898850"), Equal(n, 2)),
            Tuple(Decimal("0.788740"), Equal(n, 3)))))),
    Variables(x, n),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(n, Set(0, 1, 2, 3)))))

make_entry(ID("306699"),
    Formula(Where(Implies(Greater(x, Subscript(x, 0)), Greater(RealDerivative(Brackets(LogBarnesG(x)), For(x, x, n)), 0)),
        Equal(Subscript(x, 0), Cases(
            Tuple(3, Equal(n, 0)),
            Tuple(Decimal("2.557664"), Equal(n, 1)),
            Tuple(Decimal("1.925864"), Equal(n, 2)),
            Tuple(0, Equal(n, 3)))))),
    Variables(x, n),
    Assumptions(And(Element(x, OpenInterval(0, Infinity)), Element(n, Set(0, 1, 2, 3)))))


