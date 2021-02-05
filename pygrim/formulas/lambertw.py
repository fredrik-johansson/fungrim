# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Lambert W-function"),
    Section("Definition"),
    Entries(
        "6da738",
    ),
    Section("Illustrations"),
    Entries(
        "cb0a9b",
    ),
    Section("Transcendental equations"),
    Entries(
        "88168b",
        "d7136f",
        "314807",
        "636929",
        "8654a3",
        "ed7dac",
        "30bd5b",
        "a172c7",
    ),
    Section("Specific values"),
    Entries(
        "0be17d",
        "c95c4f",
        "b93d09",
        "d09380",
        "5d4cce",
        "c87ff4",
        "8e8a59",
        "f372e9",
        "e1dd64",
    ),
    Section("Symmetry"),
    Entries(
        "6d936e",
    ),
    Section("Analytic properties"),
    Entries(
        "0d3b91",
        "2caf78",
        "aca420",
        "41ece5",
        "17eaad",
        "e6e7a2",
        "fdfb16",
        "276d78",
        "6191cd",
        "f0f17c",
        "766302",
    ),
    Section("Derivatives and integrals"),
    Entries(
        "8d486c",
        "72b6ca",
    ),
    Section("Series expansions"),
    Subsection("Taylor series"),
    Entries(
        "58c19a",
    ),
    Subsection("Puiseux series"),
    Entries(
        "c5a8c2",
        "0983d1",
        "d37d0f",
        "adf83a",
        "e50532",
        "99ff4c",
    ),
    Subsection("Logarithmic expansion"),
    Entries(
        "1fc63b",
        "da0f15",
    ),
    Section("Range"),
    Subsection("Tiling of the plane"),
    Entries(
        "c0ae5b",
        "6e05c9",
    ),
    Subsection("Image of the principal branch"),
    Entries(
        "ee86fb",
        "55498b",
        "44ad09",
        "2d3356",
    ),
    Subsection("Image of the non-principal branches"),
    Entries(
        "21d9a0",
        "d5917b",
        "bf3e29",
    ),
    Section("Bounds and inequalities"),
    Subsection("Complex parts"),
    Entries(
        "4257f4",
        "82926c",
        "e5bba3",
        "a68e0e",
    ),
    Subsection("Derivative bounds"),
    Entries(
        "f171a6",
        "a34260",
        "9be916",
        "b3d435",
        "8e06be",
        "72712c",
        "9136b9",
        "0eb699",
        "214b1c",
        "a1e634",
    ),
)

make_entry(ID("6da738"),
    SymbolDefinition(LambertW, LambertW(z), "Lambert W-function"),
    Description("Called with one argument", SourceForm(LambertW(z)), "(rendered", LambertW(z), ") represents the principal branch",
        "of the Lambert W-function."),
    Description("Called with two arguments", SourceForm(LambertW(z,k)), "(rendered", LambertW(z,k), ") represents the", k, "-th branch",
        "of the Lambert W-function."),
    Description("Called with three arguments", SourceForm(LambertW(z,k,r)), "(rendered", LambertW(z,k,r), ") represents the",
            r, "-th derivative of the", k, "-th branch of the Lambert W-function, with inherited branch cuts."),
    Description(SourceForm(LambertW(z,k)), "is equivalent to", SourceForm(LambertW(z,k,0)), "."),
    Description("The following table lists conditions such that", SourceForm(LambertW(z,k,r)), "is defined in Fungrim."),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        TableSection("Numbers"),
        Tuple(And(Element(k, ZZ), Element(z, SetMinus(CC, Set(0)))), Element(LambertW(z,k), CC)),
        Tuple(And(Element(k, ZZ), Element(z, SetMinus(CC, Set(0, -Exp(-1)))), Element(r, ZZGreaterEqual(0))), Element(LambertW(z,k,r), CC)),
        Tuple(Element(r, ZZGreaterEqual(0)), Element(LambertW(0,0,r), QQ)),
      )),
    )

make_entry(ID("cb0a9b"),
    Image(Description("X-ray of", LambertW(z), "on", Element(z, ClosedInterval(-3,3) + ClosedInterval(-3,3)*ConstI)),
        ImageSource("xray_lambertw")),
    description_xray,
    )

# Transcendental equations

