# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Bell numbers"),
    Section("Definitions"),
    Entries(
        "1706bb",
        "60dc3e",
    ),
    Section("Domain and codomain"),
    Entries(
        "16fe51",
    ),
    Section("Specific values"),
    Subsection("First cases as set partitions"),
    Entries(
        "4b4816",
        "534f7d",
        "3627de",
        "92cc17",
    ),
    Subsection("Tables"),
    Entries(
        "4c6267",
        "7466a2",
    ),
    Section("Infinite series representations"),
    Entries(
        "050c46",
    ),
    Section("Sum representations"),
    Entries(
        "948167",
        "4b65d0",
        "1026e3",
    ),
    Section("Generating functions"),
    Entries(
        "9d666f",
        "aab4e3",
    ),
    Section("Integral representations"),
    Entries(
        "f4e249",
        "a71381",
    ),
    Section("Asymptotics"),
    Entries(
        "343946",
        "589758",
    ),
    Section("Bounds and inequalities"),
    Subsection("Monotonicity and convexity"),
    Entries(
        "2e576e",
        "320dc9",
        "fb6ce2",
        "46bc62",
        "1e00d2",
        "d1438d",
    ),
    Subsection("Upper bounds"),
    Entries(
        "d1f218",
        "512beb",
    ),
    Subsection("Lower bounds"),
    Entries(
        "7e449a",
        "a747a4",
        "468def",
        "b29b24",
    ),
    Section("Divisibility properties"),
    Subsection("Touchard's congruence"),
    Entries(
        "60740b",
        "dd9d26",
        "b41c49",
    ),
    Subsection("Periodicity"),
    Entries(
        "050ee1",
        "a4d6fc",
        "b7e899",
    ),
    Subsection("Prime values"),
    Entries(
        "a1108d",
    ),
    Section("Matrix fomulas"),
    Entries(
        "b5a382",
        "dc6806",
    ),
    Section("Related topics"),
    Description("Restricted set partitions: ", TopicReference("Stirling numbers")),
    Description("Integer partitions: ", TopicReference("Partition function")),
)

# Definitions

make_entry(ID("1706bb"),
    SymbolDefinition(BellNumber, BellNumber(n), "Bell number"),
    Description(SourceForm(BellNumber(n)), ", rendered as", BellNumber(n),
        ", gives the ", n, ":th Bell number, counting the number of partitions of a set of size", n, "."),
    References("http://mathworld.wolfram.com/BellNumber.html",
        "https://en.wikipedia.org/wiki/Bell_number",
        SloaneA("A000110")))

# Domain and codomain

make_entry(ID("16fe51"),
    Implies(Element(n, ZZGreaterEqual(0)), Element(BellNumber(n), ZZGreaterEqual(1))),
    Variables(n))


# Specific values

# todo: not found by ordner?
make_entry(ID("4b4816"),
    Equal(BellNumber(0), Cardinality(Set(
        Set(Set()))),
    1))

make_entry(ID("534f7d"),
    Equal(BellNumber(1), Cardinality(Set(
        Set(Set(1)))),
    1))

make_entry(ID("3627de"),
    Equal(BellNumber(2), Cardinality(Set(
        Set(Set(1), Set(2)),
        Set(Set(1, 2)))),
        2))

make_entry(ID("92cc17"),
    Equal(BellNumber(3), Cardinality(Set(
        Set(Set(1), Set(2), Set(3)),
        Set(Set(1), Set(2, 3)),
        Set(Set(2), Set(1, 3)),
        Set(Set(3), Set(1, 2)),
        Set(Set(1, 2, 3)))),
        5))

make_entry(ID("4c6267"),
    Description("Table of", BellNumber(n), "for", LessEqual(0, n, 40)),
    Table(
      Var(n),
      TableValueHeadings(n, BellNumber(n)),
      TableSplit(2),
      List(
    Tuple(0, 1),
    Tuple(1, 1),
    Tuple(2, 2),
    Tuple(3, 5),
    Tuple(4, 15),
    Tuple(5, 52),
    Tuple(6, 203),
    Tuple(7, 877),
    Tuple(8, 4140),
    Tuple(9, 21147),
    Tuple(10, 115975),
    Tuple(11, 678570),
    Tuple(12, 4213597),
    Tuple(13, 27644437),
    Tuple(14, 190899322),
    Tuple(15, 1382958545),
    Tuple(16, 10480142147),
    Tuple(17, 82864869804),
    Tuple(18, 682076806159),
    Tuple(19, 5832742205057),
    Tuple(20, 51724158235372),
    Tuple(21, 474869816156751),
    Tuple(22, 4506715738447323),
    Tuple(23, 44152005855084346),
    Tuple(24, 445958869294805289),
    Tuple(25, 4638590332229999353),
    Tuple(26, 49631246523618756274),
    Tuple(27, 545717047936059989389),
    Tuple(28, 6160539404599934652455),
    Tuple(29, 71339801938860275191172),
    Tuple(30, 846749014511809332450147),
    Tuple(31, 10293358946226376485095653),
    Tuple(32, 128064670049908713818925644),
    Tuple(33, 1629595892846007606764728147),
    Tuple(34, 21195039388640360462388656799),
    Tuple(35, 281600203019560266563340426570),
    Tuple(36, 3819714729894818339975525681317),
    Tuple(37, 52868366208550447901945575624941),
    Tuple(38, 746289892095625330523099540639146),
    Tuple(39, 10738823330774692832768857986425209),
    Tuple(40, 157450588391204931289324344702531067),
    )))

