# -*- coding: utf-8 -*-

from .expr import *

def_Topic(
    Title("Fibonacci numbers"),
    Section("Definitions"),
    Entries(
        "fe11ce",
    ),
    Section("Tables"),
    Entries(
        "b506ad",
        "5818e3",
    ),
    Section("Symmetry"),
    Entries(
        "ce6dd0",
    ),
    Section("Recurrence relations"),
    Subsection("Consecutive terms"),
    Entries(
        "22dc6e",
        "6d437c",
        "a8f2ac",
        "10165f",
    ),
    Subsection("Distant terms"),
    Entries(
        "7ef2c7",
        "cbfe21",
        "5cb57e",
        "a104b0",
        "70878b",
    ),
    Subsection("Doubling"),
    Entries(
        "35956b",
        "2ca869",
        "5745bd",
        "fc4fd1",
    ),
    Subsection("Cassini's identity and generalizations"),
    Entries(
        "073466",
        "ab563e",
        "8db61e",
        "301081",
    ),
    Section("Algebraic formulas"),
    Entries(
        "24107d",
        "050fdb",
        "ad0d7a",
    ),
    Section("Matrix formulas"),
    Entries(
        "8a548e",
        "0e2425",
        "3a9c67",
    ),
    Section("Generating functions"),
    Entries(
        "05209f",
        "d0d91a",
    ),
    Section("Sum representations"),
    Entries(
        "9638c1",
        "d7c89c",
        "b8ed8f",
    ),
    Section("Elementary functions"),
    Entries(
        "12b336",
        "fd732d",
        "bceed4",
        "c4d78a",
    ),
    Section("Chebyshev polynomials"),
    Entries(
        "aadf90",
        "223ce1",
        "ae76a3",
    ),
    Section("Hypergeometric functions"),
    Entries(
        "1c90fb",
        "90c290",
    ),
    Section("Finite sums"),
    Entries(
        "1eb5e7",
        "3bb7e4",
        "5eb446",
        "82373a",
        "ac4d13",
        "f95561",
        "d454a3",
    ),
    Section("Divisibility"),
    Entries(
        "4b3947",
        "7b0abf",
        "aaa244",
        "da45c0",
        "6db705",
        "c84407",
        "a0206a",
        "4ec333",
        "f5f706",
        "9d26d2",
    ),
    Section("Asymptotics and limits"),
    Entries(
        "0574c1",
        "fdfdcc",
        "d56025",
    ),
    Section("Bounds and inequalities"),
    Entries(
        "f3aff5",
        "9c53d7",
        "412334",
    ),
    Section("Reciprocal series"),
    Entries(
        "ae9d30",
        "344963",
        "da1873",
        "22b67a",
        "6d8bf0",
    ),
)

make_entry(ID("fe11ce"),
    SymbolDefinition(Fibonacci, Fibonacci(n), "Fibonacci number"),
    References("http://oeis.org/A000045"))

# Symmetry

