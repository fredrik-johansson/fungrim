from .expr import *

def_Topic(
    Title("Bernoulli numbers and polynomials"),
    Entries(
        "ac8eca",
        "1f88a4",
    ),
    Section("Tables"),
    Entries(
        "aed6bd",
        "588889",
    ),
    Section("Generating functions"),
    Entries(
        "522b04",
        "f79ff0",
    ),
    Section("Sum representations"),
    Entries(
        "555e10",
    ),
    Section("Representations by special functions"),
    Entries(
        "14ecc4",
    ),
    Section("Specific values"),
    Entries(
        "a98234",
        "d10873",
        "a1d2d7",
        "829185",
        "03ee0b",
    ),
    Section("Functional equations"),
    Entries(
        "8b4f7f",
        "c2dcfa",
        "f80439",
    ),
    Section("Derivatives and integrals"),
    Entries(
        "7adfd6",
        "05202b",
        "e89eb5",
    ),
    Section("Summation"),
    Entries(
        "4aab8a",
    ),
    Section("Denominators"),
    Entries(
        "ff190c",
        "c33e2b",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "0f02a5",
        "3a1316",
        "1d2f4a",
        "69ca86",
        "292d70",
        "4246ae",
    ),
)

make_entry(ID("ac8eca"),
    SymbolDefinition(BernoulliB, BernoulliB(n), "Bernoulli number"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, ZZGreaterEqual(0)), Element(BernoulliB(n), QQ)),
      )))

make_entry(ID("1f88a4"),
    SymbolDefinition(BernoulliPolynomial, BernoulliPolynomial(n, z), "Bernoulli polynomial"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(z, RR)), Element(BernoulliPolynomial(n, z), RR)),
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(z, CC)), Element(BernoulliPolynomial(n, z), CC)),
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(z, R), Element(R, Rings), SubsetEqual(QQ, R)), Element(BernoulliPolynomial(n, z), R)),
      )))

make_entry(ID("aed6bd"),
    Description("Table of", BernoulliB(n), "for", LessEqual(0, n, 50)),
    Table(TableRelation(Tuple(n, y, r), And(Equal(BernoulliB(n), y), Equal(NearestDecimal(BernoulliB(n), 30), r))),
      TableHeadings(n, BernoulliB(n), NearestDecimal(BernoulliB(n), 30)), TableSplit(1),
      List(
Tuple(0, 1, Decimal("1.00000000000000000000000000000")),
Tuple(1, -Div(1,2), Decimal("-0.500000000000000000000000000000")),
Tuple(2, Div(1,6), Decimal("0.166666666666666666666666666667")),
Tuple(3, 0, Decimal("0")),
Tuple(4, -Div(1,30), Decimal("-0.0333333333333333333333333333333")),
Tuple(5, 0, Decimal("0")),
Tuple(6, Div(1,42), Decimal("0.0238095238095238095238095238095")),
Tuple(7, 0, Decimal("0")),
Tuple(8, -Div(1,30), Decimal("-0.0333333333333333333333333333333")),
Tuple(9, 0, Decimal("0")),
Tuple(10, Div(5,66), Decimal("0.0757575757575757575757575757576")),
Tuple(11, 0, Decimal("0")),
Tuple(12, -Div(691,2730), Decimal("-0.253113553113553113553113553114")),
Tuple(13, 0, Decimal("0")),
Tuple(14, Div(7,6), Decimal("1.16666666666666666666666666667")),
Tuple(15, 0, Decimal("0")),
Tuple(16, -Div(3617,510), Decimal("-7.09215686274509803921568627451")),
Tuple(17, 0, Decimal("0")),
Tuple(18, Div(43867,798), Decimal("54.9711779448621553884711779449")),
Tuple(19, 0, Decimal("0")),
Tuple(20, -Div(174611,330), Decimal("-529.124242424242424242424242424")),
Tuple(21, 0, Decimal("0")),
Tuple(22, Div(854513,138), Decimal("6192.12318840579710144927536232")),
Tuple(23, 0, Decimal("0")),
Tuple(24, -Div(236364091,2730), Decimal("-86580.2531135531135531135531136")),
Tuple(25, 0, Decimal("0")),
Tuple(26, Div(8553103,6), Decimal("1425517.16666666666666666666667")),
Tuple(27, 0, Decimal("0")),
Tuple(28, -Div(23749461029,870), Decimal("-27298231.0678160919540229885057")),
Tuple(29, 0, Decimal("0")),
Tuple(30, Div(8615841276005,14322), Decimal("601580873.900642368384303868175")),
Tuple(31, 0, Decimal("0")),
Tuple(32, -Div(7709321041217,510), Decimal("-15116315767.0921568627450980392")),
Tuple(33, 0, Decimal("0")),
Tuple(34, Div(2577687858367,6), Decimal("429614643061.166666666666666667")),
Tuple(35, 0, Decimal("0")),
Tuple(36, -Div(26315271553053477373,1919190), Decimal("-13711655205088.3327721590879486")),
Tuple(37, 0, Decimal("0")),
Tuple(38, Div(2929993913841559,6), Decimal("488332318973593.166666666666667")),
Tuple(39, 0, Decimal("0")),
Tuple(40, -Div(261082718496449122051,13530), Decimal("-19296579341940068.1486326681449")),
Tuple(41, 0, Decimal("0")),
Tuple(42, Div(1520097643918070802691,1806), Decimal("841693047573682615.000553709856")),
Tuple(43, 0, Decimal("0")),
Tuple(44, -Div(27833269579301024235023,690), Decimal("-40338071854059455413.0768115942")),
Tuple(45, 0, Decimal("0")),
Tuple(46, Div(596451111593912163277961,282), Decimal("2115074863808199160560.14539007")),
Tuple(47, 0, Decimal("0")),
Tuple(48, -Div(5609403368997817686249127547,46410), Decimal("-120866265222965259346027.311937")),
Tuple(49, 0, Decimal("0")),
Tuple(50, Div(495057205241079648212477525,66), Decimal("7500866746076964366855720.07576")))))


