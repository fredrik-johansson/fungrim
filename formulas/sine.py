from .expr import *

def_Topic(
    Title("Sine"),
    Section("Definition"),
    Entries(
        "b63dce",
    ),
    Section("Differential equations"),
    Entries(
        "21f156",
        "984d9c",
        "f1691f",
    ),
    Section("Specific values"),
    Entries(
        "c52772",
        "e2161b",
        "69c5ef",
        "56667c",
        "3c833f",
        "5fc688",
        "ad6b74",
        "c62afa",
        "506d0c",
        "09cd0b",
        "713501",
        "056c0e",
        "2f6818",
        "c5bdcc",
        "ad04bd",
        "bfe28b",
        "27766c",
    ),
    Section("Analytic properties"),
    Entries(
        "114913",
        "f4cc9e",
        "6aa0bc",
        "96550d",
        "a45c61",
    ),
    Section("Symmetry and periodicity"),
    Entries(
        "a2a30d",
        "82c83f",
        "6a8889",
        "393b62",
        "1c22f1",
        "9cc0f2",
        "bae475",
        "da58f7",
    ),
    Section("Addition and multiplication formulas"),
    Entries(
        "742943",
        "508e2c",
        "3b839c",
        "755655",
        "1b11be",
        "729215",
        "e3f8a4",
        "d59bd9",
        "e69cf6",
        "ad6c1c",
        "012eba",
        "f183d0",
        "6c3ba9",
        "adbc1a",
    ),
    Section("Powers"),
    Entries(
        "4948ea",
        "954066",
        "244127",
        "cf6e35",
        "acf63c",
        "2a6702",
        "54f420",
        "71a264",
        "d0505f",
        "2392f5",
        "f6d0c6",
    ),
    Section("Sums and products"),
    Entries(
        "b8ab9c",
        "906569",
    ),
    Section("Representations through other functions"),
    Entries(
        "925e5b",
        "3fb3ca",
        "18f40c",
        "299209",
        "cfc5c3",
        "54daa9",
        "0fbd15",
        "d38a03",
    ),
    Section("Complex parts"),
    Entries(
        "729b70",
        "037a6e",
        "abaf91",
    ),
    Section("Derivatives and integrals"),
    Entries(
        "f7ab32",
        "297b3c",
        "612b21",
        "a6667d",
        "d81355",
        "c93b81",
#        "3c7c4c",
    ),
    Section("Series expansions"),
    Entries(
        "f340cb",
        "6b13be",
        "11687b",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "4039ec",
        "c47a86",
        "f77752",
        "dd5787",
        "3dd162",
        "092377",
        "1721bf",
        "941a86",
        "f3a901",
        "03f713",
    ),
)

make_entry(ID("b63dce"),
    SymbolDefinition(Sin, Sin(z), "Sine"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(Element(z, RR), Element(Sin(z), ClosedInterval(-1, 1))),
        Tuple(Element(z, CC), Element(Sin(z), CC)),
        TableSection("Formal power series"),
        Tuple(Element(z, FormalPowerSeries(RR, x)), Element(Sin(z), FormalPowerSeries(RR, x))),
        Tuple(Element(z, FormalPowerSeries(CC, x)), Element(Sin(z), FormalPowerSeries(CC, x))),
      )))

# Differential equations

C_1 = Subscript(c, 1)
C_2 = Subscript(c, 2)

