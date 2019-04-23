from .expr import *

# todo: separate page for bell numbers, +A011971 ?

def_Topic(
    Title("Stirling numbers"),
    Entries(
        "778fa2",
        "2e9d0c",
        "4c6c43",
        "1706bb",
    ),
    Section("Tables"),
    Entries(
        "f88455",
        "a93679",
        "cecede",
        "4c6267",
    ),
    Section("Recurrence relations"),
    Entries(
        "f0d72c",
        "18ec99",
        "9fbe4f",
    ),
    Section("Connection formulas"),
    Entries(
        "071a94",
    ),
    Section("Generating functions"),
    Entries(
        "21241f",
        "f46e0e",
        "b823b0",
        "b01280",
        "a9a610",
    ),
    Section("Sum representations"),
    Entries(
        "6189b9",
    ),
    Section("Sums"),
    Entries(
        "ea9e2f",
        "255576",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "7774a3",
    ),
)

make_entry(ID("778fa2"),
    SymbolDefinition(StirlingCycle, StirlingCycle(n, k), "Unsigned Stirling number of the first kind"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0))), Element(StirlingCycle(n, k), ZZGreaterEqual(0))),
      )))

make_entry(ID("2e9d0c"),
    SymbolDefinition(StirlingS1, StirlingS1(n, k), "Signed Stirling number of the first kind"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0))), Element(StirlingS1(n, k), ZZ)),
      )))

make_entry(ID("4c6c43"),
    SymbolDefinition(StirlingS2, StirlingS2(n, k), "Stirling number of the second kind"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0))), Element(StirlingS2(n, k), ZZGreaterEqual(0))),
      )))

make_entry(ID("1706bb"),
    SymbolDefinition(BellNumber, BellNumber(n), "Bell number"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, ZZGreaterEqual(0)), Element(BellNumber(n), ZZGreaterEqual(1))),
      )))


make_entry(ID("f0d72c"),
    Formula(Equal(StirlingCycle(n+1, k), n*StirlingCycle(n,k) + StirlingCycle(n, k-1))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(1)))))

make_entry(ID("18ec99"),
    Formula(Equal(StirlingS1(n+1, k), StirlingS1(n, k-1) - n*StirlingS1(n,k))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(1)))))

make_entry(ID("9fbe4f"),
    Formula(Equal(StirlingS2(n+1, k), k * StirlingS2(n, k) + StirlingS2(n,k-1))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(1)))))


make_entry(ID("071a94"),
    Formula(Equal(StirlingS1(n, k), (-1)**(n+k) * StirlingCycle(n, k))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))))


make_entry(ID("21241f"),
    Formula(Equal(RisingFactorial(x, n), Sum(StirlingCycle(n, k) * x**k, Tuple(k, 0, n)))),
    Variables(x, n),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("f46e0e"),
    Formula(Equal(RisingFactorial(x-n+1, n), Sum(StirlingS1(n, k) * x**k, Tuple(k, 0, n)))),
    Variables(x, n),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("b823b0"),
    Formula(Equal(x**n, Sum(StirlingS2(n, k) * RisingFactorial(x-n+1, n), Tuple(k, 0, n)))),
    Variables(x, n),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("b01280"),
    Formula(Equal(Div((Log(1+x))**k, Factorial(k)), Sum((-1)**(n-k) * StirlingCycle(n,k) * Div(x**n, Factorial(n)), Tuple(n, k, Infinity)))),
    Variables(x, k),
    Assumptions(And(Element(k, ZZGreaterEqual(0)), Element(x, CC), Less(Abs(x), 1))))

make_entry(ID("a9a610"),
    Formula(Equal(Div((Exp(x)-1)**k, Factorial(k)), Sum(StirlingS2(n,k) * Div(x**n, Factorial(n)), Tuple(n, k, Infinity)))),
    Variables(x, k),
    Assumptions(And(Element(k, ZZGreaterEqual(0)), Element(x, CC))))


