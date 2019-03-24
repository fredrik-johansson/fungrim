from .expr import *

def_Topic(
    Title("Stirling numbers"),
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
    Variables(x, n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("f46e0e"),
    Formula(Equal(RisingFactorial(x-n+1, n), Sum(StirlingS1(n, k) * x**k, Tuple(k, 0, n)))),
    Variables(x, n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("b823b0"),
    Formula(Equal(x**n, Sum(StirlingS2(n, k) * RisingFactorial(x-n+1, n), Tuple(k, 0, n)))),
    Variables(x, n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)), Element(x, CC))))

make_entry(ID("b01280"),
    Formula(Equal(Div((Log(1+x))**k, Factorial(k)), Sum((-1)**(n-k) * StirlingCycle(n,k) * Div(x**n, Factorial(n)), Tuple(n, k, Infinity)))),
    Variables(x, n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)), Element(x, CC), Less(Abs(x), 1))))

make_entry(ID("a9a610"),
    Formula(Equal(Div((Exp(x)-1)**k, Factorial(k)), Sum(StirlingS2(n,k) * Div(x**n, Factorial(n)), Tuple(n, k, Infinity)))),
    Variables(x, n, k),
    Assumptions(And(Element(n, ZZGreaterEqual(0)), Element(k, ZZGreaterEqual(0)), Element(x, CC))))


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