make_entry(ID("88168b"),
    Formula(Equal(LambertW(z,k) * Exp(LambertW(z,k)), z)),
    Variables(k, z),
    Assumptions(Or(And(Element(k, ZZ), Element(z, SetMinus(CC, Set(0)))),
        And(Equal(k, 0), Equal(z, 0)))))

make_entry(ID("d7136f"),
    Formula(Equal(Solutions(Brackets(Equal(w * Exp(w), z)), ForElement(w, CC)),
        Set(LambertW(z,k), For(k), And(Element(k, ZZ), Or(NotEqual(z, 0), Equal(k, 0)))))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("314807"),
    Formula(Equal(UniqueSolution(Brackets(Equal(w * Exp(w), x)), ForElement(w, ClosedOpenInterval(-1, Infinity))),
        LambertW(x))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(-(1/ConstE), Infinity))))

make_entry(ID("636929"),
    Formula(Equal(UniqueSolution(Brackets(Equal(w * Exp(w), x)), ForElement(w, OpenClosedInterval(-Infinity, -1))),
        LambertW(x,-1))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(-(1/ConstE), 0))))

make_entry(ID("8654a3"),
    Formula(Equal(LambertW(x*Exp(x)), x)),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(-1, Infinity))))

make_entry(ID("ed7dac"),
    Formula(Equal(LambertW(x*Exp(x),-1), x)),
    Variables(x),
    Assumptions(Element(x, OpenClosedInterval(-Infinity, -1))))

make_entry(ID("30bd5b"),
    Formula(Equal(LambertW(x*Log(x)), Log(x))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(1/ConstE, Infinity))))

make_entry(ID("a172c7"),
    Formula(Equal(LambertW(x*Log(x),-1), Log(x))),
    Variables(x),
    Assumptions(Element(x, OpenClosedInterval(0, -(1/ConstE)))))

# Specific values

make_entry(ID("0be17d"),
    Formula(Equal(LambertW(0), 0)))

make_entry(ID("c95c4f"),
    Formula(Equal(LambertW(ConstE), 1)))

make_entry(ID("b93d09"),
    Formula(Equal(LambertW(-(1/ConstE)), -1)))

make_entry(ID("d09380"),
    Formula(Equal(LambertW(-(1/ConstE),-1), -1)))

make_entry(ID("5d4cce"),
    Formula(Element(LambertW(1), RealBall(Decimal("0.56714329040978387299996866221035554975381578718651"), Decimal("2.51e-51")))))

make_entry(ID("c87ff4"),
    Formula(Equal(LambertW(0,0,1), 1)))

make_entry(ID("8e8a59"),
    Formula(Equal(LambertW(0,0,r), (-r)**(r-1))),
    Variables(r),
    Assumptions(Element(r, ZZGreaterEqual(1))))

make_entry(ID("f372e9"),
    Formula(Equal(LambertW(0,k), -Infinity)),
    Variables(k),
    Assumptions(Element(k, SetMinus(ZZ, Set(0)))))

make_entry(ID("e1dd64"),
    Formula(Equal(LambertW(-(Pi/2)), ConstI*Pi/2)))


# Symmetry

make_entry(ID("6d936e"),
    Formula(Equal(LambertW(Conjugate(z),k), Conjugate(LambertW(z,-k)))),
    Variables(k, z),
    Assumptions(And(Element(k, ZZ), Element(z, CC),
        Or(And(Equal(k, 0), NotElement(z, OpenInterval(-Infinity, -Exp(-1)))),
           And(NotEqual(k, 0), NotElement(z, OpenClosedInterval(-Infinity, 0)))))))

# Analytic properties

make_entry(ID("0d3b91"),
    Formula(IsHolomorphic(LambertW(z), ForElement(z, SetMinus(CC, OpenClosedInterval(-Infinity, -Exp(-1)))))))

make_entry(ID("2caf78"),
    Formula(IsHolomorphic(LambertW(z,k), ForElement(z, SetMinus(CC, OpenClosedInterval(-Infinity, 0))))),
    Variables(k),
    Assumptions(Element(k, SetMinus(ZZ, Set(0)))))

make_entry(ID("aca420"),
    Formula(Equal(Poles(LambertW(z,k), ForElement(z, Union(CC, Set(UnsignedInfinity)))), Set())),
    Variables(k),
    Assumptions(Element(k, ZZ)))