make_entry(ID("7466a2"),
    Description("Table of", BellNumber(10**n), "to 50 digits for", LessEqual(0, n, 20)),
    Table(
      Var(n),
      TableValueHeadings(n, NearestDecimal(BellNumber(10**n), 50)),
      TableSplit(1),
      List(
        Tuple(0, Decimal("1")),
        Tuple(1, Decimal("115975")),
        Tuple(2, Decimal("4.7585391276764833658790768841387207826363669686826e+115")),
        Tuple(3, Decimal("2.9899013356824084214804223538976464839473928098212e+1927")),
        Tuple(4, Decimal("1.5921722925574210311304813561932450033887865728335e+27664")),
        Tuple(5, Decimal("1.0433942425429389984540246838845160786245861774676e+364471")),
        Tuple(6, Decimal("6.9407979938401739982227098407865685636554898570286e+4547585")),
        Tuple(7, Decimal("4.3145155655649390291431304090943630466481496281332e+54670462")),
        Tuple(8, Decimal("1.0661323224103766871234871127158157404496071219044e+639838112")),
        Tuple(9, Decimal("2.6930773812723249433116475845718644555421493748165e+7338610158")),
        Tuple(10, Decimal("5.1453972928520420466420608273749029965573268638547e+82857366966")),
        Tuple(11, Decimal("2.1856659331923642401145024809343148851214345631527e+923836121336")),
        Tuple(12, Decimal("2.3531206591649838226542749070017497015282621676683e+10195466552696")),
        Tuple(13, Decimal("5.8027995692250857595662702057260821919793528709088e+111562912181760")),
        Tuple(14, Decimal("4.3473012694977341957607161339632765549165135069010e+1212025087283000")),
        Tuple(15, Decimal("1.2100916983919003930868324120105540724015107284657e+13086887678097716")),
        Tuple(16, Decimal("1.1988608581471804602537538050476211671930061609078e+140558364519453118")),
        Tuple(17, Decimal("2.9133991743205108132890536872295316466697644906027e+1502680138594030689")),
        Tuple(18, Decimal("1.1492776754825558262089653108689792631425178848431e+15999539613219703746")),
        Tuple(19, Decimal("3.5599898595325449556740567588576528872183367386397e+169738493504812320257")),
        Tuple(20, Decimal("5.3827011317628161073953431454940317253902192049701e+1794956117137290721328")))))

# Infinite series representations