make_entry(ID("588889"),
    Description("Table of", BernoulliPolynomial(n,x), "for", LessEqual(0, n, 10)),
    Table(TableRelation(Tuple(n, p), Equal(BernoulliPolynomial(n,x), p)),
      TableHeadings(n, BernoulliPolynomial(n,x)), TableSplit(1),
      List(
Tuple(0, 1),
Tuple(1, x - Div(1,2)),
Tuple(2, x**2 - x + Div(1,6)),
Tuple(3, x**3 - Div(3,2)*x**2 + Div(1,2)*x),
Tuple(4, x**4 - 2*x**3 + x**2 - Div(1,30)),
Tuple(5, x**5 - Div(5,2)*x**4 + Div(5,3)*x**3 - Div(1,6)*x),
Tuple(6, x**6 - 3*x**5 + Div(5,2)*x**4 - Div(1,2)*x**2 + Div(1,42)),
Tuple(7, x**7 - Div(7,2)*x**6 + Div(7,2)*x**5 - Div(7,6)*x**3 + Div(1,6)*x),
Tuple(8, x**8 - 4*x**7 + Div(14,3)*x**6 - Div(7,3)*x**4 + Div(2,3)*x**2 - Div(1,30)),
Tuple(9, x**9 - Div(9,2)*x**8 + 6*x**7 - Div(21,5)*x**5 + 2*x**3 - Div(3,10)*x),
Tuple(10, x**10 - 5*x**9 + Div(15,2)*x**8 - 7*x**6 + 5*x**4 - Div(3,2)*x**2 + Div(5,66)))),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("522b04"),
    Formula(Equal(z/(Exp(z)-1),
        Sum(BernoulliB(n) * (z**n / Factorial(n)), Tuple(n, 0, Infinity)))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), 2 * ConstPi), Unequal(z, 0))))

make_entry(ID("f79ff0"),
    Formula(Equal(z*Exp(x*z)/(Exp(z)-1),
        Sum(BernoulliPolynomial(n,x) * (z**n / Factorial(n)), Tuple(n, 0, Infinity)))),
    Variables(z, x),
    Assumptions(And(Element(x, CC), Element(z, CC), Less(Abs(z), 2 * ConstPi), Unequal(z, 0))))