make_entry(ID("41ece5"),
    Formula(Equal(BranchPoints(LambertW(z,0), z, Union(CC, Set(UnsignedInfinity))), Set(-Exp(-1), UnsignedInfinity))))

make_entry(ID("17eaad"),
    Formula(Equal(BranchPoints(LambertW(z,k), z, Union(CC, Set(UnsignedInfinity))), Set(0, -Exp(-1), UnsignedInfinity))),
    Variables(k),
    Assumptions(Element(k, Set(-1,1))))

make_entry(ID("e6e7a2"),
    Formula(Equal(BranchPoints(LambertW(z,k), z, Union(CC, Set(UnsignedInfinity))), Set(0, UnsignedInfinity))),
    Variables(k),
    Assumptions(Element(k, SetMinus(ZZ, Set(-1,0,1)))))

make_entry(ID("fdfb16"),
    Formula(Equal(BranchCuts(LambertW(z,0), z, CC), Set(OpenClosedInterval(-Infinity, -Exp(-1))))))

make_entry(ID("276d78"),
    Formula(Equal(BranchCuts(LambertW(z,k), z, CC), Set(OpenClosedInterval(-Infinity, -Exp(-1)), ClosedInterval(-Exp(-1), 0), OpenClosedInterval(-Infinity, 0)))),
    Variables(k),
    Assumptions(Element(k, Set(-1,1))))

make_entry(ID("6191cd"),
    Formula(Equal(BranchCuts(LambertW(z,k), z, CC), Set(OpenClosedInterval(-Infinity, 0)))),
    Variables(k),
    Assumptions(Element(k, SetMinus(ZZ, Set(-1,0,1)))))

make_entry(ID("f0f17c"),
    Formula(Equal(Zeros(LambertW(z,0), ForElement(z, CC)), Set(0))))

make_entry(ID("766302"),
    Formula(Equal(Zeros(LambertW(z,k), ForElement(z, CC)), Set())),
    Variables(k),
    Assumptions(Element(k, SetMinus(ZZ, Set(0)))))

# Derivatives and integrals

make_entry(ID("8d486c"),
    Formula(Equal(LambertW(z,k,1), 1/((1+LambertW(z,k))*Exp(LambertW(z,k))))),
    Variables(k,z),
    Assumptions(Or(
        And(Equal(k,0), Element(z, SetMinus(CC, Set(-Exp(-1))))),
        And(Equal(k,-1), Element(z, SetMinus(CC, Set(0,-Exp(-1))))),
        And(Element(k, SetMinus(ZZ, Set(0,1))), Element(z, SetMinus(CC, Set(0)))))))

make_entry(ID("72b6ca"),
    Formula(Equal(LambertW(z,k,1), LambertW(z,k)/(z*(1+LambertW(z,k))))),
    Variables(k,z),
    Assumptions(Or(
        And(Element(k,Set(0,1)), Element(z, SetMinus(CC, Set(0,-Exp(-1))))),
        And(Element(k, SetMinus(ZZ, Set(0,1))), Element(z, SetMinus(CC, Set(0)))))))

# todo: polynomials for higher derivatives


# Series expansions

# Taylor series