make_entry(ID("6189b9"),
    Formula(Equal(StirlingS2(n,k), Div(1,Factorial(k)) * Sum((-1)**i * Binomial(k,i) * (k-i)**n, Tuple(i, 0, k)))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("ea9e2f"),
    Formula(Equal(Sum(StirlingCycle(n,k), Tuple(k, 0, n)), Factorial(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("255576"),
    Formula(Equal(Sum(StirlingS2(n,k), Tuple(k, 0, n)), BellNumber(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))


make_entry(ID("7774a3"),
    LessEqual(StirlingCycle(n, k), (2**n*Factorial(n))/Factorial(k)),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("f88455"),
    Description("Table of", StirlingCycle(n, k), "for", LessEqual(0, n, 10), "and", LessEqual(0, k, 10)),
    Table(TableRelation(Tuple(n, k, y), Equal(StirlingCycle(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        List(
        Tuple(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, 6, 11, 6, 1, 0, 0, 0, 0, 0, 0),
        Tuple(0, 24, 50, 35, 10, 1, 0, 0, 0, 0, 0),
        Tuple(0, 120, 274, 225, 85, 15, 1, 0, 0, 0, 0),
        Tuple(0, 720, 1764, 1624, 735, 175, 21, 1, 0, 0, 0),
        Tuple(0, 5040, 13068, 13132, 6769, 1960, 322, 28, 1, 0, 0),
        Tuple(0, 40320, 109584, 118124, 67284, 22449, 4536, 546, 36, 1, 0),
        Tuple(0, 362880, 1026576, 1172700, 723680, 269325, 63273, 9450, 870, 45, 1),
    )))

make_entry(ID("a93679"),
    Description("Table of", StirlingS1(n, k), "for", LessEqual(0, n, 10), "and", LessEqual(0, k, 10)),
    Table(TableRelation(Tuple(n, k, y), Equal(StirlingS1(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        List(
        Tuple(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, 2, -3, 1, 0, 0, 0, 0, 0, 0, 0),
        Tuple(0, -6, 11, -6, 1, 0, 0, 0, 0, 0, 0),
        Tuple(0, 24, -50, 35, -10, 1, 0, 0, 0, 0, 0),
        Tuple(0, -120, 274, -225, 85, -15, 1, 0, 0, 0, 0),
        Tuple(0, 720, -1764, 1624, -735, 175, -21, 1, 0, 0, 0),
        Tuple(0, -5040, 13068, -13132, 6769, -1960, 322, -28, 1, 0, 0),
        Tuple(0, 40320, -109584, 118124, -67284, 22449, -4536, 546, -36, 1, 0),
        Tuple(0, -362880, 1026576, -1172700, 723680, -269325, 63273, -9450, 870, -45, 1),
    )))

make_entry(ID("cecede"),
    Description("Table of", StirlingS2(n, k), "for", LessEqual(0, n, 10), "and", LessEqual(0, k, 10)),
    Table(TableRelation(Tuple(n, k, y), Equal(StirlingS2(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        List(
            Tuple(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0),
            Tuple(0, 1, 7, 6, 1, 0, 0, 0, 0, 0, 0),
            Tuple(0, 1, 15, 25, 10, 1, 0, 0, 0, 0, 0),
            Tuple(0, 1, 31, 90, 65, 15, 1, 0, 0, 0, 0),
            Tuple(0, 1, 63, 301, 350, 140, 21, 1, 0, 0, 0),
            Tuple(0, 1, 127, 966, 1701, 1050, 266, 28, 1, 0, 0),
            Tuple(0, 1, 255, 3025, 7770, 6951, 2646, 462, 36, 1, 0),
            Tuple(0, 1, 511, 9330, 34105, 42525, 22827, 5880, 750, 45, 1),
    )))

make_entry(ID("4c6267"),
    Description("Table of", BellNumber(n), "for", LessEqual(0, n, 40)),
    Table(TableRelation(Tuple(n, y), Equal(BellNumber(n), y)),
      TableHeadings(n, BellNumber(n)), TableSplit(2),
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

