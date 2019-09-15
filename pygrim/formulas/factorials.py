# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Factorials and binomial coefficients"),
    Entries(
        "81aeba",
        "def588",
        "579595",
        "3c2469",
    ),
    Section("Specific values"),
    SeeTopics("Specific values of factorials and binomial coefficients"),
    Entries(
        "3009a7",
        "fb5d88",
        "29741c",
        "63f368",
    ),
    Section("Product representations"),
    Entries(
        "55bf43",
        "788fa4",
        "19f13b",
        "a5852d",
    ),
    Section("Functional equations and recurrence relations"),
    Entries(
        "4f20ff",
        "2362af",
        "081188",
        "209fc8",
        "6e1f13",
        "56d4ff",
        "02ee06",
        "d651d1",
        "c640bf",
        "41f950",
        "fe9fb7",
    ),
    Section("Connection formulas"),
    Entries(
        "62c6c9",
        "e87c43",
        "332721",
        "1d5e92",
        "22ee07",
        "c733f7",
        "e78989",
        "30652c",
    ),
    Section("Sums and generating functions"),
    Entries(
        "6f7746",
        "7c014b",
        "858c8f",
        "4d1365",
        "1635f5",    # exp taylor series
        "65c610",
        "50f57e",
        "2b2066",
        "c9bcf7",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "bb8a75",
        "f9efd0",
        "25b7bd",
        "6b3af0",
        "001a0b",
        "5d6f99",
        "4e7120",
        "fc8d5d",
        "1745f5",
        "d3baaf",
        "5f7334",
        "433d8b",
        "fa3b53",
    ),
)

def_Topic(
    Title("Specific values of factorials and binomial coefficients"),
    SeeTopics("Factorials and binomial coefficients"),
    Section("Tables"),
    Entries(
        "3009a7",
        "fb5d88",
        "29741c",
        "63f368",
    ),
    Section("Special cases"),
    Entries(
        "d8c274",
        "988310",
        "8c21f5",
        "471485",
        "5b85bf",
        "1df686",
        "e78084",
        "973b2c",
        "0feb19",
        "5b414d",
        "a7b330",
        "355c22",
        "0d92f6",
    ),
)

# Symbols

make_entry(ID("81aeba"),
    SymbolDefinition(Factorial, Factorial(n), "Factorial"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(Element(n, ZZGreaterEqual(0)), Element(Factorial(n), ZZGreaterEqual(1))),
      )))

make_entry(ID("def588"),
    SymbolDefinition(Binomial, Binomial(n, k), "Binomial coefficient"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0))), Element(Binomial(n, k), ZZGreaterEqual(0))),
        Tuple(And(Element(n, CC), Element(k, ZZGreaterEqual(0))), Element(Binomial(n, k), CC)),
      )))

make_entry(ID("579595"),
    SymbolDefinition(RisingFactorial, RisingFactorial(z, k), "Rising factorial"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(z, CC), Element(k, ZZGreaterEqual(0))), Element(RisingFactorial(z, k), CC)),
      )))

make_entry(ID("3c2469"),
    SymbolDefinition(FallingFactorial, FallingFactorial(z, k), "Falling factorial"),
    Table(TableRelation(Tuple(P, Q), Implies(P, Q)),
      TableHeadings(Description("Domain"), Description("Codomain")),
      List(
        Tuple(And(Element(z, CC), Element(k, ZZGreaterEqual(0))), Element(FallingFactorial(z, k), CC)),
      )))

# Tables

make_entry(ID("3009a7"),
    Description("Table of", Factorial(n), "for", LessEqual(0, n, 30)),
    Table(
      Var(n),
      TableValueHeadings(n, Factorial(n)),
      TableSplit(2),
      List(
    Tuple(0, 1),
    Tuple(1, 1),
    Tuple(2, 2),
    Tuple(3, 6),
    Tuple(4, 24),
    Tuple(5, 120),
    Tuple(6, 720),
    Tuple(7, 5040),
    Tuple(8, 40320),
    Tuple(9, 362880),
    Tuple(10, 3628800),
    Tuple(11, 39916800),
    Tuple(12, 479001600),
    Tuple(13, 6227020800),
    Tuple(14, 87178291200),
    Tuple(15, 1307674368000),
    Tuple(16, 20922789888000),
    Tuple(17, 355687428096000),
    Tuple(18, 6402373705728000),
    Tuple(19, 121645100408832000),
    Tuple(20, 2432902008176640000),
    Tuple(21, 51090942171709440000),
    Tuple(22, 1124000727777607680000),
    Tuple(23, 25852016738884976640000),
    Tuple(24, 620448401733239439360000),
    Tuple(25, 15511210043330985984000000),
    Tuple(26, 403291461126605635584000000),
    Tuple(27, 10888869450418352160768000000),
    Tuple(28, 304888344611713860501504000000),
    Tuple(29, 8841761993739701954543616000000),
    Tuple(30, 265252859812191058636308480000000),
    )))