make_entry(ID("58c19a"),
    Formula(Equal(LambertW(z), Sum((-n)**(n-1) / Factorial(n) * z**n, For(n, 1, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 1/ConstE))))

# Puiseux series

make_entry(ID("c5a8c2"),
    SymbolDefinition(LambertWPuiseuxCoefficient, LambertWPuiseuxCoefficient(k), "Coefficient in scaled Puiseux expansion of Lambert W-function"))

make_entry(ID("0983d1"),
    Description("Table of", LambertWPuiseuxCoefficient(k), "for", LessEqual(0, k, 15)),
    Table(TableRelation(Tuple(k, mu, r), And(Equal(LambertWPuiseuxCoefficient(k), mu), Equal(NearestDecimal(LambertWPuiseuxCoefficient(k), 30), r))),
      TableHeadings(k, LambertWPuiseuxCoefficient(k), NearestDecimal(LambertWPuiseuxCoefficient(k), 30)), TableSplit(1),
      List(
        Tuple(0, -1, Decimal("-1.00000000000000000000000000000")),
        Tuple(1, 1, Decimal("1.00000000000000000000000000000")),
        Tuple(2, Div(-1,3), Decimal("-0.333333333333333333333333333333")),
        Tuple(3, Div(11,72), Decimal("0.152777777777777777777777777778")),
        Tuple(4, Div(-43,540), Decimal("-0.0796296296296296296296296296296")),
        Tuple(5, Div(769,17280), Decimal("0.0445023148148148148148148148148")),
        Tuple(6, Div(-221,8505), Decimal("-0.0259847148736037624926513815403")),
        Tuple(7, Div(680863,43545600), Decimal("0.0156356325323339212228101116990")),
        Tuple(8, Div(-1963,204120), Decimal("-0.00961689202429943170683911424652")),
        Tuple(9, Div(226287557,37623398400), Decimal("0.00601454325295611786095325189975")),
        Tuple(10, Div(-5776369,1515591000), Decimal("-0.00381129803489199922670430215012")),
        Tuple(11, Div(169709463197,69528040243200), Decimal("0.00244087799114398266589685852864")),
        Tuple(12, Div(-1118511313,709296588000), Decimal("-0.00157693034468678425392340953993")),
        Tuple(13, Div(667874164916771,650782456676352000), Decimal("0.00102626332050760715443754815339")),
        Tuple(14, Div(-500525573,744761417400), Decimal("-0.000672061631156136204002020043419")),
        Tuple(15, Div(103663334225097487,234281684403486720000), Decimal("0.000442473061814620909930207608585")),
    )))

make_entry(ID("d37d0f"),
    Formula(Where(Equal(LambertWPuiseuxCoefficient(k),
        ((k-1)/(k+1))*(LambertWPuiseuxCoefficient(k-2)/2 + alpha_(k-2)/4) - alpha_(k)/2 - LambertWPuiseuxCoefficient(k-1)/(k+1)),
        Def(alpha_(k), 
            Cases(Tuple(2, Equal(k, 0)),
                  Tuple(-1, Equal(k, 1)),
                  Tuple(Sum(LambertWPuiseuxCoefficient(j)*LambertWPuiseuxCoefficient(k+1-j), For(j, 2, k-1)), Otherwise))))),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(2))))

make_entry(ID("adf83a"),
    Formula(Less(Abs(LambertWPuiseuxCoefficient(k)), 2 * Div(4,5)**k)),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(0))))

make_entry(ID("e50532"),
    Formula(Where(Equal(LambertW(z), Sum(LambertWPuiseuxCoefficient(n) * v**n, For(n, 0, Infinity))),
        Equal(v, Sqrt(2*(ConstE*z+1))))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(ConstE*z+1), 1))))

make_entry(ID("99ff4c"),
    Formula(Where(Equal(LambertW(z,k), Sum(LambertWPuiseuxCoefficient(n) * v**n, For(n, 0, Infinity))),
        Equal(v, -Sqrt(2*(ConstE*z+1))))),
    Variables(k, z),
    Assumptions(And(Element(z, CC), Less(Abs(ConstE*z+1), 1), Or(And(Equal(k, -1), GreaterEqual(Im(z), 0)), And(Equal(k, 1), Less(Im(z), 0))))))

# Logarithmic series

#L1 = L_(1)
#L2 = L_(2)
L1 = Expr(symbol_name="L_1")
L2 = Expr(symbol_name="L_2")

asympdefs = Equal(L1, Log(z) + 2*Pi*ConstI*k), Equal(L2, Log(L1)), Equal(sigma, 1/L1), Equal(tau, L2/L1)
asympser = L1 - L2 + Sum(Sum((-1)**n / Factorial(m) * StirlingCycle(n+m, n+1) * sigma**n * tau**m, For(m, 1, Infinity)), For(n, 0, Infinity))
asympsertrunc = L1 - L2 + Sum(Sum((-1)**n / Factorial(m) * StirlingCycle(n+m, n+1) * sigma**n * tau**m, For(m, 1, M-1)), For(n, 0, N-1))

make_entry(ID("1fc63b"),
    Formula(Equal(LambertW(z,k),
        Where(asympser, *asympdefs))),
    Variables(k, z),
    Assumptions(Where(And(Element(k, ZZ), Element(z, SetMinus(CC, Set(0))),
        Less(Abs(sigma), Div(1,4)), Less(Abs(tau), Div(1,4)), Or(NotEqual(k, 0), Greater(Abs(z), 1))),
            *asympdefs)))