make_entry(ID("555e10"),
    Formula(Equal(BernoulliPolynomial(n,x), Sum(Binomial(n,k) * BernoulliB(n-k) * x**k, Tuple(k, 0, n)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("14ecc4"),
    Formula(Equal(BernoulliB(2*n), (-1)**(n+1) * (2 * Factorial(2*n) * RiemannZeta(2*n) / (2 * ConstPi)**(2*n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("a98234"),
    Formula(Equal(BernoulliB(2*n+3), 0)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("d10873"),
    Formula(Greater((-1)**(n+1) * BernoulliB(2*n+2), 0)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("a1d2d7"),
    Formula(Equal(BernoulliPolynomial(n, 0), BernoulliB(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("829185"),
    Formula(Equal(BernoulliPolynomial(n, 1), (-1)**n * BernoulliB(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("03ee0b"),
    Formula(Equal(BernoulliPolynomial(n, Div(1,2)), (2**(1-n)-1) * BernoulliB(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))


make_entry(ID("8b4f7f"),
    Formula(Equal(BernoulliPolynomial(n, x+1), BernoulliPolynomial(n, z) + n * x**(n-1))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("c2dcfa"),
    Formula(Equal(BernoulliPolynomial(n, 1-x), (-1)**n * BernoulliPolynomial(n, x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("f80439"),
    Formula(Equal(BernoulliPolynomial(n, -x), (-1)**n * (BernoulliPolynomial(n, x) + n * x**(n-1)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("7adfd6"),
    Formula(Equal(Integral(BernoulliPolynomial(n, t), Tuple(t, a, b)), (BernoulliPolynomial(n+1,b) - BernoulliPolynomial(n+1,a)) / (n+1))),
    Variables(n, a, b),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(a, CC), Element(b, CC))))

make_entry(ID("05202b"),
    Formula(Equal(Integral(BernoulliPolynomial(n, t), Tuple(t, z, z+1)), z**n)),
    Variables(n, z),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("e89eb5"),
    Formula(Equal(Derivative(BernoulliPolynomial(n, x), Tuple(x, x, 1)), n * BernoulliPolynomial(n-1, x))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(x, CC))))


# todo: variable lower endpoint??
make_entry(ID("4aab8a"),
    Formula(Equal(Sum(k**n, Tuple(k, 1, m)), (BernoulliPolynomial(n+1, m+1) - BernoulliB(m+1)) / (m+1))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))))


make_entry(ID("0f02a5"),
    Formula(Less(Abs(BernoulliB(2*n)), (1 + 1/n) * (2 * Factorial(2*n) / ((2*ConstPi)**(2*n))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("3a1316"),
    Formula(Less(Abs(BernoulliB(2*n)), (1 + 1/n) * 4 * Sqrt(ConstPi * n) * (n / (ConstPi * ConstE))**(2*n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("1d2f4a"),
    Formula(Greater(Abs(BernoulliB(2*n)), 2 * Factorial(2*n) / (2*ConstPi)**(2*n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("69ca86"),
    Formula(Greater(Abs(BernoulliB(2*n)), 4 * Sqrt(ConstPi * n) * (n / (ConstPi * ConstE))**(2*n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("292d70"),
    Formula(LessEqual(Abs(BernoulliPolynomial(2*n, x)), Abs(BernoulliB(2*n)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, ClosedInterval(0, 1)))))

make_entry(ID("4246ae"),
    Formula(Less(Abs(BernoulliPolynomial(2*n, x)), Abs(BernoulliB(2*n)))),
    Variables(n, x),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(x, OpenInterval(0, 1)))))

make_entry(ID("ff190c"),
    Formula(Element(Parentheses(BernoulliB(2*n) + SumCondition(1/p, p, And(Element(p, PP), Divides(Parentheses(p-1), 2*n)))), ZZ)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("c33e2b"),
    Formula(Element(Parentheses(BernoulliB(2*n) * ProductCondition(1/p, p, And(Element(p, PP), Divides(Parentheses(p-1), 2*n)))), ZZ)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))