make_entry(ID("21f156"),
    Formula(Equal(Derivative(Sin(z), Tuple(z, z, 2)) + Sin(z), 0)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("984d9c"),
    Formula(Where(Equal(Derivative(y(z), Tuple(z, z, 2)) + y(z), 0), Equal(y(z), C_1 * Sin(z) + C_2 * Cos(z)))),
    Variables(z, C_1, C_2),
    Assumptions(And(Element(z, CC), Element(C_1, CC), Element(C_2, CC))))

make_entry(ID("f1691f"),
    Formula(Where(Equal(Derivative(y(z), Tuple(z, z, 2)) + a**2 * y(z) + b, 0), Equal(y(z), C_1 * Sin(a*z) + C_2 * Cos(a*z) - b/a**2))),
    Variables(z, a, b, C_1, C_2),
    Assumptions(And(Element(z, CC), Element(a, SetMinus(CC, Set(0))), Element(b, CC), Element(C_1, CC), Element(C_2, CC))))

# Specific values

make_entry(ID("c52772"),
    Formula(Equal(Sin(0), 0)))

make_entry(ID("e2161b"),
    Formula(Equal(Sin(ConstPi), 0)))

make_entry(ID("69c5ef"),
    Formula(Equal(Sin(ConstPi/2), 1)))

make_entry(ID("56667c"),
    Formula(Equal(Sin(3*ConstPi/2), -1)))

make_entry(ID("3c833f"),
    Formula(Equal(Sin(ConstPi/3), Sqrt(3)/2)))

make_entry(ID("5fc688"),
    Formula(Equal(Sin(ConstPi/4), Sqrt(2)/2)))

make_entry(ID("ad6b74"),
    Formula(Equal(Sin(ConstPi/6), Div(1,2))))

make_entry(ID("c62afa"),
    Formula(Equal(Sin(ConstPi*k), 0)),
    Variables(k),
    Element(k, ZZ))

make_entry(ID("506d0c"),
    Formula(Equal(Sin(ConstPi/2 + ConstPi*k), (-1)**k)),
    Variables(k),
    Element(k, ZZ))


make_entry(ID("09cd0b"),
    Formula(NotElement(Sin(alpha), AlgebraicNumbers)),
    References("Consequence of the Lindemann-Weierstrass theorem."),
    Variables(alpha),
    Assumptions(Element(alpha, SetMinus(AlgebraicNumbers, Set(0)))))

make_entry(ID("713501"),
    Formula(Element(Sin(ConstPi * x), AlgebraicNumbers)),
    Variables(x),
    Assumptions(Element(x, QQ)))

make_entry(ID("056c0e"),
    Formula(Implies(And(Element(x, QQ), Element(Sin(ConstPi*x), QQ)), Element(Sin(ConstPi*x), Set(0, Div(1,2), -Div(1,2), 1, -1)))),
    References("Niven's theorem"))

make_entry(ID("2f6818"),
    Formula(Equal(Zeros(Brackets(Sin(z)), z, Element(z, CC)), SetBuilder(ConstPi * n, n, Element(n, ZZ)))))

make_entry(ID("c5bdcc"),
    Formula(Equal(ArgMax(Brackets(Sin(x)), x, Element(x, RR)), SetBuilder(ConstPi * (2 * n + Div(1,2)), n, Element(n, ZZ)))))

make_entry(ID("ad04bd"),
    Formula(Equal(ArgMin(Brackets(Sin(x)), x, Element(x, RR)), SetBuilder(ConstPi * (2 * n - Div(1,2)), n, Element(n, ZZ)))))

make_entry(ID("bfe28b"),
    Formula(Equal(Maximum(Brackets(Sin(x)), x, Element(x, RR)), 1)))

make_entry(ID("27766c"),
    Formula(Equal(Minimum(Brackets(Sin(x)), x, Element(x, RR)), -1)))

# Analytic properties

make_entry(ID("114913"),
    Formula(Equal(HolomorphicDomain(Sin(z), z, Union(CC, Set(UnsignedInfinity))), CC)))

make_entry(ID("f4cc9e"),
    Formula(Equal(Poles(Sin(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("6aa0bc"),
    Formula(Equal(EssentialSingularities(Sin(z), z, Union(CC, Set(UnsignedInfinity))), Set(UnsignedInfinity))))

make_entry(ID("96550d"),
    Formula(Equal(BranchPoints(Sin(z), z, Union(CC, Set(UnsignedInfinity))), Set())))

make_entry(ID("a45c61"),
    Formula(Equal(BranchCuts(Sin(z), z, CC), Set())))

# Symmetry and periodicity

make_entry(ID("a2a30d"),
    Formula(Equal(Sin(-z), -Sin(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("82c83f"),
    Formula(Equal(Sin(Conjugate(z)), Conjugate(Sin(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("6a8889"),
    Formula(Equal(Sin(z + 2*ConstPi*k), Sin(z))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZ))))

make_entry(ID("393b62"),
    Formula(Equal(Sin(z + ConstPi*k), (-1)**k * Sin(z))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZ))))

make_entry(ID("1c22f1"),
    Formula(Equal(Sin(ConstPi + z), -Sin(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("9cc0f2"),
    Formula(Equal(Sin(ConstPi - z), Sin(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("bae475"),
    Formula(Equal(Sin(ConstPi/2 + z), Cos(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("da58f7"),
    Formula(Equal(Sin(ConstPi/2 - z), Cos(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Addition and multiplication formulas

make_entry(ID("742943"),
    Formula(Equal(Sin(a+b), Sin(a)*Cos(b) + Cos(a)*Sin(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("508e2c"),
    Formula(Equal(Sin(a-b), Sin(a)*Cos(b) - Cos(a)*Sin(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("3b839c"),
    Formula(Equal(Sin(a+b*ConstI), Sin(a)*Cosh(b) + ConstI*Cos(a)*Sinh(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("755655"),
    Formula(Equal(Sin(ConstI*z), ConstI*Sinh(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("1b11be"),
    Formula(Equal(Sin(2*z), 2*Sin(z)*Cos(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("729215"),
    Formula(Equal(Sin(3*z), 3*Sin(z) - 4*Sin(z)**3)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e3f8a4"),
    Formula(Equal(Sin(n*z), Sum((-1)**k * Binomial(n, 2*k+1) * Cos(z)**(n-2*k-1) * Sin(z)**(2*k+1), Tuple(k, 0, Floor((n-1)/2))))),
    Variables(n, z),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("d59bd9"),
    Formula(Equal(Sin(a) + Sin(b), 2*Sin((a+b)/2)*Cos((a-b)/2))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("e69cf6"),
    Formula(Equal(Sin(a) - Sin(b), 2*Cos((a+b)/2)*Sin((a-b)/2))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("ad6c1c"),
    Formula(Equal(Sin(a)*Sin(b), (Cos(a-b) - Cos(a+b))/2)),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("012eba"),
    Formula(Equal(Sin(a)*Cos(b), (Sin(a+b) + Sin(a-b))/2)),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("f183d0"),
    Formula(Equal(Sin(z) + Cos(z), Sqrt(2) * Sin(z + ConstPi / 4))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("6c3ba9"),
    Formula(Equal(Sin(z) - Cos(z), Sqrt(2) * Sin(z - ConstPi / 4))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("adbc1a"),
    Formula(Equal(Cos(z) + ConstI * Sin(z), Exp(ConstI*z))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Powers

make_entry(ID("4948ea"),
    Formula(Equal(Sin(z)**2 + Cos(z)**2, 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("954066"),
    Formula(Equal(Sin(z)**2 - Cos(z)**2, -Cos(2*z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("244127"),
    Formula(Equal(Sin(z)**2, 1 - Cos(z)**2)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("cf6e35"),
    Formula(Equal(Sin(z)**2, (1 - Cos(2*z))/2)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("acf63c"),
    Formula(Equal(Sin(z)**2, Tan(z)**2 / (1 + Tan(z)**2))),
    Variables(z),
    Assumptions(And(Element(z, CC),
        NotElement(z, SetBuilder((2*n+1)*ConstPi/2, n, Element(n, ZZ))))))

make_entry(ID("2a6702"),
    Formula(Equal(Sin(z)**3, (3*Sin(z) - Sin(3*z))/4)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("54f420"),
    Formula(Equal(Sin(z)**(2*n), 1/4**n * Binomial(2*n, n) + 2/4**n * Sum((-1)**(n+k) * Binomial(2*n, k) * Cos(2*(n-k)*z), Tuple(k, 0, n-1)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("71a264"),
    Formula(Equal(Sin(z)**(2*n+1), 1/4**n * Sum((-1)**(n+k) * Binomial(2*n+1, k) * Sin((2*n-2*k+1)*z), Tuple(k, 0, n)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("d0505f"),
    Formula(Equal((Cos(z) + ConstI * Sin(z))**n, Cos(n*z) + ConstI*Sin(n*z))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZ))))

make_entry(ID("2392f5"),
    Formula(Equal(Sin(a)**2 - Sin(b)**2, Sin(a+b)*Sin(a-b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

make_entry(ID("f6d0c6"),
    Formula(Equal(Sin(a)**2 - Cos(b)**2, -Cos(a+b)*Cos(a-b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

# Sums and products

make_entry(ID("b8ab9c"),
    Formula(Equal(Sum(Sin(2*a*k+b), Tuple(k, 0, n)), Sin(a*(n+1)) * Sin(a*n+b) / Sin(a))),
    Variables(a, n),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), NotElement(a / ConstPi, ZZ))))

make_entry(ID("906569"),
    Formula(Equal(Product(Sin(k*ConstPi/n), Tuple(k, 1, n-1)), n/2**(n-1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

# Representations through other functions

make_entry(ID("925e5b"),
    Formula(Equal(Sin(z), Cos(ConstPi/2-z), Cos(z-ConstPi/2), -Cos(z+ConstPi/2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("3fb3ca"),
    Formula(Equal(Sin(z), (2*Tan(z/2))/(Tan(z/2)**2 + 1))),
    Variables(z),
    Assumptions(And(Element(z, CC), NotElement(z, SetBuilder((2*n+1)*ConstPi, n, Element(n, ZZ)))),
        And(Element(z, FormalPowerSeries(CC, x)), NotElement(z, SetBuilder((2*n+1)*ConstPi, n, Element(n, ZZ))))))

make_entry(ID("18f40c"),
    Formula(Equal(Sin(z), (Exp(ConstI*z) - Exp(-ConstI*z)) / (2 * ConstI))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("299209"),
    Formula(Equal(Sin(x), Im(Exp(ConstI*x)))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("cfc5c3"),
    Formula(Equal(Sin(z), -ConstI * Sinh(ConstI * z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("54daa9"),
    Formula(Equal(Sin(z), z * Hypergeometric0F1(Div(3,2), -Div(1,4) * z**2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("0fbd15"),
    Formula(Equal(Sin(z), Sqrt(ConstPi * z / 2) * BesselJ(Div(1,2), z))),
    Variables(z),
    Assumptions(Element(z, CC)))

# todo: cos: 1/2+z, 1/2-z
make_entry(ID("d38a03"),
    Formula(Equal(Sin(ConstPi * z), ConstPi / (GammaFunction(z) * GammaFunction(1 - z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Complex parts

make_entry(ID("729b70"),
    Formula(Equal(Re(Sin(x+ConstI*y)), Sin(x)*Cosh(y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("037a6e"),
    Formula(Equal(Im(Sin(x+ConstI*y)), Cos(x)*Sinh(y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("abaf91"),
#    Formula(Equal(Abs(Sin(x+ConstI*y)), Sqrt(Sin(x)**2*Cosh(y)**2 + Cos(x)**2*Sinh(y)**2))),
    Formula(Equal(Abs(Sin(x+ConstI*y)), Sqrt(Sin(x)**2 + Sinh(y)**2))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

# Derivatives and integrals

make_entry(ID("f7ab32"),
    Formula(Equal(Derivative(Sin(z), Tuple(z, z, 1)), Cos(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("297b3c"),
    Formula(Equal(Derivative(Sin(z), Tuple(z, z, 2)), -Sin(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("612b21"),
    Formula(Equal(Derivative(Sin(z), Tuple(z, z, r)), Sin(z + ConstPi*r/2))),
    Variables(z, r),
    Assumptions(And(Element(z, CC), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("a6667d"),
    Formula(Equal(Derivative(Sin(z), Tuple(z, z, r+2)), -Derivative(Sin(z), Tuple(z, z, r)))),
    Variables(z, r),
    Assumptions(And(Element(z, CC), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("d81355"),
    Formula(Equal(Derivative(Sin(z), Tuple(z, z, r+4)), Derivative(Sin(z), Tuple(z, z, r)))),
    Variables(z, r),
    Assumptions(And(Element(z, CC), Element(r, ZZGreaterEqual(0)))))

make_entry(ID("c93b81"),
    Formula(Equal(Integral(Sin(z), Tuple(z, a, b)), Cos(a) - Cos(b))),
    Variables(a, b),
    Assumptions(And(Element(a, CC), Element(b, CC))))

#make_entry(ID("3c7c4c"),
#    Formula(Equal(Integral(z * Sin(z), Tuple(z, a, b)), Parentheses(Sin(b)-b*Cos(b)) - (Sin(a)-a*Cos(a)))),
#    Variables(a, b),
#    Assumptions(And(Element(a, CC), Element(b, CC))))


# Series expansions

make_entry(ID("f340cb"),
    Formula(Equal(Sin(z), Sum((-1)**k * (z**(2*k+1) / Factorial(2*k+1)), Tuple(k, 0, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("6b13be"),
    Formula(Equal(Sin(z + x), Sum(Sin(z + ConstPi * k / 2) * (x**k / Factorial(k)), Tuple(k, 0, Infinity)))),
    Variables(z, x),
    Assumptions(And(Element(z, CC), Element(x, CC))))

make_entry(ID("11687b"),
    Formula(Equal(Sin(z), z * Product(Parentheses(1 - z**2 / (ConstPi**2 * k**2)), Tuple(k, 1, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Bounds and inequalities

make_entry(ID("4039ec"),
    Formula(LessEqual(Abs(Sin(x)), 1)),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("c47a86"),
    Formula(LessEqual(Abs(Sin(x)), Abs(x))),
    Variables(x),
    Assumptions(Element(x, RR)))

make_entry(ID("f77752"),
    Formula(LessEqual(Abs(Sin(x+y*ConstI)), Cosh(y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("dd5787"),
    Formula(LessEqual(Abs(Sin(x+y*ConstI)), Exp(Abs(y)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("3dd162"),
    Formula(GreaterEqual(Abs(Sin(x+y*ConstI)), Sinh(Abs(y)))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("092377"),
    Formula(GreaterEqual(Abs(Sin(x+y*ConstI)), Abs(y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("1721bf"),
    Formula(LessEqual(Abs(Sin(z)), Sinh(Abs(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("941a86"),
    Formula(Less(Abs(Sin(z)), Exp(Abs(z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("f3a901"),
    Formula(LessEqual(Abs(Sin(x + y) - Sin(x)), 2)),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

make_entry(ID("03f713"),
    Formula(LessEqual(Abs(Sin(x + y) - Sin(x)), Abs(y))),
    Variables(x, y),
    Assumptions(And(Element(x, RR), Element(y, RR))))