make_entry(ID("da0f15"),
    Formula(Where(LessEqual(Abs(LambertW(z,k) - Parentheses(asympsertrunc)), (4*Abs(tau)*(4*Abs(sigma))**N + (4*Abs(tau))**M)/((1-4*Abs(sigma))*(1-4*Abs(tau)))),
        *asympdefs)),
    Variables(k, z, N, M),
    Assumptions(Where(And(Element(N, ZZGreaterEqual(0)), Element(M, ZZGreaterEqual(0)), Element(k, ZZ), Element(z, SetMinus(CC, Set(0))),
        Less(Abs(sigma), Div(1,4)), Less(Abs(tau), Div(1,4)), Or(NotEqual(k, 0), Greater(Abs(z), 1))),
            *asympdefs)))

# Range

make_entry(ID("c0ae5b"),
    Formula(Equal(Set(LambertW(z,k), For(Tuple(k,z)), And(Element(k, ZZ), Element(z, CC), Or(NotEqual(z, 0), Equal(k, 0)))), CC)))

k1 = Subscript(k,1)
k2 = Subscript(k,2)
z1 = Subscript(z,1)
z2 = Subscript(z,2)

make_entry(ID("6e05c9"),
    Formula(NotEqual(LambertW(z1,k1), LambertW(z2,k2))),
    Variables(k1,z1,k2,z2),
    Assumptions(And(Element(k1,ZZ),Element(k2,ZZ),Element(z1,CC),Element(z2,CC),Or(NotEqual(k1,k2),NotEqual(z1,z2)),
        NotElement(LambertW(z1,k1), Set(-1,-Infinity)))))

# Image of the principal branch

make_entry(ID("ee86fb"),
    Formula(Equal(Set(LambertW(x), ForElement(x, OpenInterval(-Exp(-1), Infinity))), OpenInterval(-1, Infinity))))

make_entry(ID("55498b"),
    Formula(Equal(Set(LambertW(x), ForElement(x, Set(-Exp(-1)))), Set(-1))))

make_entry(ID("44ad09"),
    Formula(Equal(Set(LambertW(x), ForElement(x, OpenInterval(-Infinity, -Exp(-1)))),
        Set(-y*Cot(y) + y*ConstI, ForElement(y, OpenInterval(0, Pi))))))

make_entry(ID("2d3356"),
    Formula(Equal(Set(LambertW(z), ForElement(z, SetMinus(CC, RR))),
        Set(x+y*ConstI, For(Tuple(x, y)), And(Element(y, SetMinus(OpenInterval(-Pi, Pi), Set(0))), Element(x, OpenInterval(-y*Cot(y), Infinity)))))))

# Image of the non-principal branches

make_entry(ID("21d9a0"),
    Formula(Equal(Set(LambertW(z,-1), ForElement(z, SetMinus(CC, Set(0)))),
        Union(OpenClosedInterval(-Infinity, -1), Set(x+y*ConstI, For(Tuple(x, y)),
            Where(And(Element(x, RR), Element(y, RR), Or(And(Less(0, u, 2), LessEqual(t, v)), Parentheses(LessEqual(1, u, 2)), And(Less(1, u, 3), Greater(t, v)))),
                Equal(t, x*Sinc(y)), Equal(v, -Cos(y)), Equal(u, -(y/Pi))))))))

make_entry(ID("d5917b"),
    Formula(Equal(Set(LambertW(z,k), ForElement(z, SetMinus(CC, Set(0)))),
        Set(x+y*ConstI, For(Tuple(x, y)),
            Where(And(Element(x, RR), Element(y, RR), Or(And(Less(2*k-2, u, 2*k), Less(t, v)), Parentheses(LessEqual(2*k-1, u, 2*k)), And(Less(2*k-1, u, 2*k+1), GreaterEqual(t, v)))),
                Equal(t, x*Sinc(y)), Equal(v, -Cos(y)), Equal(u, y/Pi))))),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(1))))

make_entry(ID("bf3e29"),
    Formula(Equal(Set(LambertW(z,-k), ForElement(z, SetMinus(CC, Set(0)))),
        Set(x+y*ConstI, For(Tuple(x, y)),
            Where(And(Element(x, RR), Element(y, RR), Or(And(Less(2*k-2, u, 2*k), LessEqual(t, v)), Parentheses(LessEqual(2*k-1, u, 2*k)), And(Less(2*k-1, u, 2*k+1), Greater(t, v)))),
                Equal(t, x*Sinc(y)), Equal(v, -Cos(y)), Equal(u, -(y/Pi)))))),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(2))))