make_entry(ID("fb5d88"),
    Description("Table of", Binomial(n, k), "for", LessEqual(0, n, 15), "and", LessEqual(0, k, 15)),
    Table(TableRelation(Tuple(n, k, y), Equal(Binomial(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
        List(
            Tuple(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 4, 6, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 5, 10, 10, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 6, 15, 20, 15, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 7, 21, 35, 35, 21, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 8, 28, 56, 70, 56, 28, 8, 1, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 9, 36, 84, 126, 126, 84, 36, 9, 1, 0, 0, 0, 0, 0, 0),
            Tuple(1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1, 0, 0, 0, 0, 0),
            Tuple(1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1, 0, 0, 0, 0),
            Tuple(1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1, 0, 0, 0),
            Tuple(1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1, 0, 0),
            Tuple(1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1, 0),
            Tuple(1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1),
    )))

make_entry(ID("29741c"),
    Description("Table of", RisingFactorial(n, k), "for", LessEqual(0, n, 10), "and", LessEqual(0, k, 10)),
    Table(TableRelation(Tuple(n, k, y), Equal(RisingFactorial(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        List(
            Tuple(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800),
            Tuple(1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800),
            Tuple(1, 3, 12, 60, 360, 2520, 20160, 181440, 1814400, 19958400, 239500800),
            Tuple(1, 4, 20, 120, 840, 6720, 60480, 604800, 6652800, 79833600, 1037836800),
            Tuple(1, 5, 30, 210, 1680, 15120, 151200, 1663200, 19958400, 259459200, 3632428800),
            Tuple(1, 6, 42, 336, 3024, 30240, 332640, 3991680, 51891840, 726485760, 10897286400),
            Tuple(1, 7, 56, 504, 5040, 55440, 665280, 8648640, 121080960, 1816214400, 29059430400),
            Tuple(1, 8, 72, 720, 7920, 95040, 1235520, 17297280, 259459200, 4151347200, 70572902400),
            Tuple(1, 9, 90, 990, 11880, 154440, 2162160, 32432400, 518918400, 8821612800, 158789030400),
            Tuple(1, 10, 110, 1320, 17160, 240240, 3603600, 57657600, 980179200, 17643225600, 335221286400),
    )))

make_entry(ID("63f368"),
    Description("Table of", FallingFactorial(n, k), "for", LessEqual(0, n, 10), "and", LessEqual(0, k, 10)),
    Table(TableRelation(Tuple(n, k, y), Equal(FallingFactorial(n, k), y)),
        TableHeadings(Description(n, "\\", k), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        TableColumnHeadings(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        List(
            Tuple(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 3, 6, 6, 0, 0, 0, 0, 0, 0, 0),
            Tuple(1, 4, 12, 24, 24, 0, 0, 0, 0, 0, 0),
            Tuple(1, 5, 20, 60, 120, 120, 0, 0, 0, 0, 0),
            Tuple(1, 6, 30, 120, 360, 720, 720, 0, 0, 0, 0),
            Tuple(1, 7, 42, 210, 840, 2520, 5040, 5040, 0, 0, 0),
            Tuple(1, 8, 56, 336, 1680, 6720, 20160, 40320, 40320, 0, 0),
            Tuple(1, 9, 72, 504, 3024, 15120, 60480, 181440, 362880, 362880, 0),
            Tuple(1, 10, 90, 720, 5040, 30240, 151200, 604800, 1814400, 3628800, 3628800),
    )))

# Product representations

make_entry(ID("55bf43"),
    Equal(Factorial(n), Product(k, Tuple(k, 1, n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("788fa4"),
    Equal(Binomial(z, k), Product((z+1-i)/i, Tuple(i, 1, k)), Product((z-i)/(i+1), Tuple(i, 0, k-1))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("19f13b"),
    Equal(RisingFactorial(z, k), Product(Parentheses(z+i-1), Tuple(i, 1, k)), Product(Parentheses(z+i), Tuple(i, 0, k-1))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("a5852d"),
    Equal(FallingFactorial(z, k), Product(Parentheses(z-i+1), Tuple(i, 1, k)), Product(Parentheses(z-i), Tuple(i, 0, k-1))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

# Specific values

make_entry(ID("d8c274"),
    Formula(Equal(Factorial(0), 1)))

make_entry(ID("988310"),
    Formula(Equal(Binomial(n, 0), 1)),
    Variables(n),
    Assumptions(Element(n, CC)))

make_entry(ID("8c21f5"),
    Formula(Equal(Binomial(n, n), 1)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("471485"),
    Formula(Equal(Binomial(n, n+m), 0)),
    Variables(n, m),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(1)))))

make_entry(ID("5b85bf"),
    Formula(Equal(Binomial(z, 1), z)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("1df686"),
    Formula(Equal(Binomial(z, 2), (z*(z-1))/2)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("e78084"),
    Formula(Equal(RisingFactorial(z, 0), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("973b2c"),
    Formula(Equal(RisingFactorial(z, 1), z)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("0feb19"),
    Formula(Equal(RisingFactorial(1, k), Factorial(k))),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(0))))

make_entry(ID("5b414d"),
    Formula(Equal(FallingFactorial(z, 0), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("a7b330"),
    Formula(Equal(FallingFactorial(z, 1), z)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("355c22"),
    Formula(Equal(FallingFactorial(k, k), Factorial(k))),
    Variables(k),
    Assumptions(Element(k, ZZGreaterEqual(0))))

make_entry(ID("0d92f6"),
    Formula(Equal(Binomial(2 * n, n), Factorial(2 * n) / Factorial(n)**2)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Recurrence relations

make_entry(ID("4f20ff"),
    Formula(Equal(Factorial(n), (n) * Factorial(n-1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("2362af"),
    Formula(Equal(Binomial(n, k), Binomial(n, n-k))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZBetween(0, n)))))

make_entry(ID("081188"),
    Formula(Equal(Binomial(z + 1, k + 1), Binomial(z, k) + Binomial(z, k + 1))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZBetween(0, n)))))

make_entry(ID("209fc8"),
    Formula(Equal(Binomial(z, k + 1), ((z - k) / (k + 1)) * Binomial(z, k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("6e1f13"),
    Formula(Equal(Binomial(z + 1, k + 1), ((z + 1) / (k + 1)) * Binomial(z, k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("56d4ff"),
    Formula(Equal(Binomial(z, k), (-1)**k * Binomial(k-z-1, k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("02ee06"),
    Formula(Equal(RisingFactorial(z, k + m), RisingFactorial(z, k) * RisingFactorial(z + k, m))),
    Variables(z, k, m),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)), Element(m, ZZGreaterEqual(0)))))

make_entry(ID("d651d1"),
    Formula(Equal(RisingFactorial(z, 2 * k), 4**k * RisingFactorial(z/2, k) * RisingFactorial((z+1)/2, k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("c640bf"),
    Formula(Equal(RisingFactorial(-z, k), (-1)**k * RisingFactorial(z-k+1, k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("41f950"),
    Formula(Equal(RisingFactorial(z + 1, k), ((z+k)/z) * RisingFactorial(z, k))),
    Variables(z, k),
    Assumptions(And(Element(z, SetMinus(CC, Set(0))), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("fe9fb7"),
    Formula(Equal(RisingFactorial(z, k + 1), (z + k) * RisingFactorial(z, k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

# Connection formulas

make_entry(ID("62c6c9"),
    Formula(Equal(Factorial(n), GammaFunction(n+1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("e87c43"),
    Formula(Equal(Binomial(z,k), GammaFunction(z+1) / (GammaFunction(k + 1) * GammaFunction(z - k + 1)))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)), NotElement(z-k, ZZLessEqual(-1)))))

make_entry(ID("332721"),
    Formula(Equal(Binomial(n, k), Factorial(n) / (Factorial(k) * Factorial(n-k)))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("1d5e92"),
    Formula(Equal(Binomial(z, k), FallingFactorial(z, k) / Factorial(k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("22ee07"),
    Formula(Equal(Binomial(z, k), RisingFactorial(z-k+1, k) / Factorial(k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("c733f7"),
    Formula(Equal(RisingFactorial(z, k), GammaFunction(z+k)/GammaFunction(z))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)), NotElement(z+k, ZZLessEqual(0)))))

make_entry(ID("e78989"),
    Formula(Equal(RisingFactorial(z, k), FallingFactorial(z + k - 1, k))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("30652c"),
    Formula(Equal(RisingFactorial(n, k), Factorial(n+k-1)/Factorial(n-1))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(k, ZZGreaterEqual(0)))))

# Sums and generating functions

make_entry(ID("6f7746"),
    Formula(Equal(Sum(Binomial(n, k) * x**k * y**(n-k), Tuple(k, 0, n)), (x+y)**n)),
    Variables(x, y, n),
    Assumptions(And(Element(x, CC), Element(y, CC), Element(n, ZZGreaterEqual(0)))))

make_entry(ID("7c014b"),
    Formula(Equal(Sum(Binomial(z, k) * x**k, Tuple(k, 0, Infinity)), (1+x)**z)),
    Variables(z, x),
    Assumptions(And(Element(z, CC), Element(x, CC), Less(Abs(x), 1)),
                And(Element(z, ZZGreaterEqual(0)), Element(z, CC))))

make_entry(ID("858c8f"),
    Formula(Equal(Sum(Binomial(n, k), Tuple(k, 0, n)), 2**n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("4d1365"),
    Formula(Equal(Binomial(z, k), Sum(StirlingS1(k,i) * (z**i / Factorial(k)), Tuple(i, 0, k)))),
    Variables(z, k),
    Assumptions(And(Element(z, CC), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("65c610"),
    Formula(Equal(Exp(x+y), Sum(Sum(Binomial(n+k,k) * ((x**k * y**n) / Factorial(n+k)), Tuple(n, 0, Infinity)), Tuple(k, 0, Infinity)))),
    Variables(x, y),
    Assumptions(And(Element(x, CC), Element(y, CC))))

make_entry(ID("50f57e"),
    Formula(Equal(Sum(Binomial(2*n,n) * (x**n / Factorial(n)), Tuple(n, 0, Infinity)), Exp(2*x) * BesselI(0, 2*x))),
    Variables(x),
    Assumptions(Element(x, CC)))

make_entry(ID("2b2066"),
    Formula(Equal(Sum(Binomial(2*n,n) * x**n, Tuple(n, 0, Infinity)), 1/Sqrt(1-4*x))),
    Variables(x),
    Assumptions(And(Element(x, CC), Less(Abs(x), Div(1,4)))))

make_entry(ID("c9bcf7"),
    Formula(Equal(Sum((1/Binomial(2*n,n)) * x**n, Tuple(n, 0, Infinity)), Hypergeometric2F1(1,1,Div(1,2),x/4),
        Where(1/(1-u) + (Sqrt(u) * Asin(Sqrt(u)))/(1-u)**Div(3,2), Equal(u, x/4)))),
    Variables(x),
    Assumptions(And(Element(x, CC), Less(Abs(x), 4))))



# Bounds and inequalities

make_entry(ID("bb8a75"),
    Formula(LessEqual(Factorial(n), n**n)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("f9efd0"),
    Formula(Greater(Factorial(n), Exp(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(6))))

make_entry(ID("25b7bd"),
    Formula(Greater(Factorial(n), C**n)),
    Variables(C, n),
    Assumptions(And(Element(n, ZZGreaterEqual(1)), Element(C, OpenInterval(0, Infinity)), GreaterEqual(n, C * ConstE))))

make_entry(ID("6b3af0"),
    Formula(LessEqual(Binomial(n, k), n**k / Factorial(k))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("001a0b"),
    Formula(GreaterEqual(Binomial(n, k), n**k / k**k)),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZBetween(0, n)))))

make_entry(ID("5d6f99"),
    Formula(LessEqual(Binomial(n, k), (n*ConstE)**k / k**k)),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))))

make_entry(ID("4e7120"),
    Formula(LessEqual(Binomial(n, k), (n**n / (k**k * (n-k)**(n-k))))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZBetween(0, n)))))

make_entry(ID("fc8d5d"),
    Formula(Less(Factorial(n), Sqrt(2*ConstPi) * n**(n+Div(1,2)) * Exp(-n) * Exp(1/(12*n)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))),
    References("H. Robbins (1955), A remark on Stirling's formula, Am. Math. Monthly 62(1), pp. 26-29."))

make_entry(ID("1745f5"),
    Formula(Greater(Factorial(n), Sqrt(2*ConstPi) * n**(n+Div(1,2)) * Exp(-n) * Exp(1/(12*n+1)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))),
    References("H. Robbins (1955), A remark on Stirling's formula, Am. Math. Monthly 62(1), pp. 26-29."))

make_entry(ID("d3baaf"),
    Formula(Less(Binomial(n, k), (1/Sqrt(2*ConstPi)) * Sqrt(n/(k*(n-k))) * (n**n / (k**k * (n-k)**(n-k))))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(k, ZZBetween(1, n-1)))))

make_entry(ID("5f7334"),
    Formula(GreaterEqual(Binomial(n, k), (1/Sqrt(8)) * Sqrt(n/(k*(n-k))) * (n**n / (k**k * (n-k)**(n-k))))),
    Variables(n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(2)), Element(k, ZZBetween(1, n-1)))))

make_entry(ID("433d8b"),
    Formula(Less(Binomial(2*n, n), 4**n / Sqrt(ConstPi * n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("fa3b53"),
    Formula(LessEqual(Binomial(n, k), 2**n)),
    Variables(n),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)))))