make_entry(ID("ce6dd0"),
    Formula(Equal(Fibonacci(-n), (-1)**(n+1) * Fibonacci(n))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Tables

make_entry(ID("b506ad"),
    Description("Table of", Fibonacci(n), "for", LessEqual(0, n, 100)),
    Table(TableRelation(Tuple(n, y), Equal(Fibonacci(n), y)),
      TableHeadings(n, Fibonacci(n)), TableSplit(2),
      List(
    Tuple(0, 0),
    Tuple(1, 1),
    Tuple(2, 1),
    Tuple(3, 2),
    Tuple(4, 3),
    Tuple(5, 5),
    Tuple(6, 8),
    Tuple(7, 13),
    Tuple(8, 21),
    Tuple(9, 34),
    Tuple(10, 55),
    Tuple(11, 89),
    Tuple(12, 144),
    Tuple(13, 233),
    Tuple(14, 377),
    Tuple(15, 610),
    Tuple(16, 987),
    Tuple(17, 1597),
    Tuple(18, 2584),
    Tuple(19, 4181),
    Tuple(20, 6765),
    Tuple(21, 10946),
    Tuple(22, 17711),
    Tuple(23, 28657),
    Tuple(24, 46368),
    Tuple(25, 75025),
    Tuple(26, 121393),
    Tuple(27, 196418),
    Tuple(28, 317811),
    Tuple(29, 514229),
    Tuple(30, 832040),
    Tuple(31, 1346269),
    Tuple(32, 2178309),
    Tuple(33, 3524578),
    Tuple(34, 5702887),
    Tuple(35, 9227465),
    Tuple(36, 14930352),
    Tuple(37, 24157817),
    Tuple(38, 39088169),
    Tuple(39, 63245986),
    Tuple(40, 102334155),
    Tuple(41, 165580141),
    Tuple(42, 267914296),
    Tuple(43, 433494437),
    Tuple(44, 701408733),
    Tuple(45, 1134903170),
    Tuple(46, 1836311903),
    Tuple(47, 2971215073),
    Tuple(48, 4807526976),
    Tuple(49, 7778742049),
    Tuple(50, 12586269025),
    Tuple(51, 20365011074),
    Tuple(52, 32951280099),
    Tuple(53, 53316291173),
    Tuple(54, 86267571272),
    Tuple(55, 139583862445),
    Tuple(56, 225851433717),
    Tuple(57, 365435296162),
    Tuple(58, 591286729879),
    Tuple(59, 956722026041),
    Tuple(60, 1548008755920),
    Tuple(61, 2504730781961),
    Tuple(62, 4052739537881),
    Tuple(63, 6557470319842),
    Tuple(64, 10610209857723),
    Tuple(65, 17167680177565),
    Tuple(66, 27777890035288),
    Tuple(67, 44945570212853),
    Tuple(68, 72723460248141),
    Tuple(69, 117669030460994),
    Tuple(70, 190392490709135),
    Tuple(71, 308061521170129),
    Tuple(72, 498454011879264),
    Tuple(73, 806515533049393),
    Tuple(74, 1304969544928657),
    Tuple(75, 2111485077978050),
    Tuple(76, 3416454622906707),
    Tuple(77, 5527939700884757),
    Tuple(78, 8944394323791464),
    Tuple(79, 14472334024676221),
    Tuple(80, 23416728348467685),
    Tuple(81, 37889062373143906),
    Tuple(82, 61305790721611591),
    Tuple(83, 99194853094755497),
    Tuple(84, 160500643816367088),
    Tuple(85, 259695496911122585),
    Tuple(86, 420196140727489673),
    Tuple(87, 679891637638612258),
    Tuple(88, 1100087778366101931),
    Tuple(89, 1779979416004714189),
    Tuple(90, 2880067194370816120),
    Tuple(91, 4660046610375530309),
    Tuple(92, 7540113804746346429),
    Tuple(93, 12200160415121876738),
    Tuple(94, 19740274219868223167),
    Tuple(95, 31940434634990099905),
    Tuple(96, 51680708854858323072),
    Tuple(97, 83621143489848422977),
    Tuple(98, 135301852344706746049),
    Tuple(99, 218922995834555169026),
    Tuple(100, 354224848179261915075),
    )))

make_entry(ID("5818e3"),
    Description("Table of", Fibonacci(10**n), "to 50 digits for", LessEqual(0, n, 20)),
    Table(TableRelation(Tuple(n, y), Equal(NearestDecimal(Fibonacci(10**n), 50), y)),
      TableHeadings(n, Fibonacci(10**n)), TableSplit(1),
      List(
    Tuple(0, Decimal("1")),
    Tuple(1, Decimal("55")),
    Tuple(2, Decimal("354224848179261915075")),
    Tuple(3, Decimal("4.3466557686937456435688527675040625802564660517372e+208")),
    Tuple(4, Decimal("3.3644764876431783266621612005107543310302148460680e+2089")),
    Tuple(5, Decimal("2.5974069347221724166155034021275915414880485386518e+20898")),
    Tuple(6, Decimal("1.9532821287077577316320149475962563324435429965919e+208987")),
    Tuple(7, Decimal("1.1298343782253997603170636377458663729448371904890e+2089876")),
    Tuple(8, Decimal("4.7371034734563369625489713133510386575486828937720e+20898763")),
    Tuple(9, Decimal("7.9523178745546834678293851961971481892555421852344e+208987639")),
    Tuple(10, Decimal("1.4135212296147024564096151864184089768135166603147e+2089876402")),
    Tuple(11, Decimal("4.4502906390486589597158064980525302063183707085571e+20898764024")),
    Tuple(12, Decimal("4.2584226889958835886348336943722259069350042910726e+208987640249")),
    Tuple(13, Decimal("2.7406444081225493607051434240988555526172053810282e+2089876402499")),
    Tuple(14, Decimal("3.3411188533931480763928505837976694567574715082316e+20898764024997")),
    Tuple(15, Decimal("2.4226142638072665895512781785852365306378154520894e+208987640249978")),
    Tuple(16, Decimal("9.7321259036507402774301623570261041248903959860292e+2089876402499786")),
    Tuple(17, Decimal("1.0652271003503856899342263856673297764435665668329e+20898764024997873")),
    Tuple(18, Decimal("2.6289788186792204674075064891600428077435502009263e+208987640249978733")),
    Tuple(19, Decimal("2.2041233236015343583064006979459206416375776690474e+2089876402499787337")),
    Tuple(20, Decimal("3.7820208747205569470350747417141015056709733674715e+20898764024997873376")),
    )))


# Recurrence relations

make_entry(ID("22dc6e"),
    Formula(Equal(Fibonacci(n), Fibonacci(n-1) + Fibonacci(n-2))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("6d437c"),
    Formula(Equal(Fibonacci(n), Fibonacci(n+2) - Fibonacci(n+1))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("a8f2ac"),
    Formula(Equal(Fibonacci(n+1), Fibonacci(n) + Fibonacci(n-1))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("10165f"),
    Formula(Equal(Fibonacci(n+2), Fibonacci(n+1) + Fibonacci(n))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("7ef2c7"),
    Formula(Equal(Fibonacci(n), 2 * Fibonacci(n-2) + Fibonacci(n-3))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("cbfe21"),
    Formula(Equal(Fibonacci(n), 3 * Fibonacci(n-3) + 2 * Fibonacci(n-4))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("5cb57e"),
    Formula(Equal(Fibonacci(n), Fibonacci(m+1) * Fibonacci(n-m) + Fibonacci(m) * Fibonacci(n-m-1))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("a104b0"),
    Formula(Equal(Fibonacci(m+n), Fibonacci(m) * Fibonacci(n+1) + Fibonacci(m-1) * Fibonacci(n))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZ), Element(n, ZZ))))

make_entry(ID("70878b"),
    Formula(Equal(Fibonacci(m+n-1), Fibonacci(m) * Fibonacci(n) + Fibonacci(m-1) * Fibonacci(n-1))),
    Variables(m, n),
    Assumptions(And(Element(m, ZZ), Element(n, ZZ))))

# Doubling

make_entry(ID("35956b"),
    Formula(Equal(Fibonacci(2*n), Fibonacci(n+1)**2 - Fibonacci(n-1)**2)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("2ca869"),
    Formula(Equal(Fibonacci(2*n), (Fibonacci(n+1) + Fibonacci(n-1))*Fibonacci(n))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("5745bd"),
    Formula(Equal(Fibonacci(2*n), (Fibonacci(n+2)**2 - Fibonacci(n+1)**2 - 2*Fibonacci(n)**2))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("fc4fd1"),
    Formula(Equal(Fibonacci(2*n+1), Fibonacci(n+1)**2 + Fibonacci(n)**2)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("073466"),
    Formula(Equal(Fibonacci(n)**2, Fibonacci(n+1)*Fibonacci(n-1) - (-1)**n)),
    Description("Cassini's identity"),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("ab563e"),
    Formula(Equal(Fibonacci(n)**2, Fibonacci(n+m)*Fibonacci(n-m) + (-1)**(n+m) * Fibonacci(m)**2)),
    Description("Catalan's identity"),
    Variables(n, m),
    Assumptions(And(Element(n, ZZ), Element(m, ZZ))))

make_entry(ID("8db61e"),
    Formula(Equal(Fibonacci(n+i)*Fibonacci(n+j) - Fibonacci(n)*Fibonacci(n+i+j), (-1)**n * Fibonacci(i)*Fibonacci(j))),
    Description("Vajda's identity"),
    Variables(n, i, j),
    Assumptions(And(Element(n, ZZ), Element(i, ZZ), Element(j, ZZ))))

make_entry(ID("301081"),
    Formula(Equal(Fibonacci(m)*Fibonacci(n+1) - Fibonacci(m+1)*Fibonacci(n), (-1)**n * Fibonacci(m-n))),
    Description("d'Ocagne's identity"),
    Variables(n, m),
    Assumptions(And(Element(n, ZZ), Element(m, ZZ))))


# Algebraic representations

make_entry(ID("24107d"),
    Formula(Equal(Fibonacci(n), (GoldenRatio**n - (-GoldenRatio)**(-n)) / Sqrt(5))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("050fdb"),
    Formula(Equal(Fibonacci(n), Floor(GoldenRatio**n / Sqrt(5) + Div(1,2)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# todo: define Fibonacci(n) for non-integer n?
make_entry(ID("ad0d7a"),
    Formula(Equal(Fibonacci(n), (GoldenRatio**n - Cos(ConstPi*n) * GoldenRatio**(-n)) / Sqrt(5))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Matrix formulas

make_entry(ID("8a548e"),
    Formula(Equal(Pow(Matrix2x2(1,1,1,0), n), Matrix2x2(Fibonacci(n+1), Fibonacci(n), Fibonacci(n), Fibonacci(n-1)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("0e2425"),
    Formula(Equal(Matrix2x1(Fibonacci(n+1), Fibonacci(n)), Matrix2x2(1,1,1,0) * Matrix2x1(Fibonacci(n), Fibonacci(n-1)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("3a9c67"),
    Formula(Equal(Matrix2x1(Fibonacci(n+m), Fibonacci(n+m-1)), Matrix2x2(1,1,1,0)**m * Matrix2x1(Fibonacci(n), Fibonacci(n-1)))),
    Variables(n, m),
    Assumptions(And(Element(n, ZZ), Element(m, ZZ))))

# Generating functions

make_entry(ID("05209f"),
    Formula(Equal(Sum(Fibonacci(n) * z**n, Tuple(n, 0, Infinity)), z/(1-z-z**2))),
    Variables(z),
    Assumptions(And(Element(z, CC), Less(Abs(z), GoldenRatio-1))))

make_entry(ID("d0d91a"),
    Formula(Equal(Sum(Fibonacci(n) * (z**n / Factorial(n)), Tuple(n, 0, Infinity)),
        (2/Sqrt(5)) * Exp(z/2) * Sinh((Sqrt(5)/2) * z))),
    Variables(z),
    Assumptions(Element(z, CC)))

# Sum representations

make_entry(ID("9638c1"),
    Formula(Equal(Fibonacci(n), Sum(Binomial(n-k-1,k), Tuple(k, 0, n-1)))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("d7c89c"),
    Formula(Equal(Fibonacci(n), Sum(Binomial(n-k-1,k), Tuple(k, 0, Floor((n-1)/2))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("b8ed8f"),
    Formula(Equal(Fibonacci(n), (1/2**(n-1)) * Sum(5**k * Binomial(n,2*k+1), Tuple(k, 0, Floor((n-1)/2))))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Elementary functions

make_entry(ID("12b336"),
    Formula(Equal(Fibonacci(n), Where((Exp(n*u) - Cos(ConstPi*n)*Exp(-n*u))/Sqrt(5), Equal(u, Log(GoldenRatio))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("fd732d"),
    Formula(Equal(Fibonacci(n), (2/Sqrt(5)) * Where(Cases(Tuple(Sinh(n*u), Even(n)),
            Tuple(Cosh(n*u), Odd(n))), Equal(u, Log(GoldenRatio))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

#    Formula(Equal(Fibonacci(2*n), (2/Sqrt(5)) * Sinh(n*Log(1+GoldenRatio)))),
#    Formula(Equal(Fibonacci(2*n+1), (2/Sqrt(5)) * Cosh((n+Div(1,2))*Log(1+GoldenRatio)))),

make_entry(ID("bceed4"),
    Formula(Equal(Fibonacci(n), Where(((1+Cos(ConstPi*n))*Sinh(n*u) + (1-Cos(ConstPi*n))*Cosh(n*u)) / Sqrt(5), Equal(u, Log(GoldenRatio))))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("c4d78a"),
    Formula(Equal(Fibonacci(n), (2/Sqrt(5)) * (-ConstI)**n * Sinh(n*(Log(GoldenRatio) + Div(1,2)*ConstPi*ConstI)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# Hypergeometric functions

make_entry(ID("aadf90"),
    Formula(Equal(Fibonacci(2*n), ChebyshevU(n-1, Div(3,2)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("223ce1"),
    Formula(Equal(Fibonacci(2*n+1), (2/Sqrt(5)) * ChebyshevT(2*n+1, Sqrt(5)/2))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("ae76a3"),
    Formula(Equal(Fibonacci(n), ConstI**(n-1) * ChebyshevU(n-1, -(ConstI/2)))),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("1c90fb"),
    Formula(Equal(Fibonacci(n), (n/2**(n-1)) * Hypergeometric2F1((1-n)/2, (2-n)/2, Div(3,2), 5))),
    Variables(n),
    Assumptions(Element(n, ZZ)),
    References("http://functions.wolfram.com/IntegerFunctions/Fibonacci/26/01/01/0007/"))

make_entry(ID("90c290"),
    Formula(Equal(Fibonacci(n), Hypergeometric2F1((1-n)/2, (2-n)/2, 1-n, -4))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

# Divisibility

make_entry(ID("4b3947"),
    Formula(Divides(Fibonacci(d), Fibonacci(d*n))),
    Variables(d, n),
    Assumptions(And(Element(d, SetMinus(ZZ, Set(0))), Element(n, ZZ))))

make_entry(ID("7b0abf"),
    Formula(Equal(GCD(Fibonacci(n), Fibonacci(n+1)), 1)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("aaa244"),
    Formula(Equal(GCD(Fibonacci(n), Fibonacci(n+2)), 1)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

# --- da45c0: included from gcd

make_entry(ID("6db705"),
    Formula(Divides(p, Fibonacci(p - KroneckerSymbol(p, 5)))),
    Variables(p),
    Assumptions(Element(p, PP)))

make_entry(ID("c84407"),
    Formula(CongruentMod(Fibonacci(p), KroneckerSymbol(p, 5), p)),
    Variables(p),
    Assumptions(Element(p, PP)))

make_entry(ID("a0206a"),
    Formula(Equivalent(Element(x, SetBuilder(Fibonacci(n), n, Element(n, ZZGreaterEqual(0)))),
        Or(Element(Sqrt(5*x**2+4), ZZ), Element(Sqrt(5*x**2-4), ZZ)))),
    Variables(x),
    Assumptions(Element(x, ZZGreaterEqual(0))))

make_entry(ID("4ec333"),
    Formula(Equal(Cardinality(SetBuilder(k, k, And(Element(k, ZZ), Divides(n, Fibonacci(k))))), Cardinality(ZZ))),
    Variables(n),
    Assumptions(Element(n, SetMinus(ZZ, Set(0)))))

make_entry(ID("f5f706"),
    Formula(CongruentMod(Fibonacci(n+60), Fibonacci(n), 10)),
    Variables(n),
    Assumptions(Element(n, ZZ)))

make_entry(ID("9d26d2"),
    Formula(Equal(SetBuilder(Fibonacci(n), n, And(Element(n, ZZGreaterEqual(0)), Element(Sqrt(Fibonacci(n)), ZZ))),
        Set(Fibonacci(0), Fibonacci(1), Fibonacci(2), Fibonacci(12)), Set(0, 1, 144))))

# Finite sums

make_entry(ID("1eb5e7"),
    Formula(Equal(Sum(Fibonacci(k), Tuple(k, 0, n)), Fibonacci(n+2)-1)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("3bb7e4"),
    Formula(Equal(Sum(Fibonacci(2*k), Tuple(k, 0, n)), Fibonacci(2*n+1)-1)),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("5eb446"),
    Formula(Equal(Sum(Fibonacci(2*k+1), Tuple(k, 0, n)), Fibonacci(2*n+2))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("82373a"),
    Formula(Equal(Sum(Fibonacci(k)**2, Tuple(k, 0, n)), Fibonacci(n)*Fibonacci(n+1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("ac4d13"),
    Formula(Equal(Sum(Binomial(n,k) * Fibonacci(k), Tuple(k, 0, n)), Fibonacci(2*n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("f95561"),
    Formula(Equal(Sum((-1)**(k+1) * Binomial(n,k) * Fibonacci(k), Tuple(k, 0, n)), Fibonacci(n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("d454a3"),
    Formula(Equal(Sum(Binomial(n,k) * 2**k * Fibonacci(k), Tuple(k, 0, n)), Fibonacci(3*n))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

# Asymptotics

make_entry(ID("0574c1"),
    Formula(Equal(AsymptoticTo(Fibonacci(n), GoldenRatio**n / Sqrt(5), n, Infinity))))

make_entry(ID("fdfdcc"),
    Formula(Equal(SequenceLimit(Fibonacci(n+1)/Fibonacci(n), n, Infinity), GoldenRatio)))

make_entry(ID("d56025"),
    Formula(Equal(SequenceLimit(Fibonacci(n+m)/Fibonacci(n), n, Infinity), GoldenRatio**m)),
    Variables(m),
    Assumptions(Element(m, ZZ)))

# Bounds and inequalities

make_entry(ID("f3aff5"),
    Formula(Less(Fibonacci(n), (GoldenRatio**n + 1)/Sqrt(5))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(0))))

make_entry(ID("9c53d7"),
    Formula(Greater(Fibonacci(n), (GoldenRatio**n - 1)/Sqrt(5))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(1))))

make_entry(ID("412334"),
    Formula(Less(Fibonacci(2*n), Fibonacci(n+1)**2, Fibonacci(2*n+1))),
    Variables(n),
    Assumptions(Element(n, ZZGreaterEqual(2))))

# Reciprocal series

make_entry(ID("ae9d30"),
    Formula(Equal(Sum(1/(Fibonacci(2*n+1)+1), Tuple(n, 0, Infinity)),
        Sqrt(5)/2)),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987."))

make_entry(ID("344963"),
    Formula(Equal(Sum((-1)**(n+1)/(Fibonacci(n)*Fibonacci(n+1)), Tuple(n, 1, Infinity)),
        (Sqrt(5)-1)/2)),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987."))

make_entry(ID("da1873"),
    Formula(Equal(Sum(1/Fibonacci(2*n+1), Tuple(n, 0, Infinity)),
        Where((Sqrt(5)/4) * JacobiTheta2(0, tau)**2, Equal(tau, (1/(ConstPi*ConstI)) * Log((3-Sqrt(5))/2))))),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987."))

make_entry(ID("22b67a"),
    Formula(Equal(Sum(1/Fibonacci(n)**2, Tuple(n, 1, Infinity)),
        Where(Div(5,24) * (JacobiTheta2(0, tau)**4 - JacobiTheta4(0, tau)**4 + 1), Equal(tau, (1/(ConstPi*ConstI)) * Log((3-Sqrt(5))/2))))),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987."))

make_entry(ID("6d8bf0"),
    Formula(Equal(Sum(1/Fibonacci(2**n), Tuple(n, 0, Infinity)),
        (7-Sqrt(5))/2)),
    References("J. M. Borwein and P. B. Borwein. Pi and the AGM. Wiley, New York, 1987."))