# Bounds

make_entry(ID("4257f4"),
    Formula(Less(Abs(Im(LambertW(z))), Pi)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("82926c"),
    Formula(Element(Im(LambertW(z,1)), OpenInterval(0, 3*Pi))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

make_entry(ID("e5bba3"),
    Formula(Element(Im(LambertW(z,-1)), OpenClosedInterval(-(3*Pi), 0))),
    Variables(z),
    Assumptions(Element(z, SetMinus(CC, Set(0)))))

# todo: move sign to RHS; make sure test code works with set * constant
make_entry(ID("a68e0e"),
    Formula(Element(Sign(k) * Im(LambertW(z,k)), OpenInterval((2*Abs(k)-2)*Pi, (2*Abs(k)+1)*Pi))),
    Variables(z, k),
    Assumptions(And(Element(z, SetMinus(CC, Set(0))), Element(k, SetMinus(ZZ, Set(-1, 0, 1))))))

# Derivative bounds

make_entry(ID("f171a6"),
    Formula(LessEqual(LambertW(x,0,1), 1/(x+1))),
    Variables(x),
    Assumptions(Element(x, ClosedOpenInterval(0, Infinity))))

make_entry(ID("a34260"),
    Formula(Less(LambertW(x,0,1), 2/Sqrt(1+ConstE*x))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(-Exp(-1), Infinity))))

make_entry(ID("9be916"),
    Formula(Less(Abs(LambertW(x,-1,1)), 2/Sqrt(1+ConstE*x) + 2/Abs(x))),
    Variables(x),
    Assumptions(Element(x, OpenInterval(-Exp(-1), 0))))

make_entry(ID("b3d435"),
    Formula(LessEqual(Abs(LambertW(z,k,1)), Abs(Decimal("1.2")/z))),
    Variables(k,z),
    Assumptions(And(Element(k, SetMinus(ZZ, Set(-1,0,1))), Element(z, CC))))

make_entry(ID("8e06be"),
    Formula(LessEqual(Abs(LambertW(z,k,1)), Abs(Decimal("1.5")/z))),
    Variables(k,z),
    Assumptions(And(Element(z, CC), Or(And(Equal(k,1), GreaterEqual(Im(z), 0)), And(Equal(k,-1), Less(Im(z), 0))))))

make_entry(ID("72712c"),
    Formula(LessEqual(Abs(LambertW(z,k,1)), 1/Abs(z))),
    Variables(k,z),
    Assumptions(Or(And(Equal(k,0), GreaterEqual(Abs(z), 1)), And(Element(k, ZZ), Element(z, CC), GreaterEqual(Abs(z), 4*(Abs(k)+1))))))

make_entry(ID("9136b9"),
    Formula(LessEqual(Abs(LambertW(z,k,1)), Abs(1/z) * Max(3, Abs(Decimal("1.5") / Sqrt(Abs(ConstE*z+1)))))),
    Variables(k,z),
    Assumptions(And(Element(k, ZZ), Element(z, CC))))

make_entry(ID("0eb699"),
    Formula(Where(LessEqual(Abs(LambertW(z,0,1)), Abs(Decimal("2.25") / Sqrt(t * (1 + t)))), Equal(t, Abs(ConstE*z+1)))),
    Variables(z),
    Assumptions(And(Element(z, CC), LessEqual(Abs(z), 64))))

make_entry(ID("214b1c"),
    Formula(LessEqual(Abs(LambertW(z,k,1)), Abs(1/Abs(z) * (1 + 1/(4 + Abs(z)**2))))),
    Variables(k,z),
    Assumptions(And(Element(z, CC),
        Or(
            And(Element(k, Set(1, -1)), GreaterEqual(Re(z), 0)),
            And(Equal(k, -1), Less(Im(z), 0)),
            And(Equal(k, 1), GreaterEqual(Im(z), 0))))))

make_entry(ID("a1e634"),
    Formula(LessEqual(Abs(LambertW(z,k,1)), Abs(1/Abs(z) * (1 + Div(23,32) * (1/Sqrt(Abs(ConstE*z+1))))))),
    Variables(k,z),
    Assumptions(And(Element(z, CC), Element(k, Set(-1, 1)))))