make_entry(ID("050c46"),
    Formula(Equal(BellNumber(n), (1/ConstE) * Sum(k**n / Factorial(k), For(k, 0, Infinity)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Sum representations

make_entry(ID("948167"),
    Formula(Equal(BellNumber(n), Sum(StirlingS2(n,k), For(k, 0, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("4b65d0"),
    Formula(Equal(BellNumber(n), Sum(k**n / Factorial(k) * Sum((-1)**j / Factorial(j), For(j, 0, n-k)), For(k, 1, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("1026e3"),
    Formula(Equal(BellNumber(n+1), Sum(Binomial(n, k) * BellNumber(k), For(k, 0, n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Generating functions

# todo: as formal power series
make_entry(ID("9d666f"),
    Formula(Equal(Sum(BellNumber(n) * x**n, For(n, 0, Infinity)), Sum(x**k/Product(Parentheses(1-j*x), For(j, 1, k)), For(k, 0, Infinity)))),
    Variables(x),
    Assumptions(Equal(x, 0)))

make_entry(ID("aab4e3"),
    Formula(Equal(Sum(BellNumber(n) / Factorial(n) * x**n, For(n, 0, Infinity)), Exp(Exp(x)-1))),
    Variables(x),
    Assumptions(Element(x, CC)))

# Integral representations

make_entry(ID("f4e249"),
    Formula(Equal(BellNumber(n), (2*Factorial(n))/(Pi*ConstE) * Im(Integral(ConstE**(ConstE**(ConstE**(ConstI*x))) * Sin(n*x), For(x, 0, Pi))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))),
    References("https://arxiv.org/abs/0708.3301"))

make_entry(ID("a71381"),
    Formula(Equal(BellNumber(n), (2*Factorial(n))/(Pi*ConstE) *
        Integral(ConstE**(ConstE**(Cos(x))*Cos(Sin(x))) * Sin(ConstE**(Cos(x))*Sin(Sin(x))) * Sin(n*x), For(x, 0, Pi)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))),
    References("https://arxiv.org/abs/0708.3301"))

# Asymptotics

# todo: error term O(log(log(n))/log(n)**2)
make_entry(ID("343946"),
    Formula(AsymptoticTo(Log(BellNumber(n))/n, Log(n) - Log(Log(n)) - 1 + Log(Log(n))/Log(n) + 1/Log(n) + Div(1,2) * (Log(Log(n))/Log(n))**2, n, Infinity)))

make_entry(ID("589758"),
    Formula(AsymptoticTo(BellNumber(n), n**(-Div(1,2)) * (n/LambertW(n))**(n+Div(1,2)) * Exp(n/LambertW(n)-n-1), n, Infinity)))

# Bounds and inequalities

make_entry(ID("2e576e"),
    Formula(GreaterEqual(BellNumber(n+1), BellNumber(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("320dc9"),
    Formula(Greater(BellNumber(n+1), BellNumber(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("fb6ce2"),
    Formula(Less(BellNumber(n+1), n * BellNumber(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(4))))

make_entry(ID("46bc62"),
    Formula(GreaterEqual(BellNumber(n+1), 2 * BellNumber(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("d1f218"),
    Formula(LessEqual(BellNumber(n), Factorial(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# todo: reference "improved bounds on bell numbers..."
make_entry(ID("512beb"),
    Formula(LessEqual(BellNumber(n), ((Decimal("0.792")*n)/Log(n+1))**n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("7e449a"),
    Formula(GreaterEqual(BellNumber(n), Exp(n-2))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("a747a4"),
    Formula(GreaterEqual(BellNumber(n), k**(n-k))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))),
    References("https://cs.stackexchange.com/q/93003"))

make_entry(ID("468def"),
    Formula(GreaterEqual(BellNumber(n), (n/(ConstE*Log(n)))**n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(2))))

make_entry(ID("b29b24"),
    Formula(GreaterEqual(BellNumber(n), PartitionsP(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("1e00d2"),
    Formula(LessEqual(BellNumber(n)**2, BellNumber(n-1)*BellNumber(n+1), (1+1/n) * BellNumber(n)**2)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))),
    References("https://arxiv.org/abs/math/0104137"))

make_entry(ID("d1438d"),
    Formula(LessEqual(BellNumber(n)*BellNumber(m), BellNumber(n+m), Binomial(n+m,n)*BellNumber(n)*BellNumber(m))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))),
    References("https://arxiv.org/abs/math/0104137"))

# Divisibility properties

make_entry(ID("60740b"),
    Formula(CongruentMod(BellNumber(p), 2, p)),
    Variables(p),
    Assumptions(Element(p, PP)))

make_entry(ID("dd9d26"),
    Formula(CongruentMod(BellNumber(n+p), BellNumber(n) + BellNumber(n+1), p)),
    Variables(n, p),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(p, PP))))

make_entry(ID("b41c49"),
    Formula(CongruentMod(BellNumber(n+p**m), m*BellNumber(n) + BellNumber(n+1), p)),
    Variables(n, p, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(p, PP), Element(m, ZZGreaterEqual(1)))))

make_entry(ID("050ee1"),
    Formula(CongruentMod(BellNumber(n), Cases(Tuple(0, CongruentMod(n, 2, 3)), Tuple(1, Otherwise)), 2)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("a4d6fc"),
    Formula(Where(CongruentMod(BellNumber(n+a), BellNumber(n), m), Equal(a,
        Cases(Tuple(3, Equal(m, 2)), Tuple(13, Equal(m, 3)), Tuple(12, Equal(m, 4)), Tuple(781, Equal(m, 5)), Tuple(39, Equal(m, 6)))))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, Range(2, 6)))))

make_entry(ID("b7e899"),
    Formula(Where(CongruentMod(BellNumber(n+a), BellNumber(n), m), Equal(a, SloaneA("A054767", m)))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(1)))))

make_entry(ID("a1108d"),
    Formula(Implies(Element(n, Set(2, 3, 7, 13, 42, 55, 2841)), Element(BellNumber(n), PP))),
    Variables(n),
    References(SloaneA("A051130")))

# Determinants

# todo: define IdentityMatrix
make_entry(ID("b5a382"),
    Formula(Equal(BellNumber(n), Item(Exp(Matrix(Binomial(i,j), For(i, 0, N), For(j, 0, N)) - IdentityMatrix(N+1)), Tuple(n+1, 1)))),
    Variables(N, n),
    Assumptions(And(Element(N, ZZGreaterEqual(0)), Element(n, Range(0, N)))))

# todo: printing
make_entry(ID("dc6806"),
    Formula(Equal(Det(Matrix(BellNumber(i+j), For(i, 0, n), For(j, 0, n))), Product(Factorial(k), For(k, 1, n)), BarnesG(n+2))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

